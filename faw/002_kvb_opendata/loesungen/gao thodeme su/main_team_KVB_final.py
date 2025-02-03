import pprint
import json
import bibliothek
import math

aufzuege_dict=bibliothek.Data_manage('aufzuege.json', "Haltestellenbereich", ("coordinates","Kennung"))
aufzugstoerungen_dict=bibliothek.Data_manage('aufzugstoerungen.json', "Haltestellenbereich", ("Kennung","timestamp"))
fahrtreppen_dict=bibliothek.Data_manage('fahrtreppen.json', "Haltestellenbereich", ("coordinates","Kennung"))
fahrtreppenstoerungen_dict=bibliothek.Data_manage('fahrtreppenstoerungen.json', "Haltestellenbereich", ("Kennung","timestamp"))
haltestellen_dict=bibliothek.Data_manage('haltestellen.json', "Name", ("Betriebsbereich","ASS","Linien","coordinates"))
haltestellenbereiche_dict=bibliothek.Data_manage('haltestellenbereiche.json', "Haltestellenname", ("Haltestellenbereich","Betriebsbereich","Linien","VRSNummer"))
haltestellenbereichemitdfi_dict=bibliothek.Data_manage('haltestellenbereichemitdfi.json', "Haltestellenbereich", ())
verkaufsorte_dict=bibliothek.Data_manage('verkaufsorte.json', "haltestellenbereich", ("Segment",))

#==========================================================================================================

report_dict = {}                                        # creat a dict to store infomation for reporting
report_list = []                                        # creat a list for reporting text
report_list.append("ITQ - KVB Project - Team: Gao, Xusheng (X.) <xgao20@ford.com>, Thodeme, Sree Ram (G.R.) <sthodeme@ford.com>, Su, Zhou (Z.) <zsu2@ford.com>")
report_list.append(f'')
report_list.append("Schwierigkeitsgrad - leicht")
report_list.append(f'')

#==========================================================================================================
# Schwierigkeitsgrad - leicht
# •	Wie viele Linien (Busse und Bahnen) und wie viele Haltestellenbereiche gibt es insgesamt?
# - append all the Linien from haltestellen_dict to one list. convert list to set and return len of set
# - check the line number from Linien set to seperate Bus and STRB
# - sum_Haltestellenbereiche = len of haltestellenbereiche_dict
sum_Haltestellenbereiche = len(haltestellenbereiche_dict)

linienList_all, STRB_Linien, Bus_Linien = bibliothek.Linien(haltestellenbereiche_dict)
sum_LinienList_all = len(linienList_all)
sum_Bus_Linien = len(Bus_Linien)
sum_STRB_Linien = len(STRB_Linien)

report_dict.update({"sum_Haltestellenbereiche":sum_Haltestellenbereiche,"sum_Bus_Linien":sum_Bus_Linien,"STRB_Linien":sum_STRB_Linien, "Bus_Linien": Bus_Linien, "STRB_Linien": STRB_Linien})
report_list.append("Q1, Wie viele Linien (Busse und Bahnen) und wie viele Haltestellenbereiche gibt es insgesamt?")
report_list.append(f'   Bus_Linien: {sum_Bus_Linien:<15}')
report_list.append(f'   STRB_Linien: {sum_STRB_Linien:<15}')
report_list.append(f'   Haltestellenbereiche: {sum_Haltestellenbereiche:<15}')
report_list.append(f'')


#==========================================================================================================
# •	Welcher Haltestellenbereich hat die meisten Haltestellen und an welchem Treffen sich die meisten Linien?
# - in Haltestellen_dict max(acount('Name'))
report_list.append("Q2, Welcher Haltestellenbereich hat die meisten Haltestellen und an welchem Treffen sich die meisten Linien?")
haltestellenbereich_maxHalteNr, haltestellenbereich_maxHalte = bibliothek.Haltestellenbereich_meisten_Haltestellen(haltestellen_dict)

report_dict.update({"Haltestellenbereich hat die meisten Haltestellen": bibliothek.Haltestellenbereich_meisten_Haltestellen(haltestellen_dict)})
report_list.append(f'   Haltestellenbereich hat die meisten Haltestellen: {haltestellenbereich_maxHalte} hat {haltestellenbereich_maxHalteNr} Haltestellen')

# - Haltestellenbereich which has max(len(Linien)

max_key, max_length, haltestellen_dict_int = bibliothek.Haltestellenbereich_meisten_Linien(haltestellenbereiche_dict)
report_dict.update({"Haltestellenbereich hat meisten Linien": [max_key, max_length]})
report_list.append(f'   Haltestellenbereich hat meisten Linien: {max_key} hat {max_length} Linien')
report_list.append(f'')

dict = []
for key in haltestellen_dict.keys():
    sub_dict = []
    sub_dict.append(int(len(haltestellen_dict[key])/4))
    sub_dict.append(key)
    dict.append(sub_dict)

dict = sorted(dict)

meisten_Haltestellen = max([len(item) for item in haltestellen_dict.keys()])
# print(meisten_Haltestellen)


#==========================================================================================================
# •	Wieviel Haltestellenbereiche haben Fahrtreppen, Aufzüge, beides oder keines von beidem?
report_list.append("Q3, Wieviel Haltestellenbereiche haben Fahrtreppen, Aufzüge, beides oder keines von beidem?")
aufzuege_Haltestellenbereiche_set = set(map(str,aufzuege_dict.keys()))
report_list.append(f'   {len(aufzuege_Haltestellenbereiche_set)} Haltestellenbereiche haben Aufzüge:')
report_list.append("    "+", ".join(aufzuege_Haltestellenbereiche_set))
report_list.append(f'')


fahrtreppen_Haltestellenbereiche_set = set(map(str,fahrtreppen_dict.keys()))
report_list.append(f'   {len(fahrtreppen_Haltestellenbereiche_set)} Haltestellenbereiche haben Fahrtreppen:')
report_list.append("    "+", ".join(fahrtreppen_Haltestellenbereiche_set))
report_list.append(f'')

intersection_aufzeuge_fahrtreppen_set = aufzuege_Haltestellenbereiche_set & fahrtreppen_Haltestellenbereiche_set
report_list.append(f'   {len(intersection_aufzeuge_fahrtreppen_set)} Haltestellenbereiche haben Aufzüge und Fahrtreppen:')
report_list.append("    "+", ".join(intersection_aufzeuge_fahrtreppen_set))
report_list.append(f'')

#==========================================================================================================
# •	Wieviel Haltestellenbereiche decken jeweils die Betriebsbereich „BUS“, „STRAB“ oder beides ab?
# - haltestellenbereiche_dict filter 'Betriebsbereich Index 1
report_list.append("Q4, Wieviel Haltestellenbereiche decken jeweils die Betriebsbereich „BUS“, „STRAB“ oder beides ab?")
Bus_Haltestellenbereiche_list = [key for key, value in haltestellenbereiche_dict.items() if value[1].strip() == "BUS"]
STRB_Haltestellenbereiche_list = [key for key, value in haltestellenbereiche_dict.items() if value[1].strip() == "STRAB"]
Bus_STRB_Haltestellenbereiche_list = [key for key, value in haltestellenbereiche_dict.items() if value[1].strip() == "BUS STRAB"]
report_list.append(f'   {len(Bus_Haltestellenbereiche_list)} Haltestellenbereiche decken NUR die Betriebsbereich „BUS“ ab')
report_list.append(f'   {len(STRB_Haltestellenbereiche_list)} Haltestellenbereiche decken NUR die Betriebsbereich „STRAB“ ab')
report_list.append(f'   {len(Bus_STRB_Haltestellenbereiche_list)} Haltestellenbereiche decken die Betriebsbereich „BUS“ und "STRB" ab')
report_list.append(f'')


#==========================================================================================================
# •	Bestimme den nördlichsten, westlichsten, südlichsten und östlichsten Haltstellenbereich.
# - nördlichsten Haltstellenbereich:    Max(Breitengrad)    index 1
# - südlichsten Haltstellenbereich:     Min(Breitengrad)    index 1
# - östlichste Haltstellenbereich:      Max(Längengrad)     index 0
# - westlichsten Haltstellenbereich:    Min(Längengrad)     index 0
# •	Wie kann man die Position eines Haltestellenbereichs berechnen?
# - 
report_list.append("Q5, Bestimme den nördlichsten, westlichsten, südlichsten und östlichsten Haltstellenbereich.?")

Max_Laengengrad = max([value[3][0] for key, value in haltestellen_dict.items()])
oestlichste_Haltstellenbereich = [key for key, value in haltestellen_dict.items() if value[3][0] == Max_Laengengrad]
Min_Laengengrad = min([value[3][0] for key, value in haltestellen_dict.items()])
westlichste_Haltstellenbereich = [key for key, value in haltestellen_dict.items() if value[3][0] == Min_Laengengrad]
Max_Breitengrad = max([value[3][1] for key, value in haltestellen_dict.items()])
noerdlichste_Haltstellenbereich = [key for key, value in haltestellen_dict.items() if value[3][1] == Max_Breitengrad]
Min_Breitengrad = min([value[3][1] for key, value in haltestellen_dict.items()])
suedlichste_Haltstellenbereich = [key for key, value in haltestellen_dict.items() if value[3][1] == Min_Breitengrad]

report_list.append(f'   nördlichsten Haltstellenbereich: {noerdlichste_Haltstellenbereich}')
report_list.append(f'   südlichsten Haltstellenbereich: {suedlichste_Haltstellenbereich}')
report_list.append(f'   westlichste_Haltstellenbereich: {westlichste_Haltstellenbereich}')
report_list.append(f'   östlichste_Haltstellenbereich: {oestlichste_Haltstellenbereich}')
report_list.append(f'')

#==========================================================================================================
# Schwierigkeitsgrad – mittel
# •	Welche beiden Linien haben die größte Anzahl gemeinsamer Stationen?
report_list.append("\n")
report_list.append("Schwierigkeitsgrad – mittel")
report_list.append(f'')
report_list.append("Mittel-Q1, Welche beiden Linien haben die größte Anzahl gemeinsamer Stationen?")

# *********************************************************************
# linien_list []: each item in list is a dictionary with    key: "linien"   value: linien, key: "haltestellen"  value: all haltestellen as list[]

linien_halt_list = []

for linien in linienList_all:
    linien_list_dict = {}
    linien_list_dict.update({"linien":linien, "haltestellen": [],"haltestellenbereich": []})
    for key in haltestellenbereiche_dict.keys():
        if str(linien) in haltestellenbereiche_dict[key][2]:
            linien_list_dict["haltestellen"].append(key)
            linien_list_dict["haltestellenbereich"].append(haltestellenbereiche_dict[key][0])
    linien_halt_list.append(linien_list_dict)

# change "haltestellen" from list to set
for item in linien_halt_list:
    for key, value in item.items():
        item["haltestellen"] = set(item["haltestellen"])  

# creat a intersection_list = [] to store [index 0: linien_a, index1: linien_b, index2: number of intersaction haltstellen]
   
intersection_list = []
for i in range(len(linien_halt_list)):
    for item in linien_halt_list[(i+1):]:
        intersection_pair_list = []
        intersection_pair_list.append(linien_halt_list[i]["linien"])
        intersection_pair_list.append(item["linien"])
        intersection_pair_list.append(len(linien_halt_list[i]["haltestellen"].intersection(item["haltestellen"])))
        intersection_list.append(intersection_pair_list)

# finde the max of index 2 in intersection_list = [] and return the index 0 and index 1 of it, which is the linien_a and linien_b
max_intersection = 0
max_intersection_linien = ()
for item in intersection_list:
    if item[2] > max_intersection:
        max_intersection = item[2]
        max_intersection_linien = (item[0],item[1])

# print(max_intersection)
# print(max_intersection_linien)

report_list.append(f'   Linien {max_intersection_linien[0]} und Linien {max_intersection_linien[1]} haben {max_intersection} gemeinsamer Stationen und haben die größte Anzahl')
report_list.append(f'')


#==========================================================================================================
# •	Welche Linie ist an all ihren Haltestellen prozentual am besten mit digitalen Fahrgastinformationsanzeigen ausgestattet? Das gleiche auch für Fahrtreppen und Aufzüge.
# - Linien_dict

# haltestellenbereichemitdfi_list: store all the haltestellenbreiche nr mit digital Anzeiger as a list
haltestellenbereichemitdfi_list = list(map(list, haltestellenbereichemitdfi_dict.items()))
haltestellenbereichemitdfi_list = [item[0] for item in haltestellenbereichemitdfi_list]

haltestellenbereichemitdfi_list = [key for key in haltestellenbereichemitdfi_dict.keys()]
aufzuege_list = [key for key in aufzuege_dict.keys()]
aufzuege_nr_list = [(key,len(value)/2) for key, value in aufzuege_dict.items()]
fahrtreppen_list = [key for key in fahrtreppen_dict.keys()]

haltestellenbereichemitdfi_set = set(haltestellenbereichemitdfi_list)
aufzuege_set = set(aufzuege_list)
fahrtreppen_set = set(fahrtreppen_list)

# convert the haltestellenbereich in linien_list from list to set
for item in linien_halt_list:
    item["haltestellenbereich"] = set(item["haltestellenbereich"])

# loop through linien_list and store len of intersection-index 1 and "linien"-index 0 in a linien_mit_dfi = []
linien_mit_dfi = []
linien_mit_aufzuege = []
linien_mit_fahrtreppen = []

for item in linien_halt_list:
    linien_mit_dfi_sub = []
    linien_mit_dfi_sub.append(item["linien"])
    linien_mit_dfi_sub.append(len(item["haltestellenbereich"].intersection(haltestellenbereichemitdfi_set))/len(item['haltestellen']))
    linien_mit_dfi.append(linien_mit_dfi_sub)
    linien_mit_aufzuege_sub = []
    linien_mit_aufzuege_sub.append(item["linien"])
    linien_mit_aufzuege_sub.append(len(item["haltestellenbereich"].intersection(aufzuege_set))/len(item['haltestellen']))
    linien_mit_aufzuege.append(linien_mit_aufzuege_sub)
    linien_mit_fahrtreppen_sub = []
    linien_mit_fahrtreppen_sub.append(item["linien"])
    linien_mit_fahrtreppen_sub.append(len(item["haltestellenbereich"].intersection(fahrtreppen_set))/len(item['haltestellen']))
    linien_mit_fahrtreppen.append(linien_mit_fahrtreppen_sub)

# print(linien_mit_dfi)
# print(linien_mit_aufzuege)
# print(linien_mit_fahrtreppen)
# print(linien_halt_list[0])

# finde the max of index 2 in intersection_list = [] and return the index 0 and index 1 of it, which is the linien_a and linien_b

max_mit_dfi = max(list(i[1] for i in linien_mit_dfi))    
linien_mit_max_dfi = [i[0] for i in linien_mit_dfi if i[1] == max_mit_dfi]
# print(linien_mit_max_dfi)

max_mit_aufzuege = max(list(i[1] for i in linien_mit_aufzuege))    
linien_mit_max_aufzuege = [i[0] for i in linien_mit_aufzuege if i[1] == max_mit_aufzuege]
# print(linien_mit_max_aufzuege)

max_mit_fahrtreppen = max(list(i[1] for i in linien_mit_fahrtreppen))    
linien_mit_max_fahrtreppen = [i[0] for i in linien_mit_fahrtreppen if i[1] == max_mit_fahrtreppen]
# print(linien_mit_max_fahrtreppen)

report_list.append("Mittel-Q2, Welche Linie ist an all ihren Haltestellen prozentual am besten mit digitalen Fahrgastinformationsanzeigen ausgestattet? Das gleiche auch für Fahrtreppen und Aufzüge.")
report_list.append(f'   Linien {linien_mit_max_dfi} hat {max_mit_dfi*100:}% Haltestellen mit digitalen Fahrgastinformationsanzeigen und ist am besten mit digitalen Fahrgastinformationsanzeigen ausgestattet')
report_list.append(f'   Linien {linien_mit_max_aufzuege} hat {max_mit_aufzuege*100:.2f}% Haltestellen mit digitalen Fahrgastinformationsanzeigen und ist am besten mit digitalen Fahrgastinformationsanzeigen ausgestattet')
report_list.append(f'   inien {linien_mit_max_fahrtreppen} hat {max_mit_fahrtreppen*100:.2f}% Haltestellen mit digitalen Fahrgastinformationsanzeigen und ist am besten mit digitalen Fahrgastinformationsanzeigen ausgestattet')
report_list.append(f'')

haltestellenbereiche_mitAufzuege_list = [key for key in aufzuege_dict.keys()]
haltestellenbereiche_mitfahrtreppen_list = [key for key in fahrtreppen_dict.keys()]

#==========================================================================================================
# •	Der Kölner weiß das eine zweistellige Nummer eine Straßenbahn und eine dreistellige Nummer ein Bus ist. Aber könnte man diese Information auch aus den Daten ziehen? Direkt angegeben ist es nicht.

for item in linien_halt_list:
    if int(item['linien']) < 100:
        item.update({"Betriebsbereich": "STRAB"})
    if int(item['linien']) >= 100:
        item.update({"Betriebsbereich": "Bus"})

report_list.append("Mittel-Q3, Der Kölner weiß das eine zweistellige Nummer eine Straßenbahn und eine dreistellige Nummer ein Bus ist. Aber könnte man diese Information auch aus den Daten ziehen? Direkt angegeben ist es nicht.")
report_list.append(f'   ja, ein key für "Bus" und "STRB" in Linien dictionary einfügen')
report_list.append(f'')
#==========================================================================================================
# •	Liste alle Straßenbahnlinien jeweils mit allen Straßenbahnlinien in die man auf ihrem Weg direkt umsteigen kann auf.

# seperate Bus and STRB from linien_halt_list. and creat for each a list for better analysis
STRAB_linien_halt_list = []
Bus_linien_halt_list = []
for item in linien_halt_list:
    if item['Betriebsbereich'] == "STRAB":
        STRAB_linien_halt_list.append(item)
    if item['Betriebsbereich'] == "Bus":
        Bus_linien_halt_list.append(item)

# each linien instersetion with each linien (including itself) once and stores the len of intersection in one list, index 0 of this list is the linien number. 
STRAB_intersection_linien_halt_list = []
for item in STRAB_linien_halt_list:
    inside_list = []
    inside_list.append(item['linien'])
    for other_item in STRAB_linien_halt_list:
        inside_list.append(len(set(item['haltestellenbereich']).intersection(set(other_item['haltestellenbereich']))))
    STRAB_intersection_linien_halt_list.append(inside_list)

# print(len(STRAB_intersection_linien_halt_list))

# filter if all len of instersetion of one linien are greater than 0, return the index 0 of this sublist, which is the linien number. 
STRAB_linien_intersection_withall_List = []
for item in STRAB_intersection_linien_halt_list:
    if not 0 in item:
        STRAB_linien_intersection_withall_List.append(item[0])

# print(STRAB_linien_intersection_withall_List)        

report_list.append("Mittel-Q4, Liste alle Straßenbahnlinien jeweils mit allen Straßenbahnlinien in die man auf ihrem Weg direkt umsteigen kann auf?")
report_list.append(f'   Mit Straßenbahnlinien {STRAB_linien_intersection_withall_List} kann man mit allen Straßenbahnlinien auf ihrem Weg direkt umsteigen')
report_list.append(f'')

#==========================================================================================================
# •	Haben alle Straßenbahnlinien mindestens ein Kundencenter an einer ihrer Haltestellen? Und von welchen Linien ohne Kundencenter kann man mit einmal Umsteigen in eine andere Linie zu einem Kundencenter gelangen. 

# pprint.pprint(verkaufsorte_dict)
# filter all the haltestellenbereiche which has KundenCenter from verkaufsorte_dict and store them in a list

haltestellenbereiche_mitKundenCenter_list = []
for key, value in verkaufsorte_dict.items():
    if "KundenCenter" in value:
        haltestellenbereiche_mitKundenCenter_list.append(key)
# print(haltestellenbereiche_mitKundenCenter_list)

# filter all the linien, stations of this linien which has KundenCenter by intersection of two sets
linien_mit_kundencenter = []
for item in linien_halt_list:
    linien_mit_kundencenter_sub = []
    linien_mit_kundencenter_sub.append(item["linien"])
    linien_mit_kundencenter_sub.append(len(set(item["haltestellenbereich"]).intersection(set(haltestellenbereiche_mitKundenCenter_list))))
    linien_mit_kundencenter.append(linien_mit_kundencenter_sub)
# print(linien_mit_kundencenter)

# seperate STRB Linien from
STRABlinien_mit_kundencenter = []
for item in linien_mit_kundencenter:
    if item[0] < 100 and item[1] >0:
        STRABlinien_mit_kundencenter.append(item[0])
# print(STRABlinien_mit_kundencenter, len(STRABlinien_mit_kundencenter))

report_list.append("Mittel-Q5.1, Haben alle Straßenbahnlinien mindestens ein Kundencenter an einer ihrer Haltestellen?")
report_list.append(f'   Nein, {len(STRABlinien_mit_kundencenter)} Linien haben Kundencenter. und die Linien sind {STRABlinien_mit_kundencenter}')
report_list.append(f'')

# filter STRB Linien which do not have kundencenter
# print(STRB_Linien)
STRAB_linien_ohne_kundencenter = set(STRB_Linien).difference(set(STRABlinien_mit_kundencenter))
# print(STRAB_linien_ohne_kundencenter)

report_list.append("Mittel-Q5.2, Und von welchen Linien ohne Kundencenter kann man mit einmal Umsteigen in eine andere Linie zu einem Kundencenter gelangen?")
report_list.append(f'   Straßenbahnlinien {STRAB_linien_ohne_kundencenter} hat kein Kundencenter. Man kann mit einmal Umsteigen von {STRAB_linien_ohne_kundencenter} in eine andere Linie zu einem Kundencenter gelangen.')
report_list.append(f'\n')
report_list.append(f'\n')
bibliothek.report(report_list,"KVB_Report")

#==========================================================================================================
# Schwierigkeitsgrad - schwer (Die Erde ist eine Scheibe – behandele Längen und Breitengrad als X,Y Koordinaten)
# Schwer - Q1
# •	Suche für eine eingegebene Position:                                function: distance_two_positions
# o	Die nächste Straßenbahnhaltestelle                                  dictionay: with coordinate as key, with ASS, Fahrtreppen, Aufzug as values
# o	Die nächste Straßenbahnhaltestelle mit Fahrtreppen (Störung?)
# o	Die nächste Straßenbahnhaltestelle mit Aufzug (Störung?)


report_list.append("Schwierigkeitsgrad - schwer")
bibliothek.report(report_list,"KVB_Report")
report_list.append(f'')

# print(bibliothek.distance_two_positions_haversine(50.93682155148997, 6.952888324756933,50.77505912062104, 6.089643665583605))
# print(bibliothek.distance_two_positions_haversine(48.8566, 2.3522,50.0647,19.9450))

# creat an coodinates_haltestellen_dict_list

coodinates_haltestellen_dict_list = []

haltestellen_list = [value for value in haltestellen_dict.values()]

# creat an coodinates_haltestellen_dict_list
coodinates_haltestellen_dict_list = []

for key, value in haltestellen_dict.items():
    sub_dict = {"coordinate": None}
    sub_dict = {"Linien": None}
    sub_dict = {"ASS": None}
    sub_dict = {"Betriebsbereich": None}
    sub_dict = {"Haltestellen": None}
    for index in range(int(len(value)/4)):
        sub_dict["Haltestellen"] = key
        sub_dict["coordinate"] = value[3+index*4]
        sub_dict["Linien"]= value[(2+index*4)]
        sub_dict["ASS"] = value[1+index*4]
        sub_dict["Betriebsbereich"] = value[0+index*4]
    coodinates_haltestellen_dict_list.append(sub_dict)

# pprint.pprint(coodinates_haltestellen_dict_list)

# lat = 50.93876833721875 
# long = 6.948352642626962

def naechste_STRAB_haltestelle_sucher(latitude,longitude):
    """
    finde the nearst STRAB Station in Köln

    input:      longitude,latitude

    return:     nearst STRAB Station, distance to nearst STRAB Station
    
    """

    naechste_STRAB_haltestelle = {"naechste_STRAB_haltestelle": None, "Linien": None, "Entfernung zu naechste STRAB Haltestelle": None} 
    min_distance = 1000000
    for item in coodinates_haltestellen_dict_list:
        if item["Betriebsbereich"] == "STRAB":
            naechste_haltestellen_distance = bibliothek.distance_two_positions_haversine(latitude,longitude,*item["coordinate"][::-1])
            if naechste_haltestellen_distance < min_distance:
                min_distance = naechste_haltestellen_distance
                naechste_STRAB_haltestelle["naechste_STRAB_haltestelle"] = item["Haltestellen"]
                naechste_STRAB_haltestelle["Linien"] = item["Linien"]
                naechste_STRAB_haltestelle["Entfernung zu naechste STRAB Haltestelle"] = naechste_haltestellen_distance

    return naechste_STRAB_haltestelle

naechste_STRAB_haltestelle = naechste_STRAB_haltestelle_sucher(50.9350701403915, 6.88517257745734)
                                                          
# bibliothek.distance_two_positions_haversine(lat,long,)

report_list.append("Schwer-Q1,Suche für eine eingegebene Position: Die nächste Straßenbahnhaltestelle")
report_list.append(f'   Bitte Funktion "naechste_STRAB_haltestelle_sucher" im Quell-Code Line 384-405 anschauen')
report_list.append(f'   Position: 50.9350701403915, 6.88517257745734')
report_list.append(f'   {naechste_STRAB_haltestelle}')
report_list.append(f'\n')
bibliothek.report(report_list,"KVB_Report")

#==========================================================================================================
# Schwer-Q2
# •	Leider gibt es in den Daten keine direkten Informationen in welcher Reihenfolge die einzelnen Linien die Haltestellen abfahren. Könnte man das anhand der Vorgabe einer der beiden Endhaltestellen und den „Entfernungen“ der Haltestellen durch ihre Koordinaten berechnen. Wie akkurat wäre diese Berechnung? Gebt dazu einer der Strecken von Hand ein und vergleicht. Entwickelt vorher die Datenstruktur, in der alle Haltestellen aller Linien in ihrer Reihenfolge gespeichert werden können.
# - Linien_dict

# *********************************************************************************************************
# Data Structure
## - rearrange data structure for further analysis
## - calculate the avg of longitude and latitude of each haltestellenbereich
## - haltestellenbereich_coordinate_dict: key: 911 haltestellenbereich / value: avg coordinate of each haltestellenbereich 

haltestellenbereich_coordinate_dict = {}
for key, value in haltestellen_dict.items():
    sum_longitude = 0
    sum_latitude = 0
    for index in range(int(len(value)/4)):
        sum_longitude = sum_longitude + value[3+index*4][0]
        sum_latitude = sum_latitude + value[3+index*4][1]
    haltestellenbereich_coordinate_dict.update({key: [sum_longitude/(len(value)/4),sum_latitude/(len(value)/4)]})

# pprint.pprint(haltestellenbereich_coordinate_dict)
# print(len(haltestellenbereich_coordinate_dict))

# *********************************************************************************************************
## update linien_halt_list with coordination
## update add each linien in linien_halt_list with a new key "coordiante": and with a dictionary(haltestellenbreich: avg coordiante []) as value

for linien in linien_halt_list:
    station_coordiate = {}
    for station in linien['haltestellen']: 
        for key in haltestellenbereich_coordinate_dict:
            if station == key:
                station_coordiate.update({station: haltestellenbereich_coordinate_dict[key]})
    linien.update({"coordinate": station_coordiate})

# pprint.pprint(linien_halt_list[0])


# *********************************************************************************************************
# Algorithm
# write a function to finde max distance across all combination of staions in one linien
# loop all the linien, and each stations of each linien, and return the distance between any staion to station.
# store the sum of all cross station as total distance of each station and store the station name as key in a list[dict]: station_total_distance_dict = []

# --------------------------------------------------------------------------------------------------------------------------------------------------------------------
# cross stations: one-side-matrix version:
# single sation total distance: full matrix

station_distance_dict = []
station_total_distance_dict = []
for linien in linien_halt_list:   
    station_distance_sub_dict = {}
    station_key = []
    station_key = list(linien['coordinate'].keys())
    station_total_distance_sub_dict={}
    for i in range(len(station_key)):
        total_distance = 0 
        for j in range(len(station_key)):
            two_stations_distance = bibliothek.distance_two_positions_haversine(*linien['coordinate'][station_key[i]],*linien['coordinate'][station_key[j]])
            total_distance += two_stations_distance        
        station_total_distance_sub_dict.update({station_key[i]: total_distance})
    station_total_distance_dict.append(station_total_distance_sub_dict)
    linien.update({"station_total_distance":station_total_distance_sub_dict})
    for i in range(0,len(station_key)-1):
        for j in range((i+1),len(station_key)):
            two_stations_distance = bibliothek.distance_two_positions_haversine(*linien['coordinate'][station_key[i]],*linien['coordinate'][station_key[j]])
            station_distance_sub_dict.update({(station_key[i],station_key[j]): two_stations_distance})    
    station_distance_dict.append(station_distance_sub_dict)
    linien.update({"station_distance":station_distance_sub_dict})


# ------------------------------------------------------------------------------------------------------------------------------------------------------------------
# list all the STRAB Linien in Sequence Oder - works

for linien in linien_halt_list:                                                                                                                 # loop each linien
    if linien['Betriebsbereich'] == "STRAB":                                                                                                    # filter only STRAB
        linien_station = list(linien['station_total_distance'].keys())
        linien_station_distance_dict = {key:value for key,value in linien['station_distance'].items()}                                          # seperate linien_station_distance_dict from linien_halt_list for while looping 
        end_station = bibliothek.max_min_dict_finder(linien['station_total_distance'],"max")['max_value_key']                                   # find one end station of each linien
        linien.update({"linien_plan":[end_station]}) 
        first_station = end_station                                                                                                             # save first sation in linien["linien_plan"] key as list value

        while len(linien_station) > 1:
            first_station            
            from_first_station_dict = {key:value for key,value in linien_station_distance_dict.items() if key[0] == first_station}              # filter all the distance from station_1 
            to_first_station_dict = {key:value for key,value in linien_station_distance_dict.items() if key[1] == first_station}                # filter all the distance to station_1
            first_station_crossdistance_dict = from_first_station_dict | to_first_station_dict                                                  # list all the cross distance to station_1 from rest of stations

            next_station = bibliothek.max_min_dict_finder(first_station_crossdistance_dict,"min")['min_value_key']                              # find min distance next station
            for item in next_station:                                                                                                           # seperate the next station from tuple
                if item != first_station:
                    next_station = item

            linien["linien_plan"].append(next_station)
            linien_station.remove(first_station)                                                                                                # for next loop next_station = first_station
            linien_station_distance_dict = {key:value for key,value in linien_station_distance_dict.items() if key[0] != first_station}         # remove all the key and value with first station from distance_dict for next loop                                                                                                                     # pop first station from the stations_list
            linien_station_distance_dict = {key:value for key,value in linien_station_distance_dict.items() if key[1] != first_station}
            first_station = next_station                                                                                                                                                            

# pprint.pprint(linien_halt_list[10])

STRAB_Linien_fahrplan_dict = {}
for linien in linien_halt_list:
    if linien['Betriebsbereich'] == "STRAB":
        STRAB_Linien_fahrplan_dict.update({linien["linien"]: linien["linien_plan"]})

# pprint.pprint(STRAB_Linien_fahrplan_dict)

report_list.append("Schwer-Q2, alle Haltestellen aller STRAB Linien in ihrer Reihenfolge:")
report_list.append(f'')
for key, value in STRAB_Linien_fahrplan_dict.items():
    report_list.append(f'   Straßenbahnlinien {key} : {value}')
    report_list.append(f'')
bibliothek.report(report_list,"KVB_Report")
report_list.append(f'\n')

# ------------------------------------------------------------------------------------------------------------------------------------------------------------------

linien_18_station = []
for linien in linien_halt_list:
    if linien['linien'] == 18:
        linien_18_station = list(linien['station_total_distance'])

# print(linien_18_station)

#==========================================================================================================
# Schwierigkeitsgrad – unmenschlich (Die Erde ist doch rund, um genau zu sein, eine Kugel)
# •	Entwickelt eine Funktion die die Entfernung zweier Koordinatenpaare in Meter/Kilometer berechnen kann. Stichwort :„Orthodrome“. 
#   Überarbeitet die Funktionen der Bibliothek die mit Entfernungen arbeiten, das mit Meter oder Kilometer arbeiten.
#   Nutzt dazu die Erde als idealisierte Kugel mit einem Radius von 6371 km. Lasst euch dabei von Google oder dem LLM eures Vertrauens helfen.

# bibliothek.distance_two_positions_haversine(lat,long,)


    """
    Haversine Formula:

    d = 2R * sin⁻¹(√[sin²((θ₂ - θ₁)/2) + cosθ₁ * cosθ₂ * sin²((φ₂ - φ₁)/2)])

        where:  θ₁, φ₁ - First point latitude and longitude coordinates;
                θ₂, φ₂ - Second point latitude and longitude coordinates;
                R -  Earth's radius (R = 6371 km); and
                d - Distance between them along Earth's surface.
    """


report_list.append("Schwer-Q3, Entwickelt eine Funktion die die Entfernung zweier Koordinatenpaare in Meter/Kilometer berechnen kann (Die Erde ist doch rund, um genau zu sein, eine Kugel).")
report_list.append(f'   Bitte Funktion "distance_two_positions_haversine" im "bibliothek" Quell-Code Line 163-196 anschauen')
report_list.append(f'\n')
report_list.append(f'   Haversine Formula: d = 2R * sin⁻¹(√[sin²((θ₂ - θ₁)/2) + cosθ₁ * cosθ₂ * sin²((φ₂ - φ₁)/2)])')
report_list.append(f'   θ₁, φ₁ - First position latitude and longitude coordinates;')
report_list.append(f'   θ₂, φ₂ - Second position latitude and longitude coordinates;')
report_list.append(f'   R -  Earth Radius 6371 km')
report_list.append(f'   d - Distance between them along Earth surface')
bibliothek.report(report_list,"KVB_Report")
