import functions, functions_loader, pprint
#**************************************************************************************************
# ------------------- Schwierigkeitsgrad – leicht -------------------------------------------------
#**************************************************************************************************
#
print(f"-"*150)
# --- Anzahl der Bus und Bahnlinien ----------------------------------------------------------------
aus_line = functions_loader.func_all_lines_list()
print (f"Es gibt {len(set(aus_line))} Bus- und Bahnlinien")
#
# --- Anzahl Haltestellenbereiche ------------------------------------------------------------------
prop_dict =  functions_loader.load_Data("haltestellenbereiche.json")
haltestellenbereich = [idx["Haltestellenbereich"] for idx in prop_dict]
numb_hstb = len(haltestellenbereich)
print (f"und {numb_hstb} Haltestellen")
#
# --- Welcher Haltestellenbereich hat die meisten Haltestellen ?
print(f"-"*150) 
rehst, max_count = functions.hstb_max_hast()
print (f"Die meisten Haltestellenbereiche hat {rehst} mit {max_count} Bereichen.")
# --- an welchem Haltestelle treffen sich die meisten Linien?----------------------------------
#
name_hst, max_lint = functions.hst_max_linien()
print (f"An der Haltestelle {name_hst} kommen {max_lint} Linien zusammen.")
#
# --- Wieviel Haltestellenbereiche haben Fahrtreppen, Aufzüge, beides oder keines von beidem? ------
hstb_mit_rollt_und_aufz, hstb_mit_aufz,hstb_mit_rollt,bus,strab,bus_strab = functions.aufz_trpp()
print(f"-"*150) 
print (f"Es gibt {len(hstb_mit_rollt_und_aufz)} Haltestellen die Aufzüge und Rolltreppen haben,")
print (f"an {len(hstb_mit_aufz)} Haltestellen gibt es nur Aufzüge und an {len(hstb_mit_rollt)} nur Rolltreppen.")
#
#---- •	Wieviel Haltestellenbereiche decken jeweils die Betriebsbereich „BUS“, „STRAB“ oder beides ab?---
print(f"-"*150) 
print (f"Es gibt {bus} Bus-, {strab} Straßenbahn- und {bus_strab} kompinierte Stationen.")
#
#------- Bestimme den nördlichsten, westlichsten, südlichsten und östlichsten Haltstellenbereich ----
#
print(f"-"*150) 
geo = (functions_loader.load_geo_Data("haltestellen.json","Name","coordinates"))                # lädt die Koordinaten und Haltestellennamen aus json Datei
#print (geo)
koordinaten = geo[1]                                                                # separiert die Koordinaten-Liste von der Namensliste
x_wert = [koordinate[0] for koordinate in koordinaten]                              # aufteilen in X Werte
y_wert = [koordinate[1] for koordinate in koordinaten]                              # und y Werte

idx_ost = x_wert.index(max(x_wert))                                                # ermittelt den max X Wert und gibt den Index des Wertes zurück
hst_ost = geo[0][idx_ost]                                                         # gibt den Namen an dem Index des max X Wertes aus 
#print (idx_ost)
print (f"{hst_ost} ist die östlichste Haltestelle der KVB")

idx_west = x_wert.index(min(x_wert))                                                # ermittelt den min X Wert und gibt den Index des Wertes zurück
hst_west = geo[0][idx_west]                                                         # gibt den Namen an dem Index des min X Wertes aus
#print (idx_west)
print (f"{hst_west} ist die westlichste Haltestelle der KVB")

idx_nord = y_wert.index(max(y_wert))                                                 # ermittelt den max Y Wert und gibt den Index des Wertes zurück
hst_nord = geo[0][idx_nord]                                                           # gibt den Namen an dem Index des max Y Wertes aus 
#print (idx_nord)
print (f"{hst_nord} ist die nördlichste Haltestelle der KVB")

idx_sued = y_wert.index(min(y_wert))                                                # ermittelt den min Y Wert und gibt den Index des Wertes zurück
hst_sued = geo[0][idx_sued]                                                         # gibt den Namen an dem Index des min Y Wertes aus
#print (idx_sued)
print (f"{hst_sued} ist die südlichste Haltestelle der KVB")

#********************************************************************************************************
# ------------------- Schwierigkeitsgrad – mittel -------------------------------------------------------
#********************************************************************************************************
#
# -----------------   Welche beiden Linien haben die größte Anzahl gemeinsamer Stationen? ---------------
print(f"-"*150)
print (f"Die Linien {functions.common_stations()[0]} haben insgesamt {functions.common_stations()[1]} gemeinsame Haltestellen.")
#
# --- eine zweistellige Nummer steht für eine Straßenbahn und eine dreistellige Nummer für ein Bus -------
#
print(f"-"*150)
print (f"Es gibt nur Buslinien mit ein- oder zweistelligen Nummern. Das sind sie:{functions.bus_strab_digits()[1],}")
print (f"Es gibt nur Strassenbahnlinien mit dreistelligen Nummern. Das sind sie:{functions.bus_strab_digits()[0],}")
#
# ---- Liste alle Straßenbahnlinien jeweils mit allen Straßenbahnlinien in die man auf ihrem Weg direkt umsteigen kann auf ---
print(f"-"*150)
result  = functions.strab_umst()

print (f"Von der Line 1 kann man in folgende Straßenbahnlinien umsteigen:{result['1']}")
print (f"Von der Line 3 kann man in folgende Straßenbahnlinien umsteigen:{result['3']}")
print (f"Von der Line 4 kann man in folgende Straßenbahnlinien umsteigen:{result['4']}")
print (f"Von der Line 5 kann man in folgende Straßenbahnlinien umsteigen:{result['5']}")
print (f"Von der Line 7 kann man in folgende Straßenbahnlinien umsteigen:{result['7']}")
print (f"Von der Line 9 kann man in folgende Straßenbahnlinien umsteigen:{result['9']}")
print (f"Von der Line 12 kann man in folgende Straßenbahnlinien umsteigen:{result['12']}")
print (f"Von der Line 13 kann man in folgende Straßenbahnlinien umsteigen:{result['13']}")
print (f"Von der Line 15 kann man in folgende Straßenbahnlinien umsteigen:{result['15']}")
print (f"Von der Line 16 kann man in folgende Straßenbahnlinien umsteigen:{result['16']}")
print (f"Von der Line 17 kann man in folgende Straßenbahnlinien umsteigen:{result['17']}")
print (f"Von der Line 18 kann man in folgende Straßenbahnlinien umsteigen:{result['18']}")
#



