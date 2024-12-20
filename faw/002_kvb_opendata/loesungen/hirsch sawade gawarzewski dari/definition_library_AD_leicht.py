# Isabell Hirsch
# Alfred Sawade
# Axel Gawarzewski
# Ali Dari

#Schwierigkeitsgrad - leicht


def number_of_bus_lines(dataset):
    """
    Searching all bus and train lines

    Parameter:
        dataset: containing station_area information "linien"
    
    Return:
        int: count of all bus and train lines (all_bus_trains)
    """
    bus_trains_set = set() 

    for station_area in dataset:
        bus_trains_set.update(dataset[station_area]["linien"])

        all_bus_trains = len(bus_trains_set)

    return all_bus_trains


def most_stops_in_area(dataset):
    """
    Searching station area with most stops

    Parameter:
        dataset: containing data_for_stations information "kurzname" 
    
    Return:
        list: name_list with "kurzname"
        int: count of stops (most_stops_count)
    """

    kurzname = dict()
    name_list = list()
    most_stops_count = 0

    for data_for_stations in dataset:
        if not kurzname.get(dataset[data_for_stations]["kurzname"]):                
           kurzname[dataset[data_for_stations]["kurzname"]] = 1                    
        else:
            kurzname[dataset[data_for_stations]["kurzname"]] += 1                   
        
        most_stops_count = max([kurzname[n] for n in kurzname])                     
        name_list = [n for n in kurzname if most_stops_count == kurzname[n]]
    return  most_stops_count, name_list 

    
def most_connections(dataset):
    """
    Searching station area with most connections

    Parameter:
        dataset: containing station_area_data information "linien"
    
    Return:
        list: VRS numbers (vrsnumber_list)
        int:  count of most connections (most_connections)
    """
    vrsnumber_list = list()
    most_connections_count:int = 0

    for station_area_data in dataset:
        if len(dataset[station_area_data]["linien"]) == most_connections_count:  
           vrsnumber_list.append(station_area_data)

        if len(dataset[station_area_data]["linien"]) > most_connections_count:
            most_connections_count = len(dataset[station_area_data]["linien"])     
            vrsnumber_list = [station_area_data]
                                                                                                                      
    return  most_connections_count, vrsnumber_list 


def escalator(dataset):
    """
    Searching areas with escalators

    Parameter:
        dataset: containing station_area_data information "fahrtreppen"
    
    Return:
        list: escalators in station area (escalators_in_area)
    """    
    escalators_in_area = list()

    for station_area_data in dataset:
        if dataset[station_area_data]["fahrtreppen"]:
            escalators_in_area.append(station_area_data)
    
    return escalators_in_area


def elevator(dataset):
    """
    Searching areas with elevators

    Parameter:
        dataset: containing station_area_data information "aufzuge"
    
    Return:
        list: areas with escalators (elevators_in_area)
    """ 
    elevators_in_area = list()

    for station_area_data in dataset:
        if dataset[station_area_data]["aufzuge"]:
            elevators_in_area.append(station_area_data)

    return elevators_in_area


def elevator_and_escalator(dataset):
    """
    Searching areas with elevators and elevators

    Parameter:
        dataset: containing station_area_data "fahrtreppen" and "aufzuge"
    
    Return:
        list: areas with elevators and escalators (elevators_and_escalators_in_area)
    """    
    elevators_and_escalators_in_area = list()

    for station_area_data in dataset:
        if dataset[station_area_data]["fahrtreppen"] and dataset[station_area_data]["aufzuge"]:
            elevators_and_escalators_in_area.append(station_area_data)

    return elevators_and_escalators_in_area


def no_elevator_and_escalator(dataset):
    """
    Searching areas with no elevators and elevators

    Parameter:
        dataset: containing station_area_data elevator and escalator information "fahrtreppen" and "aufzuge"
    
    Return:
        list:  areas with no elevators and no escalators (no_elevators_and_escalators_in_area)
    """    
    no_elevators_and_escalators_in_area = list()

    for station_area_data in dataset:
        if not dataset[station_area_data]["fahrtreppen"] and not dataset[station_area_data]["aufzuge"]:
            no_elevators_and_escalators_in_area.append(station_area_data)

    return no_elevators_and_escalators_in_area


def bus_connection(dataset):
    """
    Counting areas with bus connection

    Parameter:
        dataset: containing station_area_data information "bus"
    
    Return:
        list: areas with bus connection (bus_connection)
    """      
    bus_connection = list()

    for station_area_data in dataset:
        if dataset[station_area_data]["bus"]:
            bus_connection.append(station_area_data) 
    
    return bus_connection


def train_connection(dataset):
    """
    Searching areas with train connection

    Parameter:
        dataset: containing station_area_data information "strassenbahn"
    
    Return:
        list: areas with train connection (train_connection)
    """
    train_connection = list()

    for station_area_data in dataset:
        if dataset[station_area_data]["strassenbahn"]:
            train_connection.append(station_area_data)

    return train_connection


def train_and_bus_connection(dataset):
    """
    Searching areas with train and bus connection

    Parameter:
        dataset: containing station_area_data information "bus" and "strassenbahn"
    
    Return:
        list: areas with train and bus connection (train_and_bus_connection)
    """
    train_and_bus_connection = list()

    for station_area_data in dataset:
        if dataset[station_area_data]["bus"] and dataset[station_area_data]["strassenbahn"]:
            train_and_bus_connection.append(station_area_data)
    
    return train_and_bus_connection


def far_out_stop_locations(dataset):
    """
    Searching most northern, southern, western and eastern stop

    Parameter:
        dataset: containing data_for_stations information "koordinaten"
    
    Return:
        Dict: with far out stop location area (stop_locations) and VRS numbers (vrs_num)
    """   
    
    stop_locations = dict()
    vrs_num = dict()

    for data_for_stations in dataset:
        if not stop_locations:
            stop_locations = {"northern":dataset[data_for_stations]["koordinaten"][1],
                              "southern":dataset[data_for_stations]["koordinaten"][1],
                              "eastern":dataset[data_for_stations]["koordinaten"][0],
                              "western":dataset[data_for_stations]["koordinaten"][0]
                             }
            vrs_num  =      {"northern":dataset[data_for_stations],
                              "southern":dataset[data_for_stations],
                              "eastern":dataset[data_for_stations],
                              "western":dataset[data_for_stations]
                            }
        if  dataset[data_for_stations]["koordinaten"][1] > stop_locations["northern"]:
            stop_locations["northern"] = dataset[data_for_stations]["koordinaten"][1]
            vrs_num["northern"] = data_for_stations
            
        if  dataset[data_for_stations]["koordinaten"][1] < stop_locations["southern"]:
            stop_locations["southern"] = dataset[data_for_stations]["koordinaten"][1]
            vrs_num["southern"] = data_for_stations

        if  dataset[data_for_stations]["koordinaten"][0] > stop_locations["eastern"]:
            stop_locations["eastern"] = dataset[data_for_stations]["koordinaten"][0]
            vrs_num["eastern"] = data_for_stations

        if  dataset[data_for_stations]["koordinaten"][0] < stop_locations["western"]:
            stop_locations["western"] = dataset[data_for_stations]["koordinaten"][0]
            vrs_num["western"] = data_for_stations

    return stop_locations, vrs_num