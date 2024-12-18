# import modules

import json
import os
import statistics
import math


#===================================================
# Read all files and set up new structure
#===================================================

def read_json_file(filename, subdirectory, encoding_in='utf-8'):
    """Read Json Format file

    Args:
        filename : name of the file
        subdirectory : location of the file
        encoding_in : Defaults to 'utf-8'.

    Returns:
        data: Dataset with all Stationareas (subtracting features layer)
    """
    filepath = os.path.join(subdirectory, filename)
    with open(filepath, 'r', encoding=encoding_in) as file:
        data = json.load(file)
    return data['features']

def read_files(json_subdirectory):
    """Read all json files wihtin given Folder

    Args:
        json_subdirectory (dir)): relativ directory of json files

    Returns:
        station_area_ds:            dict/list combination of all information sorted by station areas
        elevator_malfunction_data:  Information about defect elevators
        escalator_malfunction_data: Information about defect ecalators
    """
    #============================================================
    # input files

    station_area_file = 'haltestellenbereiche.json'
    station_file = 'haltestellen.json'
    station_area_diginfo_file = 'haltestellenbereichemitdfi.json'
    place_of_sale_file = 'verkaufsorte.json'
    elevator_file = 'aufzuege.json'
    elevator_malfunction_file = 'aufzugstoerungen.json'
    escalator_file = 'fahrtreppen.json'
    escalator_malfunction_file = 'fahrtreppenstoerungen.json'

    #============================================================
    # read all files

    station_area_data = read_json_file(station_area_file, json_subdirectory, 'latin-1')
    station_data = read_json_file(station_file, json_subdirectory, 'latin-1')
    station_area_diginfo_data = read_json_file(station_area_diginfo_file, json_subdirectory)
    place_of_sale_data = read_json_file(place_of_sale_file, json_subdirectory, 'latin-1')
    elevator_data = read_json_file(elevator_file, json_subdirectory)
    elevator_malfunction_data = read_json_file(elevator_malfunction_file, json_subdirectory)
    escalator_data = read_json_file(escalator_file, json_subdirectory)
    escalator_malfunction_data = read_json_file(escalator_malfunction_file, json_subdirectory, 'latin-1')

    #============================================================
    # create new data structure

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

    # add station data (properties and coordinates)
    for station in station_data:
        station_dict = get_properties(station)
        key = station_area_key_ds[station_dict.pop('Name')]

        station_dict.pop('Kurzname') # insert sanity check???
        station_dict['Koordinaten'] = station['geometry']['coordinates']

        if station_area_ds[key].get('Haltestellen') == None:
            station_area_ds[key]['Haltestellen'] = []
        station_area_ds[key]['Haltestellen'].append(station_dict)

    # add data for digital passenger information
    for diginfo in station_area_diginfo_data:
        diginfo_dict = get_properties(diginfo)
        key = diginfo_dict['Haltestellenbereich']

        station_area_ds[key]['DFI'] = ['true']

    # add elevator data (properties and coordinates)v
    for elevator in elevator_data:
        elevator_dict = get_properties(elevator)
        key = elevator_dict.pop('Haltestellenbereich')

        elevator_dict['Koordinaten'] = elevator['geometry']['coordinates']

        if station_area_ds[key].get('Aufzüge') == None:
            station_area_ds[key]['Aufzüge'] = []
        station_area_ds[key]['Aufzüge'].append(elevator_dict)

    # add escalator data (properties and coordinates)
    for escalator in escalator_data:
        escalator_dict = get_properties(escalator)
        key = escalator_dict.pop('Haltestellenbereich')

        escalator_dict['Koordinaten'] = escalator['geometry']['coordinates']

        if station_area_ds[key].get('Fahrtreppen') == None:
            station_area_ds[key]['Fahrtreppen'] = []
        station_area_ds[key]['Fahrtreppen'].append(escalator_dict)

    # add place of sale data ()
    for place_of_sale in place_of_sale_data:
        place_of_sale_dict_temp = get_properties(place_of_sale)
        key = place_of_sale_dict_temp.pop('haltestellenbereich')

        place_of_sale_dict = dict()
        place_of_sale_dict['Segment'] = place_of_sale_dict_temp['Segment']
        place_of_sale_dict['Koordinaten'] = place_of_sale['geometry']['coordinates']

        if station_area_ds[key].get('Verkaufsorte') == None:
            station_area_ds[key]['Verkaufsorte'] = []
        station_area_ds[key]['Verkaufsorte'].append(place_of_sale_dict)

    # add a False boolean entry if digital info is not available
    # and add empty lists for elevator, escalator & places of sale to station area if not available
    # and add coordinates for station area based on the station coordinates
    for key, station_area in station_area_ds.items():
        if station_area.get('DFI') == None:
              station_area_ds[key]['DFI'] = []                 #CS new leer
        if station_area.get('Aufzüge') == None:
              station_area_ds[key]['Aufzüge'] = []
        if station_area.get('Fahrtreppen') == None:
              station_area_ds[key]['Fahrtreppen'] = []
        if station_area.get('Verkaufsorte') == None:
             station_area_ds[key]['Verkaufsorte'] = []
        station_area_ds[key]['Koordinaten'] = calc_mean_station_coords(station_area['Haltestellen'])

# Option: save station area dictionary to file for visualization
# with open('station_area_temporary.json', 'w', encoding='utf-8') as file:
#        json.dump(station_area_ds, file, indent=4, ensure_ascii=False)
    return station_area_ds, elevator_malfunction_data, escalator_malfunction_data

#===================================================
# commonly used local functions
#===================================================

def list_all_lines(station_area_ds):
    """list_all_lines

    Args:
        station_area_ds : Dataset with all Stationareas 

    Returns:
        List of Strings: Numerical sorted List of all lines in string format (so it can be compared easy str entries in dataset)
    """
    lines = set()
    for key, station_area in station_area_ds.items():
        if station_area.get('Linien'):
            # Use set type to make sure just unique lines are in list
            lines.update(set(station_area.get('Linien')))
    # sort string entries in list numerically and save as strings                      
    lines_list = list(map(str, sorted(list(map(int, lines))) ))    
    return lines_list

def list_all_strab(station_area_ds):
    """List all STRAB

    Args:
        station_area_ds: Dataset with all Stationareas 

    Returns:
        List of Strings: Numerical sorted List of all STRAB lines in string format (so it can be compared easy str entries in dataset)
    """

    trab_lines = []
    lines_list = list_all_lines(station_area_ds)
    for element in lines_list:
        # filter all lines with less than three digits
        if len(element) < 3:
            trab_lines.append(element)
            pass
    return trab_lines

def gps_to_m(coordinates): 
    """Convert GPS (Lat/Lon) to m

    Args:
        coordinates (Lat/Lon): Convert GPS W83 coordinates to meter

    Returns:
        List: List of GPS in meters. Fist entry is distance to equator (Lat = 0), second distance to Greenwich (Lon = 0). Both in [m]
    """
    # Assumption: Radius of world: 6371008 m [wiki]
    R = 6371008
    gps_in_m = [(max(coordinates)*2*math.pi*R) / 360 , (2*math.pi*R *min(coordinates) *  math.cos(math.radians(max(coordinates))))/360]
    return gps_in_m

def find_closest_point(position, gps_list):
    """Find the point in a list of GPS data which is smallest distance to position.

    Args:
        position (X/Y): two-dimensional reference postion (in Lat/Lat or x/y Format)
        gps_list (List of GPS): List of two-dimensional point (in Lat/Lon or x/y Format)

    Returns:
        Closest point (Index of list, X, Y): Pointer to index in the list which point is closest and it's x/y coordinates 
    """
    #Initiliase local indices
    closest_point = [0 ,0 ,0]
    min_distance = float('inf')
    idx = 0
    for point in gps_list:
                #convert gps to m to have the same weight of x/y in distance calculation (1° Lon is significantly different than 1° Lat in m in the area of cologne)
                point_in_m = gps_to_m(point)
                position_in_m = gps_to_m(position)
                #Pythagoras for distance calculation
                distance = math.sqrt((point_in_m[0]-position_in_m[0]) ** 2 + (point_in_m[1]-position_in_m[1]) **2 )
                if distance < min_distance:
                    min_distance = distance
                    closest_point[0] = idx
                    closest_point[1] = max(point)
                    closest_point[2] = min(point)
                idx += 1
    return closest_point

def get_properties(dict_in): 
    """Get Properties

    Args:
        dict_in (dict): Station Area dict in file (raw) structure

    Returns:
        Dict out (dict): Sorted dict with 'Linien' and 'Betriebsbereich' dict structure
    """
    dict_out = dict()
    for property in dict_in['properties']:
        if property == 'Linien' or property == 'Betriebsbereich':
            dict_out[property] = dict_in['properties'][property].split()
        else:
            dict_out[property] = dict_in['properties'][property]
    return dict_out

def calc_mean_station_coords(stations):
    """Calulate Station Area mean GPS coordinates

    Args:
        stations (dict): All stations within a station area

    Returns:
        GPS: Mean GPS position of all stops, which represents the mean GPS value a station area
    """
    station_coords = []
    for station in stations:
         station_coords.append(station['Koordinaten'])
    x_mean = statistics.mean([coords[0] for coords in station_coords])
    y_mean = statistics.mean([coords[1] for coords in station_coords])
    return [round(x_mean, 5), round(y_mean, 5)]

def most_elements(station_area_ds, key):
    """Count elements and provide maximum

    Args:
        station_area_ds (dict): Dataset with all Stationareas
        key (str): the key element which will be counted

    Returns:
        _type_: _description_
    """
    max_key_length = 0
    max_key = []
    max_key_name = str()
    for station_area_key, station_area in station_area_ds.items():
        if station_area.get(key) != None:
            key_length = len(station_area.get(key))
            if key_length == max_key_length:
                max_key.append(station_area_key)
            elif key_length > max_key_length:
                max_key_length = key_length
                max_key = [station_area_key]
                if len(station_area.get("Haltestellenname")) > 0:
                    max_key_name = station_area.get("Haltestellenname")
                else:
                    max_key_name = 'No name'
    return(max_key, max_key_name, max_key_length)

def station_line_count(station_area_ds, key):
    """calculate all lines with dfi, elevators, escavators

    Args:
        station_area_ds (dict): Dataset with all Stationareas
        key (str): identifies wich property shall be investigated

    Returns:
        Line_counter: Returns a list of the line and number of the maximum found keys/identifiers
    """
    #Initialize
    max_count = 0
    line_counter = []
    max_count_pct = float()
    line_count_pct = float()
    lines_list = list_all_lines(station_area_ds)
    #Outer Loop: Go through all the lines
    for line in lines_list:
        #Initialize line_count for element on line counter and total_count for total stations count
        line_count = 0
        line_count_pct = float()
        total_count = 0
        #Inner Loop: Search in all station areas
        for station_area_key, station_area in station_area_ds.items():
            #Find all stations for the line (outer loop)
            if station_area.get('Linien') != None:
                if line in station_area.get('Linien') and len(station_area.get(key)) > 0:
                    #Add to list if key is element in stationarea
                    line_count += 1
                if line in station_area.get('Linien'):
                    #Add to list of all station along line, also if key is not element
                    total_count += 1                    
        line_count_pct = line_count / total_count * 100          
        if line_count_pct > max_count_pct:
            max_count_pct = line_count_pct
            max_count = line_count
            max_count_line = line
    line_counter = [max_count_line, max_count, max_count_pct]
    return line_counter

#===================================================
#  Tasks
#===================================================
#===================================================
#  Leicht
#===================================================

# Task: Einfach 1:

def count_routes(station_area_ds):
    """List all Lines running

    Args:
        station_area_ds (dict): Dataset with all Stationareas 

    Returns:
        Lines (set): A set of all the lines stopping at all stations areas (unique)
    """
    routes = set()
    for key, station_area in station_area_ds.items():
        if station_area.get('Linien'):
            routes.update(set(station_area.get('Linien')))
    einfach_1 = ('',
                 '=================================',
                 ' Leicht',
                 '=================================',
                 'Leicht - 1:',
                 'Wie viele Linien (Busse und Bahnen) und wie viele Haltestellenbereiche gibt es insgesamt?',
                 '',
                 f"Linien gesamt: {len(routes)}" ,
                 f"Haltestellenbereiche: {len(station_area_ds)}")
    for n in range(len(einfach_1)):
        print(einfach_1[n])
    return (einfach_1)

# Task: Einfach 2:
def most_stops_and_lines(station_area_ds):
    """Count elements and provide maximum

    Args:
        station_area_ds (dict): Dataset with all Stationareas
        key (str): the key element which will be counted

    Returns:
        _type_: _description_
    """
                       
    #Repeat all for lines
    key = 'Linien'
    max_key_hs, max_key_name_hs, max_key_length_hs = most_elements(station_area_ds, 'Haltestellen')
    max_key_li, max_key_name_li, max_key_length_li = most_elements(station_area_ds, 'Linien')
    einfach_2 = ('',
        '=================================',
        'Leicht - 2:',
        'Welcher Haltestellenbereich hat die meisten Haltestellen und an welchem Treffen sich die meisten Linien?',
        '', 
        f"Haltestellenbereich mit meisten Haltestellen: Bereich {max_key_hs[0]}, {max_key_name_hs}, {max_key_length_hs} Haltestellen",
        f"Haltestellenbereich mit meisten Linien: Bereich {max_key_li[0]}, {max_key_name_li}, {max_key_length_li} Haltestellen")
    for n in range(len(einfach_2)):
        print(einfach_2[n])
    return (einfach_2)

# Task: Einfach 3:
def number_entries(station_area_ds):
    """Count number of entries (Fahrtreppen, Aufzüge)

    Args:
        station_area_ds (dict): Dataset with all Stationareas

    Returns:
        List: List of all possible combinations of station entries
    """
    #Initialize possible combinations
    number_entries = {
        'NONE' : 0,
        'BUS' : 0, 
        'STRAB': 0,
        'BOTH': 0
    }
    for station_area_key, station_area in station_area_ds.items():
        if station_area.get('Betriebsbereich') != None:
            if 'BUS' in station_area.get('Betriebsbereich'):
                number_entries['BUS'] += 1
            if 'STRAB' in station_area.get('Betriebsbereich'):
                number_entries['STRAB'] += 1
            if len(station_area.get('Betriebsbereich')) == 2:
                number_entries['BOTH'] += 1
        else:
            number_entries['NONE'] += 1
        einfach_3 = ('',
        '=================================',
        'Leicht - 3:',
        'Wieviel Haltestellenbereiche decken jeweils die Betriebsbereich „BUS“, „STRAB“ oder beides ab?',
        '', 
        f"keine:{number_entries['NONE']}",
        f"Bus: {number_entries['BUS']}",
        f"Strassenbahn: {number_entries['STRAB']}",
        f"Beide: {number_entries['BOTH']}")
    for n in range(len(einfach_3)):
        print(einfach_3[n])
    return einfach_3

# Task: Einfach 4:
def corners(station_area_ds):
    """Calculate gps corners of staion map

    Args:
        station_area_ds (dict): Dataset with all Stationareas

    Returns:
        Dict: Dictionary with a List of all corner names and coordinates
    """
    #Initialise one point for each 'corner' to compare to
    North = [station_area_ds['1']['Haltestellen'][0]["Koordinaten"][0], station_area_ds['1']['Haltestellen'][0]["Koordinaten"][1]]
    South = [station_area_ds['1']['Haltestellen'][0]["Koordinaten"][0], station_area_ds['1']['Haltestellen'][0]["Koordinaten"][1]]
    West = [station_area_ds['1']['Haltestellen'][0]["Koordinaten"][0], station_area_ds['1']['Haltestellen'][0]["Koordinaten"][1]]
    East = [station_area_ds['1']['Haltestellen'][0]["Koordinaten"][0], station_area_ds['1']['Haltestellen'][0]["Koordinaten"][1]]
    #Go through all Station stops and compare
    for station_area_key, station_area in station_area_ds.items():
        if station_area.get('Haltestellen' ) != None:
            for stations in station_area.get('Haltestellen' ):
                if station_area['Haltestellen'][0]["Koordinaten"][1] > North[1]:
                    North = [station_area['Haltestellen'][0]["Koordinaten"][0], station_area['Haltestellen'][0]["Koordinaten"][1]]
                    n_station = station_area["Haltestellenname"]
                if station_area['Haltestellen'][0]["Koordinaten"][1] < South[1]:
                    South = [station_area['Haltestellen'][0]["Koordinaten"][0], station_area['Haltestellen'][0]["Koordinaten"][1]]
                    s_station = station_area["Haltestellenname"]
                if station_area['Haltestellen'][0]["Koordinaten"][0] > East[0]:
                    East = [station_area['Haltestellen'][0]["Koordinaten"][0], station_area['Haltestellen'][0]["Koordinaten"][1]]
                    e_station = station_area["Haltestellenname"]
                if station_area['Haltestellen'][0]["Koordinaten"][0] < West[0]:
                    West = [station_area['Haltestellen'][0]["Koordinaten"][0], station_area['Haltestellen'][0]["Koordinaten"][1]]
                    w_station = station_area["Haltestellenname"]
    corner = {
        'Nord' : (n_station, North),
        'Ost' : (e_station, East),
        'Sued' : (s_station, South),
        'West' : (w_station, West)
        }
    einfach_4 = ('',
        '=================================',
        'Leicht - 4:',
        'Bestimme den noerdlichsten, westlichsten, suedlichsten und oestlichsten Haltstellenbereich. Wie kann man die Position eines Haltestellenbereichs berechnen?',
        '', 
        f"Nord: {corner['Nord'][0]:<25}{corner['Nord'][1]}",
        f"Sued: {corner['Sued'][0]:<25}{corner['Sued'][1]}",
        f"Ost:  {corner['Ost'][0]:<25}{corner['Ost'][1]} ",
        f"West: {corner['West'][0]:<25}{corner['West'][1]} ")
    for n in range(len(einfach_4)):
        print(einfach_4[n])
    return einfach_4

#===================================================
#  Mittel
#===================================================

# Task: Mittel 1:
def lines_by_stations(station_area_ds):
    """Sort Lines

    Args:
        station_area_ds (dict): Dataset with all Stationareas

    Returns:
        max_common, line_pair, sec_max_common, sec_line_pair (int): Most and second to most common stations for two lines
    """
    #Initialize most station pair
    most_stations_line = 0
    #Get a list of all Lines possible
    lines_list = list_all_lines(station_area_ds)
    #Create a list of all possible line cross combination
    station_lines = []
    for station_area_key, station_area in station_area_ds.items():
        #Exclude Stops with no or just one line (no crossing lines)
        if station_area.get('Linien') != None and len(station_area.get('Linien')) > 1:
            lines= (set(station_area.get('Linien')))
            station_lines.append(lines)
    #Initialize return values
    max_common = 0 
    sec_max_common = 0
    line_pair = (None, None)
    sec_line_pair = (None, None)
    for line1 in lines_list:                                  # first part of pair (smaller number)
        for line2 in lines_list:                              # second part of pair (higher number)
            if line2 > line1:                                 # must not be the same and second the higher number
                common_stations = 0                           # Initiliaze inner loop with no common station
                for stations in station_lines:                # look at each station for the pair first,second
                    if line1 in stations and line2 in stations:              
                        common_stations += 1                  #add counter only if pair exists
                if common_stations > max_common:
                    max_common = common_stations
                    line_pair = (line1, line2)
                if common_stations > sec_max_common and common_stations < max_common:
                    sec_max_common = common_stations
                    sec_line_pair = (line1, line2)
    #Output
    mittel_1 = ('',
        '=================================',
        ' Mittel ',
        '=================================',
        'Mittel - 1:',
        'Welche beiden Linien haben die größte Anzahl gemeinsamer Stationen?',
        '', 
        f"Linien mit den meisten gemeinsamen Stationen:{line_pair} Stationen: {max_common}",
        f"Linien mit den zweitmeisten gemeinsamen Stationen:{sec_line_pair} Stationen: {sec_max_common}")
    #Print to Terminal
    for n in range(len(mittel_1)):
        print(mittel_1[n])
    return mittel_1

# Task: Mittel 2:
def station_percent(station_area_ds):
    """Calculate all DFI, Farhtreppen, Aufzüge Information per stop in relation to all stops along a line

    Args:
        station_area_ds (dict): Dataset with all Stationareas
    Returns:
        line_dfi, line_ele, line_rol: DFI, Farhtreppen, Aufzüge Information per stop in relation to all stops along a line
    """
    line_dfi = station_line_count(station_area_ds,"DFI")
    line_ele = station_line_count(station_area_ds,"Aufzüge")
    line_rol = station_line_count(station_area_ds,"Fahrtreppen")
    #Output
    mittel_2 = ('',
        '=================================',
        'Mittel - 2:',
        'Welche Linie ist an all ihren Haltestellen prozentual am besten mit digitalen Fahrgastinformationsanzeigen ausgestattet? Das gleiche auch fuer Fahrtreppen und Aufzuege.',
        '', 
        f"Linie {line_dfi[0]} hat die meisten Haltestellen mit Digitalenfahrgastinformation. Und zwar an {line_dfi[1]} Haltestellen, was {line_dfi[2]:.2f} % entspricht",
        f"Linie {line_ele[0]} hat die meisten Aufzuege. Und zwar {line_ele[1]} Aufzuege, was {line_ele[2]:.2f} % entspricht",
        f"Linie {line_rol[0]} hat die meisten Fahrtreppen. Und zwar {line_rol[1]} Fahrtreppen, was {line_rol[2]:.2f} % entspricht")
    #print to Terminal
    for n in range(len(mittel_2)):
        print(mittel_2[n])
    return mittel_2

# Task: Mittel 3:
def assign_lines_type(station_area_ds):
    """Show that all one and two digit lines are STRAB and three digits are BUS

    Args:
        station_area_ds (dict): Dataset with all Stationareas

    Returns:
        digit_type: Describes the type of line for one and two digit lines and the three digit lines
    """
    #Initialize
    digit_type_bus = set()
    digit_type_strab = set()
    for station_area_key, station_area in station_area_ds.items():
        if station_area.get('Haltestellen') != None:            
            for stellen in station_area.get('Haltestellen'):
                if "Linien" in stellen:
                    if len(stellen["Linien"][0]) == 3:
                        digit_type_bus.add((stellen["Betriebsbereich"][0]))
                    if len(stellen["Linien"][0]) == 1 or len(stellen["Linien"][0]) == 2:
                        digit_type_strab.add((stellen["Betriebsbereich"][0]))
    digit_type = [digit_type_bus, digit_type_strab]
    #Output
    mittel_3 = ('',
        '=================================',
        'Mittel - 3:',
        'Der Koelner weiss das eine zweistellige Nummer eine Strassenbahn und eine dreistellige Nummer ein Bus ist. Aber koennte man diese Information auch aus den Daten ziehen? Direkt angegeben ist es nicht.',
        '', 
        f"Alle drei-stelligen Linien werden von {digit_type[0]} angefahren. Alle ein- und zwei-stelligen Linien werden von {digit_type[1]} angefahren")
    #print to Terminal
    for n in range(len(mittel_3)):
        print(mittel_3[n])
    return mittel_3

# Task: Mittel 4:
def find_line_crossing(station_area_ds):
    """find all cross sections of all lines

    Args:
        station_area_ds (dict): Dataset with all Stationareas

    Returns:
        crossing_lines (list): A List of all lines with its crossing lines
    """
    crossing_lines = {}
    strab_lines=list_all_strab(station_area_ds)
    for line_source in strab_lines:                                                # define source line to compare with
        for lines_crossing in strab_lines:                                         # check crossing with all others
            if line_source != lines_crossing:                                      # must not be the same
                station_crossing_lines = set()                                     # Set type to avoid multiples
                for station_area_key, station_area in station_area_ds.items():     # check in all stations
                    if "Linien" in station_area:
                        if line_source in station_area.get("Linien"):              # check if line is in station
                            strab_only = []                                        # List type for indexing
                            for element in station_area.get("Linien"):             # erase all non-STRAB
                                if len(element) < 3:
                                    strab_only.append(element)
                            strab_only.remove(line_source)                         # take out source line
                        station_crossing_lines.update(set(strab_only))
                        crossing_lines[line_source] = station_crossing_lines       # assign crossing lines to source line
    #Output
    mittel_4 = ['',
        '=================================',
        'Mittel - 4:',
        'Liste alle Strassenbahnlinien jeweils mit allen Strassenbahnlinien in die man auf ihrem Weg direkt umsteigen kann auf.',
        '']
    for key, element in crossing_lines.items():
        print_temp = sorted(list(map(int,crossing_lines[key])))
        mittel_4.append(f"Linie {key:<4}  kann auf {len(print_temp):<4} Linien umsteigen.Linien: {print_temp}. ")
    #print to Terminal
    for n in range(len(mittel_4)):
        print(mittel_4[n])
    return mittel_4

# Task: Mittel 5:
def find_line_kundencenter(station_area_ds):
    """find all 'Kundencecnter'

    Args:
        station_area_ds (dict): Dataset with all Stationareas

    Returns:
        lines_with_KC, no_kc_lines: List of all lines with 'Kundencenter'. To counter-check also the list which has not
    """
    #Initialize as set (avoid multiples)
    lines_with_KC = set()
    #Go through the stations and search for 'Kundencenter' in 'Verkaufsorte/segment'
    for station_area_key, station_area in station_area_ds.items():
        if len(station_area.get("Verkaufsorte")) > 0:
            for idx in range(len(station_area.get("Verkaufsorte"))):
                if station_area.get("Verkaufsorte")[idx]["Segment"] == "KundenCenter" :
                    if len((station_area.get("Linien"))) > 0:  
                        lines_with_KC.update(set(station_area.get("Linien")))
    #Sort out all STRAB (2 digit lines)
    temp = []
    for element in lines_with_KC: 
        if len(element) < 3:
            temp.append(int(element))
    a = sorted(temp)
    lines_with_KC = list(map(str, a))
    #Get all available STRAB lines for comparison
    trab_lines = list_all_strab(station_area_ds)
    no_kc_lines = list(set(lines_with_KC) ^ (set(trab_lines)))    # ^ = XOR
    #Output
    mittel_5 = ['',
        '=================================',
        'Mittel - 5:',
        'Haben alle Strassenbahnlinien mindestens ein Kundencenter an einer ihrer Haltestellen? Und von welchen Linien ohne Kundencenter kann man mit einmal Umsteigen in eine andere Linie zu einem Kundencenter gelangen.',
        '',
        f"Strassenbahnlinien mit einem Kundencenter an der Station: {lines_with_KC}",
        f"Strassenbahnlinien ohne ein Kundencenter an der Station:{no_kc_lines}",
        f"Wie in Aufgabe Mittel - 4  beschrieben kann Linie {no_kc_lines} auf die entsprechenden Linien mit Kundencenter Umsteigen"]
    #print to Terminal
    for n in range(len(mittel_5)):
        print(mittel_5[n])
    return mittel_5

#===================================================
#  Schwer / Unmenschlich
#===================================================

# Task: Schwer 1a:
def find_closest_sation(station_area_ds, position):
    """Find closest Station
    Args:
        station_area_ds (dict): Dataset with all Stationareas
        position (X/Y): Reference position for distance calculation

    Returns:
        closest_station (list): List of information of the closest station: Name of station, distance in m, lat, lon coordinates
                                
    """
    #Initialize 
    closest_station = ['none',0 ,0 ,0]
    min_distance = float('inf')
    #Outer Loop: Go through all station areas
    for station_area_key, station_area in station_area_ds.items():
        # Make sure there is an entry
        if len(station_area.get("Haltestellen")) > 0:
            #Inner loop: Go through all stops at station area
            for idx in range(len(station_area.get("Haltestellen"))):
                station_gps = station_area.get("Haltestellen")[idx]["Koordinaten"]                                               #Get GPS of stop
                station_gps_in_m = gps_to_m(station_gps)                                                                         #convert to meters
                position_in_m = gps_to_m(position)
                distance = math.sqrt((station_gps_in_m[0]-position_in_m[0]) ** 2 + (station_gps_in_m[1]-position_in_m[1]) **2 )  #Get distance with Pythagoras
                if distance < min_distance:                                                                                      #Overwrite min if smaller than min
                    min_distance = distance
                    closest_station[0] = station_area.get("Haltestellenname")
                    closest_station[1] = distance
                    closest_station[2] = max(station_gps)
                    closest_station[3] = min(station_gps)
    #Output
    schwer_1a = ['',
        '=================================',
        ' Schwer',
        '=================================',
        'Schwer - 1a:',
        'Suche fuer eine eingegebene Position: Die naechste Strassenbahnhaltestelle',
        '',
        f"Position: {position}",
        f"Die naeheste Station ist {closest_station[0]} in {closest_station[1]:.2f} m.",
        f"GPS: Lat/Lon: {closest_station[2]} / {closest_station[3]}"]
    #print to Terminal
    for n in range(len(schwer_1a)):
        print(schwer_1a[n])                
    return schwer_1a 

# Task: Schwer 1b:
def find_closest_sation_with_esc(station_area_ds, position, escalator_malfunction_data):
    """Find closest Station with escelator
    Args:
        station_area_ds (dict): Dataset with all Stationareas
        position (X/Y): Reference position for distance calculation
        escalator_malfunction_data (dict) : Dict of all escalators with a malfunction
    Returns:
        closest_station (list): List of information of the closest station: Name of station, distance in m, lat, lon coordinates
                                
    """
    # initialize 
    closest_station_with_esc = ['none',0 ,0 ,0]
    min_distance = float('inf')
    defect = 0
    #Outer Loop: Go through all station areas with 'Fahrtreppen'
    for station_area_key, station_area in station_area_ds.items():
        if len(station_area.get("Haltestellen")) > 0 and len(station_area.get("Fahrtreppen")) > 0:
            #Inner loop: Go through all stops at station area
            for idx in range(len(station_area.get("Haltestellen"))):
                station_gps = station_area.get("Haltestellen")[idx]["Koordinaten"] 
                station_gps_in_m = gps_to_m(station_gps)
                position_in_m = gps_to_m(position)
                distance = math.sqrt((station_gps_in_m[0]-position_in_m[0]) ** 2 + (station_gps_in_m[1]-position_in_m[1]) **2 )
                if distance < min_distance:
                    min_distance = distance
                    closest_station_with_esc[0] = station_area.get("Haltestellenname")
                    closest_station_with_esc[1] = distance
                    closest_station_with_esc[2] = max(station_gps)
                    closest_station_with_esc[3] = min(station_gps)
                    num_ele = len(station_area.get("Fahrtreppen"))
                    escalator = []
                    # Get all escalators "Kennung" of the station for malfunction association
                    for n in range(len(station_area.get("Fahrtreppen"))):
                        escalator.append(station_area.get("Fahrtreppen")[n]["Kennung"])
    #Go through all malfunction escalators and compare to found ones
    for defect_esc in escalator_malfunction_data:
        for esc_num in escalator:
            if defect_esc.get("properties")["Kennung"] == esc_num:
                defect += 1
    #Output
    schwer_1b = ['',
        '=================================',
        'Schwer - 1b:',
        'Die naechste Strassenbahnhaltestelle mit Fahrtreppen (Stoerung?)',
        '',
        f"Position: {position[0]} / {position[1]}",
        f"Die naeheste Station mit Fahrtreppen ist {closest_station_with_esc[0]} in {closest_station_with_esc[1]:.2f} m.",
        f"Defekte Fahrtreppen: {defect} von {num_ele}",
        f"GPS: Lat/Lon: {closest_station_with_esc[2]} / {closest_station_with_esc[3]}"]
    #print to Terminal
    for n in range(len(schwer_1b)):
        print(schwer_1b[n]) 
    return schwer_1b

# Task: Schwer 1c:
def find_closest_sation_with_ele(station_area_ds, position, elevator_malfunction_data):
    """Find closest Station with elevator
    Args:
        station_area_ds (dict): Dataset with all Stationareas
        position (X/Y): Reference position for distance calculation
        escalator_malfunction_data (dict) : Dict of all elevators with a malfunction
    Returns:
        closest_station (list): List of information of the closest station: Name of station, distance in m, lat, lon coordinates
                                
    """
    # initialize 
    closest_station_with_ele = ['none',0 ,0 ,0]
    min_distance = float('inf')
    defect = 0
    #Outer Loop: Go through all station areas with 'Aufzüge'
    for station_area_key, station_area in station_area_ds.items():
        if len(station_area.get("Haltestellen")) > 0 and len(station_area.get("Aufzüge")) > 0:
            #Inner loop: Go through all stops at station area
            for idx in range(len(station_area.get("Haltestellen"))):
                station_gps = station_area.get("Haltestellen")[idx]["Koordinaten"] 
                station_gps_in_m = gps_to_m(station_gps)
                position_in_m = gps_to_m(position)
                distance = math.sqrt((station_gps_in_m[0]-position_in_m[0]) ** 2 + (station_gps_in_m[1]-position_in_m[1]) **2 )
                if distance < min_distance:
                    min_distance = distance
                    closest_station_with_ele[0] = station_area.get("Haltestellenname")
                    closest_station_with_ele[1] = distance
                    closest_station_with_ele[2] = max(station_gps)
                    closest_station_with_ele[3] = min(station_gps)
                    num_ele = len(station_area.get("Fahrtreppen"))
                    # Get all elevtor "Kennung" of the station for malfunction association
                    elevators = []
                    for n in range(len(station_area.get("Aufzüge"))):
                        elevators.append(station_area.get("Aufzüge")[n]["Kennung"])
    #Go through all malfunction elevators and compare to found ones
    for defect_ele in elevator_malfunction_data:
        for ele_num in elevators:
            if defect_ele.get("properties")["Kennung"] == ele_num:
                defect += 1
    #Output
    schwer_1c = ['',
        '=================================',
        'Schwer - 1c:',
        'Die naechste Strassenbahnhaltestelle mit Aufzuegen (Stoerung?)',
        '',
        f"Position: {position[0]} / {position[1]}",
        f"Die naeheste Station mit Aufzuegen ist {closest_station_with_ele[0]} in {closest_station_with_ele[1]:.2f} m.",
        f"Defekte Fahrtreppen: {defect} von {num_ele}",
        f"GPS: Lat/Lon: {closest_station_with_ele[2]} / {closest_station_with_ele[3]}"]
    #print to Terminal
    for n in range(len(schwer_1c)):
        print(schwer_1c[n])
    return schwer_1c

# Task: Schwer 2
def line_stations(station_area_ds, line, start):
    """Find order of stations for a line (given one endpoint)

    Args:
        station_area_ds (dict): Dataset with all Stationareas
        line (str): The line which shall be shown as route
        start (X/Y): Two dimensional gps coordinate with start/end point of line

    Returns:
        stations (list): A List of all stations a line will approach in order of arrival
    """
    #=====================================
    #Find all Stop for the specified line
    #=====================================
    # All line stations, unsorted
    stations_us = []
    stations = [[start[0], start[1], line]]
    #Outer Loop: Go through all stationareas
    for station_area_key, station_area in station_area_ds.items():
        #Inner Loop: Look at all stops in stationarea
        for stops in range(len(station_area.get("Haltestellen"))):            
            if "Linien" in station_area.get("Haltestellen")[stops]:
                if line in station_area.get("Haltestellen")[stops]["Linien"]:     # find stop of line
                    stations_us.append([max(station_area.get("Koordinaten")), min(station_area.get("Koordinaten")) ,station_area.get("Haltestellenname")])
            #In case there is one station found, if-loop shall be closed to prevent doubles in list (each line has two stops per area, one for each direction)
            break
    #=====================================
    #Sort the Stops of the line in order of nearest distance from each other
    #=====================================
    #Repeat until no station is left
    while len(stations_us) > 0:
        #Loop: Stations along the line
        for stops in stations_us:
            gps_list = []
            #Create a gps list of all remaining (unsorted) stations for comparison
            for n in range(len(stations_us)):
              gps_list.append([stations_us[n][0], stations_us[n][1]])
            #Find closest station to the last point
            next = find_closest_point([stations[-1][0],stations[-1][1]], gps_list)
            #extend sorted list with nearest station
            stations.append(stations_us[next[0]])
            #exclude nearest station from remaining unsorted list
            stations_us.remove(stations_us[next[0]])
    #Output
    schwer_2 = ['',
        '=================================',
        'Schwer - 2:',
        'Koennte man das anhand der Vorgabe einer der beiden Endhaltestellen und den „Entfernungen“ der Haltestellen durch ihre Koordinaten berechnen.',
        '',
        f"Alle Stationen fuer Linie {stations[0][2]} in der Reihenfolge des kuerzesten Abstandes zu einander:"]
    for element in stations:
        schwer_2.append(f"Haltestelle: {element[2]:<30} Koordinaten:{element[0]},{element[1]}")
    #print to Terminal
    for n in range(len(schwer_2)):
        print(schwer_2[n])
    return schwer_2




#===================================================
#  Print to file
#===================================================

def print_to_file(einfach, mittel, schwer):
    with open("output.txt", 'w') as f:
        f.write('Loesungen')
    with open("output.txt", 'a') as f:    
        for n in range(len(einfach)):
            f.write('\n'.join(einfach[n]))
        for n in range(len(mittel)):
            f.write('\n'.join(mittel[n]))
        for n in range(len(schwer)):
            f.write('\n'.join(schwer[n]))
    return ()