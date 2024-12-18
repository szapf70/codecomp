# Teammitglieder:
# Christoph Schierjott
# Helmut Kindl
# Christian Hofmann

#============================================================

# import modules

import json
import kvb_functions

#============================================================
# input files

json_subdirectory = 'json'

station_area_file = 'haltestellenbereiche.json'
station_file = 'haltestellen.json'
station_area_diginfo_file = 'haltestellenbereichemitdfi.json'
place_of_sale_file = 'verkaufsorte.json'
elevator_file = 'aufzuege.json'
elevator_malfunction_file = 'aufzugstoerungen.json'
escalator_file = 'fahrtreppen.json'
escalator_malfunction_file = 'fahrtreppenstoerungen.json'

#============================================================
# read all files (files are not encoded the same way)

station_area_data = kvb_functions.read_json_file(station_area_file, json_subdirectory, 'latin-1')
station_data = kvb_functions.read_json_file(station_file, json_subdirectory, 'latin-1')
station_area_diginfo_data = kvb_functions.read_json_file(station_area_diginfo_file, json_subdirectory)
place_of_sale_data = kvb_functions.read_json_file(place_of_sale_file, json_subdirectory, 'latin-1')
elevator_data = kvb_functions.read_json_file(elevator_file, json_subdirectory)
elevator_malfunction_data = kvb_functions.read_json_file(elevator_malfunction_file, json_subdirectory)
escalator_data = kvb_functions.read_json_file(escalator_file, json_subdirectory)
escalator_malfunction_data = kvb_functions.read_json_file(escalator_malfunction_file, json_subdirectory, 'latin-1')

#============================================================
# create new data structure based on station area data

station_area_ds, station_area_key_ds = kvb_functions.create_station_area_ds(station_area_data)
station_area_ds = kvb_functions.add_station_data_to_ds(station_area_ds, station_area_key_ds, station_data)
station_area_ds = kvb_functions.add_diginfo_data_to_ds(station_area_ds, station_area_diginfo_data)
station_area_ds = kvb_functions.add_elevator_data_to_ds(station_area_ds, elevator_data)
station_area_ds = kvb_functions.add_escalator_data_to_ds(station_area_ds, escalator_data)
station_area_ds = kvb_functions.add_place_of_sale_data_to_ds(station_area_ds, place_of_sale_data)
station_area_ds = kvb_functions.add_missing_infos_to_ds(station_area_ds)

#============================================================
# easy difficulty tasks

print(f'Aufgabe: Leicht - 1:')
# determine number of routes
routes = kvb_functions.count_routes(station_area_ds)
print(f'Anzahl Linien gesamt: {routes}')
# determine number of station areas
station_areas = kvb_functions.count_station_areas(station_area_ds)
print(f'Anzahl Haltestellenbereiche gesamt: {station_areas}')
print()

print(f'Aufgabe: Leicht - 2:')
# determine station area with highest number of stations
station_areas_most_stations, most_stations = kvb_functions.find_station_area_with_most_elements(station_area_ds, 'Haltestellen')
print(f"Haltestellenbereich(e) mit den meisten ({most_stations}) Haltestellen: {[station_area_ds[station_area_most_stations]['Haltestellenname'] for station_area_most_stations in station_areas_most_stations]}")
# determine station area with highest number of routes
station_areas_most_routes, most_routes = kvb_functions.find_station_area_with_most_elements(station_area_ds, 'Linien')
print(f"Haltestellenbereich(e) mit den meisten ({most_routes}) Linien: {[station_area_ds[station_area_most_routes]['Haltestellenname'] for station_area_most_routes in station_areas_most_routes]}")
print()

print(f'Aufgabe: Leicht - 3:')
# count number of station areas with elevator, escalator, both or none
count_elevator, count_escalator, count_both_fac, count_none_fac = kvb_functions.count_facilities(station_area_ds)
print(f'Haltestellenbereiche ausschließlich mit Aufzügen: {count_elevator}')
print(f'Haltestellenbereiche ausschließlich mit Fahrtreppen: {count_escalator}')
print(f'Haltestellenbereiche mit Aufzügen und Fahrtreppen: {count_both_fac}')
print(f'Haltestellenbereiche mit keinem von beidem: {count_none_fac}')
print()

print(f'Aufgabe: Leicht - 4:')
# count number of station areas with bus, tram, both or no operating type
count_bus, count_tram, count_both_op, count_none_op = kvb_functions.count_operation_type(station_area_ds)
print(f'Haltestellenbereiche ausschließlich mit Bushaltestellen: {count_bus}')
print(f'Haltestellenbereiche ausschließlich mit Straßenbahnhaltestellen: {count_tram}')
print(f'Haltestellenbereiche mit Bus- und Straßenbahnhaltestellen: {count_both_op}')
print(f'Haltestellenbereiche mit keiner Haltestelle: {count_none_op}')
print()

print(f'Aufgabe: Leicht - 5:')
# determine northernmost, westernmost, southernmost and easternmost station areas
northernmost_station_area, westernmost_station_area, southernmost_station_area, easternmost_station_area = kvb_functions.find_most_nwse(station_area_ds)
#print(northernmost_station_area, westernmost_station_area, southernmost_station_area, easternmost_station_area)
print(f"Nördlichster Haltestellenbereich: {station_area_ds[northernmost_station_area]['Haltestellenname']}")
print(f"Westlichster Haltestellenbereich: {station_area_ds[westernmost_station_area]['Haltestellenname']}")
print(f"Südlichster Haltestellenbereich: {station_area_ds[southernmost_station_area]['Haltestellenname']}")
print(f"Östlichster Haltestellenbereich: {station_area_ds[easternmost_station_area]['Haltestellenname']}")
print()

#============================================================
# preparations for medium difficulty tasks

# create dictionary for routes containing all stations for each route
route_ds = kvb_functions.create_route_ds(station_area_ds)
# add information about station facilities to route dictionary
route_ds = kvb_functions.add_facility_info_to_routes(station_area_ds, route_ds, 'DFI')
route_ds = kvb_functions.add_facility_info_to_routes(station_area_ds, route_ds, 'Aufzüge')
route_ds = kvb_functions.add_facility_info_to_routes(station_area_ds, route_ds, 'Fahrtreppen')
# add information about operation type (bus or tram) to route dictionary
route_ds = kvb_functions.add_operation_type_to_routes(station_area_ds, route_ds)
# add information about connections to other routes to route directory
route_ds = kvb_functions.add_connections_to_route(station_area_ds, route_ds)

#============================================================
# medium difficulty tasks

print(f'Aufgabe: Mittel - 1:')
# find two routes with most common stations
routes_most_common_stations, count_common_stations = kvb_functions.find_routes_with_most_common_stations(route_ds)
print(f'Folgende Linien haben die meisten ({count_common_stations}) gemeinsamen Haltestellen: {routes_most_common_stations}')
print()

print(f'Aufgabe: Mittel - 2:')
# determine routes with best coverage for digital informations
route_covered_best_dfi, coverage_prc_dfi = kvb_functions.route_coverage(route_ds, 'DFI')
print(f'Folgende Linie(n) sind an ihren Haltestellen mit {coverage_prc_dfi}% am besten mit DFI abgedeckt: {route_covered_best_dfi}')
# determine routes with best coverage for escalators
route_covered_best_esc, coverage_prc_esc = kvb_functions.route_coverage(route_ds, 'Fahrtreppen')
print(f'Folgende Linie(n) sind an ihren Haltestellen mit {coverage_prc_esc}% am besten mit Fahrtreppen abgedeckt: {route_covered_best_esc}')
# determine routes with best coverage for elevators
route_covered_best_ele, coverage_prc_ele = kvb_functions.route_coverage(route_ds, 'Aufzüge')
print(f'Folgende Linie(n) sind an ihren Haltestellen mit {coverage_prc_ele}% am besten mit Aufzügen abgedeckt: {route_covered_best_ele}')
print()

print(f'Aufgabe: Mittel - 3:')
# get all bus and all tram routes and sort them
bus_routes, tram_routes = kvb_functions.get_bus_and_tram_routes(route_ds)
print(f'Alle Buslinien sortiert: {bus_routes}')
print(f'Buslinie mit niedrigster Nummer: {min([int(bus_route) for bus_route in bus_routes])}')
print(f'Alle Straßenbahnlinien sortiert: {tram_routes}')
print(f'Straßenbahnlinie mit höchster Nummer: {max([int(tram_route) for tram_route in tram_routes])}')
print()

print(f'Aufgabe: Mittel - 4:')
# print for all tram routes the connections to other tram routes
kvb_functions.print_route_connections(route_ds, tram_routes)
print()

print(f'Aufgabe: Mittel - 5:')
# get all tram routes without any service center on their stations
routes_without_service = kvb_functions.get_routes_without_service(station_area_ds, route_ds, tram_routes)
# check for all tram routes without any service center on their stations
# if another route with service center is within reach by changing the route once
routes_with_service_within_reach = kvb_functions.get_routes_with_service_within_reach(route_ds, routes_without_service, tram_routes)
print(f'Folgende Linien haben kein Kundencenter an einer ihrer Haltestellen: {routes_without_service}')
print(f'Folgende Linien, die nicht direkt an ein Kundencenter angeschlossen sind, können ein Kundencenter durch einmaliges Umsteigen erreichen:')
for route_with_service_within_reach in routes_with_service_within_reach:
    print(f'Linien mit Kundencenter, die Line {route_with_service_within_reach[0]} kreuzen: {route_with_service_within_reach[1]}')
print()

#============================================================
# high difficulty tasks

# coordinatees of Ford Development Centre Merkenich (used in 1st task)
x = 6.94109
y = 51.02822
# tram route number including a station in Merkenich (used in 2nd task)
route = '12'

print(f'Aufgabe: Schwer - 1:')
# get ids for all elevator and escalators malfunctions
elevator_malfunction_ids = kvb_functions.get_malfunction_ids(elevator_malfunction_data)
escalator_malfunction_ids = kvb_functions.get_malfunction_ids(escalator_malfunction_data)

# find next tram station to [x, y] without further conditions
next_tram_station_1, next_station_area_1 = kvb_functions.find_next_station(station_area_ds, [x, y], 'STRAB')
print(f'Die nächste Straßenbahnhaltestelle zu den Koordinaten {[x, y]}')
print(f"liegt im Haltestellenbereich: {station_area_ds[next_station_area_1]['Haltestellenname']}")
print(f'{next_tram_station_1}')
print()

# find next tram station to [x, y] with an elevator without malfunction
next_tram_station_2, next_station_area_2 = kvb_functions.find_next_station(station_area_ds, [x, y], 'STRAB', 'Aufzüge', elevator_malfunction_ids)
print(f'Die nächste Straßenbahnhaltestelle zu den Koordinaten {[x, y]}')
print(f"mit funktionierendem Aufzug liegt im Haltestellenbereich: {station_area_ds[next_station_area_2]['Haltestellenname']}")
print(f'{next_tram_station_2}')
print()

# find next tram station to [x, y] with an escalator without malfunction
next_tram_station_3, next_station_area_3 = kvb_functions.find_next_station(station_area_ds, [x, y], 'STRAB', 'Fahrtreppen', elevator_malfunction_ids)
print(f'Die nächste Straßenbahnhaltestelle zu den Koordinaten {[x, y]}')
print(f"mit funktionierender Fahrteppe liegt im Haltestellenbereich: {station_area_ds[next_station_area_3]['Haltestellenname']}")
print(f'{next_tram_station_3}')
print()

print(f'Aufgabe: Schwer - 2:')
# order stations based on their proximity on their route
ordered_stations = kvb_functions.order_stations_on_route(station_area_ds, route_ds, route)
print(f'Die Stationen der Linie {route} werden in der folgenden Reihenfolge (oder umgekehrt) abgefahren:')
for index, station in enumerate(ordered_stations, 1):
    print(f"{index}.) {station_area_ds[station]['Haltestellenname']}")

#============================================================    

# save station area dictionary to file for visualization
with open('station_area_dict.json', 'w', encoding='utf-8') as file:
    json.dump(station_area_ds, file, indent=4, ensure_ascii=False)

# save station area key dictionary to file for visualization
with open('station_area_key_dict.json', 'w', encoding='utf-8') as file:
    json.dump(station_area_key_ds, file, indent=4, ensure_ascii=False)

# save route dictionary to file for visualization
with open('route_dict.json', 'w', encoding='utf-8') as file:
    json.dump(route_ds, file, indent=4, ensure_ascii=False)