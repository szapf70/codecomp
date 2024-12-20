# Isabell Hirsch
# Alfred Sawade
# Axel Gawarzewski
# Ali Dari

#Schwierigkeitsgrad - schwer

import read_json_files
import definition_library_AD_leicht

def area_kvb(station_area_data):
    """
    Get the minimum and maximum coordinate values for the KVB area 
    :param station_area_data: dict with station area data
    :return: coordinate values for the KVB area 
    """
    farest_coordinates = definition_library_AD_leicht.far_out_stop_locations(station_area_data)
    area_borders = {"x_min": farest_coordinates[0]["western"]-0.05, 
                    "x_max": farest_coordinates[0]["eastern"]+0.05, 
                    "y_min": farest_coordinates[0]["southern"]-0.05, 
                    "y_max": farest_coordinates[0]["northern"]+0.05}
    return area_borders

def get_coordinate_input(dataset):
    """
    Get a pair of coordinates from the User
    :param station_area_data: dict with station area data
    :return: x,y coordinates input from user
    """
    area_borders = area_kvb(dataset)
    x_input = input("Soll die nächste Haltestelle zu Wunschkoordinaten ermittelt "
                    f"werden?\nDie KVB liegt im Bereich x von {area_borders['x_min']}"
                    f" bis {area_borders['x_max']} und y von {area_borders['y_min']} "
                    f"bis {area_borders['y_max']} \nWenn ja, bitte den x-Wert als "
                    "Gleikommazahl eingeben: ")
    x_input = x_input.replace(",",".")
    if not x_input.replace(".","",1).isdecimal():
        return "stop"
    x_input = float(x_input)
    y_input = input("Bitte den y-Wert als Gleikommazahl eingeben: ").replace(",",".")
    while not y_input.replace(".","",1).isdecimal():
        y_input = input("Der y-Wert ist keine Gleikommazahl, bitte noch einmal oder 'stop' eingeben: ").replace(",",".")
        # tbd: Add maximum count of tries?
        if y_input == "stop":
            print("Die Koordinateneingabe wird abgebrochen.\n")
            return "stop"
    y_input = float(y_input)
    return (x_input, y_input)

def get_distance_of_two_points_in_xy_format(point1:tuple, point2:tuple):
    """
    Calculate the distance of two points with x,y coordinates.
    :param point1: (x/y)-coordinates of one point
    :param point2: (x/y)-coordinates of an other point
    :return: distance of the two points
    """
    distance = ((point1[0] - point2[0])**2 + (point1[1] - point2[1])**2)**0.5
    return distance

def get_distance_of_two_points_orthodrome(point1:tuple, point2:tuple):
    """
    Calculate the distance of two points based on orthodromes.
    :param point1: coordinates of one point
    :param point2: coordinates of an other point
    :return: distance in km
    """
    #TODO
    distance = "in development"
    return distance

def find_next_station(dataset, coordinates:tuple, consider_escalators = False, consider_elevators = False):
    """
    Searching the closest station with operative escalator based on a given tuple 
    with x,y coordinates.
    :param dataset: dataset containing station information
    :param coordinates: x,y coordinates the closest station is required for
    :param consider_escalators: only consider stations with all escalators operative
    :param consider_elevators: only consider stations with all elevators operative
    :return: ID of the station identified to have the closest position
    """
    next_station_data = {"notification": ([], []), 
                         "shortest_distance": None, 
                         "next_station": "not defined"}
    # find closest station
    for station_area in dataset:
        # restrict for escalator/elevator
        if (not dataset[station_area]["fahrtreppen"] and consider_escalators) or (not dataset[station_area]["aufzuge"] and consider_elevators):
            continue
        station_area_coord = dataset[station_area]["koordinaten"]
        station_area_distance = get_distance_of_two_points_in_xy_format(coordinates, station_area_coord)
        if not next_station_data["shortest_distance"]:
            next_station_data["shortest_distance"] = station_area_distance
        if station_area_distance > next_station_data["shortest_distance"]:
            next_station_data["shortest_distance"] = station_area_distance
            next_station_data["next_station"] = station_area
        # TODO: replace with orthodrom funtion if required
        # station_area_distance = get_distance_of_two_points_orthodrome(coordinates, station_area_coord)

    #check for escalator/elevator incidents and create a related notification
    if consider_escalators:
        #TODO: add capturing of 'Ausnahmebehandlung'
        escalator_incidents = read_json_files.get_escalator_incidents(dataset)
        if escalator_incidents.get(next_station_data["next_station"], False):
            for escalator in escalator_incidents:
                next_station_data["notification"][0].append(escalator + " - " + escalator["bezeichnung"])
    if consider_elevators:
        #TODO: add capturing of 'Ausnahmebehandlung'
        elevator_incidents = read_json_files.get_elevator_incidents(dataset)
        if elevator_incidents.get(next_station_data["next_station"], False):
            for elevator in elevator_incidents:
                next_station_data["notification"][1].append(elevator + " - " + elevator["bezeichnung"])

    return next_station_data

def find_final_destinations(dataset, stations:set):
    """
    Searching the stations with the farest distance of a set of stations. 
    :param dataset: dataset containing station information
    :param stations: set of stations (by ID), where the farest two shall be determined  
    :return: tuple of the stations farest away from each other
    """
    #TODO
    stations = ("in development", "also in development")
    return stations

def find_a_stations_next_station(stating_point, stations_in_question:set):
    """
    Searching the station closest to a defind station. 
    :param stating_point: ID of the station, which the closest one shall be determind
    :param stations_in_question: set of stations (by ID) that are to search for the closest station  
    :return: ID of the station, which was identified to be the closest one
    """
    #TODO
    # TODO - tbd: exclude "Longerich Friedhof as this is an alternate shorter route?"
    station = "in development"
    return station

def order_line_stations_by_distance(dataset, stations_of_one_line:set) -> list:
    """
    Ordering the stations of a list from "endpoint" to "endpoint"  
    :param dataset: dataset containing station area information
    :param stations_of_one_line: set of stations (by ID) from one line  
    :return: stations ordered in a list
    """
    #TODO
    final_destinations = find_final_destinations(dataset, stations_of_one_line)
    ordered_stations = []
    return ordered_stations

def order_train_stations_by_distance(dataset, train_line_data):
    """
    For each train line the station areas are ordered from one endpoint to the other
    endpoint. And stored to train_line_data["haltestellen"].
    :param dataset: dataset containing station area information
    :param train_line_data: dataset containing train line information 
                            (key "haltestellen" will be modified)
    """
    #TODO
    #find_final_destinations()
    #find_a_stations_next_station()
    #order_line_stations_by_distance()
    pass
