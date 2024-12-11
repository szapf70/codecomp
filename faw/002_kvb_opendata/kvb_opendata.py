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
    # Dateien schließen, auch wen was schiefging
    finally:    
        hsb_file.close()
        hs_file.close()
        hsbdfi_file.close()
        ft_file.close()
        az_file.close()
        vo_file.close()

    # Erstellen der "Megastruktur" und der LookUpTable
    
    all_data = {}
    lut = {}
    
    # Basisdatenstamm aus 'haltestellenbereiche.json'
    for e in hsb['features']:
        p = e['properties'] # Kompakter Zugriff
        lut[p['Haltestellenbereich']] = p['kurzname'] # lut Eintrag erstellen.
        all_data[p['kurzname']] = {
                                    'Haltestellenbereich' : p['Haltestellenbereich'],
                                    'Haltestellenname' : p['Haltestellenname'],
                                    'Linien' : p.get('Linien', "").lstrip(),
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
            _hs['nb'] = g[1]
            _hs['ol'] = g[0]        

        if 'Linien' in p:
            _hs['Linien'] = p['Linien']
        
        
        all_data[p['Kurzname']]['Haltestellen'].append(_hs)    
    
    # Anreicherung durch 'aufzuege.json'
    
    for e in ft['features']:
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
    
    
    # Komplettdatensatz speichern.
    
    with open('json/all_data.json', 'w') as a:
        a.write(json.dumps(all_data, indent = 4))
    
    return all_data, lut    