import pprint

import kvb_opendata

def trn(ln = 30):
    """Druckt Trennzeile aus.
    
    Parameter:
        ln: Länge der Trennlinie. (Standardwert: 30)
    
    """
    print("=" * ln)
    return


def anzahl_linien(data):
    """Ermittelt die Anzahl der verschiedenen Linien (Busse und Bahnen) in dem sie alle Haltestellenbereiche 
       nach den dort Verkehrenden Linien befragt.
    
    Parameter:
        data: Von kvb_opendata.import_kvb_opendata() generierte Datenstruktur.
        
    Rückgabe:
        int: Anzahl der Linien
    
    """
    linien = set()
    for hsb in data:
        if data[hsb]['Linien']:
            linien = linien.union(set(data[hsb]['Linien'].split())) 
    return len(linien)  
   
def max_haltestellen_max_linien(data):
    """Ermittelt die Anzahl der verschiedenen Linien (Busse und Bahnen) in dem sie alle Haltestellenbereiche 
       nach den dort Verkehrenden Linien befragt.
    
    Parameter:
        data: Von kvb_opendata.import_kvb_opendata() generierte Datenstruktur.
        
    Rückgabe:
        int: Anzahl der Linien
    
    """

    _max = {'haltestellen' : [],
            'h_max' : 0,
            'linien' : [],
            'l_max' : 0}   
    
    for hsb in data:
        _h = len(data[hsb]['Haltestellen'])
        _l = len(data[hsb]['Linien'].split())
        if _h >= _max['h_max']:
            _max['h_max'] = _h
            _max['haltestellen'].append((data[hsb]['Haltestellenname'], _h))
        if _l >= _max['l_max']:
            _max['l_max'] = _l
            _max['linien'].append((data[hsb]['Haltestellenname'], _l))
    _max['haltestellen'] = list(filter(lambda e: e[1] == _max['h_max'],_max['haltestellen']))        
    _max['linien'] = list(filter(lambda e: e[1] >= _max['l_max'],_max['linien']))        
    return _max    
    
        
data, lut = kvb_opendata.import_kvb_opendata()

trn()
print("Wie viele Linien (Busse und Bahnen) und wie viele Haltestellenbereiche gibt es insgesamt?")
print("Linien:",anzahl_linien(data))
print("Haltestellenbereiche:", len(data))
trn()
print("Welcher Haltestellenbereich hat die meisten Haltestellen und an welchem Treffen sich die meisten Linien?")
ans = max_haltestellen_max_linien(data)
print("Die meisten Haltestellen hat(haben):")
for e in ans['haltestellen']:
    print(e[0], '-', e[1], "Haltestellen." )
print("Die meisten Linien hat(haben):")
for e in ans['linien']:
    print(e[0], '-', e[1], "Linien." )
trn()
print("Wieviel Haltestellenbereiche haben Fahrtreppen, Aufzüge, beides oder keines von beidem?")    


