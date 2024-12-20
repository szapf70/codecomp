# Isabell Hirsch
# Alfred Sawade
# Axel Gawarzewski
# Ali Dari

#Schwierigkeitsgrad - mittel


def most_common_stops(dataset):
    """
    Searching 2 train lines with most common stops 

    Parameter:
        dataset: data_for_stations containing line information "linien", "station"
    
    Return:
        int: ID of trains (line_1, line_2) + count of common stops
    """
    
    from itertools import combinations
    
    stop_dict = {}
    line_dict = {}
    stop_count = 0

    for data_for_stations in dataset:
        common_stops = list(combinations(dataset[data_for_stations]["linien"],2))
        stop_dict[data_for_stations] = common_stops

    for line_data in stop_dict:
        for combination in stop_dict[line_data]:
            if not line_dict.get(combination):
                line_dict[combination] = 0
            line_dict[combination] +=1

    most_common_stops = max([line_dict[line_pair] for line_pair in line_dict])
    line_pair_list = [line_pair for line_pair in line_dict if most_common_stops == line_dict[line_pair]]

    return most_common_stops, line_pair_list


def most_dfi(dataset):
    """
    Searching line with most digital information (percent) 

    Parameter:
        dataset: data_for_stations containing dfi information "linien", "digitalanzeige"
    
    Return:
        float: most_dfi_percentage with percentige of line with most dfi
        list: line_list with line information
    """
    station_dict = {}

    for data_for_stations_areas in dataset:

        for linie in dataset[data_for_stations_areas]["linien"]:
            if not station_dict.get(linie):
                station_dict[linie] = {}
                station_dict[linie]["total_stops"] = 0 
                station_dict[linie]["dfi_count"] = 0
            station_dict[linie]["total_stops"] += 1
            if dataset[data_for_stations_areas]["digitalanzeige"]:
                station_dict[linie]["dfi_count"] += 1

        for linie in station_dict:
            station_dict[linie]["percentage"] = station_dict[linie]["dfi_count"]/station_dict[linie]["total_stops"]*100

        most_dfi_percentage = max([station_dict[linie]["percentage"] for linie in station_dict])
        line_list = [linie for linie in station_dict if most_dfi_percentage == station_dict[linie]["percentage"]]
        
            
    return  most_dfi_percentage, line_list

    
def most_escalators(dataset):
    """
    Searching line with most escalators (percent)

    Parameter:
        dataset: data_for_stations containing escalator information "linien", "fahrtreppen"
    
    Return:
        float: most_escalator_percentage with percentige of line with most escalators
        list: line_list with line information
    """
    station_dict = {}

    for data_for_stations_areas in dataset:

        for linie in dataset[data_for_stations_areas]["linien"]:
            if not station_dict.get(linie):
                station_dict[linie] = {}
                station_dict[linie]["total_stops"] = 0 
                station_dict[linie]["escalator_count"] = 0
            station_dict[linie]["total_stops"] += 1
            if dataset[data_for_stations_areas]["fahrtreppen"]:
                station_dict[linie]["escalator_count"] += 1

        for linie in station_dict:
            station_dict[linie]["percentage"] = station_dict[linie]["escalator_count"]/station_dict[linie]["total_stops"]*100

        most_escalator_percentage = max([station_dict[linie]["percentage"] for linie in station_dict])
        line_list = [linie for linie in station_dict if most_escalator_percentage == station_dict[linie]["percentage"]]
        
            
    return  most_escalator_percentage, line_list
      

def most_elevators(dataset):
    """
    Searching line with most elevators (percent)

    Parameter:
        dataset: data_for_stations containing escalator information "linien", "aufzuge"
    
    Return:
        float: most_elevator_percentage with percentige of line with most elevators
        list: line_list with line information
    """
    station_dict = {}

    for data_for_stations_areas in dataset:

        for linie in dataset[data_for_stations_areas]["linien"]:              
            if not station_dict.get(linie):
                station_dict[linie] = {}
                station_dict[linie]["total_stops"] = 0 
                station_dict[linie]["elevator_count"] = 0
            station_dict[linie]["total_stops"] += 1
            if dataset[data_for_stations_areas]["aufzuge"]:
                station_dict[linie]["elevator_count"] += 1

        for linie in station_dict:
            station_dict[linie]["percentage"] = station_dict[linie]["elevator_count"]/station_dict[linie]["total_stops"]*100

        most_elevator_percentage = max([station_dict[linie]["percentage"] for linie in station_dict])
        line_list = [linie for linie in station_dict if most_elevator_percentage == station_dict[linie]["percentage"]]
        
            
    return  most_elevator_percentage, line_list


def all_bus_numbers(dataset):
    """    
    Searching all bus lines

    Parameter:
        dataset: dict with station area data "linien"
    
    Return:
        list: with all bus lines (all_bus)
    """
    all_bus = list

    for data_for_station_areas in dataset:
        if int(data_for_station_areas["linien"]) > 99:                      # muss hier ein split hin?
            list(set(all_bus.append(data_for_station_areas["linien"])))     # set nur um dopplete rauszufiltern

    return all_bus


def all_train_numbers(dataset):
    """
    Searching all train lines
    
    Parameter:
        dataset: dict with station area data "linien"
    
    Return:
        set: with all train lines (all_train_lines )
    """
    all_train_lines = set

    for data_for_station_areas in dataset:
        if int(data_for_station_areas["linien"]) < 99:
            set(all_train_lines.update(data_for_station_areas["linien"]))

    return all_train_lines


def all_train_connections(dataset):
    """    
    Searching all train lines with connection train lines
    :param dataset: dataset containing train information
    :return: all_train_connections (dict of lines with their connection line as list)
    """
    # not required, as handled in read_json_files.py
    return all_train_connections


def lines_with_service_point(dataset):
    """    
    Searching all trains with min. one customer point along  lines
    :param dataset: dataset containing service point information
    :return: all_lines_with_service-point (list)
    """
    # not required, as handled in read_json_files.py
    return all_lines_with_service_point


def connecting_lines_with_service_point(dataset):
    """    
    Searching all trains with min. one customer point connected by one transfer max
    :param dataset: dataset containing service point information
    :return: connecting_lines_with_service-point (list)
    """
    #TODO
    return connecting_lines_with_service_point

def check_service_points_for_train_lines(dataset):
    """    
    Searching all trains with min. one customer point connected by one transfer max
    :param dataset: dataset containing train line information
    :return: dict of train lines with related service point information,
             properties: "anzahl_anliegender_kc":int, "umsteigelinien_mit_kc":list of int
    """
    # not required, as handled in read_json_files.py
    return service_points
