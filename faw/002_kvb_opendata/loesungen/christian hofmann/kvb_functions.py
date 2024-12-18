# import modules

import json
import os
import statistics
import math

#============================================================

def read_json_file(filename, subdirectory, encoding_in='utf-8'):
    """
    Reads a JSON file from a specified subdirectory and returns the 'features' key from the JSON data.

    Arguments:
        filename (str): name of the JSON file to read
        subdirectory (str): subdirectory where the JSON file is located
        encoding_in (str, optional): encoding used to read the file. Defaults to 'utf-8'

    Returns:
        list: The list of features extracted from the 'features' key in the JSON file.
    """

    # construct the full file path
    filepath = os.path.join(subdirectory, filename)

    # open and read the JSON file
    with open(filepath, 'r', encoding=encoding_in) as file:
        # load the JSON data
        data = json.load(file)

    # return the features list from the JSON data
    return data['features']

#============================================================

def get_properties(dict_in):
    """
    Extracts and processes properties from a given dictionary, formatting specific fields as lists.

    Arguments:
        dict_in (dict): dictionary containing a 'properties' key, which is itself a dictionary with various properties

    Returns:
        dict: A new dictionary with processed properties, where 'Linien' and 'Betriebsbereich' are converted to lists.
    """

    # initialization
    dict_out = dict()

    # iterate over each property in the input dictionary's 'properties'
    for property in dict_in['properties']:
        # check if the property is 'Linien' or 'Betriebsbereich'
        if property == 'Linien' or property == 'Betriebsbereich':
            # split the property value into a list of strings
            dict_out[property] = dict_in['properties'][property].split()
        else:
            # directly assign the property value to the output dictionary
            dict_out[property] = dict_in['properties'][property]

    # return the processed properties dictionary
    return dict_out


def calc_mean_station_coords(stations):
    """
    Calculates the mean coordinates for a list of stations, rounding the result to five decimal places.

    Arguments:
        stations (list): list of station dictionaries, each containing 'Koordinaten' (coordinates) as a list [x, y]

    Returns:
        list: A list containing the mean x and y coordinates, rounded to five decimal places.
    """

    # initialization
    station_coords = []

    # iterate over each station to extract its coordinates
    for station in stations:
         station_coords.append(station['Koordinaten'])

    # calculate the mean of the x-coordinates
    x_mean = statistics.mean([coords[0] for coords in station_coords])
    # calculate the mean of the y-coordinates
    y_mean = statistics.mean([coords[1] for coords in station_coords])

    # return the mean coordinates, rounded to five decimal places    
    return [round(x_mean, 5), round(y_mean, 5)]

#============================================================

def create_station_area_ds(station_area_data):
    """
    Creates a dictionary for station areas, mapping each area key to its properties
    and a dictionary mapping each station names to their keys.

    Arguments:
        station_area_data (dict): dictionary for station areas including data from a JSON file

    Returns:
        tuple: A tuple containing two dictionaries:
               1. station_area_ds: Maps each station area key to its properties.
               2. station_area_key_ds: Maps each station name to its corresponding station area key.
    """

    # initialization
    station_area_ds = dict()
    station_area_key_ds = dict()

    # iterate over each station area in the provided data
    for station_area in station_area_data:
        # extract properties from the station area dictionary
        station_area_dict = get_properties(station_area)
        # retrieve and remove the station area key from the properties
        key = station_area_dict.pop('Haltestellenbereich')
        # map the station area key to its properties
        station_area_ds[key] = station_area_dict
        # map the station name to the station area key
        station_area_key_ds[station_area_ds[key]['Haltestellenname']] = key

    # return the two dictionaries
    return station_area_ds, station_area_key_ds


def add_station_data_to_ds(station_area_ds, station_area_key_ds, station_data):
    """
    Adds detailed station data, including properties and coordinates, to the station area data structure.

    Arguments:
        station_area_ds (dict): dictionary mapping station area keys to their properties
        station_area_key_ds (dict): dictionary mapping station names to their corresponding station area keys
        station_data (dict): dictionary of station data, each containing properties and geometric coordinates

    Returns:
        dict: The updated station area data structure with detailed station data added under each station area.
    """
    
    # iterate over each station in the provided station data
    for station in station_data:
        # extract properties from the station
        station_dict = get_properties(station)
        # retrieve the station area key using the station's name
        key = station_area_key_ds[station_dict.pop('Name')]

        # remove 'Kurzname' from the station properties
        station_dict.pop('Kurzname')
        # add coordinates to the station properties
        station_dict['Koordinaten'] = station['geometry']['coordinates']

        # check if the 'Haltestellen' list exists in the station area, if not, initialize it
        if station_area_ds[key].get('Haltestellen') == None:
            station_area_ds[key]['Haltestellen'] = []
        # append the station's properties to the 'Haltestellen' list
        station_area_ds[key]['Haltestellen'].append(station_dict)

    # return the updated station area data structure
    return station_area_ds


def add_diginfo_data_to_ds(station_area_ds, station_area_diginfo_data):
    """
    Adds digital information data to the station area data sturcture, marking areas with digital facilities.

    Arguments:
        station_area_ds (dict): dictionary mapping station area keys to their properties
        station_area_diginfo_data (list): dictionary of digital information data for station areas

    Returns:
        dict: The updated station area data structure with digital information flags added.
    """
    
    # iterate over each digital information entry in the provided data
    for diginfo in station_area_diginfo_data:
        # extract properties from the digital information entry
        diginfo_dict = get_properties(diginfo)
        # retrieve the station area key from the digital information properties
        key = diginfo_dict['Haltestellenbereich']
        # mark the station area as having digital facilities by setting 'DFI' to True
        station_area_ds[key]['DFI'] = True

    # return the updated station area data structure
    return station_area_ds


def add_elevator_data_to_ds(station_area_ds, elevator_data):
    """
    Adds elevator data to the station area data structure, including properties and coordinates for each elevator.

    Arguments:
        station_area_ds (dict): dictionary mapping station area keys to their properties
        elevator_data (dict): dictionary of elevator data, each containing properties and geometric coordinates

    Returns:
        dict: The updated station area data structure with elevator data added.
    """

    # iterate over each elevator in the provided elevator data
    for elevator in elevator_data:
        # extract properties from the elevator
        elevator_dict = get_properties(elevator)
        # retrieve and remove the station area key from the elevator properties
        key = elevator_dict.pop('Haltestellenbereich')

        # remove 'Info' from the elevator properties
        elevator_dict.pop('Info')
        # add coordinates to the elevator properties
        elevator_dict['Koordinaten'] = elevator['geometry']['coordinates']

        # check if the 'Aufzüge' list exists in the station area, if not, initialize it
        if station_area_ds[key].get('Aufzüge') == None:
            station_area_ds[key]['Aufzüge'] = []
        # append the elevator's properties to the 'Aufzüge' list
        station_area_ds[key]['Aufzüge'].append(elevator_dict)

    # return the updated station area data structure
    return station_area_ds

def add_escalator_data_to_ds(station_area_ds, escalator_data):
    """
    Adds escalator data to the station area data sturcture, including properties and coordinates for each escalator.

    Arguments:
        station_area_ds (dict): dictionary mapping station area keys to their properties
        escalator_data (dirct): dictionary of escalator data, each containing properties and geometric coordinates

    Returns:
        dict: The updated station area data structure with escalator data added.
    """

    # iterate over each escalator in the provided escalator data
    for escalator in escalator_data:
        # extract properties from the escalator
        escalator_dict = get_properties(escalator)
        # retrieve and remove the station area key from the escalator properties
        key = escalator_dict.pop('Haltestellenbereich')

        # remove 'Info' from the escalator properties
        escalator_dict.pop('Info')
        # add coordinates to the escalator properties
        escalator_dict['Koordinaten'] = escalator['geometry']['coordinates']

        # check if the 'Fahrtreppen' list exists in the station area, if not, initialize it
        if station_area_ds[key].get('Fahrtreppen') == None:
            station_area_ds[key]['Fahrtreppen'] = []
        # append the escalator's properties to the 'Fahrtreppen' list
        station_area_ds[key]['Fahrtreppen'].append(escalator_dict)

    # return the updated station area data structure
    return station_area_ds


def add_place_of_sale_data_to_ds(station_area_ds, place_of_sale_data):
    """
    Adds place of sale data to the station area data structure, including segment information and coordinates for each place of sale.

    Arguments:
        station_area_ds (dict): dictionary mapping station area keys to their properties.
        place_of_sale_data (dict): dictionary of place of sale data, each containing properties and geometric coordinates.

    Returns:
        dict: The updated station area data structure with place of sale data added.
    """

    # iterate over each place of sale in the provided data
    for place_of_sale in place_of_sale_data:
        # extract properties from the place of sale
        place_of_sale_dict_temp = get_properties(place_of_sale)
        # retrieve and remove the station area key from the place of sale properties
        key = place_of_sale_dict_temp.pop('haltestellenbereich')

        # create a dictionary for the place of sale with relevant details
        place_of_sale_dict = dict()
        place_of_sale_dict['Segment'] = place_of_sale_dict_temp['Segment']
        place_of_sale_dict['Koordinaten'] = place_of_sale['geometry']['coordinates']

        # check if the 'Verkaufsorte' list exists in the station area, if not, initialize it
        if station_area_ds[key].get('Verkaufsorte') == None:
            station_area_ds[key]['Verkaufsorte'] = []
        # append the place of sale's properties to the 'Verkaufsorte' list
        station_area_ds[key]['Verkaufsorte'].append(place_of_sale_dict)

    # return the updated station area data structure
    return station_area_ds


def add_missing_infos_to_ds(station_area_ds):
    """
    Fills in missing information for each station area, ensuring all necessary fields are present and calculating mean coordinates.

    Arguments:
        station_area_ds (dict): dictionary mapping station area keys to their properties

    Returns:
        dict: The updated station area data structure with missing information filled in and mean coordinates calculated.
    """

    # iterate over each station area in the data structure
    for key, station_area in station_area_ds.items():
        # set 'DFI' to False if it is not already present
        if station_area.get('DFI') == None:
            station_area_ds[key]['DFI'] = False
        # initialize 'Aufzüge' as an empty list if not present
        if station_area.get('Aufzüge') == None:
            station_area_ds[key]['Aufzüge'] = []
        # initialize 'Fahrtreppen' as an empty list if not present
        if station_area.get('Fahrtreppen') == None:
            station_area_ds[key]['Fahrtreppen'] = []
        # initialize 'Verkaufsorte' as an empty list if not present
        if station_area.get('Verkaufsorte') == None:
            station_area_ds[key]['Verkaufsorte'] = []
        # calculate and set the mean coordinates based on stations
        station_area_ds[key]['Koordinaten'] = calc_mean_station_coords(station_area['Haltestellen'])

    # return the updated station area data structure
    return station_area_ds

#============================================================

def count_routes(station_area_ds):
    """
    Counts the total number of unique routes across all station areas in the data structure.

    Arguments:
        station_area_ds (dict): dictionary containing station area data

    Returns:
        int: The total number of unique routes across all station areas
    """

    # initialization
    routes = set()

    # iterate over each station area in the data structure
    for _, station_area in station_area_ds.items():
        # check if there are routes in the station area
        if station_area.get('Linien'):
            # update the set with routes from the current station area
            routes.update(set(station_area.get('Linien')))

    # return the number of unique routes
    return len(routes)


def count_station_areas(station_area_ds):
    """
    Counts the total number of station areas in the data structure.

    Arguments:
        station_area_ds (dict): dictionary containing station area data

    Returns:
        int: The total number of station areas in the data structure
    """
    
    # return the number of station areas by counting the keys in the dictionary
    return len(station_area_ds)


def find_station_area_with_most_elements(station_area_ds, key):
    """
    Identifies station areas with the most elements for a specified key and returns those areas and the count of elements.

    Arguments:
        station_area_ds (dict): dictionary containing station area data
        key (str): key for which to count the elements (e.g., 'Aufzüge', 'Fahrtreppen')

    Returns:
        tuple: A tuple containing:
               1. A list of station area identifiers with the most elements for the specified key
               2. The maximum number of elements found.
    """

    # initialization
    max_key_length = 0
    max_key = []

    # iterate over each station area in the data structure
    for station_area_key, station_area in station_area_ds.items():
        # check if the specified key is present in the station area
        if station_area.get(key):
            # get the number of elements for the specified key
            key_length = len(station_area.get(key))

            # check if the current station area has more elements than the previous maximum
            if key_length > max_key_length:
                # reset the list with the new maximum station area
                max_key_length = key_length
                max_key = [station_area_key]
            # if the number of elements is equal to the current maximum, add the station area to the list
            elif key_length == max_key_length:
                max_key.append(station_area_key)
    
    # return the list of station areas with the most elements and the maximum number of elements
    return max_key, max_key_length


def count_facilities(station_area_ds):
    """
    Counts the number of station areas equipped with elevators, escalators, both, or neither.

    Arguments:
        station_area_ds (dict): dictionary containing station area data

    Returns:
        tuple: A tuple containing counts of station areas with elevators, escalators, both, and neither, respectively.
    """

    # initialization
    count_elevator = 0
    count_escalator = 0
    count_both = 0
    count_none = 0

    # iterate over each station area in the data structure
    for _, station_area in station_area_ds.items():
        # check if both elevators and escalators are present
        if len(station_area['Aufzüge']) > 0 and len(station_area['Fahrtreppen']) > 0:
            count_both += 1
        # check if only elevators are present
        elif len(station_area['Aufzüge']) > 0:
            count_elevator += 1
        # check if only escalators are present
        elif len(station_area['Fahrtreppen']) > 0:
            count_escalator += 1
        # check if neither facility is present
        else:
            count_none += 1

    # return the counts of station areas by facility type
    return count_elevator, count_escalator, count_both, count_none


def count_operation_type(station_area_ds):
    """
    Counts the number of station areas served by buses, trams, both, or neither.

    Arguments:
        station_area_ds (dict): dictionary containing station area data

    Returns:
        tuple: A tuple containing counts of station areas served by buses, trams, both, and neither, respectively.
    """

    # initialization
    count_bus = 0
    count_tram = 0
    count_both = 0
    count_none = 0

    # iterate over each station area in the data structure
    for _, station_area in station_area_ds.items():
        # create a set of operation types present in the station area
        operation_type = set(station_area['Betriebsbereich'])

        # check if both bus and tram services are present
        if 'BUS' in operation_type and 'STRAB' in operation_type:
            count_both += 1
        # check if only bus service is present
        elif 'BUS' in operation_type:
            count_bus += 1
        # check if only tram service is present
        elif 'STRAB' in operation_type:
            count_tram += 1
        # check if neither service is present
        else:
            count_none += 1

    # return the counts of station areas by service type
    return count_bus, count_tram, count_both, count_none


def find_most_nwse(station_area_ds):
    """
    Identifies the northernmost, westernmost, southernmost, and easternmost station areas based on coordinates.

    Arguments:
        station_area_ds (dict): dictionary containing station area data

    Returns:
        tuple: tuple containing the identifiers of the northernmost, westernmost, southernmost, and easternmost
               station areas.
    """

    # initialization
    northernmost_coord = -float('inf')
    westernmost_coord = float('inf')
    southernmost_coord = float('inf')
    easternmost_coord = -float('inf')

    # initialization
    northernmost_station_area = None
    westernmost_station_area = None
    southernmost_station_area = None
    easternmost_station_area = None

    # iterate over each station area in the data structure
    for key, station_area in station_area_ds.items():
        x, y = station_area['Koordinaten']
        
        # check for the northernmost station
        if y > northernmost_coord:
            northernmost_coord = y
            northernmost_station_area = key
        # check for the westernmost station
        if x < westernmost_coord:
            westernmost_coord = x
            westernmost_station_area = key
        # check for the southernmost station
        if y < southernmost_coord:
            southernmost_coord = y
            southernmost_station_area = key
        # check for the easternmost station
        if x > easternmost_coord:
            easternmost_coord = x
            easternmost_station_area = key

    # return the identifiers of the northernmost, westernmost, southernmost, and easternmost station areas
    return northernmost_station_area, westernmost_station_area, southernmost_station_area, easternmost_station_area

#============================================================
# functions for medium difficulty tasks

def create_route_ds(station_area_ds):
    """
    Creates a route data structure from station area data, mapping each route to its corresponding stations.

    Arguments:
        station_area_ds (dict): dictionary containing station area data

    Returns:
        dict: route data structure where each key is a route identifier, and its value is a dictionary containing
              a list of stations that the route serves.
    """

    # initialize an empty dictionary to store routes and their stations
    route_ds = dict()

    # iterate over each station area in the data structure
    for key, station_area in station_area_ds.items():
        # iterate over each route associated with the station area
        for route in station_area.get('Linien', []):
            # check if the route is not already in the route data structure
            if route_ds.get(route) == None:
                # initialization
                route_ds[route] = dict()
                route_ds[route]['Haltestellen'] = []
            # append the current station area key to the route's list of stations
            route_ds[route]['Haltestellen'].append(key)
    return route_ds


def find_routes_with_most_common_stations(route_ds):
    """
    Identifies the pair of routes that share the most common stations and returns their identifiers and the count.

    Arguments:
        route_ds (dict): dictionary of route data

    Returns:
        tuple: A tuple containing the identifiers of the two routes with the most common stations and the count of those stations.
    """

    # initialization
    count_common_stations = 0
    routes_most_common_stations = ()

    # create a copy of the route data structure to avoid modifying the original during iteration
    route_ds_copy = route_ds.copy()

    # iterate over each route in the original route data structure
    for route1_key, route1 in route_ds.items():
        # iterate over each route in the copied data structure
        for route2_key, route2 in route_ds_copy.items():
            # ensure the route is not compared with itself
            if route2_key != route1_key:
                # find common stations between the two routes
                common_stations = set(route1['Haltestellen']).intersection(route2['Haltestellen'])

                # check if the current pair has more common stations than the previous maximum
                if len(common_stations) > count_common_stations:
                    # update the routes with the most common stations
                    count_common_stations = len(common_stations)
                    routes_most_common_stations = route1_key, route2_key

        # remove the current route from the copied data structure to avoid redundant comparisons
        route_ds_copy.pop(route1_key)

    # return the pair of routes with the most common stations and the count of those stations
    return routes_most_common_stations, count_common_stations


def add_facility_info_to_routes(station_area_ds, route_ds, facility_key):
    """
    Adds information to routes about the number of stations equipped with a specific facility.

    Arguments:
        station_area_ds (dict): dictionary containing station area data
        route_ds (dict): dictionary of route data
        facility_key (str): key representing the facility to check for ('DFI', 'Aufzüge', 'Fahrtreppen')

    Returns:
        dict: The updated route data structure with the number of stations having the specified facility added.
    """

    # iterate over each route in the route data structure
    for route_key, route in route_ds.items():
        # initialization
        covered_stations = []

        # iterate over each station in the route
        for station in route['Haltestellen']:
            if not station_area_ds[station][facility_key]:
                # append 0 if the facility is not present
                covered_stations.append(0)
            else:
                # append 1 if the facility is present
                covered_stations.append(1)

        # add the total count of stations with the facility to the route's data
        route_ds[route_key][f'Haltestellen mit {facility_key}'] = sum(covered_stations)
    return route_ds



def route_coverage(route_ds, facility_key):
    """
    Determines which routes have the highest percentage of stations with a specific facility.

    Arguments:
        route_ds (dict): dictionary of route data
        facility_key (str): key representing the facility to check for coverage ('DFI', 'Aufzüge', 'Fahrtreppen')

    Returns:
        tuple: A tuple containing a list of route identifiers with the best coverage and the maximum coverage percentage.
    """

    # initialization
    max_coverage_prc = 0
    route_covered_best = []

    # iterate over each route in the data structure
    for route_key, route in route_ds.items():
        # calculate the number of stations covered by the facility
        covered_stations = route[f'Haltestellen mit {facility_key}']
        # calculate the coverage percentage
        coverage_prc = covered_stations / len(route['Haltestellen']) * 100

        # check if the current route has better coverage than the previous maximum
        if coverage_prc > max_coverage_prc:
            max_coverage_prc = coverage_prc
            # reset the list with the new best route
            route_covered_best = [route_key]
        # if the coverage is equal to the current maximum, add the route to the list
        elif coverage_prc == max_coverage_prc:
            route_covered_best.append(route_key)
    # return the list of best-covered routes and the maximum coverage percentage rounded to 2 decimal places
    return route_covered_best, round(max_coverage_prc, 2)


def add_operation_type_to_routes(station_area_ds, route_ds):
    """
    Adds the operation type to routes in the route data structure based on the station areas.

    Arguments:
        station_area_ds (dict): dictionary containing station area data
        route_ds (dict): dictionary of route data

    Returns:
        dict: The updated route data structure with operation type added to routes.
    """

    # iterate over each station area in the data structure
    for _, station_area in station_area_ds.items():
        # iterate over each station area in the data structure
        for station in station_area.get('Haltestellen', []):
            # iterate over each route associated with the station
            for route in station.get('Linien', []):
                # check if the route's operational area is not set
                if route_ds[route].get('Betriebsbereich') == None:
                    # assign the operation area from the station
                    route_ds[route]['Betriebsbereich'] = station['Betriebsbereich'][0]
    return route_ds


def get_bus_and_tram_routes(route_ds):
    """
    Separates routes into bus and tram categories based on their operational area.

    Arguments:
        route_ds (dict): dictionary of route data

    Returns:
        tuple: Two lists containing sorted route identifiers, one for bus routes and one for tram routes.
    """

    # initialization
    bus_routes = []
    tram_routes = []

    # iterate over each route in the route data structure
    for route_key, route in route_ds.items():
        # check if the route is a bus route
        if route['Betriebsbereich'] == 'BUS':
            bus_routes.append(route_key)
        # check if the route is a tram route
        elif route['Betriebsbereich'] == 'STRAB':
            tram_routes.append(route_key)

    # return sorted lists of bus and tram routes
    return sorted(bus_routes, key=int), sorted(tram_routes, key=int)


def add_connections_to_route(station_area_ds, route_ds):
    """
    Adds each route's options for route change by identifying common stations shared with other routes.

    Arguments:
        route_ds (dict): dictionary of route data
        station_area_ds (dict): dictionary containing station area data

    Returns:
        dict: updated route data structure with route change options for each route.
    """

    # iterate over each route in the route data structure
    for route1_key, route1 in route_ds.items():
        # initialization
        connections = set()

        # compare the current route with every other route in the data structure
        for route2_key, route2 in route_ds.items():
            # ensure the route is not compared with itself
            if route2_key != route1_key:
                # find common stations between the two routes
                common_stations = set(route1['Haltestellen']).intersection(route2['Haltestellen'])

                # for each common station, update the connections with routes available at that station
                for station_area in common_stations:
                    connections.update(station_area_ds[station_area]['Linien'])

        # remove the current route from its own list of connections
        connections.discard(route1_key)
        # add the route's options for route change to the the route data structure
        route_ds[route1_key]['Umstiegsmöglichkeiten'] = sorted(list(connections), key=int)
    return route_ds


def print_route_connections(route_ds, route_filter):
    """
    Prints the route change options for each route in the given filter.

    Arguments:
        route_ds (dict): dictionary of route data
        route_filter (list): list of route identifiers to consider for printing route change options

    This function iterates over the routes specified in the route filter and prints the route
    change options, ensuring that only routes within the filter are considered.
    """

    # iterate over each route in the route filter
    for route_key in route_filter:
        # find the intersection of route change options with the route filter
        filtered_routes = set(route_ds[route_key]['Umstiegsmöglichkeiten']).intersection(route_filter)
        # print the sorted list of route change options for the route
        print(f"Umstiegsmöglichkeiten für Linie {route_key}: {sorted(list(filtered_routes), key=int)}")


def get_routes_without_service(station_area_ds, route_ds, route_filter):
    """
    Identifies routes that do not have a service center available.

    Arguments:
        station_area_ds (dict): dictionary containing station area data
        route_ds (dict): dictionary of route data
        route_filter (list): list of route identifiers to consider for checking service center availability.

    Returns:
        list: sorted list of route identifiers that do not have a service center available.
    """

    #initialization
    routes_without_service = []

    # iterate over each route in the route data structure
    for route_key, route in route_ds.items():
        # check if the route is in the route filter
        if route_key in route_filter:
            # initialization
            service_found = False

            # iterate over each station on the route
            for station in route['Haltestellen']:
                # check each place of sale at the station
                for place_of_sale in station_area_ds[station]['Verkaufsorte']:
                    # if a 'KundenCenter' is found, set the flag to True
                    if place_of_sale['Segment'] == 'KundenCenter':
                        service_found = True

            # if no 'KundenCenter' was found, add the route to the list    
            if service_found == False:
                routes_without_service.append(route_key)
    # return the sorted list of routes without a service center
    return sorted(routes_without_service, key=int)


def get_routes_with_service_within_reach(route_ds, routes_without_service, route_filter):
    """
    Identifies routes that, despite lacking a service center, are within reach of other routes
    that have a service center (by changing the routes once), based on a given filter.

    Arguments:
        route_ds (dict): dictionary of route data
        routes_without_service (list): list of route identifiers that do not have a service center
        route_filter (list): list of route identifiers to consider for determining reachability
                             (e.g., only bus or tram routes).

    Returns:
        list: A sorted list of tuples containing:
              1. The route identifiers that are within reach of other routes with a service center (by changing the routes once).
              2. The corresponding routes within reach that have a service center on their route.
    """
    
    # initialization
    routes_with_service_within_reach = []

    # iterate over each route that lacks a service center
    for route_without_service in routes_without_service:
        # determine the set of reachable routes that are also in the route filter
        reachable_routes = set(route_ds[route_without_service]['Umstiegsmöglichkeiten']).intersection(route_filter)
        # check if there are any reachable routes that are not in the list of routes without a service center
        # => remaining stations must have a service center on their route
        if reachable_routes.difference(set(routes_without_service)):
            # determine routes within reach with a service center
            routes_within_reach = sorted(reachable_routes.difference(set(routes_without_service)), key=int)
            routes_with_service_within_reach.append((route_without_service, routes_within_reach))
    # return a sorted list of tuples containing:
    # (route identifiers that are within reach of other routes with a service center (by changing the routes once),
    #  corresponding routes within reach that have a service center on their route)
    return sorted(routes_with_service_within_reach, key=lambda route_in_tuple: routes_with_service_within_reach[0])

#============================================================
# functions for high difficulty tasks

def get_malfunction_ids(malfunction_data):
    """
    Extracts malfunction IDs from a list of malfunction data entries.

    Arguments:
        malfunction_data (list): list of dictionaries containing malfunction data for facilities

    Returns:
        list: A list of malfunction IDs ('Kennung') extracted from the malfunction data.
    """

    # initialization
    malfunction_ids = []

    # iterate over each malfunction entry in the data
    for malfunction in malfunction_data:
        # retrieve the dictionaries containing the malfunctions
        malfunction_dict = get_properties(malfunction)
        # append the 'Kennung' (ID) from the malfunction properties to the list
        malfunction_ids.append(malfunction_dict['Kennung'])
    return malfunction_ids


# def calculate_distance(coords1, coords2):
#     """
#     Calculates the Euclidean distance between two points in a 2D space.

#     Arguments:
#         coords1 (list): list containing the x and y coordinates of the first point
#         coords2 (list): list containing the x and y coordinates of the second point

#     Returns:
#         float: The Euclidean distance between the two points.
#     """

#     # calculate the difference in x and y coordinates
#     dx = coords2[0] - coords1[0]
#     dy = coords2[1] - coords1[1]

#     # calculate the Euclidean distance using the Pythagorean theorem
#     distance = (dx**2 + dy**2)**(1/2)
#     return distance


def find_next_station_area(station_area_ds, coords, operation_type):
    """
    Finds the next station area from a dictionary of station areas based on proximity and operation type.

    Arguments:
        station_area_ds (dict): dictionary containing station area data
        coords (list): list containing the x and y coordinates of the current location
        operation_type (str): The type of operation ('BUS', 'STRAB') that the station area must support.

    Returns:
        str: The key of the next closest station area that supports the specified operation type.
    """

    # initialization
    next_station_area = None
    closest_distance = float('inf')

    # iterate over each station area to find the one closest to the given coordinates
    for station_area_key, station_area in station_area_ds.items():
        # check if the station area supports the specified operation type
        if operation_type in station_area['Betriebsbereich']:
            # calculate the distance from the current location to the station area
            distance = calculate_distance(coords, station_area['Koordinaten'])
            # update the next station area if this area is closer
            if distance < closest_distance:
                closest_distance = distance
                next_station_area = station_area_key
    return next_station_area


def find_next_station_in_stations(stations, coords, operation_type):
    """
    Finds the closest station that supports a specific operation type.

    Arguments:
        stations (list): list of station dictionaries
        coords (list): list containing the x and y coordinates of the current location
        operation_type (str): type of operation ('BUS', 'STRAB') that the station must support

    Returns:
        dict: The station dictionary that is closest to the given coordinates and supports the specified operation type.
    """

    # initialization
    next_station = None
    closest_distance = float('inf')

    # iterate over each station to find the one closest to the given coordinates
    for station in stations:
        # check if the station supports the specified operation type
        if operation_type in station['Betriebsbereich']:
            # calculate the distance from the current location to the station
            distance = calculate_distance(coords, station['Koordinaten'])
            # update the next station if this station is closer
            if distance < closest_distance:
                closest_distance = distance
                next_station = station
    return next_station


def find_next_station(station_area_ds, coords, operation_type, facility_type='', facility_malfunction_ids=[]):
    """
    Finds the next station for a given operation type with optional filtering for specific facilities.

    Arguments:
        station_area_ds (dict): dictionary containing station area data
        coords (list): list containing the x and y coordinates of the current location
        operation_type (str): The type of operation ('BUS', 'STRAB') that determines valid stations
        facility_type (str, optional): The type of facility to filter stations by ('Aufzüge', 'Fahrtreppe')
        facility_malfunction_ids (list, optional): list of facility IDs that are malfunctioning and should be avoided

    Returns:
        tuple: A tuple containing the next station and the station area identifier

    The function iterates over station areas to find the next suitable station based on the given criteria.
    If a facility type is specified, it ensures the facility is operational and available at the station.
    """

    # create a copy of the station area data structure to avoid modifying the original during iteration
    station_area_ds_copy = station_area_ds.copy()

    while True:
        # find the next station area based on current coordinates and operation type
        next_station_area = find_next_station_area(station_area_ds_copy, coords, operation_type)

        # check if the station area contains the desired facility
        if station_area_ds_copy[next_station_area].get(facility_type, []):
            stations_with_facility = []
            for facility in station_area_ds[next_station_area][facility_type]:
                # ensure the facility is not malfunctioning
                if not facility['Kennung'] in facility_malfunction_ids:
                    # find the next station within the station area that supports the operation type
                    next_station_to_facility = find_next_station_in_stations(station_area_ds[next_station_area]['Haltestellen'], facility['Koordinaten'], operation_type)
                    if operation_type in next_station_to_facility['Betriebsbereich']:
                        stations_with_facility.append(next_station_to_facility)

            # if there are stations with the desired facility, find the next one
            if stations_with_facility:
                next_station = find_next_station_in_stations(stations_with_facility, coords, operation_type)
                return next_station, next_station_area
            else:
                # remove the station area if no suitable facility was found
                station_area_ds_copy.pop(next_station_area)
        elif not facility_type:
            # if no facility type is specified, find the next station without filtering
            next_station = find_next_station_in_stations(station_area_ds[next_station_area]['Haltestellen'], coords, operation_type)
            return next_station, next_station_area
        else:
            # remove the station area if it doesn't meet the facility criteria
            station_area_ds_copy.pop(next_station_area)


def order_stations_on_route(station_area_ds, route_ds, route):
    """
    Orders the stations on a specified route based on their geographic proximity.

    Arguments:
        station_area_ds (dict): dictionary containing station area information
        route_ds (dict): dictionary containing route information
        route (str): identifier of the route for which stations need to be ordered

    Returns:
        list: an ordered list of station area identifiers representing the sequence
              of stations on the route, ordered by proximity.

    The function determines whether the route is a 'STRAB' (tram) or 'BUS' based on
    the route number. It then retrieves all station area identifiers for the specified
    route. Using a proximity-based approach, the function orders these stations.
    """
    
    # determine the operation type based on the route number
    operation_type = 'STRAB' if int(route) < 100 else 'BUS'

    # filter the station areas that are part of the given route
    route_station_area_ds = {}
    for station_area_key in route_ds[route]['Haltestellen']:
        if station_area_key in station_area_ds:
            route_station_area_ds[station_area_key] = station_area_ds[station_area_key]

    # initialize the list to hold ordered stations
    ordered_stations = []
    # order the stations based on proximity
    while route_station_area_ds:
        if not ordered_stations:
            # start with the first station if the list is empty
            first_station_area_key, _ = route_station_area_ds.popitem()
            ordered_stations.append(first_station_area_key)
        else:
            # get coordinates of the first and last stations in the ordered list
            first_station_coords = station_area_ds[ordered_stations[0]]['Koordinaten']
            last_station_coords = station_area_ds[ordered_stations[-1]]['Koordinaten']
            # find the next closest station to the first and last stations
            station_area_key_1 = find_next_station_area(route_station_area_ds, first_station_coords, operation_type)
            station_area_key_2 = find_next_station_area(route_station_area_ds, last_station_coords, operation_type)
            # get coordinates of the potential next stations
            station_coords_1 = route_station_area_ds[station_area_key_1]['Koordinaten']
            station_coords_2 = route_station_area_ds[station_area_key_2]['Koordinaten']
            # determine which station is closer and update the ordered list accordingly
            if (calculate_distance(first_station_coords, station_coords_1)
                < calculate_distance(last_station_coords, station_coords_2)):
                ordered_stations.insert(0, station_area_key_1)
                route_station_area_ds.pop(station_area_key_1)
            else:
                ordered_stations.append(station_area_key_2)
                route_station_area_ds.pop(station_area_key_2)
    return ordered_stations


#============================================================
# function update for inhuman task

def calculate_distance(coords1, coords2):
    """
    Calculates the distance between two geographical coordinates using the Haversine formula.

    Arguments:
        coords1 (list): list containing the longitude and latitude of the first point
        coords2 (list): list containing the longitude and latitude of the second point

    Returns:
        float: The distance between the two points in meters
    """

    # radius of the Earth in meters
    R = 6371000

    # convert latitude and longitude from degrees to radians
    lat1 = math.radians(coords1[1])
    lon1 = math.radians(coords1[0])
    lat2 = math.radians(coords2[1])
    lon2 = math.radians(coords2[0])

    # compute differences in coordinates
    dlat = lat2 - lat1
    dlon = lon2 - lon1

    # apply the Haversine formula
    a = math.sin(dlat / 2)**2 + math.cos(lat1) * math.cos(lat2) * math.sin(dlon / 2)**2
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))

    # calculate the distance
    distance = R * c
    return distance