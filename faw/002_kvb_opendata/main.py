import pprint
import itertools
import sys

import kvb_opendata

def trn(ln = 30):
    """Druckt Trennzeile aus.
    
    Parameter:
        ln: Laenge der Trennlinie. (Standardwert: 30)
    
    """
    print("=" * ln)
    return


def anzahl_linien(data):
    """Ermittelt die Anzahl der verschiedenen Linien (Busse und Bahnen) in dem sie alle Haltestellenbereiche 
       nach den dort Verkehrenden Linien befragt.
    
    Parameter:
        data: Von kvb_opendata.import_kvb_opendata() generierte Datenstruktur.
        
    Rueckgabe:
        int: Anzahl der Linien
    
    """
    linien = set()
    for _hsb in data:
        if data[_hsb]['Linien']:
            linien = linien.union(set(data[_hsb]['Linien'])) 
    return len(linien)  
   
def max_haltestellen_max_linien(data):
    """Ermittelt die Anzahl der verschiedenen Linien (Busse und Bahnen) in dem sie alle Haltestellenbereiche 
       nach den dort Verkehrenden Linien befragt.
    
    Parameter:
        data: Von kvb_opendata.import_kvb_opendata() generierte Datenstruktur.
        
    Rueckgabe:
        int: Anzahl der Linien
    
    """

    _max = {'haltestellen' : [],
            'h_max' : 0,
            'linien' : [],
            'l_max' : 0}   
    
    for _hsb in data:
        _h = len(data[_hsb]['Haltestellen'])
        _l = len(data[_hsb]['Linien'])
        if _h >= _max['h_max']:
            _max['h_max'] = _h
            _max['haltestellen'].append((data[_hsb]['Haltestellenname'], _h))
        if _l >= _max['l_max']:
            _max['l_max'] = _l
            _max['linien'].append((data[_hsb]['Haltestellenname'], _l))
    _max['haltestellen'] = list(filter(lambda e: e[1] == _max['h_max'],_max['haltestellen']))        
    _max['linien'] = list(filter(lambda e: e[1] >= _max['l_max'],_max['linien']))        
    return _max    
    
def zugangs_info(data):
    """Funktion zaehlt ueber alle Fahrstellenbereiche das vorhandensein von
       Fahrtreppen und Aufzuegen.
       
    Parameter:
        data: Von kvb_opendata.import_kvb_opendata() generierte Datenstruktur.

    Rueckgabe:
        dict: Vier Schluessel. Jeweils Tuple (True/False Fahrtreppen, True/False Aufzuege)        
    """
    _cnt = {(False,False) : {'cnt' : 0, 'kurznamen' : []},
            (True, False) : {'cnt' : 0, 'kurznamen' : []},
            (False, True) : {'cnt' : 0, 'kurznamen' : []},
            (True, True) : {'cnt' : 0, 'kurznamen' : []}}
    for _hsb in data:
        _act = ('Fahrtreppen' in data[_hsb],'Aufzuege' in data[_hsb])
        _cnt[_act]['cnt'] += 1
        _cnt[_act]['kurznamen'].append(_hsb)
        
    return _cnt    
  
def betriebsbereich_info(data):
    """Durchlaeuft alle Haltestellenbereiche und zaehlt 'BUS'/'STRAB' und 'BUS_STRAB
    
    Parameter:
        data: Von kvb_opendata.import_kvb_opendata() generierte Datenstruktur.
    
    Rueckgabe:
        dict: Betriebsbereichslabel als Schluessel fuer Zaehler.    
    """       
    _cnt = {'BUS' : 0,
            'BUS STRAB' : 0,
            'STRAB' : 0}
    
    for _hsb in data:
        _cnt[data[_hsb]['Betriebsbereich']] += 1
        
    return _cnt            

def windrose(data):
    """Ermittelt den weitesten Haltestellenbereich fuer jede Windrichtung.
    
    Parameter:
        data: Von kvb_opendata.import_kvb_opendata() generierte Datenstruktur.

    Rueckgabe:
        dict: key : 'N', 'O', 'S' oder 'W' 
              value : Kurzname - Name  
               
    """
    _ans = {'N' : None,
            'S' : None,
            'O' : None,
            'W' : None}
    
    n_max, s_min, o_max, w_min = 0, 90, 0, 180
    
    for _hsb in data:
        _nb = data[_hsb]['Nb']
        _ol = data[_hsb]['Ol']
        if _nb > n_max:
            n_max = _nb
            _ans['N'] = _hsb + ' - ' + data[_hsb]['Haltestellenname']
        if _nb < s_min:
            s_min = _nb
            _ans['S'] = _hsb + ' - ' + data[_hsb]['Haltestellenname']
        if _ol > o_max:
            o_max = _ol
            _ans['O'] = _hsb + ' - ' + data[_hsb]['Haltestellenname']
        if _ol < w_min:
            w_min = _ol
            _ans['W'] = _hsb + ' - ' + data[_hsb]['Haltestellenname']
    
    return _ans        

def gemeinsame_stationen(data):
    """ueber alle Haltestellenbereiche wird die Anzahl der gemeinsamen Stationen aller Linien ermittelt.

    Parameter:
        data: Von kvb_opendata.import_kvb_opendata() generierte Datenstruktur.

    Rueckgabe:
        list of tuple: (linie_a, linie_b, gemeinsame Stationen)
        
    """
    _ans = {}

    for _hsb in data:
        # Kombinationen aller Linine dieses Haltestellenbereichs erstellen.
        _cs = itertools.combinations(data[_hsb]['Linien'],2)
        for _c in _cs: 
            _ans[_c] = _ans.get(_c,0) + 1

    return [(_k, _v) for _k, _v in _ans.items()]



def div_abdeckung(data):
    """ueber alle Haltestellenbereiche wird die Anzahl der Stationen
       jeder Linie und die Anzahl der Haltestellenbereiche mit DFI, Fahrtreppen und Aufzuege
       gezaehlt. Anschluss wird die prozentuale Abdeckung berechnet.
       
    Parameter:
        data: Von kvb_opendata.import_kvb_opendata() generierte Datenstruktur.

    Rueckgabe:
        list of tuple: 
            (linie, haltestellen, abs_dfi, abs_ft, abs_az, pr_dfi, pr_ft, pr_az)       
    
    """
    _ans = {}
    
    # Daten sammeln
    
    for _hsb in data:
        for _l in data[_hsb]['Linien']:
            if not _l in _ans:
                _ans[_l] = {'cnt' : 0, 'cnt_dfi' : 0, 'cnt_ft' : 0, 'cnt_az' : 0,
                            'proz_dfi' : 0, 'proz_ft' : 0, 'proz_az' : 0}

            _ans[_l]['cnt'] += 1
            _ans[_l]['cnt_dfi'] += ('Dfi' in data[_hsb])
            _ans[_l]['cnt_ft'] += ('Fahrtreppen' in data[_hsb])
            _ans[_l]['cnt_az'] += ('Aufzuege' in data[_hsb])
            
    # Prozentuale Abdeckung berechnen.
    
    for _l in _ans:
        if _ans[_l]['cnt_dfi']:
            _ans[_l]['proz_dfi'] = round((100/_ans[_l]['cnt'])*_ans[_l]['cnt_dfi'],1)
        if _ans[_l]['cnt_ft']:
            _ans[_l]['proz_ft'] = round((100/_ans[_l]['cnt'])*_ans[_l]['cnt_ft'],1)
        if _ans[_l]['cnt_az']:
            _ans[_l]['proz_az'] = round((100/_ans[_l]['cnt'])*_ans[_l]['cnt_az'],1)

    return [(_l,_ans[_l]['cnt'],_ans[_l]['cnt_dfi'],_ans[_l]['cnt_ft'],_ans[_l]['cnt_az'],
             _ans[_l]['proz_dfi'],_ans[_l]['proz_ft'],_ans[_l]['proz_az']) for _l in _ans]
 
def ermittele_betriebsbereich(data):
    _ans = {}
    for _hsb in data:
        for _hs in data[_hsb]['Haltestellen']:
            if 'Linien' in _hs:
                _linien = list(filter(lambda l: len(l) < 3, _hs['Linien']))
                for _l in _linien:
                    if not int(_l) in _ans:
                        _ans[int(_l)] = set()
                    _ans[int(_l)].add(_hs['Betriebsbereich'])    
    return _ans

def strab_kundencenter_check(data):
    """Laeuft ueber alle Haltestellenbereiche und wenn einer ein KundenCenter hat, dann werden die Linien gespeichert
    
    Parameter:
        data: Von kvb_opendata.import_kvb_opendata() generierte Datenstruktur.

    Rueckgabe:
        dict: Linie : Azahl der KundenCenter fuer diese Linie        
    
    
    """
    
    _ans = {}
    for _hsb in data:
        for _l in data[_hsb]['Linien']:
            if len(_l) < 3:
                if _l not in _ans:
                    _ans[_l] = 0
                if 'KundenCenter' in data[_hsb]:    
                    _ans[_l] += 1

    return _ans        

def hsb_distances(data,Nb, Ol):
    """Berechnet die Entfernung jedes einzelnen Haltestellenbereiches zur übergebenen Position.
    
        Parameter:
            data: Von kvb_opendata.import_kvb_opendata() generierte Datenstruktur.
            Nb,Ol: Position zu der die Entfernung ermitteln werden soll.

        Rückgabe:
            list of tuple: (Kurzname, Entfernung) der Haltestellenbereiche zur gegebenen Position.    
    """
    ans = []
    for _hsb in data:
        dis = (abs(Nb-data[_hsb]['Nb'])**2 + abs(Ol-data[_hsb]['Ol'])**2)**.5
        ans.append((_hsb, dis))

    return ans

def get_hsb(data, line):
    """Ermittelt alle Haltestellenbereiche für die übergebene Linie
    
        Parameter:
            data: Von kvb_opendata.import_kvb_opendata() generierte Datenstruktur.
            line: Linie 

        Rückgabe:
            list: Alle Kurznaame der Haltestelle an denen die Linie verkehrt.        
    """

    ans = []

    for _hsb in data:
        if line in data[_hsb]['Linien']:
            ans.append(_hsb)

    return ans        



data, lut, disorders, fp = kvb_opendata.import_kvb_opendata()

trn()
print("Schwierigkeitsgrad - leicht")
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
print("Wieviel Haltestellenbereiche haben Fahrtreppen, Aufzuege, beides oder keines von beidem?")    
ans = zugangs_info(data)
print("Nur Fahrtreppen:", ans[(True,False)]['cnt'])
print("Nur Aufzuege:", ans[(False,True)]['cnt'])
print("Beides:", ans[(True,True)]['cnt'])
print("Keines:", ans[(False,False)]['cnt'])
trn()
print("Wieviel Haltestellenbereiche decken jeweils die Betriebsbereich „BUS“, „STRAB“ oder beides ab?")
ans = betriebsbereich_info(data)
print("BUS:", ans['BUS'])
print("STAB:", ans['STRAB'])
print("Beides:", ans['BUS STRAB'])
trn()
print("")
ans = windrose(data)
print("Der am weitesten noerdlich liegende Haltestellenbereich ist:", ans['N'])
print("Der am weitesten oestlich liegende Haltestellenbereich ist:", ans['O'])
print("Der am weitesten suedlich liegende Haltestellenbereich ist:", ans['S'])
print("Der am weitesten westlich liegende Haltestellenbereich ist:", ans['W'])
trn()

trn()
print("Schwierigkeitsgrad - mittel")
trn()


print("Welche beiden Linien haben die groesste Anzahl gemeinsamer Stationen?")
ans = gemeinsame_stationen(data)
most = sorted(ans, key = lambda c: c[1], reverse =  True)[0]
print(f"Die Linien {most[0][0]} und {most[0][1]} haben {most[1]} gemeinsame Stationen.")
trn()
print("Welche Linie ist an all ihren Haltestellen prozentual am besten mit digitalen")
print("Fahrgastinformationsanzeigen ausgestattet? Das gleiche auch fuer Fahrtreppen und Aufzuege.")
ans = div_abdeckung(data)
print("Dfi - Abdeckung")
ans = sorted(ans, key=lambda x: x[5], reverse = True)
print(ans[0][0],ans[0][5],'Prozent')
print("Fahrtreppen - Abdeckung")
ans = sorted(ans, key=lambda x: x[6], reverse = True)
print(ans[0][0],ans[0][6],'Prozent')
print("Aufzug - Abdeckung")
ans = sorted(ans, key=lambda x: x[7],  reverse = True)
print(ans[0][0], ans[0][7],'Prozent')
trn()
print("Zweistellige Linien immer Strassenbahnen?")
ans = ermittele_betriebsbereich(data)
for _l in sorted(ans.keys()):
    if len(ans[_l]) == 1:
        print(f"Linie {_l} ist eindeutig bestimmbar.{ans[_l]}")
    else:
        print(f"Linie {_l} ist nicht eindeutig bestimmbar.{ans[_l]}")

trn()
print("Liste alle Strassenbahnlinien jeweils mit allen Strassenbahnlinien in die man auf ihrem Weg direkt umsteigen kann auf.")
ans = gemeinsame_stationen(data)
_um = {}
for _l, _ in ans:
    _a, _b = _l
    if int(_a) < 99 and int(_b) < 99:
        if not _a in _um: _um[_a] = []
        if not _b in _um: _um[_b] = []
        _um[_a].append(_b)
        _um[_b].append(_a)


for _k in sorted(_um.keys(), key = lambda k: int(k)):
    print(f"Linie {_k} mit direkter Umsteigemoeglichkeit in die Linien {', '.join(_um[_k])} ")        
trn()
print("Haben alle Strassenbahnlinien mindestens ein Kundencenter an einer ihrer Haltestellen?") 
print("Und von welchen Linien ohne Kundencenter kann man mit einmal Umsteigen in eine andere Linie zu einem Kundencenter gelangen. ")
ans2 = strab_kundencenter_check(data)
for _l in sorted(ans2.keys(), key = lambda s: int(s)):
    if ans2[_l]:
        print(f"Linie {_l} hat {ans2[_l]} KundenCenter an ihrer Strecke.")
    else:
        print(f"Linie {_l} hat kein KundenCenter an ihrer Strecke.")            
        for _ul in _um[str(_l)]:
            if ans2[_ul]:
                print(f"Es ist aber ein KundenCenter ueber die Linie {_ul} erreichbar.")
                break
        else:
            print("Leider kann man auch mit einmal umsteigen kein KundenCenter erreichen.")         
        
trn()
ans = hsb_distances(data, 51.002608, 6.950598)
ans = sorted(ans, key = lambda hsb: hsb[1])
nhs = ans[0]
nhsmf, fts = None, ""
nhsma, azs = None, ""

for hsb, dis in ans:
    if 'Fahrtreppen' in data[hsb]:
        for ft in data[hsb]['Fahrtreppen']:
            if ft['Kennung'] in disorders:
                fts = "Es gibt eine Störung an einer der Fahrtreppen."
        nhsmf = (hsb,dis)
        break

for hsb, dis in ans:
    if 'Aufzuege' in data[hsb]:
        for ft in data[hsb]['Aufzuege']:
            if ft['Kennung'] in disorders:
                azs = "Es gibt eine Störung an einem der Aufzuege."
        nhsma = (hsb,dis)
        break

print("Die nächste Straßenbahnhaltestelle zum (FAW - 51.002608, 6.950598)")
print(data[nhs[0]]['Haltestellenname'])
print("Die nächste Straßenbahnhaltestelle mit Fahrtreppen zum (FAW - 51.002608, 6.950598)")
print(data[nhsmf[0]]['Haltestellenname'], fts)
print("Die nächste Straßenbahnhaltestelle mit Aufzuege zum (FAW - 51.002608, 6.950598)")
print(data[nhsma[0]]['Haltestellenname'], azs )

trn()
sys.exit()

hsb_12 = get_hsb(data, "12")

hsb_12.remove("ZSF")
linie_012_calc = ["ZSF;Zollstock Südfriedhof"]

while hsb_12:
    _act = linie_012_calc[-1]



for hsb in hsb_12:
    print(f"{hsb};{data[hsb]['Haltestellenname']}")


ans = hsb_distances(data, 51.002608, 6.950598)
ans = sorted(ans, key = lambda hsb: hsb[1])
