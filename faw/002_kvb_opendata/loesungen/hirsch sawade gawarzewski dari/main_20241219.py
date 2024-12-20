# Isabell Hirsch
# Alfred Sawade
# Axel Gawarzewski
# Ali Dari

# Main

import read_json_files
import definition_library_AD_leicht
import definition_library_AD_mittel
import functions_for_positioning

# Datensets erstellen
station_data = read_json_files.get_data_for_stations()
station_area_data = read_json_files.get_data_for_station_areas()
station_area_by_short_name = read_json_files.get_station_area_vrsnr_by_short_name(station_area_data)
train_line_data = read_json_files.get_train_line_data(station_area_data)
for potential_issue in (station_data, station_area_data, station_area_by_short_name, train_line_data):
    if type(potential_issue) == str():
      print(f"Das Einlesen der Daten ist Fehlgeschlagen. Bitte Prüfen Sie die Daten.\nDie Fehlermeldung lautet: {potential_issue}\nDas Programm wird beendet.")
      exit
read_json_files.add_coordinates_for_station_areas(station_area_data, station_data)

#------------------------------ Schwierigkeitsgrad - leicht ---------------------------
# Wie viele Linien (Busse und Bahnen) und wie viele Haltestellenbereiche gibt es insgesamt?

print(f"Es gibt {definition_library_AD_leicht.number_of_bus_lines(station_area_data)} Haltestellenbereiche im Gebiet der KVB.")

# Welcher Haltestellenbereich hat die meisten Haltestellen und an welchem Treffen sich die meisten Linien?

most_stations = definition_library_AD_leicht.most_stops_in_area(station_data)
print(f"Der/Die Haltestellenbereich(e) mit den meisten Haltestellen (Anzahl {most_stations[0]}) ist/sind:")
for haltestelle in most_stations[1]:
    print(f"{station_area_data[station_area_by_short_name[haltestelle]]['haltestellenname']}.")

    most_lines = definition_library_AD_leicht.most_connections(station_area_data)

print(f"Der/Die Haltestellenbereich(e) mit den meisten Linien (Anzahl {most_lines[0]}) ist/sind:")
for haltestelle in most_lines[1]:
    print(f"{station_area_data[haltestelle]['haltestellenname']}.")

# Wieviel Haltestellenbereiche haben Fahrtreppen, Aufzüge, beides oder keines von beidem?
count_escalator = len(definition_library_AD_leicht.escalator(station_area_data))
count_elevator = len(definition_library_AD_leicht.elevator(station_area_data))
count_elevator_and_escalator = len(definition_library_AD_leicht.elevator_and_escalator(station_area_data))
count_none = len(definition_library_AD_leicht.no_elevator_and_escalator(station_area_data))
print(f"Es gibt {count_elevator} Haltestellenbereiche mit Aufzügen und "
      f"{count_escalator} Haltestellenbereiche mit Fahrtreppen. Davon haben "
      f"{count_elevator_and_escalator} beides. Die verbleibenden {count_none}"
      " haben keines von beidem."
    )

# Wieviel Haltestellenbereiche decken jeweils die Betriebsbereich „BUS“, 
# „STRAB“ oder beides ab?
count_bus = len(definition_library_AD_leicht.bus_connection(station_area_data))
count_strab = len(definition_library_AD_leicht.train_connection(station_area_data))
count_bus_and_strab = len(definition_library_AD_leicht.train_and_bus_connection(station_area_data))
print(f"Es gibt {count_bus} Haltestellenbereiche mit dem Betriebsbereich Bus und "
      f"{count_strab} Haltestellenbereiche mit dem Betriebsbereich Bahn. Davon haben "
      f"{count_bus_and_strab} beides. "
    )

# # Bestimme den nördlichsten, westlichsten, südlichsten und östlichsten Haltstellenbereich. 
# # Wie kann man die Position eines Haltestellenbereichs berechnen?
far_out_coordinates, far_out_numbers = definition_library_AD_leicht.far_out_stop_locations(station_area_data)
print("Der noerdlichste Haltestellenbereich ist "
      f"{station_area_data[far_out_numbers['northern']]['haltestellenname']}, der suedlichste "
      f"{station_area_data[far_out_numbers['southern']]['haltestellenname']}, der westlichste "
      f"{station_area_data[far_out_numbers['western']]['haltestellenname']} und der oestlichste "
      f"{station_area_data[far_out_numbers['eastern']]['haltestellenname']}"
     )

#------------------------------ Schwierigkeitsgrad – mittel ---------------------------
# # Welche beiden Linien haben die größte Anzahl gemeinsamer Stationen?
most_common_stops = definition_library_AD_mittel.most_common_stops(station_area_data)
print("Das/Die Linien-Paar(e) mit den meisten gemeinsammen Haltestellen (Anzahl: "
       f"{most_common_stops[0]}) sind "
       f"{most_common_stops[1]}."
    )

# Welche Linie ist an all ihren Haltestellen prozentual am besten mit digitalen
# Fahrgastinformationsanzeigen ausgestattet? Das gleiche auch für Fahrtreppen und Aufzüge.
digital_screen = definition_library_AD_mittel.most_dfi(station_area_data)
most_escalators = definition_library_AD_mittel.most_escalators(station_area_data)
most_elevators = definition_library_AD_mittel.most_elevators(station_area_data)
print(f"Die Linie(n) {digital_screen[1]} hat/haben mit {digital_screen[0]:.2f}% die meisten "
      "Haltestellen mit digitalen Anzeigen."
    )
print(f"Die Linie(n) {most_escalators[1]} hat/haben mit {most_escalators[0]:.2f}% die meisten "
      "Haltestellen mit Fahrtreppen."
    )
print(f"Die Linie(n) {most_elevators[1]} hat/haben mit {most_elevators[0]:.2f}% die meisten "
      "Haltestellen mit Aufzuegen."
    )

# Der Kölner weiß das eine zweistellige Nummer eine Straßenbahn und eine dreistellige
# Nummer ein Bus ist. Aber könnte man diese Information auch aus den Daten ziehen?
# Direkt angegeben ist es nicht.
# tbd: Wir könnten von allen 'nur-Bus' und 'nur-Bahn' Haltestellen die Liniennummern 
#      sammeln und von diesen min und max vergleichen. Da sollte dann die größte Nummer
#      der Busse kleiner sein als die kleinste der Bahnen. Oder wir vermuten den
#      Zusammenhang zählen einfach nur die Anzahl der Stellen und vergleichen sie.

bus_train = read_json_files.get_lines_for_buses_and_trains(station_data)
max_len_train = max([len(l) for l in bus_train['train']])
min_len_bus = min([len(l) for l in bus_train['bus']])
if max_len_train <= 2:
    print(f"Die maximale Zeichenanzahl in Strassenbahnnummern ist {max_len_train}, wie der Kölner sagt.")
else:
    print(f"Die maximale Zeichenanzahl in Strassenbahnnummern ist mit {max_len_train}, nicht wie der Kölner sagt.")
if min_len_bus >= 3:
    print(f"Die minimale Zeichenanzahl in Busnummern ist {min_len_bus}, wie der Kölner sagt.")
else:
    print(f"Die minimale Zeichenanzahl in Busnummern ist mit {min_len_bus}, nicht wie der Kölner sagt.")

# Liste alle Straßenbahnlinien jeweils mit allen Straßenbahnlinien in die man auf ihrem
# Weg direkt umsteigen kann auf.
# Haben alle Straßenbahnlinien mindestens ein Kundencenter an einer ihrer Haltestellen?
# Und von welchen Linien ohne Kundencenter kann man mit einmal Umsteigen in eine andere
# Linie zu einem Kundencenter gelangen. 

for line in train_line_data:
    if line in bus_train['train']:
      if len(train_line_data[line]['umsteige_linien']) == 0:
          print(f"Linie {line} kann man nicht auf andere Linien umsteigen.")
      else:
          train_lines = [l for l in train_line_data[line]['umsteige_linien'] if l in bus_train['train']]
          print(f"Von Linie {line} kann man direkt auf die Linien {train_lines} umsteigen.")
      print(f"Linie {line} hat","kein" if not train_line_data[line]['kundencenter'] else "","Kundencenter am Linienverlauf.")
      if len(train_line_data[line]['kundenenter_mit_einmal_umsteigen']) == 0:
          print(f"Es kann von Linie {line} auch durch 1 mal umsteigen kein Kundencenter erreicht werden.")
      else:
          print(f"Von Linie {line} kommt man per Umstieg auf eine der Linien {train_line_data[line]['kundenenter_mit_einmal_umsteigen']} zu einem Kundencenter.")

#------------------------------ Schwierigkeitsgrad - schwer ---------------------------

while (requested_position := functions_for_positioning.get_coordinate_input(station_area_data)) != "stop":
    # Suche für eine eingegebene Position die nächste Straßenbahnhaltestelle
    # Suche für eine eingegebene Position die nächste Straßenbahnhaltestelle mit 
    # Fahrtreppen (Störung?)
    # Suche für eine eingegebene Position die nächste Straßenbahnhaltestelle mit 
    # Aufzug (Störung?)
    checks_to_happen = {" ":{"consider_escalators": False, "consider_elevators": False},
                        " mit Fahrtreppen ":{"consider_escalators": True, "consider_elevators": False},
                        " mit Aufzuegen ":{"consider_escalators": False, "consider_elevators": True}}
    
    for check in checks_to_happen:
        closest_station = functions_for_positioning.find_next_station(station_area_data, requested_position, checks_to_happen[check]["consider_escalators"], checks_to_happen[check]["consider_elevators"])
        print(f"Die naechste Strassenbahnhaltestelle{check}von Position {requested_position} ist "
            f"{station_area_data[closest_station['next_station']]['haltestellenname']} mit der Position "
            f"{station_area_data[closest_station['next_station']]['koordinaten']}"

            )

# Leider gibt es in den Daten keine direkten Informationen in welcher Reihenfolge
# die einzelnen Linien die Haltestellen abfahren. Könnte man das anhand der Vorgabe
# einer der beiden Endhaltestellen und den „Entfernungen“ der Haltestellen durch
# ihre Koordinaten berechnen. Wie akkurat wäre diese Berechnung? Gebt dazu einer 
# der Strecken von Hand ein und vergleicht. Entwickelt vorher die Datenstruktur, 
# in der alle Haltestellen aller Linien in ihrer Reihenfolge gespeichert werden können.

# functions_for_positioning.order_train_stations_by_distance(station_area_data, train_line_data)
# for one_line in train_line_data:
#     print(f"\nStrassenbahn-Linie {one_line} fährt folgende Haltestellen an:")
#     for train_station in train_line_data[one_line]["haltestellen"]:
#             print(f"\t{station_area_data[train_station]['haltestellenname']}")
 
