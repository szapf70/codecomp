# import modules

import helmuts_functions as hf
import kvb_functions
import pandas as pd
import os

# suppress Pandas Future warnings
import warnings
warnings.simplefilter(action='ignore', category=FutureWarning)

# option to display complete dataframes
pd.set_option('display.max_rows', None, 'display.max_columns', None, 'display.max_colwidth', None)


def main():
    # ============================================================
    # input files

    hf.setze_pfad()

    json_subdirectory = ""  # 'json'

    station_area_file = 'haltestellenbereiche.json'
    station_file = 'haltestellen.json'
    station_area_diginfo_file = 'haltestellenbereichemitdfi.json'
    place_of_sale_file = 'verkaufsorte.json'
    elevator_file = 'aufzuege.json'
    elevator_malfunction_file = 'aufzugstoerungen.json'
    escalator_file = 'fahrtreppen.json'
    escalator_malfunction_file = 'fahrtreppenstoerungen.json'

    # ============================================================
    # read all files

    station_area_data = kvb_functions.read_json_file(station_area_file, json_subdirectory, 'latin-1')
    station_data = kvb_functions.read_json_file(station_file, json_subdirectory, 'latin-1')
    station_area_diginfo_data = kvb_functions.read_json_file(station_area_diginfo_file, json_subdirectory)
    place_of_sale_data = kvb_functions.read_json_file(place_of_sale_file, json_subdirectory, 'latin-1')
    elevator_data = kvb_functions.read_json_file(elevator_file, json_subdirectory)
    elevator_malfunction_data = kvb_functions.read_json_file(elevator_malfunction_file, json_subdirectory)
    escalator_data = kvb_functions.read_json_file(escalator_file, json_subdirectory)
    escalator_malfunction_data = kvb_functions.read_json_file(escalator_malfunction_file, json_subdirectory, 'latin-1')

    # ============================================================
    # create new data structure

    station_area_ds, station_area_key_ds = kvb_functions.create_station_area_ds(station_area_data)
    station_area_ds = kvb_functions.add_station_data_to_ds(station_area_ds, station_area_key_ds, station_data)
    station_area_ds = kvb_functions.add_diginfo_data_to_ds(station_area_ds, station_area_diginfo_data)
    station_area_ds = kvb_functions.add_elevator_data_to_ds(station_area_ds, elevator_data)
    station_area_ds = kvb_functions.add_escalator_data_to_ds(station_area_ds, escalator_data)
    station_area_ds = kvb_functions.add_place_of_sale_data_to_ds(station_area_ds, place_of_sale_data)
    station_area_ds = kvb_functions.add_missing_infos_to_ds(station_area_ds)

    # ============================================================

    # At first build some inital data sets
    # get the main info for bus lines
    linien_dict, df_linien = hf.linien_info(station_area_ds)
    strab_dict, _ = hf.split_linien_dict(linien_dict)

    # get the main info for station areas
    df_haltestellen, _, _ = hf.haltestellenbereich_info(station_area_ds)

    # read in additional data
    daten = hf.dateneinlesen()
    
    # Next call is not required, but can be used to get the data sets
    hb_mit_dfi_set = hf.haltestellenbereichemitdfi(daten)
    
    # Existing data_frames
    #   df_linien
    #   df_haltestellen 
    #   df_hs_grouped  (df_haltestellen grouped by Haltestellennamen)
    #   df_haltestellen_mit_dfi
    #   df_haltestellen_mit_diginfo
    #   df_haltestellen_mit_elevator
    #   df_haltestellen_mit_escalator
    #   df_haltestellen_mit_place_of_sale
    #   df_max_pos
    #   df_hs_mean_pos
    
    # ########################################################
    # Aufgabe "leicht" Nr .1 - Anzahl der Haltestellenbereiche
    print(_txt := '\nAufgabe "leicht" Nr .1')
    print("=" * len(_txt) + '\n')
    print("Anzahl der Linien:", len(df_linien))
    print(_txt := "Anzahl der Haltestellenbfdf_ereiche:", len(set(df_haltestellen["Haltestellennamen"])), ".\n")
    print("=" * (len(_txt)+4) + '\n')

    # Aufgabe "leicht" Nr .2a
    print(_txt := '\nAufgabe "leicht" Nr .2a')
    print("=" * len(_txt) + '\n')

    df_hs_grouped= hf.group_df_haltestellen(df_haltestellen)
    haltestellenname, max_ass_wert = hf.find_haltestelle_with_max_ass(df_hs_grouped)
    
    print(f'Die meisten Haltestellen ({max_ass_wert}) befinden sich im Haltestellenbereich {haltestellenname}.\n')

    hf.create_html_map(df_haltestellen, "Haltestellen.html")

    # tip: df.iloc[df["Anzahl Linien"].idxmax()]["Haltestellenname"]

    # ===================================================================
    # Aufgabe "leicht" Nr .2b an welchem Treffen sich die meisten Linien?
    
    print('=============================')
    print(_txt := '\nAufgabe "leicht" Nr .2b')
    print("=" * len(_txt) + '\n')
    name, anz = hf.find_stop_with_max_lines(df_haltestellen)

    print(f'Die meisten Linien ({anz}) treffen sich im Haltestellenbereich {name}.\n')

    # =============================================================================
    # Aufgabe "leicht" Nr .3
    # Alle doppelten Haltestellen werden entfernt, denn die Einträge für die Anzahl
    # der Aufzüge etc sind gleich
    
    print('=============================')
    print(_txt := '\nAufgabe "leicht" Nr .3')
    print("=" * len(_txt) + '\n')
     
    print("\nHaltestellen mit Fahrtreppen:", (df_hs_grouped['Fahrtreppen'] > 0).sum())
    print("Haltestellen mit Aufzügen:", (df_hs_grouped['Aufzuege'] > 0).sum())
    print("Haltestellen mit Fahrtreppen und Aufzügen:", ((df_hs_grouped['Fahrtreppen'] > 0) & (df_hs_grouped['Aufzuege'] > 0)).sum())
    print("Haltestellen ohne Fahrtreppen und Aufzügen:", ((df_hs_grouped['Fahrtreppen'] == 0) & (df_hs_grouped['Aufzuege'] == 0)).sum(),"\n")


    # =====================================================
    # Aufage "leicht" Nr 4 - „BUS“, „STRAB“ oder beides ab?
    # calculate stations with BUS, STRAB or both
    
    print('=============================')
    print(_txt := '\nAufgabe "leicht" Nr .4')
    print('=' * len(_txt) + '\n')

    betriebsbereiche, counts = hf.calc_betriebsbreiche(station_area_ds)
    print(f'\n {counts["BUS"]} Haltestellenbereiche mit Bus,\
    \n {counts["STRAB"]} Haltestellenbereiche mit Straßenbahn und \
    \n {counts["BOTH"]} Haltestellenbereiche mit Bus und Straßenbahn \n')

    # =====================================================
    # Aufgabe "leicht" Nr. 5
    # Calculate the maximum positions of the stations
    
    print('=============================')
    print(_txt := '\nAufgabe "leicht" Nr .5')
    print('=' * len(_txt) + '\n')

    df_max_pos, _ = hf.calc_max_positions(df_haltestellen)

    # Provides a html-file showing the max positions of the stations
    filename = "max_positions.html"
    hf.create_html_map(df_max_pos, filename)

    # Ergänzung zu Aufgabe "leicht" - Nr 5b
    print(_txt := '\nAufgabe "leicht" Nr .5b')
    print('=' * len(_txt) + '\n')
    print("Die Mittelposition der Haltestellenbereiche sind z.B.: \n", df_hs_grouped.iloc[0:5,[0,3,4]])
    print(".......\n")

    # ==============================================
    # #### Schwierigkeitsgrad mittel ###############
    # ==============================================

    # ===================================================================================
    # Aufage "mittel" Nr 1 - Paar mit der höchsten Anzahl an gemeinsamen Elementen finden
    # ===================================================================================    
    print('=============================')
    print('=============================')
    print(_txt := '\nAufgabe "mittelt" Nr. 1 ')
    print('=' * len(_txt) + '\n')

    # Derive bus lines with the most common stations
    common_stops = hf.most_common_elements(linien_dict)

    # Paar mit der höchsten Anzahl an gemeinsamen Elementen finden
    max_common_stops = max(common_stops, key=lambda x: x[1])
    print(f"\nDie Linien {max_common_stops[0][0]} und {max_common_stops[0][1]} haben die meisten gemeinsamen Haltestellen: {max_common_stops[1]}\n   ")
    Umsteigemoeglichkeiten = ", ".join(max_common_stops[2])
    print(f"Umsteigemöglichkeiten:{Umsteigemoeglichkeiten} \n\n")
    print('=' * len(_txt) + '\n')
    
    # =====================================================
    # Aufgabe "mittel" Nr 2 - digitale Fahrgastinformation
    # =====================================================
    print(_txt := 'Aufgabe "mittelt" Nr. 2')
    print('=' * len(_txt) + '\n')

    # Function call does not need a return, the operations are made on the dataframe itself in the function
    _ = hf.digitale_fahrgastinformation(df_linien)
    
    features = ["DFI", "Treppen", "Aufzuege"]
    for feature in features:
        line_w_max_rel_feature, max_values, _rel = hf.find_highest_value_of_feature(df_linien, feature)
        print(f'\nDie Linie mit den besten prozentualen {feature} ist Linie {line_w_max_rel_feature} mit {max_values} {feature} ({_rel:.1f})') 
                  
    print('=' * len(_txt) + '\n')
    
    # =====================================================
    # Aufgabe "mittel" Nr 3 - ein- und zweistellige Nummern
    # =====================================================
    print(_txt := 'Aufgabe "mittelt" Nr. 3')
    print('=' * len(_txt) + '\n') 

    assumption = hf.check_number_assumption(betriebsbereiche, linien_dict, df_linien)
    print("Die Annahme bezüglich der ein-, zwei- und dreisstelligen Nummern ist: ", assumption)

    print('=' * len(_txt) + '\n') 
    
    # =============================================
    # Aufgabe "mittel" Nr 4 - Umsteigemöglichkeiten
    # =============================================
    print(_txt := '\nAufgabe "mittelt" Nr. 4')
    print('=' * len(_txt) + '\n') 
    
    # Derive lines with the most common stations

    results_strab = hf.most_common_elements(strab_dict)
    
    matrix = hf.list_of_changeovers(results_strab)
    print("\nEs gibt", len(matrix), "Linien mit Umsteigemöglichkeiten:")
    for linie in sorted(matrix.keys()):
        print(f"Linie {linie:>3d} hat die {len(matrix[linie]):>2d} Umsteigemöglichkeiten: {sorted(matrix[linie])}")
    
    print('=' * len(_txt) + '\n') 
    
    # ======================================================
    # Aufgabe "mittel" Nr 5a - Haltestellen mit Kundencenter
    # ======================================================  
    print(_txt := 'Aufgabe "mittelt" Nr. 5a')
    print('=' * len(_txt) + '\n') 
    df_strab = df_linien.loc[df_linien["Linie"].apply(lambda x: len(str(x)) != 3)]
    
    line_type = "strab"
    list_of_customer_center, lines_with_customer_center = hf.customer_center(station_area_ds, line_type)
    
    # all_lines = set(df_linien["Linie"].tolist())
    all_strabs = set(df_strab["Linie"].tolist())
    
    lines_wo_customer_center = all_strabs.difference(lines_with_customer_center)
    
    print("Haltestellen mit Kundencenter(n): ",[x[0] for x in list_of_customer_center])  # ", ".join(pd.DataFrame(list_of_customer_center).iloc[:,0].tolist())
    print(f"{len(lines_with_customer_center)} Linie(n) mit mindestens einem Kundencenter an einer ihrer Haltestellen: {sorted(lines_with_customer_center)}")
    print(f"{len(lines_wo_customer_center)} Linie(n), die keinen Kundencenter an einer ihrer Haltestellen haben: {sorted(lines_wo_customer_center)}")
    print(f"Insgesamt gibt es {len(all_strabs)} Linien. Das sind die Linen {sorted(all_strabs)}.")
    
    print('=' * len(_txt) + '\n')     
    
    # ============================================================
    # Aufgabe "mittel" Nr 5b - Umsteigen in Linien mit Kundencenter
    # ============================================================
    print(_txt := 'Aufgabe "mittelt" Nr. 5b')
    print('=' * len(_txt) + '\n')
    
    changeover_to_lines_wcc = hf.changeover_to_lines_with_customer_center(matrix, lines_with_customer_center, lines_wo_customer_center)
    lines_with_change_over_to_lwcc = sorted(list(changeover_to_lines_wcc.keys())) 
    for line in lines_with_change_over_to_lwcc:
        h11 = sorted(changeover_to_lines_wcc[line])
        print(f"Linie {line} hat {len(changeover_to_lines_wcc[line])} Umsteigemöglichkeiten in Linien mit Kundencenter:", *h11, sep=", ")

    print('=' * len(_txt) + '\n')
    
    # ==============================================
    # #### Schwierigkeitsgrad schwer ###############
    # ==============================================

    # ====================================
    # Aufgabe "schwer" Nr 1 - Distanzsuche
    # ====================================
    print(_txt := 'Aufgabe "schwer" Nr. 1')
    print('=' * len(_txt) + '\n')
    
    # set position to serach the nearest item
    position = (50.9417834179503, 6.95781192779762)
      
    # read in all Fahrtreppenstörungen, return >data_fahrtreppen_stoerungen< not used
    df_fahrtreppen_stoerungen, _ = hf.transport(daten, "fahrtreppenstoerungen")
    
    # read in all Aufzugstörungen, return >data_aufzuege_stoerungen< not used
    df_aufzuege_stoerungen, _ = hf.transport(daten, "aufzugstoerungen")
    
    idx_nearest = hf.search_nearest(position, df_hs_grouped)
    print(f"\nDie Haltestelle, die am nächsten liegt:\n{df_hs_grouped.iloc[idx_nearest][0:2]}")
    
    # Aufzuege !!!
    # create a dataframe with the coordinates of the elevators
    df_aufzuege, _ = hf.aufzuege_info(station_area_ds)

    # determin des index of the nearest elevator in the dataframe for elevators 
    idx_nearest = hf.search_nearest(position, df_aufzuege)
    
    # determine the nearest elevator in the dataframe for elevators
    nearest_elevator = df_aufzuege.iloc[idx_nearest]['Kennung']
    
    # Für die allgemeine Routin check_defect wird der Typ, der zu checken ist übergeben in die Funktion aufgerufen
    type_to_ceck = "Aufzug"
    hf.check_defect(type_to_ceck, position, idx_nearest, nearest_elevator, df_aufzuege, df_aufzuege_stoerungen)
        
    # Treppen !!!!
    # Dataframe mit den Koordinaten für die Aufzüge erstellen
    df_fahrtreppen, _ = hf.treppen_info(station_area_ds)

    # Den Index der nächsten Fahrtreppe im Dataframe ermitteln    
    idx_nearest = hf.search_nearest(position, df_fahrtreppen)  
    nearest_stairs = df_fahrtreppen.iloc[idx_nearest]['Kennung']
    
    # Für die allgemeine Routin check_defect wird der Typ, der zu checken ist übergeben in die Funktion aufgerufen
    type_to_ceck = "Fahrtreppe"
    hf.check_defect(type_to_ceck, position, idx_nearest, nearest_stairs, df_fahrtreppen, df_fahrtreppen_stoerungen)
   
    print('=' * len(_txt) + '\n')
   
    # =========================================================================
    # Aufgabe "schwer" Nr 2 - Reihenfolge der Haltstellen einer Linie bestimmen
    # =========================================================================
    print(_txt := '\n\nAufgabe "schwer" Nr. 2 - one can switch the flag "compare" to get information about the distance calculation')
    print('=' * (len(_txt)-2) + '\n')

    # Beispiel für die Endhaltestelle der Linie 152
    endhaltestelle = "Porz Markt"
    linie = 152
    
    sorted_haltestellen = hf.stops_in_sequence(endhaltestelle, linie, df_hs_grouped, df_linien)
    
    # printed output of the sorted stops in sequence
    hf.print_line_with_sorted_stops(sorted_haltestellen, linie, endhaltestelle, df_haltestellen, map = True)
    
    print('=' * len(_txt) + '\n')

if __name__ == "__main__":
    main()
    
# Dateieinde