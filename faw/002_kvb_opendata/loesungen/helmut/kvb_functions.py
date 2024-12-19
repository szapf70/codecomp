# import modules

import json
import os
import statistics

# ============================================================


def read_json_file(filename, subdirectory, encoding_in='utf-8'):
    filepath = os.path.join(subdirectory, filename)
    with open(filepath, 'r', encoding=encoding_in) as file:
        data = json.load(file)
    return data['features']

# ============================================================


def get_properties(dict_in): 
    dict_out = dict()
    for property in dict_in['properties']:
        if property == 'Linien' or property == 'Betriebsbereich':
            dict_out[property] = dict_in['properties'][property].split()
        else:
            dict_out[property] = dict_in['properties'][property]
    return dict_out


def calc_mean_station_coords(stations):
    station_coords = []
    for station in stations:
        station_coords.append(station['Koordinaten'])
    x_mean = statistics.mean([coords[0] for coords in station_coords])
    y_mean = statistics.mean([coords[1] for coords in station_coords])
    return [round(x_mean, 5), round(y_mean, 5)]

# ============================================================


def create_station_area_ds(station_area_data):
    # create empty dictionary for station areas
    station_area_ds = dict()
    # create an empty dictionary for the keys of the station areas based on the name
    station_area_key_ds = dict()

    # fill dictionary with station area data
    for station_area in station_area_data:
        station_area_dict = get_properties(station_area)
        key = station_area_dict.pop('Haltestellenbereich')

        station_area_ds[key] = station_area_dict
        station_area_key_ds[station_area_ds[key]['Haltestellenname']] = key

    return station_area_ds, station_area_key_ds


def add_station_data_to_ds(station_area_ds, station_area_key_ds, station_data):
    # add station data (properties and coordinates)
    for station in station_data:
        station_dict = get_properties(station)
        key = station_area_key_ds[station_dict.pop('Name')]
        
        station_dict.pop('Kurzname') # insert sanity check???
        station_dict['Koordinaten'] = station['geometry']['coordinates']

        if station_area_ds[key].get('Haltestellen') == None:
            station_area_ds[key]['Haltestellen'] = []
        station_area_ds[key]['Haltestellen'].append(station_dict)

    return station_area_ds


def add_diginfo_data_to_ds(station_area_ds, station_area_diginfo_data):
    # add data for digital passenger information
    for diginfo in station_area_diginfo_data:
        diginfo_dict = get_properties(diginfo)
        key = diginfo_dict['Haltestellenbereich']

        station_area_ds[key]['DFI'] = True

    return station_area_ds


def add_elevator_data_to_ds(station_area_ds, elevator_data):
    # add elevator data (properties and coordinates)
    for elevator in elevator_data:
        elevator_dict = get_properties(elevator)
        key = elevator_dict.pop('Haltestellenbereich')

        elevator_dict.pop('Info')
        elevator_dict['Koordinaten'] = elevator['geometry']['coordinates']

        if station_area_ds[key].get('Aufzüge') is None:
            station_area_ds[key]['Aufzüge'] = []
        station_area_ds[key]['Aufzüge'].append(elevator_dict)

    return station_area_ds


def add_escalator_data_to_ds(station_area_ds, escalator_data):
    # add escalator data (properties and coordinates)
    for escalator in escalator_data:
        escalator_dict = get_properties(escalator)
        key = escalator_dict.pop('Haltestellenbereich')

        escalator_dict.pop('Info')
        escalator_dict['Koordinaten'] = escalator['geometry']['coordinates']

        if station_area_ds[key].get('Fahrtreppen') == None:
            station_area_ds[key]['Fahrtreppen'] = []
        station_area_ds[key]['Fahrtreppen'].append(escalator_dict)

    return station_area_ds


def add_place_of_sale_data_to_ds(station_area_ds, place_of_sale_data):
    # add place of sale data (only segment and cooridnates)
    for place_of_sale in place_of_sale_data:
        place_of_sale_dict_temp = get_properties(place_of_sale)
        key = place_of_sale_dict_temp.pop('haltestellenbereich')

        place_of_sale_dict = dict()
        place_of_sale_dict['Segment'] = place_of_sale_dict_temp['Segment']
        place_of_sale_dict['Koordinaten'] = place_of_sale['geometry']['coordinates']

        if station_area_ds[key].get('Verkaufsorte') is None:
            station_area_ds[key]['Verkaufsorte'] = []
        station_area_ds[key]['Verkaufsorte'].append(place_of_sale_dict)

    return station_area_ds


def add_missing_infos_to_ds(station_area_ds):
    # add a False boolean entry if digital info is not available
    # and add empty lists for elevator, escalator & places of sale to station area if not available
    # and add coordinates for station area based on the station coordinates
    for key, station_area in station_area_ds.items():
        if station_area.get('DFI') == None:
            station_area_ds[key]['DFI'] = False
        if station_area.get('Aufzüge') == None:
            station_area_ds[key]['Aufzüge'] = []
        if station_area.get('Fahrtreppen') == None:
            station_area_ds[key]['Fahrtreppen'] = []
        if station_area.get('Verkaufsorte') == None:
            station_area_ds[key]['Verkaufsorte'] = []
        station_area_ds[key]['Koordinaten'] = calc_mean_station_coords(station_area['Haltestellen'])

    return station_area_ds
# ============================================================


def count_routes(station_area_ds):
    routes = set()
    for key, station_area in station_area_ds.items():
        if station_area.get('Linien'):
            routes.update(set(station_area.get('Linien')))
    return (len(routes))


def count_station_areas(station_area_ds):
    return len(station_area_ds)


def most_elements(station_area_ds, key):
    max_key_length = 0
    max_key = []
    for station_area_key, station_area in station_area_ds.items():
        if station_area.get(key) != None:
            key_length = len(station_area.get(key))
            if key_length == max_key_length:
                max_key.append(station_area_key)
            elif key_length > max_key_length:
                max_key_length = key_length
                max_key = [station_area_key]
    
    return max_key, max_key_length


def count_facilities(station_area_ds):
    count_elevator = 0
    count_escalator = 0
    count_both = 0
    count_none = 0

    for _, station_area in station_area_ds.items():
        if len(station_area['Aufzüge']) > 0 and len(station_area['Fahrtreppen']) > 0:
            count_both += 1
        elif len(station_area['Aufzüge']) > 0:
            count_elevator += 1
        elif len(station_area['Fahrtreppen']) > 0:
            count_escalator += 1
        else:
            count_none += 1

    return count_elevator, count_escalator, count_both, count_none


def count_operation_category(station_area_ds):
    count_bus = 0
    count_tram = 0
    count_both = 0
    count_none = 0

    for _, station_area in station_area_ds.items():
        operation_category = set(station_area['Betriebsbereich'])
        if 'BUS' in operation_category and 'STRAB' in operation_category:
            count_both += 1
        elif 'BUS' in operation_category:
            count_bus += 1
        elif 'STRAB' in operation_category:
            count_tram += 1
        else:
            count_none += 1

    return count_bus, count_tram, count_both, count_none


def find_most_nwse(station_area_ds):
    northernmost_coord = -float('inf')
    westernmost_coord = float('inf')
    southernmost_coord = float('inf')
    easternmost_coord = -float('inf')

    northernmost_station_area = None
    westernmost_station_area = None
    southernmost_station_area = None
    easternmost_station_area = None

    for key, station_area in station_area_ds.items():
        x, y = station_area['Koordinaten']
        
        if y > northernmost_coord:
            northernmost_coord = y
            northernmost_station_area = key
        if x < westernmost_coord:
            westernmost_coord = x
            westernmost_station_area = key
        if y < southernmost_coord:
            southernmost_coord = y
            southernmost_station_area = key
        if x > easternmost_coord:
            easternmost_coord = x
            easternmost_station_area = key

    return northernmost_station_area, westernmost_station_area, southernmost_station_area, easternmost_station_area

# ============================================================
def create_route_ds(station_area_ds):
    route_ds = dict()
    for key, station_area in station_area_ds.items():
        for route in station_area.get('Linien', []):
            if route_ds.get(route) == None:
                route_ds[route] = dict()
                route_ds[route]['Haltestellen'] = []
            route_ds[route]['Haltestellen'].append(key)
    return route_ds


def find_routes_with_most_common_stations(route_ds):
    count_common_stations = 0
    routes_most_common_stations = ()

    for route1_key, route1 in route_ds.items():
        for route2_key, route2 in route_ds.items():
            if route2_key != route1_key:
                common_stations = set(route1['Haltestellen']).intersection(route2['Haltestellen'])
                if len(common_stations) > count_common_stations:
                    count_common_stations = len(common_stations)
                    routes_most_common_stations = route1_key, route2_key
    
    return routes_most_common_stations, count_common_stations


def route_coverage(station_area_ds, route_ds, key_to_assess):
    max_coverage = 0
    route_covered_best = None

    for route_key, route in route_ds.items():
        covered_stations = []
        for station in route['Haltestellen']:
            if not station_area_ds[station][key_to_assess]:
                covered_stations.append(0)
            else:
                covered_stations.append(1)
        coverage = sum(covered_stations) / len(route['Haltestellen']) * 100
        if coverage > max_coverage:
            max_coverage = coverage
            route_covered_best = route_key

    return route_covered_best, round(max_coverage, 2)


# Dateiende