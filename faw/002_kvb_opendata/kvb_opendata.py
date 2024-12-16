import json

def import_kvb_opendata():
    """Diese Funktion öffnet die Datenstämme:
    
    - haltestellenbereiche.json
    - haltestellen.json
    - haltestellenbereichemitdfi.json
    - fahrtreppen.json
    - aufzuege.json
    - verkaufsorte.json
    
    und erzeugt eine neue Datenstruktur, die im Prinzip stark angereicherte
    Haltestellenbereiche sind. Desweitere wird eine LookUpTable (lut) erzeugt, 
    welche die Übersetzung Haltestellenbereich zu Kurzname möglich macht.

    Ausnahmen:
        FileNotFoundError - wird nicht behandelt.    
       
    
    Rückgabe:
        Tuple mit nodes(Haltestellenbereiche), lut("1" -> "HMG")
    
    """

    # Öffnen der json-Dateien und ablegen in Dictionaries
    try:
        hsb_file = open('json/haltestellenbereiche.json')
        hsb = json.load(hsb_file)
        hs_file = open('json/haltestellen.json')    
        hs = json.load(hs_file)
        hsbdfi_file = open('json/haltestellenbereichemitdfi.json')
        hsbdfi = json.load(hsbdfi_file)
        ft_file = open('json/fahrtreppen.json')
        ft = json.load(ft_file)
        az_file = open('json/aufzuege.json')
        az = json.load(az_file)
        vo_file = open('json/verkaufsorte.json')
        vo = json.load(vo_file)
        fts_file = open('json/fahrtreppenstoerungen.json')
        fts = json.load(fts_file)
        azs_file = open('json/aufzugstoerungen.json')
        azs = json.load(azs_file)
        fp_file = open('json/fahrplaene.json')
        fp = json.load(fp_file)

    # Dateien schließen, auch wen was schiefging
    finally:    
        hsb_file.close()
        hs_file.close()
        hsbdfi_file.close()
        ft_file.close()
        az_file.close()
        vo_file.close()
        fts_file.close()
        azs_file.close()
        fp_file.close()


    # Erstellen der "Megastruktur" und der LookUpTable

    disorders = {}    
    all_data = {}
    lut = {}
    
    # Basisdatenstamm aus 'haltestellenbereiche.json'
    for e in hsb['features']:
        p = e['properties'] # Kompakter Zugriff
        lut[p['Haltestellenbereich']] = p['kurzname'] # lut Eintrag erstellen.
        all_data[p['kurzname']] = {
                                    'Haltestellenbereich' : p['Haltestellenbereich'],
                                    'Haltestellenname' : p['Haltestellenname'],
                                    'Linien' : p.get('Linien', "").strip().split(),
                                    'Betriebsbereich' : p['Betriebsbereich']
                                  }
    
    # Anreicherung durch 'haltestellen.json'
    
    for e in hs['features']:
        p = e['properties']
        if not 'Haltestellen' in all_data[p['Kurzname']]:
            all_data[p['Kurzname']]['Haltestellen'] = []
        
        _hs = {'Betriebsbereich' : p['Betriebsbereich']}
        
        if 'geometry' in e:
            g = e['geometry']['coordinates']
            _hs['Nb'] = g[1]
            _hs['Ol'] = g[0]        

        if 'Linien' in p:
            _hs['Linien'] = p['Linien'].strip().split()

        all_data[p['Kurzname']]['Haltestellen'].append(_hs)    

    # Berechnung der Haltestellenbereichskoordinaten durch
    # Mittelung der Haltestellenkoordinaten.
    
    for _hsb in all_data:
        _nb, _ol = [], []
        
        for _hs in all_data[_hsb]['Haltestellen']:
            _nb.append(_hs['Nb'])
            _ol.append(_hs['Ol'])
        
        all_data[_hsb]['Nb'] = sum(_nb)/len(_nb)
        all_data[_hsb]['Ol'] = sum(_ol)/len(_ol)    

    # Anreicherung durch 'fahrtreppen.json'
    
    for e in ft['features']:
        g = e['geometry']['coordinates']
        p = e['properties']

        _hsb = lut[p['Haltestellenbereich']]

        if not 'Fahrtreppen' in all_data[_hsb]:
            all_data[_hsb]['Fahrtreppen'] = []

        _ft = {'nb' : g[1],
               'ol' : g[0],
               'Kennung' : p['Kennung'],
               'Bezeichnung' : p['Bezeichnung']}
    
        all_data[_hsb]['Fahrtreppen'].append(_ft)
    
    # Anreicherung durch 'aufzuege.json'
    
    for e in az['features']:
        g = e['geometry']['coordinates']
        p = e['properties']

        _hsb = lut[p['Haltestellenbereich']]

        if not 'Aufzuege' in all_data[_hsb]:
            all_data[_hsb]['Aufzuege'] = []

        _az = {'nb' : g[1],
               'ol' : g[0],
               'Kennung' : p['Kennung'],
               'Bezeichnung' : p['Bezeichnung']}
    
        all_data[_hsb]['Aufzuege'].append(_az)
    
    # Anreicherung durch 'verkaufsorte.json'
    
    for e in vo['features']:
        p = e['properties']
        _hsb = lut[p['haltestellenbereich']]
        
        if p['Segment'] == 'KundenCenter':
            all_data[_hsb]['KundenCenter'] = 'Ja'    
    
    # Daten werden mit der Information aus 'haltestellenbereichemitdfi.json
    # angereichert.
    
    for e in hsb['features']:
        p = e['properties']
        all_data[lut[p['Haltestellenbereich']]]['Dfi'] = 'Ja'
    
    # Störungen von Fahrtreppen und Aufzuegen einlesen.

    for e in fts['features']:
        p = e['properties']
        disorders[p['Kennung']] = p['timestamp']
        
    for e in azs['features']:
        p = e['properties']
        disorders[p['Kennung']] = p['timestamp']
    
    # Komplettdatensatz speichern.
    
    with open('json/all_data.json', 'w', encoding = 'UTF-8') as a:
        a.write(json.dumps(all_data, indent = 4))

    return all_data, lut, disorders, fp    