import pprint

########## Anlegen der Struktur der Hauptdatei {main_data} und Auffueren der gegebenen Dateinamen, die eingelesen werden sollen. ##########

main_data = {'HST': {'ASS': {} }, 'HSTB' : {}}
filenames = {'HSTB_dfi' : "haltestellenbereichemitdfi.json", 
             'HSTB' : "haltestellenbereiche.json", 
             'HST' : "haltestellen.json", 
             'FTS' : "fahrtreppenstoerungen.json", 
             'FT' : "fahrtreppen.json", 
             'AZS' : "aufzugstoerungen.json", 
             'AZ' : "aufzuege.json",
             'VO' : "verkaufsorte.json"}

########## Import der Einlesefunktionen und Einlesen der JSON Datenstrukturen in die Hauptdatei {main_data}. ##########

from funktionsbibliothek import HSTB, HST, HSTB_dfi, AZ, AZS, FT, FTS, VO

HSTB(filenames['HSTB'], main_data)
HST(filenames['HST'], main_data)
HSTB_dfi(filenames['HSTB_dfi'], main_data)
AZ(filenames['AZ'], main_data)
AZS(filenames['AZS'], main_data)
FT(filenames['FT'], main_data)
FTS(filenames['FTS'], main_data)
VO(filenames['VO'], main_data)


#########################################################################################################################
# Aufgabe 1.1: Wie viele Linien (Busse und Bahnen) und wie viele Haltestellenbereiche gibt es insgesamt?                #
#                                                                                                                       #
# main_data (dict)                                          # Hauptdatenstruktur                                        #
# │                                                                                                                     #
# ├── HSTB (dict)                                           # Haltestellenbereiche        === Hier sind die Daten! ===  #
# │   └──                                                                                                               #
# │                                                                                                                     #
# ├── HST (dict)                                            # Haltestellen                                              #
# │   └── ASS (dict)                                        # Assoziierte Daten zu Haltestellen                         #
# │       ├── 111 (dict)                                    # Haltestellen-ID                                           #
# │       │   ├── Linien (set): {"1", "7", "9"}             # Liniennummern               === Hier sind die Daten! ===  #
# │       │   ├── Name (str): "Heumarkt"                    # Name der Haltestelle                                      #
#                                                                                                                       #
#########################################################################################################################
# Vorgehensweise: - zunächst werden alle Linien in einem set() gesammelt um Duplikate zu vermeiden.                     #
#                 - danach wird weiter über die linien iteriert und über eine if verzweigung zwischen strab und bus     #
#                   unterschieden und jeweils in ein set() abgelegt. Die Unterscheidung erfolgt durch größer/ kleiner.  #
#                 - Die Haltestellenbereiche sind in der Datenstruktur bereits gruppiert und können einfach ausgegeben  #
#                   werden.                                                                                             #
#########################################################################################################################

alle_linien = set()
strab_linien = set()
bus_linien = set()

# Daten sammeln                                                      
for eintrag in main_data['HST']['ASS'].values():        # .values holt werte verliert aber weitere Schlüssel in eintrag
    if 'Linien' in eintrag:                             # Prüfung ob daten vorhanden, leeres set(), wenn keine Linien vorhanden
        alle_linien.update(eintrag['Linien'])           # Alle Linien in ein set einfügen

# Unterscheiden in STRAB und BUS
for eintrag in alle_linien:
    if int(eintrag) < 100:                              # Schleife alle zahleneinträge (deshalb int) < 100 sind Bahnlinien
        strab_linien.add(eintrag)
    if int(eintrag) > 100:
        bus_linien.add(eintrag)                         # Schleife alle zahleneinträge (deshalb int) > 100 sind Buslinien

print(f'================================================================================') 
print(f'Aufgabe 1.1: Wie viele Linien (Busse und Bahnen) und wie viele Haltestellenbereiche gibt es insgesamt?\n')
print(f"- Es gibt {len(main_data['HSTB'])} Haltestellenbereiche im Netz der KVB.")
print(f"- Es gibt {len(alle_linien)} Linien im Netz der KVB.\n- Davon sind {len(strab_linien)} Bahnlinien und {len(bus_linien)} Buslinien")
print(f'================================================================================')


#########################################################################################################################
# Aufgabe 1.2: Welcher Haltestellenbereich hat die meisten Haltestellen und an welchem Treffen sich die meisten Linien? #
#                                                                                                                       #
# main_data (dict)                                          # Hauptdatenstruktur                                        #
# │                                                                                                                     #
# ├── HSTB (dict)                                           # Haltestellenbereiche                                      #
# │   └──                                                                                                               #
# │                                                                                                                     #
# ├── HST (dict)                                            # Haltestellen                                              #
# │   └── ASS (dict)                                        # Assoziierte Daten zu Haltestellen                         #
# │       ├── 111 (dict)                                    # Haltestellen-ID                                           #
# │       │   ├── Linien (set): {"1", "7", "9"}             # Liniennummern               === Hier sind die Daten! ===  #
# │       │   ├── Name (str): "Heumarkt"                    # Name der Haltestelle        === Hier sind die Daten! ===  #
#                                                                                                                       #
#########################################################################################################################
# Vorgehensweise: - dict anlegen mit haupschlüssel Haltestellen "HST" und weiteren schlüsseln für 'Namen' und 'Linien', #
#                   Namen werden listen gespeichert da Duplikate zum zählen benötigt werden, linien als set()           #
#                 - Haltestellen in jedem Haltestellenbereich zählen                                                    #
#                 - Häufigsten Haltestellenamen und Anzahl der Haltestellen bestimmen                                   #
#########################################################################################################################                 
    
# Counter zum auszählen über from collections import counter, könnte auch funktionieren, probieren falls Zeit und Lust...
 
max_linien_hst = {'HST' : {'Name': [],                                      # Daten sammeln alle Namen (mit duplikaten)
                           'Linien': set()}}                                # alle Linien (ohne duplikate)
max_hstb = 0                                                                # Häufigster Haltestellenbereich                                 
max_hst = 0                                                                 # Anzahl Haltestellen

# Daten sammeln 
if 'HST' in main_data and 'ASS' in main_data['HST']:                        # Prüfung ob daten vorhanden
    for eintrag in main_data['HST']['ASS'].values():                        # Schleife über 'ASS'
        if 'Name' in eintrag:
            max_linien_hst['HST']['Name'].append(eintrag['Name'])           # Haltestellenname in max_linien_hst schreiben
        if 'Linien' in eintrag:
            max_linien_hst['HST']['Linien'].update(eintrag['Linien'])       # Linien in max_linien_hst schreiben

# Haltestellen pro Haltestellenbereich zählen
namen_zaehler = {}
for name in max_linien_hst['HST']['Name']:
    namen_zaehler[name] = namen_zaehler.get(name, 0) + 1                    # .get holt den Wert des Schlüssels, start bei 0
                                                                            # + 1 zum hochzählen

# Häufigsten Haltestellenamen bestimmen
max_hstb = max(namen_zaehler, key=namen_zaehler.get)                        # Häufigster Haltestellenbereich
max_hst = namen_zaehler[max_hstb]                                           # Anzahl Haltestellen

print(f"Aufgabe 1.2: Welcher Haltestellenbereich hat die meisten Haltestellen und an welchem Treffen sich die meisten Linien?\n")
print(f"- Der Haltestellenbereich {max_hstb} hat mit {max_hst} die meisten Haltestellen")
print(f'================================================================================')


#########################################################################################################################
# Aufgabe 1.3: Wieviel Haltestellenbereiche haben Fahrtreppen, Aufzüge, beides oder keines von beidem?                  #
#                                                                                                                       #
# main_data (dict)                                          # Hauptdatenstruktur                                        #
# │                                                                                                                     #
# ├── HSTB (dict)                                           # Haltestellenbereiche                                      #
# │   └── 15250 (dict)                                      # Bereich-ID                                                #
# │       ├── Betriebsbereich (str): "BUS"                  # Betriebsbereich                                           #
# │       ├── DFI (str): "N"                                # Dynamische Fahrgastinformationen                          #
# │       ├── Haltestellenname (str): "Osterather Str."     # Name der Haltestelle                                      #
# │       ├── Linien (set): {"127"}                         # Liniennummern                                             #
# │       ├── VRSNummer (str): "15250"                      # VRS-Nummer                                                #
# │       ├── kurzname (str): "ORR"                         # Kürzel der Haltestelle                                    #
# │       ├── Aufzuege (dict): None                         # Aufzüge                   === Hier sind die Daten! ===    #
# │       ├── Fahrtreppen (dict): None                      # Fahrtreppen               === Hier sind die Daten! ===    #
# │       └── Verkaufsort (dict): None                      # Verkaufsort                                               #
#                                                                                                                       #
#########################################################################################################################
# Vorgehensweise: - einfache variablen zum zählen anlegen für nur Aufzüge, nur Fahrtreppen, beides und ohne             #   
#                 - jeweils durch einfache if verzweigungen unterscheiden und hochzählen                                #
#########################################################################################################################

hstb_nur_az = 0                 # Zähler nur Aufzüge
hstb_nur_ft = 0                 # Zähler nur Fahrtreppen
hstb_beides = 0                 # Zähler beides
hstb_ohne = 0                   # Zähler ohne

# Unterscheiden und hochzählen
for eintrag in main_data['HSTB']:
    if main_data['HSTB'][eintrag].get('Aufzuege') and main_data['HSTB'][eintrag].get('Fahrtreppen') == None:    # Aufzüge True und Fahrtreppen None
        hstb_nur_az += 1
    if main_data['HSTB'][eintrag].get('Fahrtreppen') and main_data['HSTB'][eintrag].get('Aufzuege') == None:    # Fahrtreppen True und Aufzüge None 
        hstb_nur_ft += 1
    if main_data['HSTB'][eintrag].get('Aufzuege') and main_data['HSTB'][eintrag].get('Fahrtreppen'):            # Aufzüge True und Fahrtreppen True
        hstb_beides += 1
    if main_data['HSTB'][eintrag].get('Aufzuege') == None and main_data['HSTB'][eintrag].get('Fahrtreppen') == None:  # Aufzüge None und Fahrtreppen None
        hstb_ohne += 1

print(f"Aufgabe 1.3: Wieviel Haltestellenbereiche haben Fahrtreppen, Aufzüge, beides oder keines von beidem?\n")
print(f'- {hstb_nur_az} Haltestellenbereiche haben nur Aufzüge')
print(f'- {hstb_nur_ft} Haltestellenbereiche haben nur Fahrtreppen')
print(f'- {hstb_beides} Haltestellenbereiche haben beides')
print(f'- {hstb_ohne} Haltestenebereiche haben weder Aufzüge noch Fahrtreppen')
print(f'================================================================================')


#########################################################################################################################
# Aufgabe 1.4: Wieviel Haltestellenbereiche decken jeweils die Betriebsbereich „BUS“, „STRAB“ oder beides ab?           #
#                                                                                                                       #
# main_data (dict)                                          # Hauptdatenstruktur                                        #
# │                                                                                                                     #
# ├── HSTB (dict)                                           # Haltestellenbereiche                                      #
# │   └── 15250 (dict)                                      # Bereich-ID                                                #
# │       ├── Betriebsbereich (str): "BUS"                  # Betriebsbereich            === Hier sind die Daten! ===   #
# │       ├── DFI (str): "N"                                # Dynamische Fahrgastinformationen                          #
# │       ├── Haltestellenname (str): "Osterather Str."     # Name der Haltestelle                                      #
# │       ├── Linien (set): {"127"}                         # Liniennummern                                             #
# │       ├── VRSNummer (str): "15250"                      # VRS-Nummer                                                #
# │       ├── kurzname (str): "ORR"                         # Kürzel der Haltestelle                                    #
# │       ├── Aufzuege (dict): None                         # Aufzüge                                                   #
# │       ├── Fahrtreppen (dict): None                      # Fahrtreppen                                               #
# │       └── Verkaufsort (dict): None                      # Verkaufsort                                               #
# │
#########################################################################################################################
# Vorgehensweise: - Grundsätzlich gleiche Vorgehensweise wie 1.3                                                        #
#                 - einfache variablen zum zählen anlegen für BUS, STRAB und , beides                                   #
#                 - jeweils durch einfache if verzweigungen unterscheiden und hochzählen                                #
#########################################################################################################################

hstb_nur_bus = 0                    # Zähler BUS
hstb_nur_strab = 0                  # Zähler STRAB
hstb_bus_und_strab = 0                   # Zähler BUS und STRAB

# Unterscheiden und hochzählen 
for eintrag in main_data['HSTB']:
    if main_data['HSTB'][eintrag].get('Betriebsbereich') == "BUS":          # Wenn eintrag "BUS" hochzählen
        hstb_nur_bus += 1
    if main_data['HSTB'][eintrag].get('Betriebsbereich') == "STRAB":        # Wenn eintrag "STRAB" hochzählen
        hstb_nur_strab += 1
    if main_data['HSTB'][eintrag].get('Betriebsbereich') == "BUS STRAB":    # Wenn eintrag "BUS STRAB" hochzählen
        hstb_bus_und_strab += 1

print(f"Aufgabe 1.4: Wieviel Haltestellenbereiche decken jeweils die Betriebsbereich „BUS“, „STRAB“ oder beides ab?\n")
print(f'- {hstb_nur_bus} Haltestellenbereiche haben nur Buslinien')
print(f'- {hstb_nur_strab} Haltestellenbereiche haben nur Straßenbahnlinien')
print(f'- {hstb_bus_und_strab} Haltestellenbereiche haben Bus- und Straßenbahnlinien')
print('================================================================================')


#########################################################################################################################
# Aufgabe 1.5: Bestimme den nördlichsten, westlichsten, südlichsten und östlichsten Haltstellenbereich.                 #
#              Wie kann man die Position eines Haltestellenbereichs berechnen?                                          #
#                                                                                                                       #
#    Wenn mehrere Koordinaten vorliegen und ermittelt werden soll, welche davon am weitesten südlich, östlich,          #
#    nördlich oder westlich liegt:                                                                                      #
#                                                                                                                       #
#   # 1. Weitesten Süden                                                                                                #
#        Suche nach der Koordinate mit dem kleinsten Breitengrad (niedrigster Wert).                                    #
#        Beispiel: Von den Koordinaten (30,10),(−20,40),(50,−60)(30,10),(−20,40),(50,−60) liegt (-20, 40) am            #
#        weitesten südlich.                                                                                             #
#                                                                                                                       #
#   # 2. Weitesten Norden                                                                                               #
#        # Suche nach der Koordinate mit dem größten Breitengrad (höchster Wert).                                       #
#        # Beispiel: Von (30,10),(−20,40),(50,−60)(30,10),(−20,40),(50,−60) liegt (50, -60) am weitesten nördlich.      #
#                                                                                                                       #
#   # 3. Weitesten Osten                                                                                                #
#        # Suche nach der Koordinate mit dem größten Längengrad (höchster Wert).                                        #
#        # Beispiel: Von (30,10),(−20,40),(50,−60)(30,10),(−20,40),(50,−60) liegt (-20, 40) am weitesten östlich.       #
#                                                                                                                       #
#   # 4. Weitesten Westen                                                                                               #
#        # Suche nach der Koordinate mit dem kleinsten Längengrad (niedrigster Wert).                                   #
#        # Beispiel: Von (30,10),(−20,40),(50,−60)(30,10),(−20,40),(50,−60) liegt (50, -60) am weitesten westlich.      #
#                                                                                                                       #
# main_data (dict)                                          # Hauptdatenstruktur                                        #
# │                                                                                                                     #
# ├── HSTB (dict)                                           # Haltestellenbereiche                                      #
# │   └──                                                                                                               #
# │                                                                                                                     #
# ├── HST (dict)                                            # Haltestellen                                              #
# │   └── ASS (dict)                                        # Assoziierte Daten zu Haltestellen                         #
# │       ├── 111 (dict)                                    # Haltestellen-ID                                           #
# │       │   ├── Linien (set): {"1", "7", "9"}             # Liniennummern                                             #
# │       │   ├── Name (str): "Heumarkt"                    # Name der Haltestelle                                      #
# │       │   ├── Kurzname (str): "HMG"                     # Kürzel der Haltestelle                                    #
# │       │   ├── Betriebsbereich (str): "STRAB"            # Betriebsbereich                                           #
# │       │   └── coordinates (tuple): (6.96046, 50.93576)  # Koordinaten            == Hier sind die Daten! ===        #
#########################################################################################################################
# Vorgehensweise: - einfache variablen anlegen und startwert festlegen, abhängig davon aus welcher richtung verglichen  #
#                   werden muss. Dazu noch variablen für die ausgabe des jeweils festgestellten Haltestellenbereichs    #
#                 - iterieren über alle Koordinaten in main_data[HST]                                                   #
#                   z.B. nördlichste Haltestelle liegt logischerweise im nördlichsten Haltestellenbereich               #
#                 - jeweils durch einfache if verzweigungen mit größer/kleiner unterscheiden und Haltestelle zuordnen   #
#########################################################################################################################

hstb_nord = 0           # größter Breitengrad gesucht, deshalb start bei 0
eintrag_nord = ''
hstb_sued = 100         # kleinster Breitengrad gesucht, deshalb start bei 100
eintrag_sued = ''
hstb_west = 100         # kleinster Längengrad gesucht, deshalb start bei 0
eintrag_west = ''
hstb_ost = 0            # größter Längengrad gesucht, deshalb start bei 100
eintrag_ost = ''

# Unterscheiden und zuordnen
for eintrag in main_data['HST']['ASS']:
    laengengrad, breitengrad = main_data['HST']['ASS'][eintrag].get('coordinates')
    if breitengrad > hstb_nord:             # größter Breitengrad = Norden
        hstb_nord = breitengrad
        eintrag_nord = eintrag
    if breitengrad < hstb_sued:             # kleinster Breitengrad = Süden
        hstb_sued = breitengrad
        eintrag_sued = eintrag
    if laengengrad < hstb_west:             # kleinster Längengrad = Westen
        hstb_west = laengengrad
        eintrag_west = eintrag
    if laengengrad > hstb_ost:              # größter Längengrad = Osten
        hstb_ost = laengengrad
        eintrag_ost = eintrag

print(f"Aufgabe 1.5: Bestimme den nördlichsten, westlichsten, südlichsten und östlichsten Haltstellenbereich.\nWie kann man die Position eines Haltestellenbereichs berechnen?\n")
print(f"- {main_data['HST']['ASS'][eintrag_nord]['Name']} ist der nördlichste Haltestellenbereich")
print(f"- Koordinaten: {main_data['HST']['ASS'][eintrag_nord]['coordinates']}")
print(f"- {main_data['HST']['ASS'][eintrag_sued]['Name']} ist der südlichste Haltestellenbereich")
print(f"- Koordinaten: {main_data['HST']['ASS'][eintrag_sued]['coordinates']}")
print(f"- {main_data['HST']['ASS'][eintrag_west]['Name']} ist der westlichste Haltestellenbereich")
print(f"- Koordinaten: {main_data['HST']['ASS'][eintrag_west]['coordinates']}")
print(f"- {main_data['HST']['ASS'][eintrag_ost]['Name']} ist der östlichste Haltestellenbereich")
print(f"- Koordinaten: {main_data['HST']['ASS'][eintrag_ost]['coordinates']}")
print('================================================================================')
print('================================================================================')


#########################################################################################################################
# Aufgabe 2.1: Welche beiden Linien haben die größte Anzahl gemeinsamer Stationen?                                      #
#                                                                                                                       #
# main_data (dict)                                          # Hauptdatenstruktur                                        #
# │                                                                                                                     #
# ├── HSTB (dict)                                           # Haltestellenbereiche                                      #
# │   └──                                                                                                               #
# │                                                                                                                     #
# ├── HST (dict)                                            # Haltestellen                                              #
# │   └── ASS (dict)                                        # Assoziierte Daten zu Haltestellen                         #
# │       ├── 111 (dict)                                    # Haltestellen-ID                                           #
# │       │   ├── Linien (set): {"1", "7", "9"}             # Liniennummern              === Hier sind die Daten! ===   #                        
# │       │   ├── Name (str): "Heumarkt"                    # Name der Haltestelle                                      #
# │       │   ├── Kurzname (str): "HMG"                     # Kürzel der Haltestelle                                    #
# │       │   ├── Betriebsbereich (str): "STRAB"            # Betriebsbereich                                           #
# │       │   └── coordinates (tuple): (6.96046, 50.93576)  # Koordinaten                                               #
# │       |                                                                                                             #
# └── Weitere Hauptschlüssel (falls vorhanden)              # Platzhalter für zusätzliche Schlüssel in main_data        #
#                                                                                                                       #
#########################################################################################################################
# Vorgehensweise: - Grundsätzlich müssen pro linie haltestellen gesammelt und in einem set() gespeichert werden.        #
#                   werden muss. Dazu noch variablen für die ausgabe des jeweils festgestellten Haltestellenbereichs    #
#                 - Es werden überschneideungen der sets der einzelnen Linien gebildet                                  #
#                 - das nach den überschneidungen größte set() ist die gesuchte Linie                                   #
#########################################################################################################################

haltestellen_zu_linien = {}                                     # Leeres Dict: Schlüssel = Linien, Wert = Set mit Haltestellen

# Daten sammeln
for eintrag in main_data['HST']['ASS']:                         # Äußere Schleife durch alle Haltestellen in main_data
    if 'Linien' in main_data['HST']['ASS'][eintrag]:            # Prüfen ob Linien vorhanden sind
        linien = main_data['HST']['ASS'][eintrag]['Linien']     # linien = set mit allen möglichen linien 
    if 'Name' in main_data['HST']['ASS'][eintrag]:              # Prüfen ob Name vorhanden sind
        namen = main_data['HST']['ASS'][eintrag]['Name']        # name = String mit dem Namen der Haltestelle
      
    for linie in linien:                                        # Innere Schleife über alle Linien dieser Haltestelle
        if linie not in haltestellen_zu_linien:                 # Prüfen ob Eintrag z.B. Linie '1' vorhanden ist
            haltestellen_zu_linien[linie] = set()               # wenn nicht vorhanden wird er angelegt
        haltestellen_zu_linien[linie].add(namen)                # alle Haltestellen werden als set() zu den Linien hinzugefügt
  
"""pprint.pprint(haltestellen_zu_linien)"""

# Kombinationen aller Linienpaarungen erzeugen
linien = list(haltestellen_zu_linien.keys())                    # Linien als Schlüssel des Dictionaries haltestellen_zu_linien
gesuchte_linien = tuple()                                       # ergebnis sind 2 Linien -> tuple
max_gem_hst = 0                                                 # anzahl der meisten überschneidungen

for i in range(len(linien)):                                    # Äussere Schleife mit range
    for j in range(i + 1, len(linien)):                         # Innere Schleife mit range und versatz von 1, damit nicht die gleichen Linien miteinander... war schmerzhaft...
        linie_1 = linien[i]                                     # Variable für erste Linie, wird bei jedem durchlauf überschrieben
        linie_2 = linien[j]                                     # Variable für zweite Linie, wird bei jedem durchlauf überschrieben
        schnittmenge_hst = haltestellen_zu_linien[linie_1].intersection(haltestellen_zu_linien[linie_2])        # Schnittmenge, wird bei jedem durchlauf überschrieben 
        if len(schnittmenge_hst) > max_gem_hst:                 # vergleich ob aktuelle Schnittmenge größer ist als die erste (0) oder vorangegangene 
            max_gem_hst = len(schnittmenge_hst)                 # wenn die aktuelle Schnittmenge größer ist wird max_gem_hst überschrieben
            gesuchte_linien = (linie_1, linie_2)                # wenn die aktuelle Schnittmenge größer ist wird linie_1 und linie_2 in gesuchte linien übernommen === Ergebnis! === 

print(f"Aufgabe 2.1: Welche beiden Linien haben die größte Anzahl gemeinsamer Stationen?\n")
print(f'Die Linien {gesuchte_linien} haben die meisten gemeinsamen Haltestellen ({max_gem_hst})')
print('================================================================================')


#########################################################################################################################
# Aufgabe 2.2: Welche Linie ist an all ihren Haltestellen prozentual am besten mit digitalen Fahrgast-                  #
#              informationsanzeigen ausgestattet? Das gleiche auch für Fahrtreppen und Aufzüge.                         #
#                                                                                                                       #
# main_data (dict)                                          # Hauptdatenstruktur                                        #
# │                                                                                                                     #
# ├── HSTB (dict)                                           # Haltestellenbereiche                                      #
# │   └── 15250 (dict)                                      # Bereich-ID                                                #
# │       ├── Betriebsbereich (str): "BUS"                  # Betriebsbereich                                           #
# │       ├── DFI (str): "N"                                # Dynamische Fahrgastinfo.   === Hier sind die Daten! ===   #
# │       ├── Haltestellenname (str): "Osterather Str."     # Name der Haltestelle       === Hier sind die Daten! ===   #
# │       ├── Linien (set): {"127"}                         # Liniennummern              === Hier sind die Daten! ===   #
# │       ├── VRSNummer (str): "15250"                      # VRS-Nummer                                                #
# │       ├── kurzname (str): "ORR"                         # Kürzel der Haltestelle                                    #
# │       ├── Aufzuege (dict): None                         # Aufzüge                    === Hier sind die Daten! ===   #
# │       ├── Fahrtreppen (dict): None                      # Fahrtreppen                === Hier sind die Daten! ===   #
# │       └── Verkaufsort (dict): None                      # Verkaufsort                                               #
#                                                                                                                       #
#########################################################################################################################
# Vorgehensweise: - Grundsätzlich Ähnlich der Vorangegangenen Aufgabe. Daten müssen aber neu gesammelt werden und       #
#                   können nicht von der vorherigen Aufgabe übernommen werden,da die Struktur nicht gleich angelegt ist #
#                   ['HSTB'] und ['HST'] (hat lange gedauert die Ursache für den Fehler im Ergebnis zu finden)          #
#                 - Es werden überschneideungen der sets der einzelnen Linien gebildet                                  #
#                 - das nach den überschneidungen größte set() ist die gesuchte Linie                                   #
#########################################################################################################################

linien_mit_hst = {}                                 # Leeres Dictionary: Schlüssel = Linien, Wert = Set mit Haltestellen

# Daten sammeln
for eintrag in main_data['HSTB']:                                # Schleife durch alle Haltestellenbereiche in main_data
    linien = main_data['HSTB'][eintrag].get('Linien', [])        # sicherer abruf der linien mit .get = set mit allen möglichen linien, falls nicht vorhanden, leere liste
    hst_namen = main_data['HSTB'][eintrag].get('Haltestellenname', [])      # sicherer abruf der namen mit .get = String mit dem Namen der Haltestelle, falls nicht vorhanden, leere liste
    
    if hst_namen:                                        # prüfen ob Eintrag vorhanden ist
        for linie in linien:                             # Innere Schleife über alle Linien      
            if linie not in linien_mit_hst:              # Prüfen ob Eintrag z.B. Linie '1' vorhanden ist
                linien_mit_hst[linie] = set()            # wenn nicht vorhanden wird er angelegt
            linien_mit_hst[linie].add(hst_namen)         # alle Namen (Haltestellen) werden als set() zu den jeweiligen Linien

"""pprint.pprint(linien_mit_hst)"""

# Haltestellen und DFI zählen
linien_dfi_abdeckung = {}                           # Leeres Dictionary: Schlüssel = Linien, Wert = Abdeckung in %

for linie, haltestellen in linien_mit_hst.items():                          # Über jede Linie iterieren
    hst_gesamt = len(haltestellen)                                          # Anzahl Haltestellen pro Linie
    hst_mit_dfi = 0                                                         # Anzahl der Haltestellen mit DFI

    for hst in haltestellen:                                                # Über die Haltestellen der Linie iterieren
        for eintrag in main_data['HSTB']:                                   # Suche in main_data['HSTB']
            hst_name = main_data['HSTB'][eintrag].get('Haltestellenname')   # Haltestellenname holen
            dfi_status = main_data['HSTB'][eintrag].get('DFI')              # DFI vorhanden Y / N holen

            if hst_name == hst and dfi_status == "Y":                       # Wenn DFI == "Y"
                hst_mit_dfi += 1                                            # Haltestellen mit DFI hochzählen

    # Abdeckung in Prozent
    linien_dfi_abdeckung[linie] = (hst_mit_dfi / hst_gesamt) * 100 if hst_gesamt > 0 else 0   # Berechnung Abdeckung in Prozent

"""print("DFI-Abdeckung pro Linie:", linien_dfi_abdeckung)"""

# Beste Linie mit DFI ermitteln und Abdeckung ausgeben
beste_linien_dfi = []               # Liste, da bei durchsicht der Daten mehr als eine linie 100% abdeckung erreicht (laut Lösung falsch)                      
bester_wert_dfi = 0                 # Höchster Prozentwert

###### Hier hat chatgpt geholfen... irgendwo ist hier ein Bock drin den ich nicht finde ... laut Lösung falsch und eine Leere Linie drin ######
for linie, wert in linien_dfi_abdeckung.items():        # linie und wert iterieren
    if wert > bester_wert_dfi:                              
        bester_wert_dfi = wert                          # wenn wert größer ist, wird bester_wert überschrieben
        beste_linien_dfi = [linie]                      # passende linie zum wert hat nicht funktioniert...chatgpt
    elif wert == bester_wert_dfi:
        beste_linien_dfi.append(linie)                  # Hier ist eine leere linie mit 100%, keine Ahnung wo die herkommt

print(f"Aufgabe 2.2: Welche Linie ist an all ihren Haltestellen prozentual am besten mit digitalen Fahrgastinformationsanzeigen ausgestattet? Das gleiche auch für Fahrtreppen und Aufzüge\n")
print(f"- Linien mit bester DFI-Abdeckung: {beste_linien_dfi} mit {bester_wert_dfi}% Abdeckung")

###### Hier hat chatgpt geholfen... irgendwo ist hier ein Bock drin den ich nicht finde ... laut Lösung falsch und eine Leere Linie drin ######

# Weiter mit Fahrtreppen...
linien_ft_abdeckung = {}

# Haltestellen und Fahrtreppen zählen
for linie, haltestellen in linien_mit_hst.items():                          # Über jede Linie iterieren
    hst_gesamt = len(haltestellen)                                          # Anzahl Haltestellen pro Linie
    ft_hst = 0                                                              # Anzahl der Haltestellen mit Fahrtreppen

    for hst in haltestellen:                                                # Über die Haltestellen der Linie iterieren
        for eintrag in main_data['HSTB']:                                   # Suche in main_data['HSTB']
            hst_name = main_data['HSTB'][eintrag].get('Haltestellenname')   # Haltestellenname holen
            ft_status = main_data['HSTB'][eintrag].get('Fahrtreppen')       # Fahrtreppen info holen

            if hst_name == hst and ft_status != None:                       # Vergleiche Haltestellenname und prüfe auf 'Fahrtreppe' != None
                ft_hst += 1                                                 # Haltestellen mit 'Fahrtreppe' != None hochzählen


    # Abdeckung in Prozent
    linien_ft_abdeckung[linie] = (ft_hst / hst_gesamt) * 100 if hst_gesamt > 0 else 0   # Abdeckung in Prozent

"""print("Fahrtreppen-Abdeckung pro Linie:", linien_ft_abdeckung)"""

# Beste Linie mit Fahrtreppen ermitteln und Abdeckung ausgeben
beste_linien_ft = None                                                      # Hier hat die Lösung gepasst und es ist nur eine Linie                      
bester_wert_ft = 0                                                          # Höchster Prozentwert

for linie, wert in linien_ft_abdeckung.items():                             # linie und wert iterieren
    if wert > bester_wert_ft:                              
        bester_wert_ft = wert                                               # wenn wert größer ist, wird bester_wert überschrieben
        beste_linien_ft = linie                                             # beste linie

print(f"- Linien mit bester Fahrtreppen-Abdeckung: Linie {beste_linien_ft} mit {bester_wert_ft}% Abdeckung")


# Weiter mit Aufzügen...
linien_az_abdeckung = {}

for linie, haltestellen in linien_mit_hst.items():                          # Über jede Linie iterieren
    hst_gesamt = len(haltestellen)                                          # Anzahl Haltestellen pro Linie
    az_hst = 0                                                              # Anzahl der Haltestellen mit Aufzügen

    for hst in haltestellen:                                                # Über die Haltestellen der Linie iterieren
        for eintrag in main_data['HSTB']:                                   # Suche in main_data['HSTB']
            hst_name = main_data['HSTB'][eintrag].get('Haltestellenname')   # Haltestellenname holen
            az_status = main_data['HSTB'][eintrag].get('Aufzuege')          # Aufzuege info holen

            if hst_name == hst and az_status != None:                       # Vergleiche Haltestellenname und prüfe auf 'Aufzuege' != None
                az_hst += 1                                                 # Haltestellen mit 'Aufzuege' != None hochzählen

    # Speichere Abdeckung in Prozent
    linien_az_abdeckung[linie] = (az_hst / hst_gesamt) * 100 if hst_gesamt > 0 else 0   # Abdeckung in Prozent

"""print("Fahrtreppen-Abdeckung pro Linie:", linien_ft_abdeckung)"""

# Beste Linie mit Fahrtreppen ermitteln und Abdeckung ausgeben
beste_linien_az = None                                                      # Hier hat die Lösung gepasst und es ist nur eine Linie                      
bester_wert_az = 0                                                          # Höchster Prozentwert

for linie, wert in linien_az_abdeckung.items():                             # linie und wert iterieren
    if wert > bester_wert_az:                              
        bester_wert_az = wert                                               # wenn wert größer ist, wird bester_wert überschrieben
        beste_linien_az = linie                                             # beste linie

print(f"- Linien mit bester Aufzug-Abdeckung: Linie {beste_linien_az} mit {bester_wert_az}% Abdeckung")
print('================================================================================')

#########################################################################################################################
# Aufgabe 2.3: Der Kölner weiß das eine zweistellige Nummer eine Straßenbahn und eine dreistellige Nummer ein Bus ist.  #
#              Aber könnte man diese Information auch aus den Daten ziehen? Direkt angegeben ist es nicht.              #
#                                                                                                                       #
# main_data (dict)                                          # Hauptdatenstruktur                                        #
# │                                                                                                                     #
# ├── HSTB (dict)                                           # Haltestellenbereiche                                      #
# │   └── 15250 (dict)                                      # Bereich-ID                                                #
# │       ├── Betriebsbereich (str): "BUS"                  # Betriebsbereich           === Hier sind die Daten! ===    #
# │       ├── DFI (str): "N"                                # Dynamische Fahrgastinformationen                          #
# │       ├── Haltestellenname (str): "Osterather Str."     # Name der Haltestelle                                      #
# │       ├── Linien (set): {"127"}                         # Liniennummern             === Hier sind die Daten! ===    #
# │       ├── VRSNummer (str): "15250"                      # VRS-Nummer                                                #
# │       ├── kurzname (str): "ORR"                         # Kürzel der Haltestelle                                    #
# │       ├── Aufzuege (dict): None                         # Aufzüge                                                   #
# │       ├── Fahrtreppen (dict): None                      # Fahrtreppen                                               #
# │       └── Verkaufsort (dict): None                      # Verkaufsort                                               #
#                                                                                                                       #
#########################################################################################################################
# Vorgehensweise: - Die Lösung ist ein Abgleich der des Betriebsbereiches BUS oder STRAB mit der Liniennummer.          #
#                 - 2-Stellige Linien dürfen nur den Betriebsbereich STRAB aufweisen und niemals BUS, damit wäre der    #
#                   Beweis erbracht.                                                                                    #
#########################################################################################################################

# bahnlinien sind aus Aufgabe 1.1 bekannt und können verwendet werden
"""print(bahnlinien)"""
strab_linien = set()                                        # set() für Straßenbahnlinien ohne Duplikate

# Daten sammeln
for eintrag in main_data['HSTB']:                           # Über die Haltestellenbereiche iterieren
    hst = main_data['HSTB'][eintrag]                        # alle Haltestellen holen
    linien = hst.get('Linien', set())                       # Linien der Haltestellen holen
    betriebsbereich = hst.get('Betriebsbereich', set())     # Betriebsbereich der Haltestellen holen
    
    if betriebsbereich == "STRAB":                          # Auf STRAB prüfen
        strab_linien.update(linien)                         # Wenn ja, update auf Straßenbahnlinie === Ergebnis! === 

print(f"Aufgabe 2.3: Der Kölner weiß das eine zweistellige Nummer eine Straßenbahn und eine dreistellige Nummer ein Bus ist.")
print(f"- Aber könnte man diese Information auch aus den Daten ziehen? Direkt angegeben ist es nicht.\n")    
print(f"- Werden die Linien über (STRAB) gefiltert, erhält man nur noch diese Linien:\n {', '.join(strab_linien)},\n welche eindeutig Bahnlinien sind")
print('================================================================================')


#########################################################################################################################
# Aufgabe 2.4: Liste alle Straßenbahnlinien jeweils mit allen Straßenbahnlinien in die man auf ihrem Weg direkt         #   
#              umsteigen kann auf.                                                                                      #
#                                                                                                                       #   
# main_data (dict)                                          # Hauptdatenstruktur                                        #
# │                                                                                                                     #
# ├── HSTB (dict)                                           # Haltestellenbereiche                                      #
# │   └── 15250 (dict)                                      # Bereich-ID                                                #
# │       ├── Betriebsbereich (str): "BUS"                  # Betriebsbereich                                           #
# │       ├── DFI (str): "N"                                # Dynamische Fahrgastinformationen                          #
# │       ├── Haltestellenname (str): "Osterather Str."     # Name der Haltestelle       === Hier sind die Daten! ===   #
# │       ├── Linien (set): {"127"}                         # Liniennummern              === Hier sind die Daten! ===   #
# │       ├── VRSNummer (str): "15250"                      # VRS-Nummer                                                #
# │       ├── kurzname (str): "ORR"                         # Kürzel der Haltestelle                                    #
# │       ├── Aufzuege (dict): None                         # Aufzüge                                                   #
# │       ├── Fahrtreppen (dict): None                      # Fahrtreppen                                               #
# │       └── Verkaufsort (dict): None                      # Verkaufsort                                               #
#                                                                                                                       #
#########################################################################################################################
# Vorgehensweise: - bahnlinien aus linien_mit_hst aus Aufgabe 2.2 extrahieren und schnittmengen bilden                  #
#                   größte schnittmenge entfällt, weil alle Schnittmengen gebraucht werden                              #
#                 - die Schnittmenge je Linie beschreibt die Umsteigemöglichkeiten der Linie                            #
#########################################################################################################################
    
    ##################################################################################################################
    ## Erklärung Dictionary Comprehension:                                                                          ##
    ## - die linien die übernommen werden sollen liegen in "strab_linien" und werden durch "for linie" durch        ##
    ##   iteriert                                                                                                   ##
    ## - if linie in linien_mit_hst ist die ausnahmebehandlung und stellt sicher das nur linien die auch als        ##
    ##   schlüssel in inien_mit_hst existieren berücksichtigt werden                                                ##
    ## - linie: linien_mit_hst[linie] erstellt das neue schlüssel/wertpaar, hier die jeweilige linie als schlüssel  ## 
    ##   und die haltestellen aus linien_mit_hst der jeweiligen linie                                               ##
    ##################################################################################################################


# Linien aus linien_mit_hst übernehmen und auf Straßenbahnlinien reduzieren (Dictionary Comprehension 
# kommt von chatgpt...kannte ich vorher gar nicht)
bahnlinien_dict = {linie: linien_mit_hst[linie] for linie in strab_linien if linie in linien_mit_hst}  # nur noch Bahnlinien  
umstiegsmoegl = {}                                      # dict für die umsteigemöglichkeiten mit linie als schlüssel


for linie1 in strab_linien:                             # strab_linien enthält die nummern der straßenbahnlinien
    umstiegsmoegl[linie1] = set()                       # schlüssel/wertpaar für jede linie mit leerem set() anlegen     
    
    for linie2 in strab_linien:                         # mit 2. Linie aus strab_linien holen
        if linie1 != linie2:                            # vergleich von linien mit sich selbst ausschliessen
            gemeinsame_hst = bahnlinien_dict[linie1].intersection(bahnlinien_dict[linie2]) # Schnittmenge bilden
            if gemeinsame_hst:                          # prüfen ob vorhanden und nicht leer
                umstiegsmoegl[linie1].add(linie2)       # Werte (Liniennummern) werden der ersten Linie (Schlüssel) des Verglechs zugewiesen

print(f"Aufgabe 2.4: Liste alle Straßenbahnlinien jeweils mit allen Straßenbahnlinien in die man auf ihrem Weg direkt umsteigen kann auf:\n")
print(f"- Line 1 bietet Umstiegsmöglichkeiten in die Linien: {', '.join(umstiegsmoegl['1'])}")
print(f"- Line 3 bietet Umstiegsmöglichkeiten in die Linien: {', '.join(umstiegsmoegl['3'])}")
print(f"- Line 4 bietet Umstiegsmöglichkeiten in die Linien: {', '.join(umstiegsmoegl['4'])}")
print(f"- Line 5 bietet Umstiegsmöglichkeiten in die Linien: {', '.join(umstiegsmoegl['5'])}")
print(f"- Line 7 bietet Umstiegsmöglichkeiten in die Linien: {', '.join(umstiegsmoegl['7'])}")
print(f"- Line 9 bietet Umstiegsmöglichkeiten in die Linien: {', '.join(umstiegsmoegl['9'])}")
print(f"- Line 12 bietet Umstiegsmöglichkeiten in die Linien: {', '.join(umstiegsmoegl['12'])}")
print(f"- Line 13 bietet Umstiegsmöglichkeiten in die Linien: {', '.join(umstiegsmoegl['13'])}")
print(f"- Line 15 bietet Umstiegsmöglichkeiten in die Linien: {', '.join(umstiegsmoegl['15'])}")
print(f"- Line 17 bietet Umstiegsmöglichkeiten in die Linien: {', '.join(umstiegsmoegl['17'])}")
print(f"- Line 18 bietet Umstiegsmöglichkeiten in die Linien: {', '.join(umstiegsmoegl['18'])}")
print('================================================================================')


#########################################################################################################################
# Aufgabe 2.5: Haben alle Straßenbahnlinien mindestens ein Kundencenter an einer ihrer Haltestellen? Und von welchen    #
#              Linien ohne Kundencenter kann man mit einmal Umsteigen in eine andere Linie zu einem Kundencenter        #
#              gelangen?                                                                                                #
#                                                                                                                       #
# main_data (dict)                                          # Hauptdatenstruktur                                        #
# │                                                                                                                     #
# ├── HSTB (dict)                                           # Haltestellenbereiche                                      #
# │   └── 15250 (dict)                                      # Bereich-ID                                                #
# │       ├── Betriebsbereich (str): "BUS"                  # Betriebsbereich                                           #
# │       ├── DFI (str): "N"                                # Dynamische Fahrgastinformationen                          #
# │       ├── Haltestellenname (str): "Osterather Str."     # Name der Haltestelle                                      #
# │       ├── Linien (set): {"127"}                         # Liniennummern                                             #
# │       ├── VRSNummer (str): "15250"                      # VRS-Nummer                                                #
# │       ├── kurzname (str): "ORR"                         # Kürzel der Haltestelle                                    #
# │       ├── Aufzuege (dict): None                         # Aufzüge                                                   #
# │       ├── Fahrtreppen (dict): None                      # Fahrtreppen                                               #
# │       └── Verkaufsort (dict): None                      # Verkaufsort            === Hier sind die Daten! ===       #
# │                                                                                                                     #
#########################################################################################################################
# Vorgehensweise: - über die main_data['HSTB'] herausfinden welche haltestellen einen verkaufsort haben, das ist im     #
#                   prinzip der gleiche code wie in Aufgabe 2.2 mit den Aufzügen und Fahrtreppen. Den könnte man erneut #
#                   anwenden, allerdings auf Bahnlinien beschränkt (die bahnlinien sind schon aus: bahnlinien_dict      #
#                   bekannt.bahnlinien aus linien_mit_hst aus Aufgabe 2.2 extrahieren und schnittmengen bilden.         #
#                 - hier gibt es allerdings den unterschied, das es verschiedene arten von Verkaufsorten gibt, die nach #
#                   KundenCenter gefiltert werden müssen.                                                               #
#                 - die Schnittmenge je Linie beschreibt die Umsteigemöglichkeiten der Linie                            #
#                 - die erste lösung wäre die ausgabe der menge an verkaufsorten pro linie (der prozentteil entfällt)   #
#   	            und damit auch potenziell Linien die keine KundenCenter haben                                       #
#########################################################################################################################

linien_mit_vo = {}                                                          # Linien mit Verkaufsorten

# Daten sammeln
for linie, haltestellen in bahnlinien_dict.items():                         # Über jede Linie iterieren
    hst_gesamt = len(haltestellen)                                          # kontrolle für mich, hat keine relevanz
    """print(linie, hst_gesamt)"""                                          # kontrolle für mich, hat keine relevanz
    hst_mit_vo = 0                                                          # Anzahl der Haltestellen mit Verkaufsort
    
    for hst in haltestellen:                                                # Über die Haltestellen der Linie iterieren
        for eintrag in main_data['HSTB']:                                   # Suche in main_data['HSTB']
            hst_name = main_data['HSTB'][eintrag].get('Haltestellenname')   # Haltestellenname holen
            verkaufsorte = main_data['HSTB'][eintrag].get('Verkaufsort')    # Verkaufsorte holen
            
            # Nach KundenCenter filtern                     
            if hst_name == hst and verkaufsorte != None:                    # Wenn der Haltestellenname vorhanden ist und es einen VO gibt
                for verkaufsort_id, details in verkaufsorte.items():        # verkaufsort_id ist der schlüssel und details ist ein dict 
                    if details.get('Segment') == 'KundenCenter':            # hole Segment
                        hst_mit_vo += 1                                     # Hochzählen
                    
    linien_mit_vo[linie] = hst_mit_vo                                       # Anzahl der Haltestellen mit KundenCentern für die aktuelle Linie 

print(f"Aufgabe 2.5: Haben alle Straßenbahnlinien mindestens ein Kundencenter an einer ihrer Haltestellen?")
print(f"Und von welchen Linien ohne Kundencenter kann man mit einmal Umsteigen in eine andere Linie zu einem Kundencenter gelangen?\n")
print(f"- Linie 1 hat {linien_mit_vo['1']} KundenCenter an ihrer Strecke.")
print(f"- Linie 3 hat {linien_mit_vo['3']} KundenCenter an ihrer Strecke.")      
print(f"- Linie 4 hat {linien_mit_vo['4']} KundenCenter an ihrer Strecke.")
print(f"- Linie 5 hat {linien_mit_vo['5']} KundenCenter an ihrer Strecke.")
print(f"- Linie 7 hat {linien_mit_vo['7']} KundenCenter an ihrer Strecke.")
print(f"- Linie 9 hat {linien_mit_vo['9']} KundenCenter an ihrer Strecke.")
print(f"- Linie 12 hat {linien_mit_vo['12']} KundenCenter an ihrer Strecke.")
print(f"- Linie 13 hat {linien_mit_vo['13']} KundenCenter an ihrer Strecke.")
print(f"- Linie 15 hat {linien_mit_vo['15']} KundenCenter an ihrer Strecke.")
print(f"- Linie 16 hat {linien_mit_vo['16']} KundenCenter an ihrer Strecke.")
print(f"- Linie 17 hat {linien_mit_vo['17']} KundenCenter an ihrer Strecke.")
print(f"- Linie 18 hat {linien_mit_vo['18']} KundenCenter an ihrer Strecke.")

# Linie 12 hat kein Kundencenter, welche umsteigemöglichkeit gibt es um mit einmal Umsteigen in eine andere Linie zu einem Kundencenter zu gelangen?
print('================================================================================')

"""print(umstiegsmoegl['12'])"""
"""print("linien_mit_vo", linien_mit_vo)"""

linien_ohne_kc = []                         # Linien ohne Kundencenter

for linie in linien_mit_vo:                 # Schleife durch linien_mit_vo (dict aller linien mit anzahl KC)
    if linien_mit_vo[linie] == 0:           # wenn KC der Linio == 0 
        linien_ohne_kc.append(linie)        # in liste linien_ohne_kc schreiben

erreichbare_kc = {}                         # dict für linien die Kundencenter haben

for linie, umsteig_linien in umstiegsmoegl.items():     # Schleife über Umsteigemoeglichleiten aus Aufgabe 2.4
    erreichbar = []                                     # Liste mit erreichbaren Linien mit KundenCenter
    for um_linie in umsteig_linien:                     
        if linien_mit_vo.get(um_linie) > 0:             # Verkaufsort der umsteigelininen holen (Schon auf KC gefiltert)
            erreichbar.append(um_linie)                 # zu erreichbar hinzufügen
           
    erreichbare_kc[linie] = erreichbar                  # Liste mit erreichbaren linien für linien ohne Kundencenter 

# Hätte man kürzer halten können und direkt mit linie 12 arbeiten anstatt zu prüfen welche kein KC haben...

print(f"- Linie 12 hat kein KundenCenter an ihrer Strecke.\n  Jedoch kann durch umsteigen in eine dieser Linien:\n  {erreichbar} eins erreicht werden.")
print('================================================================================')
print('================================================================================')


##################################################################################################################################################
##                                                                                                                                              ##
##  Aufgabe 3.1: Suche für eine eingegebene Position:                                                                                           ##
##      - 3.1.1: Die nächste Straßenbahnhaltestelle                                                                                             ##
##      - 3.1.2: Die nächste Straßenbahnhaltestelle mit Fahrtreppen (Störung?)                                                                  ##
##      - 3.1.3: Die nächste Straßenbahnhaltestelle mit Aufzug (Störung?)                                                                       ##
##                                                                                                                                              ## 
##  Import der Berechnungsfunktionen aus der Funktionsbibliothek                                                                                ##
##  Print-Befehlsausgabe                                                                                                                        ##
##                                                                                                                                              ##
##################################################################################################################################################

from funktionsbibliothek import hypothenuse, OL_NB_Entfber_m_Z, umr_NB, umr_OL

print(f'Ergebnis zu Aufgabe 3.1.1:')

eing_pos = (6.95, 51.1)                                                                             # Testweiser Input -> Kann gehasht/ enthasht werden
#eing_pos = ((float(input('Gib den oestlichen Laengenwert deiner Position ein: '))),                # Eingabeaufforderung -> Kann gehasht/ enthasht werden
#                        (float(input('Gib den noerdlichen Breitenwert deiner Position ein: '))))   # Eingabeaufforderung -> Kann gehasht/ enthasht werden

print(f'Die nächste Straßenbahnhaltestelle ist', 
      hypothenuse(OL_NB_Entfber_m_Z(eing_pos, main_data)[0][0], OL_NB_Entfber_m_Z(eing_pos, main_data)[0][1]), 
      f'm vom angegebenen Punkt entfernt.\nEs handelt sich um die Straßenbahnhaltestelle:',
      main_data['HST']['ASS'][OL_NB_Entfber_m_Z(eing_pos, main_data)[1]].get('Name'),
      f'an den Koordinaten:',
      main_data['HST']['ASS'][OL_NB_Entfber_m_Z(eing_pos, main_data)[1]].get('coordinates'))
print(f'Die nächste Straßenbahnhaltestelle mit Fahrtreppen (ohne Stoerung) ist', 
       hypothenuse(OL_NB_Entfber_m_Z(eing_pos, main_data, 0)[0][0], OL_NB_Entfber_m_Z(eing_pos, main_data, 0)[0][1]), 
       f'm vom angegebenen Punkt entfernt.\nEs handelt sich um die Straßenbahnhaltestelle:',
       main_data['HST']['ASS'][OL_NB_Entfber_m_Z(eing_pos, main_data, 0)[1]].get('Name'),
       f'an den Koordinaten:',
       main_data['HST']['ASS'][OL_NB_Entfber_m_Z(eing_pos, main_data, 0)[1]].get('coordinates'))
print(f'Die nächste Straßenbahnhaltestelle mit Aufzuegen (ohne Stoerung) ist', 
       hypothenuse(OL_NB_Entfber_m_Z(eing_pos, main_data, 1)[0][0], OL_NB_Entfber_m_Z(eing_pos, main_data, 1)[0][1]), 
       f'm vom angegebenen Punkt entfernt.\nEs handelt sich um die Straßenbahnhaltestelle:',
       main_data['HST']['ASS'][OL_NB_Entfber_m_Z(eing_pos, main_data, 1)[1]].get('Name'),
       f'an den Koordinaten:',
       main_data['HST']['ASS'][OL_NB_Entfber_m_Z(eing_pos, main_data, 1)[1]].get('coordinates'))
print()