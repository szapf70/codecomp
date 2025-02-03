import json

########## Funktionen zum Einlesen der Daten und Einordnen in die Datenbank "main_data". ##########

def HSTB(filename, main_data):
    '''Haltestellenbereiche werden eingelesen und in neues Dictionary-Format 'main_data' eingefuegt.
    Nicht relevante Eintraege werden nicht uebernommen.
    Eingabedaten: "haltestellenbereiche.json"'''
    with open(filename, "r") as file:
        data = json.load(file)
        for i in range(len(data['features'])):
            new_key = data['features'][i]['properties'].get('Haltestellenbereich')
            new_dict = {}
            for _ in range(len(data['features'][i]['properties'])):
                if range(len(data['features'][i]['properties'])) != 0:
                    key1, value1 = data['features'][i]['properties'].popitem()
                    if key1 != 'Haltestellenbereich' and key1 != 'Lageplan' and key1 != 'Umgebungsplan':
                        if key1 == 'Linien':
                            Linien = set()
                            value1 = value1.split(' ')
                            for element in value1:
                                Linien.add(element)
                            new_dict.update({key1 : Linien})
                        else:
                            new_dict.update({key1 : value1})
            main_data['HSTB'].update({new_key : {}})    
            main_data['HSTB'][new_key].update(new_dict)

def HST(filename, main_data):
    '''Haltestellen werden eingelesen und in neues Dictionary-Format 'main_data' eingefuegt.
    Nicht relevante Eintraege werden nicht uebernommen.
    Eingabedaten: "haltestellen.json"'''    
    with open(filename, "r") as file:
        data = json.load(file)
        for i in range(len(data['features'])):
            new_key = data['features'][i]['properties'].get('ASS')
            new_dict = {}
            for _ in range(len(data['features'][i]['properties'])):
                if range(len(data['features'][i]['properties'])) != 0:
                    key1, value1 = data['features'][i]['properties'].popitem()
                    if key1 != 'ASS':
                        if key1 == 'Linien':
                            Linien = set()
                            value1 = value1.split(' ')
                            for element in value1:
                                Linien.add(element)
                            new_dict.update({key1 : Linien})
                        else:
                            new_dict.update({key1 : value1})
            for _ in range(len(data['features'][i]['geometry'])):
                if range(len(data['features'][i]['geometry'])) != 0:
                    key1, value1 = data['features'][i]['geometry'].popitem()
                    a, b = value1
                    new_dict.update({key1 : (a,b)})
            main_data['HST']['ASS'].update({new_key : {}})    
            main_data['HST']['ASS'][new_key].update(new_dict)

def HSTB_dfi(filename, main_data):
    '''DFI der Haltestellenbereiche werden eingelesen und in neues Dictionary-Format 'main_data' eingefuegt.
    Nicht relevante Eintraege werden nicht uebernommen.
    Eingabedaten: "haltestellenbereichemitdfi.json"'''    
    with open(filename, "r") as file:
        data = json.load(file)
        for key in main_data['HSTB']:
            main_data['HSTB'][key].update({'DFI' : 'N'}) 
        for i in range(len(data['features'])):
            hstbnr = data['features'][i]['properties'].get('Haltestellenbereich')
            main_data['HSTB'][hstbnr].update({'DFI' : 'Y'}) 

def AZ(filename, main_data):
    '''Aufzuege werden eingelesen und in neues Dictionary-Format 'main_data' eingefuegt.
    Nicht relevante Eintraege werden nicht uebernommen.
    Eingabedaten: "aufzuege.json"'''        
    with open(filename, "r") as file:
        data = json.load(file)
        for i in range(len(data['features'])):
            new_key = data['features'][i]['properties'].get('Haltestellenbereich')
            new_dict = {}
            for _ in range(len(data['features'][i]['properties'])):
                if range(len(data['features'][i]['properties'])) != 0:
                    kennung = data['features'][i]['properties'].get('Kennung')
                    key1, value1 = data['features'][i]['properties'].popitem()
                    if key1 != 'Haltestellenbereich' and key1 != 'Info' and key1 != 'Kennung':
                        new_dict.update({key1 : value1})
            value2 = data['features'][i]['geometry'].get('coordinates')
            a, b = value2
            new_dict.update({'coordinates' : (a,b)})
            if main_data['HSTB'][new_key].get('Aufzuege') == None:
                main_data['HSTB'][new_key].update({'Aufzuege' : {} })
            main_data['HSTB'][new_key]['Aufzuege'].update({kennung : {} })
            main_data['HSTB'][new_key]['Aufzuege'][kennung].update(new_dict)

def AZS(filename, main_data):
    '''Aufzugstoerungen werden eingelesen und in neues Dictionary-Format 'main_data' eingefuegt.
    Nicht relevante Eintraege werden nicht uebernommen.
    Eingabedaten: "aufzugstoerungen.json"'''        
    with open(filename, "r") as file:
        data = json.load(file)
        for i in range(len(data['features'])):
            new_key = data['features'][i]['properties'].get('Haltestellenbereich')
            new_dict = {}
            kennung = data['features'][i]['properties'].get('Kennung')
            stoerung = data['features'][i]['properties'].get('timestamp')
            new_dict.update({'Stoerung' : stoerung})
            main_data['HSTB'][new_key]['Aufzuege'][kennung].update(new_dict)

def FT(filename, main_data):
    '''Fahrtreppen werden eingelesen und in neues Dictionary-Format 'main_data' eingefuegt.
    Nicht relevante Eintraege werden nicht uebernommen.
    Eingabedaten: "fahrtreppen.json"'''        
    with open(filename, "r") as file:
        data = json.load(file)
        for i in range(len(data['features'])):
            new_key = data['features'][i]['properties'].get('Haltestellenbereich')
            new_dict = {}
            for _ in range(len(data['features'][i]['properties'])):
                if range(len(data['features'][i]['properties'])) != 0:
                    kennung = data['features'][i]['properties'].get('Kennung')
                    key1, value1 = data['features'][i]['properties'].popitem()
                    if key1 != 'Haltestellenbereich' and key1 != 'Info' and key1 != 'Kennung':
                        new_dict.update({key1 : value1})
            value2 = data['features'][i]['geometry'].get('coordinates')
            a, b = value2
            new_dict.update({'coordinates' : (a,b)})
            if main_data['HSTB'][new_key].get('Fahrtreppen') == None:
                main_data['HSTB'][new_key].update({'Fahrtreppen' : {} })
            main_data['HSTB'][new_key]['Fahrtreppen'].update({kennung : {} })
            main_data['HSTB'][new_key]['Fahrtreppen'][kennung].update(new_dict)

def FTS(filename, main_data):
    '''Fahrtreppenstoerungen werden eingelesen und in neues Dictionary-Format 'main_data' eingefuegt.
    Nicht relevante Eintraege werden nicht uebernommen.
    Eingabedaten: "fahrtreppenstoerungen.json"'''        
    with open(filename, "r") as file:
        data = json.load(file)
        for i in range(len(data['features'])):
            new_key = data['features'][i]['properties'].get('Haltestellenbereich')
            new_dict = {}
            kennung = data['features'][i]['properties'].get('Kennung')
            stoerung = data['features'][i]['properties'].get('timestamp')
            new_dict.update({'Stoerung' : stoerung})
            main_data['HSTB'][new_key]['Fahrtreppen'][kennung].update(new_dict)            

def VO(filename, main_data):
    '''Verkaufsorte werden eingelesen und in neues Dictionary-Format 'main_data' eingefuegt.
    Nicht relevante Eintraege werden nicht uebernommen.
    Eingabedaten: "verkaufsorte.json"'''        
    with open(filename, "r") as file:
        data = json.load(file)
        for i in range(len(data['features'])):
            new_key = data['features'][i]['properties'].get('haltestellenbereich')
            new_dict = {}
            for _ in range(len(data['features'][i]['properties'])):
                if range(len(data['features'][i]['properties'])) != 0:
                    kennung = data['features'][i]['properties'].get('Verkaufsort')
                    key1, value1 = data['features'][i]['properties'].popitem()
                    if key1 == 'Name' or key1 == 'strasse' or key1 == 'ort' or key1 == 'Segment':
                        new_dict.update({key1 : value1})
            value2 = data['features'][i]['geometry'].get('coordinates')
            a, b = value2
            new_dict.update({'coordinates' : (a,b)})
            if main_data['HSTB'][new_key].get('Verkaufsort') == None:
                main_data['HSTB'][new_key].update({'Verkaufsort' : {} })
            main_data['HSTB'][new_key]['Verkaufsort'].update({kennung : {} })
            main_data['HSTB'][new_key]['Verkaufsort'][kennung].update(new_dict)

########## Funktionen zum Lösen der einfachen Aufgaben ##########

def BusL_BahnL_Hst(data):
    '''Die Funktion berechnet die Anzahl der Haltestellen,
    der Bus- und Bahnlinien, der Haltestellenbereiche und der 
    Haltestellen, die tatsächlich angefahren werden.
    Die Funktion greift direkt auf die angelegte Datenstruktur
    "main_data" zu.
    Die gesammelten Daten werden in einem Dictionary ausgegeben.
    Ausgabedatei:
    {'HST' : Hstellen, 'Busse' : Busse, 'Bahnen' : Bahnen, 
    'HSTB' : Bereiche, 'HST_komplett' : HST_komplett}
    '''
    Busse = set()
    Bahnen = set()
    Hstellen = 0
    HST_komplett = 0
    Bereiche = 0
    for key in data['HSTB']:
        Bereiche += 1
    for key in data['HST']['ASS']:
        HST_komplett += 1
        Linien = data['HST']['ASS'][key].get('Linien')
        Bereich = data['HST']['ASS'][key].get('Betriebsbereich')
        if Linien != None:
            if Bereich == 'BUS':
                for element in Linien:
                    Busse.add(element)
                Hstellen += 1
            if Bereich == 'STRAB':
                for element in Linien:
                    Bahnen.add(element)
                Hstellen += 1
    dic_of_sets = {'HST' : Hstellen, 'Busse' : Busse, 'Bahnen' : Bahnen, 'HSTB' : Bereiche, 'HST_komplett' : HST_komplett}
    return dic_of_sets

def most_HST_most_Linien(data):
    '''Die Funktion durchsucht die Hauptdatei nach 
    den Haltestellenbereichen mit den meisten
    Haltestellen und den Haltestellenbereichen 
    an dem die meisten Linien aufeinandertreffen.
    Die Loesung wird als ein Dictionary ausgegeben.
    Ausgabedatei:
    {'HST_name' : HST_name, 
    'HSTB_m_HST' : HSTB_m_HST, 
    'counter_HST' : counter_HST, 
    'meiste_Linien' : meiste_Linien, 
    'Set_Linien' : Set_Linien}
    '''
    meiste_Haltestellen = []
    Dic_Haltestell = {}
    counter_HST = 0
    HST_name = ''
    HSTB_m_HST = ''
    meiste_Linien = {}
    Set_Linien = set()
    for key in data['HSTB']:
        if data['HSTB'][key].get('Linien') != None:
            if len(data['HSTB'][key]['Linien']) > len(Set_Linien):
                Set_Linien = data['HSTB'][key].get('Linien')
                meiste_Linien = key
    for key in data['HST']['ASS']:
        meiste_Haltestellen.append(data['HST']['ASS'][key].get('Name'))
    for name in meiste_Haltestellen:
        Dic_Haltestell.update({name : meiste_Haltestellen.count(name)})
    for key in Dic_Haltestell:
        if Dic_Haltestell[key] > counter_HST:
            counter_HST = Dic_Haltestell[key]
            HST_name = key
    for key in data['HSTB']:
        value = data['HSTB'][key].get('Haltestellenname')
        if value == HST_name:
            HSTB_m_HST = key
    dic_of_keys = {'HST_name' : HST_name, 'HSTB_m_HST' : HSTB_m_HST, 'counter_HST' : counter_HST, 'meiste_Linien' : meiste_Linien, 'Set_Linien' : Set_Linien}        
    return dic_of_keys 

def HSTB_m_FT_AZ(data):
    '''Die Funktion durchsucht die Hauptdatei
    nach den Haltestellenbereichen und zaehlt,
    wie viele Bereiche Fahrtreppen, Aufzuege,
    Beides oder keines von beidem haben.
    Die Ausgabe ist ein Dictionary mit den 
    jeweiligen Schluesselwertpaaren.
    Ausgabedatei:
    {'HSTB_FT_AZ' : HSTB_FT_AZ, 
    'HSTB_FT' : HSTB_FT, 
    'HSTB_AZ' : HSTB_AZ, 
    'HSTB_ohne_FT_AZ' : HSTB_ohne_FT_AZ}'''
    HSTB_FT = 0
    HSTB_AZ = 0
    HSTB_FT_AZ = 0
    HSTB_ohne_FT_AZ = 0
    for key in data['HSTB']:
        if data['HSTB'][key].get('Fahrtreppen') != None:
            HSTB_FT += 1
        if data['HSTB'][key].get('Aufzuege') != None:
            HSTB_AZ += 1
        if data['HSTB'][key].get('Fahrtreppen') != None and data['HSTB'][key].get('Aufzuege') != None:
            HSTB_FT_AZ += 1
        if data['HSTB'][key].get('Fahrtreppen') == None and data['HSTB'][key].get('Aufzuege') == None:
            HSTB_ohne_FT_AZ += 1
    dic_m_FT_AZ = {'HSTB_FT_AZ' : HSTB_FT_AZ, 'HSTB_FT' : HSTB_FT, 'HSTB_AZ' : HSTB_AZ, 'HSTB_ohne_FT_AZ' : HSTB_ohne_FT_AZ}
    return dic_m_FT_AZ

def bus_o_strab(data):
    '''Die Funktion ermittelt aus der Hauptdatei,
    ob ein Haltestellenbereich die Betriebsbereiche
    BUS und STRAB oder beides abdeckt.
    Die Ergebnisse werden aufsummiert ausgegeben.
    Die Ausgabe ist ein Dictionary mit den 
    jeweiligen Schluesselwertpaaren.
    Ausgabedatei:'''
    HSTB_BUS = 0
    HSTB_STRAB = 0
    HSTB_BUS_STRAB = 0
    for key in data['HSTB']:
        if data['HSTB'][key].get('Betriebsbereich') != None:
            if data['HSTB'][key].get('Betriebsbereich') == 'BUS':
                HSTB_BUS += 1
            if data['HSTB'][key].get('Betriebsbereich') == 'STRAB':
                HSTB_STRAB += 1
            if data['HSTB'][key].get('Betriebsbereich') == 'BUS STRAB':
                HSTB_BUS_STRAB += 1
    dic_bus_o_bahn = {'HSTB_BUS_STRAB' : HSTB_BUS_STRAB, 'HSTB_BUS' : HSTB_BUS, 'HSTB_STRAB' : HSTB_STRAB}
    return dic_bus_o_bahn

def NOSW_HSTB(data):
    '''Die Funktion ermittelt aus der Hauptdatei
    den noerdlichsten, den suedlichsten,
    den oestlichsten und den westlichsten
    Haltestellenbereich und gibt diesen in einem 
    Dictionary zurück.
    Ausgabeformat:
    '''
    HSTB_noerdl = 40
    Nkey = ''
    HSTB_westl = 1
    Wkey = ''
    HSTB_suedl = 60
    Skey = ''
    HSTB_oestl = 11
    Okey = ''
    for key in data['HST']['ASS']:
        OL, NB = data['HST']['ASS'][key].get('coordinates')
        if NB > HSTB_noerdl:
            HSTB_noerdl = NB
            Nkey = key
        if NB < HSTB_suedl:
            HSTB_suedl = NB
            Skey = key
        if OL > HSTB_westl:
            HSTB_westl = OL
            Wkey = key
        if OL < HSTB_oestl:
            HSTB_oestl = OL    
            Okey = key
    dic_NOSW = {'Nkey' : Nkey, 'Okey' : Okey, 'Skey' : Skey, 'Wkey' : Wkey}
    return dic_NOSW

def HSTB_zuord(ASS, data):
    '''Ordnet den Haltestellenbereich
    in der Hauptdatei
    nach dem Haltestellennamen zu.
    Eingabewert ist die ASS-Schlüssel-NR.
    Ausgabewert ist die Haltestellenbereichs-NR.'''
    HST_name = data['HST']['ASS'][ASS].get('Name')
    for key in data['HSTB']:
        if data['HSTB'][key].get('Haltestellenname') == HST_name:
            return key
        
def HSTB_ausg(HSTB_Nr, data):
    '''Gibt für eine Haltestellenbereichsnummer
    der Hauptdatei
    den Haltestellenbereichsnamen und die -nummer
    in einem Tuple zurück.'''
    HSTB_name = data['HSTB'][HSTB_Nr].get('Haltestellenname')
    return (HSTB_name, HSTB_Nr)

########## Funktionen zum Lösen der mittelschweren Aufgaben ##########

def all_linien(data):
    '''Die Funktionerstellt aus der Hauptdatei
    ein Set aller Linien.'''
    alle_linien = set()
    for key in data['HSTB']:
        if data['HSTB'][key].get('Linien') != None:
            alle_linien.update(data['HSTB'][key].get('Linien'))
    return alle_linien


def gr_anz_gem_st(data):
    '''Die Funktion durchsucht die Hauptdatei
    nach den beiden Linien mit der groessten
    Anzahl an gemeinsamen Stationen.
    Ausgabedateiformat:
    {'key_linie01' : key_linie01, 
    'key_linie02' : key_linie02, 
    'gr_Anz' : gr_Anz}'''
    gr_Anz = 0
    key_linie01 = ''
    key_linie02 = ''
    alle_linien = all_linien(data)
    for item in alle_linien:
        linie01 = []
        for key1 in data['HSTB']:
            if data['HSTB'][key1].get('Linien') != None:
                if data['HSTB'][key1].get('kurzname') != None:
                    for element in data['HSTB'][key1].get('Linien'):
                        if element == item:
                            linie01.append(data['HSTB'][key1].get('kurzname'))                      
        for item2 in alle_linien:
            linie02 = []
            if item2 != item:
                for key2 in data['HSTB']:
                    if data['HSTB'][key2].get('Linien') != None:
                        if data['HSTB'][key2].get('kurzname') != None:
                            for element in data['HSTB'][key2].get('Linien'):
                                if element == item2:
                                    linie02.append(data['HSTB'][key2].get('kurzname'))                                
            if len(set(linie01).intersection(set(linie02))) > gr_Anz:
                gr_Anz = len(set(linie01).intersection(set(linie02)))
                key_linie01 = item
                key_linie02 = item2
                line2 = linie02
                line1 = linie01
    dic_gr_anz_gem_st = {'key_linie01' : key_linie01, 'key_linie02' : key_linie02, 'gr_Anz' : gr_Anz}
    return dic_gr_anz_gem_st

def proz_beste_Auslastung(wert,data):
    '''Durchsucht fuer einen angegeben
    wert in der Hauptdatenbank die
    Linie mit der besten Auslastung fuer 
    den angegebenen wert.
    Eingabe: wert, Datenbank
    Wobei fuer wert 
    "DFI", "Fahrtreppen" oder "Aufzuege"
    einzutragen ist.
    Ausgabeformat: 
    {('Liniennummer', 
    Prozentuale Auslastung), ...}'''
    new_list = set()
    pro_item = (0,0)
    proz_item = (0,0)
    set_proz = set()
    for item in all_linien(data):
        linie = set()
        if item != '':
            for key1 in data['HSTB']:
                if data['HSTB'][key1].get('Linien') != None:
                    if data['HSTB'][key1].get('kurzname') != None:
                        for element in data['HSTB'][key1].get('Linien'):
                            if element == item:
                                if data['HSTB'][key1].get(wert) != None:
                                    if wert == 'DFI':
                                        linie.add((data['HSTB'][key1].get('kurzname'), data['HSTB'][key1].get(wert)))
                                    if wert != 'DFI':
                                        linie.add((data['HSTB'][key1].get('kurzname'), 'Y'))
                                if data['HSTB'][key1].get(wert) == None:
                                    linie.add((data['HSTB'][key1].get('kurzname'), 'N'))
        wert1 = len(linie)
        wert2 = 0
        for item2 in linie:
            if item2[1] == 'Y':
                wert2 += 1
        if wert2 != 0:
            new_list.add((wert1, wert2))
            proz_item = (item, wert2/wert1)
        if pro_item[1] < proz_item[1]:
            set_proz = set()
            pro_item = proz_item
            set_proz.add(pro_item)
        if pro_item[1] == proz_item[1]:
            pro_item = proz_item
            set_proz.add(pro_item)

    return set_proz  

def prozent(wert):
    '''Wandelt den angegebenen wert
    in einen Prozentstring mit 
    2 Nachkommastellen um.'''
    wert = (((wert * 10000) // 1 ) / 100) 
    wert = str(wert) + '%'
    return wert

def bus_oder_bahn(eingabe, data):
    '''Ueberprueft, ob die eingegebene
    Liniennummer eine Bus- oder eine
    Bahnlinie ist.
    Ausgabe: "BUS" oder "STRAB"'''
    ausgabe = ''
    for key in data['HST']['ASS']:
        if data['HST']['ASS'][key].get('Linien') != None:
            for item in data['HST']['ASS'][key].get('Linien'):
                if item == eingabe:
                    ausgabe = data['HST']['ASS'][key].get('Betriebsbereich')
    return ausgabe

def alle_strab(data):
    '''Erzeugt ein Set mit 
    allen Bahnlinien'''
    alle_STRAB = set()
    for key in data['HSTB']:
        if data['HSTB'][key].get('Linien') != None:
            for element in data['HSTB'][key].get('Linien'):
                if element != '':
                    if int(element) < 100:
                        alle_STRAB.add(element)
    return alle_STRAB

def all_strab_m_umstieg(data, alle_STRAB):
    '''Erzeugt ein Dictionary fuer
    alle Strassenbahnlinien mit den
    jeweiligen Bahnlininen, in die man 
    direkt umsteigen kann.
    Ausgabeformat:
    {'Liniennummer' : Set_von_Verbindungen, ...}'''

    alle_strab_dict = {}
    for strab in alle_STRAB:
        verb = set()
        for key in data['HSTB']:
            if data['HSTB'][key].get('Linien') != None:
                for item in data['HSTB'][key].get('Linien'):
                    if item == strab:
                        for item2 in data['HSTB'][key].get('Linien'):
                            if int(item2) < 100:
                                if int(item2) != int(strab):
                                    verb.add(int(item2))
        verb = list(verb)
        verb.sort()
        alle_strab_dict.update({int(strab) : verb})
    return alle_strab_dict

def strab_m_kc(data, alle_STRAB):
    '''Gibt ein Dictionary mit allen
    Strassenbahnlinien und "Ja" (inkl. Anzahl
    an Kundencentern) zurueck,
    wenn es ein Kundencenter an der Linie
    gibt, anderenfalls verweist es auf 
    moegliche Umstiege, um zu einem 
    Kundencenter zu gelangen.
    Ausgabeformat:
    {'Linie' : ('Ja', Anzahl), ...}'''
    new_dict = {}
    for strab in alle_STRAB:
        new_dict.update({int(strab) : ('Nein', 'Andere Linien mit 1x Umsteigen zu KC (siehe 2.3)')})
        zaehlen = 0
        for key in data['HSTB']:
            if data['HSTB'][key].get('Linien') != None:
                for item in data['HSTB'][key].get('Linien'):
                    if item != '':
                        if int(item) == int(strab):
                            if data['HSTB'][key].get('Verkaufsort') != None:
                                for key2 in data['HSTB'][key]['Verkaufsort']:
                                    if data['HSTB'][key]['Verkaufsort'][key2].get('Segment') == 'KundenCenter':
                                        zaehlen += 1
                                        new_dict.update({int(strab) : ('Ja', zaehlen)})
                                        continue
    return new_dict

########## Funktionen zum Lösen der schweren Aufgaben ##########

def umr_OL(eingabe):
    '''Umrechnung der oestl. Laenge in Meter 
    im Bereich des 50 Breitengrades'''
    ausgabe = 71470 * eingabe
    return ausgabe

def umr_NB(eingabe):
    '''Umrechnung der oestl. Laenge in Meter'''
    ausgabe = 111200 * eingabe
    return ausgabe

def hypothenuse(a, b):
    '''Berechnung der Entfernung zweier Punkte durch Eingabe
    der Differenzen für OL und NB.
    Die Ausgabe ist gerundet auf X,XX Meter 
    (Beispielausgabe: 235.85 ).'''
    return (((a**2 + b**2)**(1/2)) * 100 // 1) / 100

def OL_NB_Entfber(eing_pos, main_data):
    '''Berechnet die Entfernung der eingebebenen Position
    zu den Koordinaten der nächsten Haltestelle.
    Der Eingabewert ist ein tuple (oestl. Laenge , noerdl. Breite).
    Der Ausgabewert ist ein tuple (wert , ASS),
    wobei wert wiederum ein tuple ist. 
    wert = (Entf. oestl. Laenge , Entf. noerdl. Breite)
    Die Entfernung ist hierbei bereits in Meter umgerechnet.'''
    wert = (10000, 10000)
    HST_key = ''
    for key in main_data['HST']['ASS']:
        entf_OL = 100
        ent_NB = 100
        if main_data['HST']['ASS'][key].get('Betriebsbereich') == 'STRAB' or main_data['HST']['ASS'][key].get('Betriebsbereich') == 'BUS STRAB':
            if (main_data['HST']['ASS'][key].get('coordinates'))[0] - eing_pos[0] > 0:
                if (main_data['HST']['ASS'][key].get('coordinates'))[0] - eing_pos[0] < entf_OL:
                    entf_OL = (main_data['HST']['ASS'][key].get('coordinates'))[0] - eing_pos[0]
            if eing_pos[0] - (main_data['HST']['ASS'][key].get('coordinates'))[0] > 0:
                if eing_pos[0] - (main_data['HST']['ASS'][key].get('coordinates'))[0] < entf_OL:
                    entf_OL = eing_pos[0] - (main_data['HST']['ASS'][key].get('coordinates'))[0]
            if (main_data['HST']['ASS'][key].get('coordinates'))[1] - eing_pos[1] > 0:
                if (main_data['HST']['ASS'][key].get('coordinates'))[1] - eing_pos[1] < ent_NB:
                    ent_NB = (main_data['HST']['ASS'][key].get('coordinates'))[1] - eing_pos[1]
            if eing_pos[1] - (main_data['HST']['ASS'][key].get('coordinates'))[1] > 0:
                if eing_pos[1] - (main_data['HST']['ASS'][key].get('coordinates'))[1] < ent_NB:
                    ent_NB = eing_pos[1] - (main_data['HST']['ASS'][key].get('coordinates'))[1]
            if (umr_OL(entf_OL) + umr_NB(ent_NB)) < wert[0] + wert[1]:
                wert = (umr_OL(entf_OL), umr_NB(ent_NB))
                HST_key = key   
    return (wert, HST_key)

def OL_NB_Entfber_m_Z(eing_pos, main_data, zusatzdef = 2):
    '''Berechnet die Entfernung der eingebebenen Position
    zu den Koordinaten der nächsten Haltestelle.
    Der Eingabewert ist ein tuple (oestl. Laenge , noerdl. Breite).
    Der Ausgabewert ist ein tuple (wert , ASS),
    wobei wert wiederum ein tuple ist. 
    wert = (Entf. oestl. Laenge , Entf. noerdl. Breite)
    Die Entfernung ist hierbei bereits in Meter umgerechnet.
    
    Als Zusatzdefinition kann überprüft werden, ob die Haltestellen
    Fahrtreppen oder Aufzuege haben 
    (Stoerungen werden direkt herausgefiltert).
    
    Zusatzdef.:
    0 für Fahrtreppen, 
    1 für Aufzuege'''
    wert = (10000, 10000)
    HST_key = ''
    if zusatzdef == 0:
        zusatz = 'Fahrtreppen'
    if zusatzdef == 1:
        zusatz = 'Aufzuege'
    if zusatzdef != 0 and zusatzdef != 1:
        zusatz = None
    for key in main_data['HST']['ASS']:
        entf_OL = 100
        ent_NB = 100
        if main_data['HST']['ASS'][key].get('Betriebsbereich') == 'STRAB' or main_data['HST']['ASS'][key].get('Betriebsbereich') == 'BUS STRAB':           
            if zusatz != None:
                for key2 in main_data['HSTB']:
                    if zusatz in main_data['HSTB'][key2]:
                        if main_data['HST']['ASS'][key].get('Name') == main_data['HSTB'][key2].get('Haltestellenname'):
                            for key3 in main_data['HSTB'][key2][zusatz]:
                                if not 'Stoerung' in main_data['HSTB'][key2][zusatz][key3]:
                                    if (main_data['HST']['ASS'][key].get('coordinates'))[0] - eing_pos[0] > 0:
                                        if (main_data['HST']['ASS'][key].get('coordinates'))[0] - eing_pos[0] < entf_OL:
                                            entf_OL = (main_data['HST']['ASS'][key].get('coordinates'))[0] - eing_pos[0]
                                    if eing_pos[0] - (main_data['HST']['ASS'][key].get('coordinates'))[0] > 0:
                                        if eing_pos[0] - (main_data['HST']['ASS'][key].get('coordinates'))[0] < entf_OL:
                                            entf_OL = eing_pos[0] - (main_data['HST']['ASS'][key].get('coordinates'))[0]
                                    if (main_data['HST']['ASS'][key].get('coordinates'))[1] - eing_pos[1] > 0:
                                        if (main_data['HST']['ASS'][key].get('coordinates'))[1] - eing_pos[1] < ent_NB:
                                            ent_NB = (main_data['HST']['ASS'][key].get('coordinates'))[1] - eing_pos[1]
                                    if eing_pos[1] - (main_data['HST']['ASS'][key].get('coordinates'))[1] > 0:
                                        if eing_pos[1] - (main_data['HST']['ASS'][key].get('coordinates'))[1] < ent_NB:
                                            ent_NB = eing_pos[1] - (main_data['HST']['ASS'][key].get('coordinates'))[1]
                                    if (umr_OL(entf_OL) + umr_NB(ent_NB)) < wert[0] + wert[1]:
                                        wert = (umr_OL(entf_OL), umr_NB(ent_NB))
                                        HST_key = key
            else:
                if (main_data['HST']['ASS'][key].get('coordinates'))[0] - eing_pos[0] > 0:
                    if (main_data['HST']['ASS'][key].get('coordinates'))[0] - eing_pos[0] < entf_OL:
                        entf_OL = (main_data['HST']['ASS'][key].get('coordinates'))[0] - eing_pos[0]
                if eing_pos[0] - (main_data['HST']['ASS'][key].get('coordinates'))[0] > 0:
                    if eing_pos[0] - (main_data['HST']['ASS'][key].get('coordinates'))[0] < entf_OL:
                        entf_OL = eing_pos[0] - (main_data['HST']['ASS'][key].get('coordinates'))[0]
                if (main_data['HST']['ASS'][key].get('coordinates'))[1] - eing_pos[1] > 0:
                    if (main_data['HST']['ASS'][key].get('coordinates'))[1] - eing_pos[1] < ent_NB:
                        ent_NB = (main_data['HST']['ASS'][key].get('coordinates'))[1] - eing_pos[1]
                if eing_pos[1] - (main_data['HST']['ASS'][key].get('coordinates'))[1] > 0:
                    if eing_pos[1] - (main_data['HST']['ASS'][key].get('coordinates'))[1] < ent_NB:
                        ent_NB = eing_pos[1] - (main_data['HST']['ASS'][key].get('coordinates'))[1]
                if (umr_OL(entf_OL) + umr_NB(ent_NB)) < wert[0] + wert[1]:
                    wert = (umr_OL(entf_OL), umr_NB(ent_NB))
                    HST_key = key
    return (wert, HST_key)