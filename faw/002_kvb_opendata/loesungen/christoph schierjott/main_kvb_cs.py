# import modules

import kvb_functions

#===================================================
# Define json file folder (relative) and read all files

json_subdirectory = 'json'
station_area_ds, elevator_malfunction_data, escalator_malfunction_data = kvb_functions.read_files(json_subdirectory)

#===================================================

# Aufgaben

#===================================================
# Leicht
#===================================================

# Leicht 1: calculate number of routes
einfach_1 = kvb_functions.count_routes(station_area_ds)

# Leicht2: calculate station area with highest number of stations
einfach_2 = kvb_functions.most_stops_and_lines(station_area_ds)

# Leicht 3: calculate Fahrtreppen, Aufzüge
einfach_3 = kvb_functions.number_entries(station_area_ds)

# Leicht 4: calculate geometrical maxima
einfach_4 = kvb_functions.corners(station_area_ds)

#===================================================
#  Mittel
#===================================================

# Mittel 1: calculate most stations in station areas per line
mittel_1 = kvb_functions.lines_by_stations(station_area_ds)

# Mittel 2: find line with most DFI on route
mittel_2 = kvb_functions.station_percent(station_area_ds)

#Mittel 3: show all 3 digit lines are BUS, 1 and 2 digits are STRAB
mittel_3 = kvb_functions.assign_lines_type(station_area_ds)

#Mittel 4: List all crossing lines per line
mittel_4 = kvb_functions.find_line_crossing(station_area_ds)

#Mittel 5 List all crossing lines per line
mittel_5 = kvb_functions.find_line_kundencenter(station_area_ds)
#===================================================
#  Schwer
#===================================================

#Schwer 1 
#Possible positions (uncomment one or the input):
position = [50.94122, 6.95671]    # Kölner Dom
#position = [50.93538, 6.95795]     # Heumarkt
#position = [50.961555, 7.0052624]  # Station mit defektem Aufzug
#position[0] = float(input(print(' Gib die Laterale Koordinate ein:')))
#position[1] = float(input(print(' Gib die Longitudinale Koordinate ein:')))
schwer_1a = kvb_functions.find_closest_sation(station_area_ds, position)
schwer_1b = kvb_functions.find_closest_sation_with_esc(station_area_ds, position, escalator_malfunction_data)
schwer_1c = kvb_functions.find_closest_sation_with_ele(station_area_ds, position, elevator_malfunction_data)

#Schwer 2
# Possible starting point and their line (uncomment one pair):
#line = '1'
#start = [50.9404, 6.81588]  # Weiden West, west end of line 1           https://www.vrs.de/lis/linie/de:vrs:1
# or
#line = '5'
#start = [50.93529, 6.95937]  # Heumarkt, South end of line 5            # Apellhofplatz is missing  https://www.vrs.de/lis/linie/de:vrs:5
# or
line = '7'                    
start =  [50.90419,  6.79735]  # Frechen Benzerath, West end of line 7    #  https://www.vrs.de/lis/linie/de:vrs:1
schwer_2 = kvb_functions.line_stations(station_area_ds, line, start)

#===================================================
# Print to file
#===================================================

einfach = [einfach_1, einfach_2, einfach_3, einfach_4]
mittel = [mittel_1, mittel_2, mittel_3, mittel_4, mittel_5]
schwer = [schwer_1a, schwer_1b, schwer_1c, schwer_2]
kvb_functions.print_to_file(einfach, mittel, schwer)


