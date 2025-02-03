import json
import os
import math
import copy
import pprint
from collections import Counter
import MarcoM

def bereichsAnalyse(bereich):
    """ 
    Zählt Anzahl der bereiche, Anzahl der Linien, 
    Anzahl der Bereiche mit Bus, Straßenbahn und beiden

    Aufgabe: Leicht 1 + 4

    :type bereich:dict
    :param bereich: dictionary der Haltestellenbereiche

    :rtype:
    :returns:
    """
    sBereiche = set()
    sLinien = set()
    anzahlBUS = 0
    anzahlSTRAB = 0
    anzahlBEIDES = 0
    for feature in bereich["features"]:                                 
        sBereiche.add(feature["properties"]["kurzname"])                #füge alle gefundenen HSTBereiche dem Set sBereiche hinzu
        if "Linien" in feature["properties"]:
            for linie in feature["properties"]["Linien"].split(" "):    #value von Linien aufsplitten weil es ein String ist
                if linie != "":                                         #weil sich ein Leerzeichen eingeschmiggekt hatte
                    sLinien.add(linie)                                  #füge gefundene Linien dem Set sLinien zu
        if "Betriebsbereich" in feature["properties"]:
            match feature["properties"]["Betriebsbereich"]:             #sortieren/zählen wenn Betriebsbereich vorhanden ist
                case "BUS":
                    anzahlBUS +=1
                case "STRAB":
                    anzahlSTRAB +=1
                case "BUS STRAB":
                    anzahlBEIDES +=1
    print(f"\nDie gesamte Anzahl an Bereichen ist:\t{len(sBereiche)} \nDie gesamte Anzahl an Linien ist:\t{len(sLinien)}" )
    print(f"\nDie Anzahl an Haltebereichen mit\nBus:\t\t{anzahlBUS}\nStraßenbahn:\t{anzahlSTRAB}\nbeidem\t\t{anzahlBEIDES}\n")
    return

def createLinienDict(bereich):
    """ 
    Erstellt auf Basis der Haltestellenbereiche ein dictionary 
    mit key=linie und value= set(Haltestellenbereiche)

    :type bereich:dict
    :param bereich: dictionary der Haltestellenbereiche wie aus JSON

    :rtype:
    :returns:
    """
    sLinien = set()
    linienBereich = set()
    linienHSTSetdict={}
    for feature in bereich["features"]:                                     #alle Linien aller bereiche einem Set hinzufügen
        if "Linien" in feature["properties"]:
            for linie in feature["properties"]["Linien"].split(" "):
                if linie != "":
                    sLinien.add(linie)
                    
    while(sLinien):                                                         #für alle Linien im Linien-set, entnehme einzelne linie und 
        element = sLinien.pop()
        for feature in bereich["features"]:                                 #durchsuche Haltebereiche nach erwähnungen.
            if "Linien" in feature["properties"]:
                if (element in feature["properties"]["Linien"].split(" ")):  
                    linienBereich.add(feature["properties"]["kurzname"])    #füge alle HSTBereiche die Linien enthalten ins linienBereich ein
        linienHSTSetdict[element]=linienBereich.copy()                      #Kopiere in linienBereich-Set als Value in dict mit key = Linie 
        linienBereich.clear()                                       
    return linienHSTSetdict                       

def countIntersects(linienDict, disable_print=False):
    """ Errechnet die Linien mit den meisten gemeinsamen Haltestellen
    und analysiert, von welcher SBahn man in welche andere SBahn umsteigen kann

    Aufgabe_ mittel: 1 und 4

    :type linienDict:dict
    :param linienDict:dictionary mit key=Linie, value = set(haltestellenbereich)

    :type disable_print: bool
    :param disable_print: false(standard) und ausgaben zu verwenden, true um ausgaben zu vermeiden

    :rtype:dict
    :returns:Key= Linie, value=set(umsteigbare linien)
    """
    intersects = set()
    os_intersectLines = ""
    i_maxIntersect = 0
    umsteigenDict ={}
    umsteigenSet = set()

    for linie in linienDict.keys():                                                 #kombiniere jede Linie mit jeder anderen Linie
        for comparelinie in linienDict.keys():
            if linie!=comparelinie:
                intersects=linienDict[linie].intersection(linienDict[comparelinie]) 
                if(intersects):                                                     #Wenn Linienpaar Schnittmenge besitzt
                    if len(intersects) > i_maxIntersect:                              #Anzahl der Elemente in Schnittmenge Zählen und maximum speichern
                        i_maxIntersect=len(intersects)
                        os_intersectLines=f"Linien {comparelinie} und {linie} haben die maximale Anzahl an gleichen Haltestellen: {i_maxIntersect}"
                    if int(linie) <100 and int(comparelinie) < 100:
                        umsteigenSet.add(comparelinie)                              #wenn Straßenbahn und Schnittmenge vorhaden, füge zu umsteigen set hinzu
        if int(linie) <100:
            umsteigenDict[linie] = umsteigenSet.copy()                              #kopiere set in dict mit value = Set aus Linien die kreuzen und key = Linie
        umsteigenSet.clear()
    if not disable_print:                                                           #nur dann ausgeben wenn gewünscht
        print(os_intersectLines)
        print("\nFolgende Umstiege sind möglich:\n")
        for x,y in umsteigenDict.items():
            print(f"{x}\t->\t{y}")
    return umsteigenDict       

def writeTrepAufzToDict(dicts):
    """ 
    Schreibt Segment = Kundencenter in die HST-Bereiche mit Kundencenter

    :type dicts:dict
    :param dicts:dictionary mit allen JSON Daten

    :raises:

    :rtype:
    :returns:
    """
    x=0
    for x,propertyHST in enumerate(dicts["haltestellenbereiche"]["features"]): #Wenn passender HST-Bereich zu Vorkaufsort gefunden und dieser ein Kundencenter ist
        for propertyTreppen in dicts["fahrtreppen"]["features"]:
            if(propertyHST["properties"]["Haltestellenbereich"]==propertyTreppen["properties"]["Haltestellenbereich"]):# and propertyVKO["properties"]["Segment"] == "KundenCenter"):
                dicts["haltestellenbereiche"]["features"][x]["properties"].update({"Fahrtreppe" : True}) #update das ursprüngliche HST-Dict mit Fahrtreppe
        for propertyAufz in dicts["aufzuege"]["features"]:
            if(propertyHST["properties"]["Haltestellenbereich"]==propertyAufz["properties"]["Haltestellenbereich"]):# and propertyVKO["properties"]["Segment"] == "KundenCenter"):
                dicts["haltestellenbereiche"]["features"][x]["properties"].update({"Aufzug" : True}) #update das ursprüngliche HST-Dict mit Fahrtreppe
    return

def writeKcenterToDict(dicts):
    """ 
    Schreibt Segment = Kundencenter in die HST-Bereiche mit Kundencenter

    :type dicts:dict
    :param dicts:dictionary mit allen JSON Daten

    :rtype:
    :returns:
    """ 
    x=0
    for x,propertyHST in enumerate(dicts["haltestellenbereiche"]["features"]): #Wenn passender HST-Bereich zu Vorkaufsort gefunden und dieser ein Kundencenter ist
        for propertyVKO in dicts["verkaufsorte"]["features"]:
            if(propertyHST["properties"]["Haltestellenbereich"]==propertyVKO["properties"]["haltestellenbereich"] and propertyVKO["properties"]["Segment"] == "KundenCenter"):
                dicts["haltestellenbereiche"]["features"][x]["properties"].update({"Segment" : propertyVKO["properties"]["Segment"]}) #update das ursprüngliche HST-Dict mit Segment = kundencenter
    return

def findkCenter(hstBereich, linienDict):
    """ 
     findet Kundencenter und checkt, ob man von Linien ohne Kundencenter in eine Linie mit Kundencenter umsteigen kann

     Aufgabe: mittel: 5

    :type hstBereich:dict
    :param hstBereich:Dictionary der Haltestellenbereiche

    :type linienDict:dict
    :param linienDict:Dictionary der Verkaufsorte

    :rtype:
    :returns:
    """
    linienKCenter = set()
    umsteigenDict = countIntersects(linienDict, True)
    for elem in hstBereich["features"]:
        if (elem["properties"].get("Segment")== "KundenCenter"):                #suche HST-Bereiche nach Kundencenter ab und füge zu set hinzu
            for linie in elem["properties"]["Linien"].split(" "):
                if (int(linie) < 100):                
                    linienKCenter.add(linie)
    print(f"\nStraßenbahnlinien mit Kundecenter: {linienKCenter}")
    for item, value in umsteigenDict.items():                                   #gehe alle items im umsteigen-dictionary durch
        if item not in linienKCenter and value.intersection(linienKCenter):     #wenn Linie gefunden OHNE Kundencenter, das aber Schnittmenge mit Kundencenterlinien hat
            print(f"\nAn Linie {item} gibt es kein Kundencenter.\nMan kann in Linie {value} mit Kundencenter umsteigen")
        elif item in linienKCenter:
            continue
        else:   
            print(f"\nAn Linie {item} gibt es kein Kundencenter.\nMan kann in keine Linie mit Kundencenter umsteigen")
    return

def calcDistance(startCoord, endCoord):
    """ 
    Berechnet die Entfernung (Luftlinie) zwischen zwei eingegebenen Punkten

    :type startCoord:Tuple
    :param startCoord:Ausgangkoordinaten (x,y)

    :type endCoord:Tuple
    :param endCoord:Endkoordinaten (x,y)

    :raises:

    :rtype:
    :returns:
    """
    xA = startCoord[0]
    yA = startCoord[1]
    xB = endCoord[0]
    yB = endCoord[1]
    x=abs(xA-xB)
    y=abs(yA-yB)
    dist=math.sqrt(x**2 +y**2)
    return dist

def finalHST(linienDictCoord, linie):
    """ 
    sucht zu einer gegebenen Haltestelle die am weitesten entferne Haltestelle der gleichen Linie (sollte dann entweder die letzte oder erste Haltestelle sein)

    :type linienDictCoord: dict
    :param linienDictCoord: dictionary mit {linie:{haltestelle:(coord x, coord y)}

    :type linie: string
    :param linie: nummer der gesuchten Linie als String

    :rtype: String
    :returns: End- oder Anfangshaltestelle
    """
    maxDist = 0
    llinienDictCoord = copy.deepcopy(linienDictCoord)
    firstStop=llinienDictCoord[linie].popitem()
    for i, (x,y) in llinienDictCoord[linie].items():        #Suche alle Haltestellen der Linien ab und ermittle die am weitesten entfernte
        dist =calcDistance(firstStop[1], (x,y))
        if dist > maxDist:
            maxDist = dist
            s_finalHst = i
    return s_finalHst

def sortHST(begin, linienDictCoord, linie, firstCall = True, sortedHSTList=[]):
    """ 
    Rekursive funktion, die beim ersten Aufruf initialisiert und die Anfangs- oder Endhaltestelle in die Ergebnisliste einträgt und dann die geografisch nächste Haltestelle sucht. 
    Jeder weitere Aufruf hängt die geografisch nächste Halstelle an die Liste an

    :type begin: tuple (x,y)
    :param begin: ausgangskoordinate (beim ersten aufruf (firstCall = True) die Anfangs- oder Endhaltestelle)

    :type linienDictCoord: Dict
    :param linienDictCoord: dictionary mit {linie:{haltestelle:(coord x, coord y)} 

    :type linie: String
    :param linie: nummer der gesuchten Linie als String

    :type firstCall: bool
    :param firstCall: initialisierungs-trigger. Wenn True, wird die zurückzugebende Liste erstellt und die erste Haltestelle ind ddie Rückgabeliste eingetragen

    :type sortedHSTList: list
    :param sortedHSTList: übergabe der zu bearbeitenden Liste da der Inhalt sonst durch den rekursiven Aufruf verloren geht. Muss nur übergeben werden wenn Funktion rekusiv aufgerufen wird

    :rtype: List
    :returns: Liste der Haltestellen in abgefahrener Reihenfolge als tuple mit Kurzname und Name. Richtung zufällig.
    """
    minDist=1000
    llinienDictCoord = copy.deepcopy(linienDictCoord)
    if firstCall:                                   #beim ersten Aufruf Liste anlegen übergebenen Wert (erste Haltestelle) in die Liste schreiben
        sortedHSTList = []
        sortedHSTList.append(begin)

    beginHST = llinienDictCoord[linie].pop(begin)   #ein element entnehmen und die nächstgelegene HST suchen
    for i, (x,y) in llinienDictCoord[linie].items():
        dist =calcDistance(beginHST, (x,y))
        if dist < minDist:
            minDist = dist
            nextHst = i    
    if llinienDictCoord[linie]:                     #wenn Liste noch Werte enthält, hänge die nächste HST an die Liste und 
        sortedHSTList.append(nextHst)                                                       
        sortHST(nextHst, llinienDictCoord, linie, 0, sortedHSTList) #rufe diese funktion nochmals (rekursiv) auf um den nächsten Halt zu ermitteln

    #wieso funktioniert hier das dicts-dict?? ist das ein globales dict?
    sortedHstNameList = [kurznToHSTname(kurzn, dicts["haltestellenbereiche"]) for kurzn in sortedHSTList]   #Suche für jeden Kurznamen den korrekten vollst. Namen

    return list(zip(sortedHSTList, sortedHstNameList))  #Packe den Kunrzn und den vollst. Namen in ein Tupel

def addCoordinates(linienDict, haltestellen):
    """ Fügt zu jeder Haltestelle im linienDict ein Koordinatenpaar hinzu und gibt das Ergebnis als ein neues dict zurück

    :type linienDict: Dict
    :param linienDict: dictionary mit key = linie und value = set aus Haltestellen

    :type haltestellen: Dict
    :param haltestellen: inhalt der JSON-Datei "haltestellen"

    :rtype: Dict
    :returns:dictionary mit {linie:{haltestelle:(coord x, coord y)} 
    """
    llinienDictCoord = {}
    halt={}
    haltSet = set ()
    for element in linienDict.keys():       
        if int(element) < 100:                      #nur für sBahn
            for lDicthst in linienDict[element]:    #element = key aud liniendict (die zu bearbeitende Linie)
                for hst in haltestellen["features"]:#für alle Haltestellen der zu bearbeitenden Linie
                    if hst["properties"].get("Linien")!=None and hst["properties"]["Kurzname"]==lDicthst and element in hst["properties"].get("Linien").split(" "): #wenn HST aus LinienDict gefunden in haltestellen-dict und Linie dort auch hält
                        halt[lDicthst]=hst["geometry"]["coordinates"]   #füge koordinaten hinzu
                        llinienDictCoord[element]=halt
        halt = {}
    return llinienDictCoord

def findNextHst(coordTuple , linienDictCoord, bereich={}, aufzug=0, treppe=0):
    """ Sucht zu angegebenen Koordinaten den nächsten Haltestellenbereich. Optional kann nach Haltestellenbereichen mit Aufzug oder Rolltreppe gesucht werden

    :type coordTuple:Tuple
    :param coordTuple: (x,y)->koordinatenpaar Ausgangspunkt

    :type linienDictCoord: Dict
    :param linienDictCoord: dictionary mit {linie:{haltestelle:(coord x, coord y)}

    :type bereich: Dict
    :param bereich: Haltestelenbereiche aus JSON-Datei

    :type aufzug: bool
    :param aufzug: true wenn HST mit Aufzug gesucht werden soll

    :type treppe: bool
    :param treppe: true wenn HST mit Rolltreppe gesucht werden soll

    :rtype: string
    :returns: nächster Haltestellenbereich
    """
    minDist = 1000
    for linie, hst in linienDictCoord.items():
        for i, (x,y) in hst.items():
            dist =calcDistance(coordTuple, (x,y))
            if dist < minDist:
                if aufzug == 0 and treppe == 0:
                    minDist = dist
                    nextHst = i
                elif aufzug == 1 and treppe == 0:
                    for HSTB in bereich["features"]:
                        if HSTB["properties"].get("Aufzug") == aufzug and HSTB["properties"]["kurzname"]==i:
                            minDist = dist
                            nextHst = i        
                elif aufzug == 0 and treppe == 1:
                    for HSTB in bereich["features"]:
                        if HSTB["properties"].get("Fahrtreppe") == treppe and HSTB["properties"]["kurzname"]==i:
                            minDist = dist
                            nextHst = i
    return nextHst  

def treppenaufzuege(Fahrtreppen,Aufzuege,HaltestellenBereiche):             # Erstellt von Marco R
    trBereiche = set()
    aufzBereiche = set()
    FahrtreppenAufzuege = set()
    HstBereiche = set()
  
    for treppen in Fahrtreppen["features"]:                                 #Fülle das Set "trBereiche" mit allen Haltestellenbereichen, die Fahrtreppen haben
        trBereiche.add(treppen["properties"]["Haltestellenbereich"])
    
    for aufzuege in Aufzuege["features"]:                                   #Fülle das Set "aufzBereiche" mit allen Haltestellenbereichen, die Haltestellen haben
        aufzBereiche.add(aufzuege["properties"]["Haltestellenbereich"])

    for bereiche in HaltestellenBereiche["features"]:                       #Fülle das Set "HstBereiche" mit allen Haltestellenbereichen
        HstBereiche.add(bereiche["properties"]["Haltestellenbereich"])

    
    FahrtreppenAufzuege = aufzBereiche.intersection(trBereiche)             #Fülle das Set "FahrtreppenAufzuege" mit allen Bereichen die Aufzuege UND Fahrtreppen haben

    Bereicheohne = len(HstBereiche) - (len(FahrtreppenAufzuege) + (len(aufzBereiche) - len(FahrtreppenAufzuege)) + (len(trBereiche) - len(FahrtreppenAufzuege)))   # errechnet die Anzahl der Haltestellenbereiche OHNE Fahrtreppen und/oder Aufzuegen
    
    print (f"\n{(len(trBereiche) - len(FahrtreppenAufzuege))} Haltestellenbereiche haben NUR Fahrtreppen\n{(len(aufzBereiche) - len(FahrtreppenAufzuege))} Haltestellenbereiche haben NUR Aufzuege\n{len(FahrtreppenAufzuege)} Haltestellenbereiche haben Aufzuege UND Fahrtreppen\n{Bereicheohne} Haltestellenbereiche haben weder Fahrtreppe noch Aufzug\n")

    return   

def findNSOW(Haltestellen): # Funktion um die nördlichste, südlichste, östlichste und westlichste Haltestelle zu finden - Erstellt von Marco R.
    NorduSuedlichst = []    # Liste anlegen nur mit der "Nord"Koordinate
    OstuWestlichst = []     # Liste anlegen nur mit der "Ost"Koordinate

    for anz in Haltestellen["features"]:                 # Daten aus dem "Haltestellen"-Dict extrahieren und 2 neue Listen anlegen
        Name = anz['properties']['Name']                 # "Name" extrahieren
        Kurzname = anz['properties']['Kurzname']         # "Kurzname" extrahieren
        KoordOst = anz['geometry']['coordinates'][0]     # "Ost-Koordinate" extrahieren
        KoordNord = anz['geometry']['coordinates'][1]    # "Nord-Koordinate" extrahieren

        NorduSuedlichst.append([KoordNord,Name, Kurzname])  # Daten "KoordNord", "Name" und "Kurzname" an Liste "NorduSuedlichst" anhängen
        OstuWestlichst.append([KoordOst, Name, Kurzname])   # Daten "KoordOst", "Name" und "Kurzname" an Liste "OstuWestlichst" anhängen

    NorduSuedlichst.sort()  # Liste aufsteigende sortieren
    print ("Der am weitesten südlich liegende Haltestellenbereich ist :", NorduSuedlichst[0][1], "-", NorduSuedlichst[0][2])  # 1. Eintrag aus sortierter Liste "NorduSuedlichst" ausgeben => niedrigste Nord-Koordinate = südlichster Haltestellenbereich
    NorduSuedlichst.sort(reverse=True)  # Liste absteigend sortieren
    print ("Der am weitesten nördlich liegende Haltestellenbereich ist :", NorduSuedlichst[0][1], "-", NorduSuedlichst[0][2]) # 1. Eintrag aus neu sortierter Liste "NorduSuedlichst" ausgeben => höchste Nord-Koordinate = nördlichster Haltestellenbereich
    OstuWestlichst.sort()   # Liste aufsteigende sortieren
    print ("Der am weitesten westlich liegende Haltestellenbereich ist :", OstuWestlichst[0][1], "-", OstuWestlichst[0][2])   # 1. Eintrag aus sortierter Liste "OstuWestlichst" ausgeben => niedrigste Ost-Koordinate = westlichster Haltestellenbereich
    OstuWestlichst.sort(reverse=True)   # Liste absteigend sortieren
    print ("Der am weitesten östlich liegende Haltestellenbereich ist :", OstuWestlichst[0][1], "-", OstuWestlichst[0][2])    # 1. Eintrag aus neu sortierter Liste "OstuWestlichst" ausgeben => höchste Ost-Koordinate = östlichster Haltestellenbereich
    print (" ")

    return

def meisteLinienUHaltestellen(Haltestellen,HaltestellenBereiche):  # Welcher Haltestellenbereich hat die meisten Linien und welcher Bereich die meisten Haltestellen - Erstellt von Marco R.
    ErgebnisListe = []

    # Filter des Haltestellenbereiches mit den meisten Linien
    for feature in HaltestellenBereiche["features"]:
                properties = feature["properties"]
                halt_name = properties["Haltestellenname"]
                linien_str = properties.get("Linien", "")                                       # Fehlt ein Eintrag bei Linien 'Linien', dann filtern
                linien = [linien.strip() for linien in linien_str.split() if linien.strip()]    # Aufteilen des Eintrags und entfernen des Leerzeichens
                anzahl = len(linien)
                ErgebnisListe.append([anzahl, linien, halt_name]) #Füge eine neue Liste zusammen

    ErgebnisListe.sort(reverse=True)  # Sortiert "ErgebnisListe" absteigend nach dem ersten Eintrag "anzahl"
    print(ErgebnisListe[0][2]," hat mit ",ErgebnisListe[0][0]," Linien die meisten Linien im Haltestellenbereich")


    # Filter des Haltestellenbereiches mit den meisten Haltestellen
    Namen = [feature['properties']['Name'] for feature in Haltestellen["features"] if "properties" in feature and "Name" in feature["properties"]]  # Extrahiert eine Liste mit den Namen der Haltestellenbereiche zu allen Haltestellen
    
    zaehler = Counter(Namen)  
    haeufigsterName = zaehler.most_common(1)[0][0]  #Häufigster Name in der Liste mit Counter-Funktion auslesen
    Anzahl = zaehler.most_common(1)[0][1]  # Wie oft kommt der häufigste Name in der Liste vor
    print("Der Haltestellenbereich mit den meisten Haltestellen ist: ",haeufigsterName , "mit", Anzahl, "Haltestellen")

    return 

def kurznToHSTname(hst, bereiche):
    """ Description
    :type hst:String
    :param hst:kurzname der haltestelle

    :type bereiche:dict
    :param bereiche:dict Haltestellenbereiche wie im JSON-File

    :rtype:String
    :returns:Voller Name der Haltestelle
    """
    for element in bereiche["features"]:
        if element["properties"]["kurzname"]==hst:
            return element["properties"]["Haltestellenname"]
    

def haversine(lon1, lat1, lon2, lat2):
    ''' 
        Berechnet die Distanz zwischen zwei Koordinatenpaaren auf einer Kugeloberfläche (hier Erde) ---> geklaut von GPT

        Parameter: zwei Parameterpaare x, y

        Rückgabe: Entfernung in Kilometern
    '''
    # Konvertiere Grad in Radianten
    lon1, lat1, lon2, lat2 = map(math.radians, [lon1, lat1, lon2, lat2])

    # Haversine-Formel
    dlon = lon2 - lon1
    dlat = lat2 - lat1
    a = math.sin(dlat/2)**2 + math.cos(lat1) * math.cos(lat2) * math.sin(dlon/2)**2
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1-a))

    # Radius der Erde in Kilometern
    R = 6371.0
    distance = R * c

    return distance

####                main            ####

folder = 'json'
dicts = {}
linienDict={}
umsteigenDict ={}
#coordTup = (6.96453, 50.95413)

for dateiname in os.listdir('json'):                            #gehe durch jede Datei im folder "json"
    filenameIter, _ = os.path.splitext(dateiname)               #trenne name von suffix
    with open('json/'+filenameIter+'.json', 'r') as file:       #öffne jedes file und schreibe inhalt in dictionary mit filename als key
        dicts[filenameIter]=json.load(file)

linienDict=createLinienDict(dicts["haltestellenbereiche"])
linienDictCoord=addCoordinates(linienDict, dicts["haltestellen"])
writeKcenterToDict(dicts)
writeTrepAufzToDict(dicts)
bereichsAnalyse(dicts["haltestellenbereiche"])
countIntersects(linienDict)
findkCenter(dicts["haltestellenbereiche"], linienDict)
treppenaufzuege(dicts["fahrtreppen"],dicts["aufzuege"],dicts["haltestellenbereiche"])
findNSOW(dicts["haltestellen"])
meisteLinienUHaltestellen(dicts["haltestellen"],dicts["haltestellenbereiche"])

while True:
    try:
        HSTErmitt=input("Möchten Sie die Reihenfolge von Haltestellen einer Linie ermitteln? 'n' für Nein, 'j' für Ja: ")
        if HSTErmitt not in ["j", "n"]:
            raise ValueError("Bitte 'j' oder 'n' eingeben.")
        if HSTErmitt=="n":
            break
        linie2Sort=input("Für welche Linie möchten Sie eine Reihenfolge der Haltestellen ermitteln?:")
        if linie2Sort not in linienDict.keys():
                raise ValueError("Diese Linie gibt es nicht.")
        final = finalHST(linienDictCoord, linie2Sort)
        sortedHstList = sortHST(final, linienDictCoord, linie2Sort)
        pprint.pprint(sortedHstList)
    except ValueError as e:
        print(f"Ungültige Eingabe: {e}")
        continue

while True:
    try:
        punktSuche=input("möchten Sie eine nahegelegene Haltestelle finden? 'n' für Nein, 'j' für Ja: ")
        if punktSuche not in ["j", "n"]:
            raise ValueError("Bitte 'j' oder 'n' eingeben.")
    except ValueError as e:
        print(f"Ungültige Eingabe: {e}")
        continue
    break

if punktSuche == "j":
    while True:
        try:
            coord_input = input("Bitte geben Sie ein x/y-Koordinatenpaar ein, von dem aus Sie die nächste Haltestelle erreichen wollen:")
            coordTup = tuple(map(float, coord_input.split(',')))
            if len(coordTup) != 2:
                raise ValueError("Es müssen genau zwei Werte eingegeben werden.")
            aufzugReq=int(input("Soll ein Aufzug vorhanden sein? 0 für Nein, 1 für Ja: "))
            if aufzugReq not in [0, 1]:
                raise ValueError("Bitte '0' oder '1' eingeben.")
            treppeReq=int(input("soll eine Rolltreppe vorhanden sein? 0 für Nein, 1 für Ja: "))
            if treppeReq not in [0, 1]:
                raise ValueError("Bitte '0' oder '1' eingeben.")
            nextHst=findNextHst((coordTup), linienDictCoord, dicts["haltestellenbereiche"], aufzugReq, treppeReq)
            print(f"Nächste Haltestelle ist: {kurznToHSTname(nextHst, dicts['haltestellenbereiche'])}")
            again = input("noch ein Haltestelle suchen?")
            if again not in ["j", "n"]:
                raise ValueError("Bitte 'j' oder 'n' eingeben.")
            if (again =="n"):
                break
        except ValueError as e:
            print(f"Ungültige Eingabe: {e}")
            continue

#print(f"lenau -> NBS = {calcDistance((6.91831,50.95864),(6.92386, 50,95722))}, lenau ->SSG ={calcDistance((6.91831,50.95864), (6.92128, 50,95469))}")
pass