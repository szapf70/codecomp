# import modules

import json
import os
import pandas as pd
import numpy as np
import folium
import itertools
from pprint import pprint
from math import asin, cos, radians, sin, sqrt

# System call
os.system("")

# Class of different styles
class style():
    BLACK = '\033[30m'
    RED = '\033[31m'
    GREEN = '\033[32m'
    YELLOW = '\033[33m'
    BLUE = '\033[34m'
    MAGENTA = '\033[35m'
    CYAN = '\033[36m'
    WHITE = '\033[37m'
    UNDERLINE = '\033[4m'
    RESET = '\033[0m'


def setze_pfad():
    """
    Function: Searching the json folder and change working directory to this folder for data reading

    Args: n.a.
    
    Returns: 
        folderpath (type: string):  name / path of the folder containing the json files, current folder
    """
    
    # get the current working directory
    akt_pfad = os.getcwd()
    # print("Aktueller Pfad:", akt_pfad)
    rel_pfad = akt_pfad.split("\\")[-1]
    # print ("Relativer Pfad:",rel_pfad)

    # checks what to add to the path to get to the json folder
    if (rel_pfad == 'Python'):
        neuer_pfad = r"Coding\\002_kvb_opendata"
        os.chdir(os.getcwd()+"\\"+neuer_pfad)
    #    print (os.getcwd())
    elif (rel_pfad == 'Coding'):
        neuer_pfad = r"002_kvb_opendata"
        os.chdir(os.getcwd()+"\\"+neuer_pfad)
    #    print (os.getcwd())
    elif (rel_pfad == '002_kvb_opendata'):
        neuer_pfad = r"json"
        os.chdir(os.getcwd()+"\\"+neuer_pfad)
    #    print (os.getcwd())

    # get the path to the current folder containing the json files
    folderpath = os.getcwd()

    # print ("Neuer Pfad: ",folderpath, "\n")

    return folderpath


def calc_betriebsbreiche(station_area_ds):
    """
    Function: Derives a list with all names of the "Betriebsbereiche" and their Bus and Strb status 
    
    Args:
        station_area_ds (type: dictionary): the overall data structure
    
    Returns:
    
        betriebsbereiche (set): a tuple with Name, STRAB(bool), BUS(bool), e.g. ('Johannesstr.', True, False)
        counts (dictionary): Total number of Betriebsbereiche with Bus, Strb or both, e.g. ({'BUS': 885, 'STRAB': 231, 'BOTH': 205})
    """
    
    betriebsbereiche = set()
    bb_list = []
    count_bus = 0
    count_strab = 0
    count_both = 0
    for key, station_area in station_area_ds.items():
        if station_area.get('Betriebsbereich'):
            temp = station_area.get('Betriebsbereich')
            strab = False
            bus = False
            while temp != []:
                match temp.pop():
                    case "STRAB":
                        strab = True
                        count_strab += 1
                    case "BUS":
                        bus = True
                        count_bus += 1
            if bus and strab:
                count_both += 1

            betriebsbereiche.add((station_area.get('Haltestellenname'), bus, strab))

            # Alternative Method with a set to avoid duplicates
            bb_list.append((station_area.get('Haltestellenname'), bus, strab))
            bb_set = set(bb_list)
            anz_bus = sum(t[1] for t in bb_set)
            anz_strab = sum(t[2] for t in bb_set)
            if anz_bus != count_bus or anz_strab != count_strab:
                print("\nERROR: Anzahl der Bus- und Strab-Betriebsbereiche stimmen nicht überein")
                print(f"BUS: {anz_bus}, STRAB: {anz_strab}")
                print(f"BUS: {count_bus}, STRAB: {count_strab}")
            
    counts = {"BUS": count_bus, "STRAB": count_strab, "BOTH": count_both}
    return betriebsbereiche, counts


def haltestellenbereich_info(station_area_ds):
    """ 
    Function: Derives a dataframe with infomation of all stations, including their position, elevators, escalator and selling points. 
        
    Args:
        station_area_ds (type: dictionary): the overall data structure
            
    Returns:
       df_haltestellen (type: dataframe): Name, ASS, Lat, Lon, Aufzuege, DFI, Fahrtreppen, Verkaufsorte
       haltestellen_list (type: list): containing a dict in each element
       haltestellen_dict (type: dictionary): key is the No. of Haltestellenbereich / Haltestellenbereichsnummer, e.g. "884"
    """
    
    data = []
    haltestellen_dict = {}
    for mainkey, station_area in station_area_ds.items():
        for haltestelle in station_area['Haltestellen']:
            longitude, latitude = haltestelle['Koordinaten']
           
            data.append(_set := {
                "Haltestellennamen": (_key := station_area_ds[mainkey])["Haltestellenname"],
                "Haltstellenbereichsnummer": mainkey,
                "ASS": haltestelle["ASS"],
                "Latitude": latitude,
                "Longitude": longitude,
                "Aufzuege": len(_key["Aufzüge"]),
                "DFI":  _key["DFI"],
                "Fahrtreppen": len(_key["Fahrtreppen"]),
                "Verkaufsorte":  len(_key["Verkaufsorte"]),
                "Linien": haltestelle.get("Linien", []),
                "Anz Linien": len(haltestelle["Linien"]) if haltestelle.get("Linien") else 0,
            })
                    
            haltestellen_dict[mainkey] = _set

    df_haltestellen = pd.DataFrame(data)
    haltestellen_list = data
    
    return df_haltestellen, haltestellen_list, haltestellen_dict


def calc_max_positions(df):
    """
    Function to claculte the maximum positions out of a prepared dataframe.
        
    Args:
        df_haltestellen (type: dataframe): infos incl. positions
    
    Returns:
        max_positions (type: dictionary): most north, most south, most east, most west bus sations, e.g.
                |  Haltestellenname      |  ASS    |  Latitude    |  Longitude
        ========+========================+=========+==============+===========
        Nord    |  Worringen Hafen       |  50122  |  51.069270   |  6.861210
        Sued    |  Olof-Palme-Allee      |  69004  |  50.705547   |  7.132506
        Ost     |  Bensberg              |  66511  |  50.963470   |  7.161960
        West    |  Frechen-Benzelrath    |  70812  |  50.904020   |  6.797060
    """
    
    h_name_nord = df.iloc[df["Latitude"].idxmax()]["Haltestellennamen"]
    ass_nord    = df.iloc[df["Latitude"].idxmax()]["ASS"].astype(object)    
    lat_nord    = df["Latitude"].max().astype(object)
    lon_nord    = df.iloc[df["Latitude"].idxmax()]["Longitude"].astype(object)    

    h_name_sued = df.iloc[df["Latitude"].idxmin()]["Haltestellennamen"]
    ass_sued    = df.iloc[df["Latitude"].idxmin()]["ASS"].astype(object)
    lat_sued    = df["Latitude"].min().astype(object)
    lon_sued    = df.iloc[df["Latitude"].idxmin()]["Longitude"].astype(object)    

    h_name_ost  = df.iloc[df["Longitude"].idxmax()]["Haltestellennamen"]
    ass_ost     = df.iloc[df["Longitude"].idxmax()]["ASS"].astype(object)
    lat_ost     = df.iloc[df["Longitude"].idxmax()]["Latitude"].astype(object)
    lon_ost     = df["Longitude"].max().astype(object)

    h_name_west = df.iloc[df["Longitude"].idxmin()]["Haltestellennamen"]
    ass_west    = df.iloc[df["Longitude"].idxmin()]["ASS"].astype(object)
    lat_west    = df.iloc[df["Longitude"].idxmin()]["Latitude"].astype(object)
    lon_west    = df["Longitude"].min().astype(object)
    
    # setup a dictionary containing the max positions with name and coordinates
    max_positions_dict = { "Nord": { "Haltestellenname": h_name_nord,
                                "ASS": ass_nord,
                                "Latitude": lat_nord,
                                "Longitude": lon_nord},
                    "Sued"  : { "Haltestellenname": h_name_sued,
                                "ASS": ass_sued,
                                "Latitude": lat_sued,
                                "Longitude": lon_sued},
                    "Ost"   : { "Haltestellenname": h_name_ost,
                                "ASS": ass_ost,
                                "Latitude": lat_ost,
                                "Longitude": lon_ost},
                    "West"  : { "Haltestellenname": h_name_west,
                                "ASS": ass_west,
                                "Latitude": lat_west,
                                "Longitude": lon_west}}
      
    # create a data frame from the dictionary with orient='index' to transpose
    df_max_pos = pd.DataFrame.from_dict(max_positions_dict)

    return df_max_pos, max_positions_dict


def create_html_map(df, filename):
    """ 
    Function to build the html file "max_positions.html" showing a map of the maximum positions out of a prepared dataframe.
    
    Args: 
        df(type: dataframe): with infos incl. position coodinates "Latitude" and "Longitude"
        filename (type: string): name of the html file
    
    Returns: 
        none
    """
    
    map = folium.Map(location=[50.9417834179503, 6.95781192779762], zoom_start=10)
    
    if filename.split(".")[-1] != "html":
        filename = filename+".html"
    
    if 'Latitude' not in df.columns:
        for column in df.columns:
            # print (row)
            latitude = df.loc["Latitude",column]
            longitude = df.loc["Longitude",column]
            haltestelle = df.loc["Haltestellenname", column]
            ass = df.loc["ASS",column]
            kennung = column+"\n"+haltestelle+" - "+str(ass)
            # kennung = str(ass)
            icon = folium.Icon(color='red', icon='info-sign')

            # print ("\nlat:",latitude,"lon:",longitude,"Kennung:",kennung)
            folium.Marker(location=[latitude, longitude], popup=kennung, icon=icon).add_to(map)
            
    elif 'Latitude' in df.columns:
        for idx, row in df.iterrows():
            # print (row)
            haltestelle = row["Haltestellennamen"]
            latitude = row["Latitude"]
            longitude = row["Longitude"]
            ass = row["ASS"]
            
            # Error treatment for empty lists in Linien
            if row["Linien"]==[]:
                row["Linien"] = [[]]
                
            if (len((row["Linien"])[0]) >= 2):
                _txt = "Bus"
                icon = folium.Icon(color='blue', icon='info-sign') 
            else:
                _txt = "Strab"
                icon = folium.Icon(color='red', icon='info-sign')   
            folium.Marker(location=[latitude, longitude], popup=haltestelle+"\n"+_txt+" - "+str(ass), icon=icon).add_to(map)
    
    akt_pfad = os.getcwd()
    print (style.YELLOW)
    print(f'New map file {filename} created. Go to {akt_pfad} to find the file!\n')
    print (style.WHITE)
    map.save(filename)


def linien_info(station_area_ds):
    """
    Function: Generates the infomation for all lines with their stops, number of DFIs, number of treppen and number of aufzuege  

    Args:
        station_area_ds (type: dictionary): the overall data structure

    Returns:
        linien_dict (type: dictionary): list of all lines (type: int) and a list of their stops (type: dictionary), No of stops, No of DFI, No of treppen and No of aufzuege
        df_linien (type: dataframe):  tranlated linien_dict to a dataframe. The list of stops is converted to a list with strings
    """
    linien_dict = {}

    for key, station_area in station_area_ds.items():
        haltestellen_namen = station_area.get('Haltestellenname')
        vrsnummer = station_area.get('VRSNummer')
        linien = station_area.get('Linien')
        dfi    = station_area.get('DFI')
        aufzuege = len(station_area.get("Aufzüge"))
        treppen  = len(station_area.get("Fahrtreppen"))
        if not linien:
            continue
        for linie in linien:
            linie = int(linie)
            if linie not in linien_dict:
                linien_dict[linie] = {'Haltestellen': [], 'VRSNummer': [], 'DFI': 0, 'Treppen': 0, 'Aufzuege': 0, 'No_of_Haltestellen': 0}
            linien_dict[linie]['Haltestellen'].append(haltestellen_namen)
            linien_dict[linie]['VRSNummer'].append(vrsnummer)
            linien_dict[linie]['DFI'] += dfi
            linien_dict[linie]['Treppen'] += treppen
            linien_dict[linie]['Aufzuege'] += aufzuege
            linien_dict[linie]['No_of_Haltestellen'] = len(linien_dict[linie]['Haltestellen'])   # Wert wird jedes Mal überschrieben
                         
    df_linien = pd.DataFrame([{'Linie': linie, 'Haltestellen': info['Haltestellen'], 'VRSNummer': info['VRSNummer'],
                               'No_of_Haltestellen': info['No_of_Haltestellen'],
                               'DFI': info['DFI'], 'Treppen': info['Treppen'], 'Aufzuege': info['Aufzuege']} #, 'Haltstellenbereichsnummer': key}
                            for linie, info in linien_dict.items()])
     
    return linien_dict, df_linien
    

def aufzuege_info(station_area_ds):
    """
    Function: Generates the information for all elevators, incl, name, haltestellenname, latitude and longitude
    
    Args:
        station_area_ds (type: dictionary): the overall data structure
        
    Returns:
        df_aufzuege (type: dataframe): Name, Bezeichnung, Haltestellenname, Latitude, Longitude
        aufzuege_list (type: list): containing a dict in each element    
    """

    data = []

    for key, station_area in station_area_ds.items():
        haltestellenname = station_area.get('Haltestellenname')
        if station_area.get('Aufzüge'):
            for aufzug in station_area.get('Aufzüge'):
                longitude, latitude = aufzug['Koordinaten']

                data.append({
                    "Kennung": aufzug.get('Kennung'),
                    "Bezeichnung": aufzug.get('Bezeichnung'),
                    "Haltestellenname": haltestellenname,
                    "Latitude": latitude,
                    "Longitude": longitude,
                })


    df_aufzuege = pd.DataFrame(data)
    aufzuege_list = data
    
    return df_aufzuege, aufzuege_list 


def treppen_info (station_area_ds):
    """
    Function: Generates the information for all stairs, incl, name, haltestellenname, latitude and longitude
    
    Args:
        station_area_ds (type: dictionary): the overall data structure
        
    Returns:
        df_treppe (type: dataframe): Name, Bezeichnung, Haltestellenname, Latitude, Longitude
        treppen_list (type: list): containing a dict in each element
            
    """

    data = []

    for key, station_area in station_area_ds.items():
        haltestellenname = station_area.get('Haltestellenname')
        if station_area.get('Fahrtreppen'):
            for treppe in station_area.get('Fahrtreppen'):
                longitude, latitude = treppe['Koordinaten']

                data.append({
                    "Kennung": treppe.get('Kennung'),
                    "Bezeichnung": treppe.get('Bezeichnung'),
                    "Haltestellenname" : haltestellenname,
                    "Latitude": latitude,
                    "Longitude": longitude,                
                })

    df_treppe = pd.DataFrame(data)
    treffen_list = data
    
    return df_treppe, treffen_list


def most_common_elements(linien_dict):
    """Function generates a list of tuples containing the pairs of lines with the most common stops

    Args:
        linien_dict (tape: dictionary): info generated by linien_info, 

    Returns:
        common_stops_list (type: list):   list of tuples containing the pairs of lines,
                                the number of common stops the 
                                a sez with the names of the common stops
    """

    # Liste, um die Ergebnisse zu speichern
    common_stops_list = []
    
    # Alle möglichen Paare von Linien vergleichen
    for (linie1, haltestellen1), (linie2, haltestellen2) in itertools.combinations(linien_dict.items(), 2):
        common_stops    = set(haltestellen1["Haltestellen"]) & set(haltestellen2["Haltestellen"])
        common_elements = len(common_stops)
        if common_elements == 0:
            continue
        common_stops_list.append(((int(linie1), int(linie2)), common_elements, common_stops))

    return common_stops_list


def list_of_changeovers(results):
    """ function generates a dictionary with lines and lists of crossing lines

    Args:
        results (type_ list): List of tuples containing the pairs of lines

    Returns:
        matrix (type: dictionary): keys are lines and values are lists of crossing lines
    """
    matrix = {}
    # Sortiere die Ergebnisse nach der Anzahl der gemeinsamen Haltestellen
    results.sort(key=lambda x: x[1], reverse=True)
    print("Die Linien mit den meisten gemeinsamen Haltestellen sind:")
    for (linie1, linie2), common_elements, common_stops in results:
        if common_elements == 0:
            continue
        if linie1 not in matrix:
            matrix[linie1] = []
        if linie2 not in matrix:
            matrix[linie2] = []
        matrix[linie1].append(linie2)
        matrix[linie2].append(linie1)

        # common_stops_str = ", ".join(common_stops)
        # print(f"Linie {linie1} und Linie {linie2} haben {common_elements} gemeinsame Haltestellen:")
        # print(f"Umsteigemöglichkeiten: {common_stops_str}\n")
    
    return matrix


def customer_center(station_area_ds, line_type):
    """ function generates a dictionary with lines and lists of crossing lines

        Args:
            station_area_ds (type: dictionary): the overall data structure

    Returns:
        _type_: _description_
    """
    list_of_customer_center = []
    lines_with_customer_center = set()
    digits = set()
    digits = (1, 2) if line_type == "strab" else (3)
    items = []

    for key, station_area in station_area_ds.items():
        
        # if len(key) in digits:
            if station_area.get('Verkaufsorte'):
                VO = station_area.get('Verkaufsorte')
                for verkaufsort in VO:
                    if verkaufsort["Segment"] == 'KundenCenter':
                        Haltestellenname = station_area.get('Haltestellenname')
                        Linien           = station_area.get('Linien')
                        for linie in Linien:
                            if len(linie) in digits:
                                items.append(linie)
                                lines_with_customer_center.add(int(linie)) 
                        list_of_customer_center.append((Haltestellenname, items))
                        items = []

                        #for linie in Linien:
                        #    lines_with_customer_center.add(int(linie))
                           
    return list_of_customer_center, lines_with_customer_center

    
def changeover_to_lines_with_customer_center(matrix, lines_with_customer_center, lines_wo_customer_center):
    """_summary_

    Args:
        matrix (type: dictionary): keys are lines and values are lists of crossing lines
        lines_with_customer_center (type: set): a set of lines with a customer center
        lines_wo_customer_center (type:set): a set of lines without a customer center
        
    Returns:
    """
    
    changeover_to_lines_wcc = {}

    for linie in matrix.keys():
        if linie in lines_wo_customer_center:
            # linie aus Matrix suchen und die Partner linien als set ablegen
            intersection = set(matrix[linie]).intersection(lines_with_customer_center)
            if intersection:
                changeover_to_lines_wcc[linie] = intersection
    
    return changeover_to_lines_wcc         


def digitale_fahrgastinformation(df_linien):
    """
    function calculates the relative DFI, Treppen and Aufzuege and append them to the dataframe
    
    Args:
        #linien_dict (type: dictionary): keys are lines and values are dictionaries of haltestellen
        df_linien (type: dataframe): Name, ASS, Lat, Lon, Aufzuege, DFI, Fahrtreppen, Verkaufsorte

    Returns:
        df_linien (type: dataframe): Name, ASS, Lat, Lon, Aufzuege, DFI, Fahrtreppen, Verkaufsorte
    """
        
    df_linien["rel_DFI"] = df_linien["DFI"].div(df_linien["No_of_Haltestellen"]).replace(np.inf, 0)
    df_linien["rel_Treppen"] = df_linien["Treppen"].div(df_linien["No_of_Haltestellen"]).replace(np.inf, 0)
    df_linien["rel_Aufzuege"] = df_linien["Aufzuege"].div(df_linien["No_of_Haltestellen"]).replace(np.inf, 0)
    
    return df_linien


def check_number_assumption(betriebsbereiche, linien_dict, df_linien):
    """ Function validates the assumption of one, two or three digits in the line number correlates to busses or straßenbahn
        
    Args:
        betriebsbereiche (type: dataframe): Name, ASS, Lat, Lon, Aufzuege, DFI, Fahrtreppen, Verkaufsorte 
        linien_dict (type: dictionary): keys are lines and values are dictionaries of haltestellen   
        df_linien (type: dataframe): Name, ASS, Lat, Lon, Aufzuege, DFI, Fahrtreppen, Verkaufsorte
    
    """
    # Zu prüfen: Haben alle Haltstellenbereiche einer ein- oder zweistellige Nummer eine STRAB?
    # Und haben alle Haltestellenbereiche einer dreistelligen Linien-Nummer eine BUS?
    
    assumption = True
    
    # Erstelle ein temporäres DataFrame mit den Betriebsbereichen und jeweils dem Flag STRAB und BUS
    df1 = pd.DataFrame(betriebsbereiche)
    df1.columns = ['Name', 'BUS', "STRAB"]
    
    # Iteriere durch alle Linien
    for linie in linien_dict.keys():
        
        # Definiere das zu prüfende Argument bei dreistelligen Linien BUS, sonst STRAB
        arg = "STRAB" if len(str(linie)) < 3 else "BUS"
        
        # Iteriere durch alle Haltestellen der Linie
        haltestellen = df_linien.loc[df_linien['Linie'] == linie]["Haltestellen"].tolist()[0]
        for haltestelle in haltestellen:
            # Wenn eine Haltestelle das zu prüfende Argument nicht hat, dann ist die Annahme falsch
            if not df1.loc[df1["Name"] == haltestelle].iloc[0][arg].astype(object):
                print(f"Die Linie {linie} hat an der Haltestelle {haltestelle} hat keine(n) {arg}")
                assumption = False
                
    return assumption


def calc_distance(pos1, pos2):
    """ function to calculate the simple distance of two position with its coordinate 
    Args:
        pos1 (_type_): _description_
        pos2 (_type_): _description_
    Returns:
        dist (type: float):  distance apprimately in kilometers
    """
    delta_lat = (pos1[0]-pos2[0])*111  # Distance between two degrees of latitude in the area of Cologne 
    delta_lon = (pos1[1]-pos2[1])*70   # Distance between two degrees of longitude in the area of Cologne
    dist = sqrt(delta_lat*delta_lat + delta_lon * delta_lon)
    
    return dist
    
 
def search_nearest(location, df):
    """ Getting the index of a dataframe, and hence a location which is the closest distance to the provided input position.capitalize()
    
    Args:
        location (type: tuple): Tuple containing the coordinates, 1st position is latitude, 2nd is longitude
        df (type: dataframe):   Containing 
        
    Returns:
        min_idx (type: int):    Index in the dataframe giving the location of the closest distance 
    
    """
   
    distances_list = []
    min_idx = 0
    min_distance = float('inf')
    
    # creating an array of extracted coordinates
    extracted_positions = df[["Latitude", "Longitude"]].values

    for (idx, position) in enumerate(extracted_positions):
        # idx is a counter not the index in the dataframe!

        dist = haversine_distance(location, position, compare=False)
               
        if dist < min_distance:
            min_distance = dist
            min_idx = idx
            # dist_old = calc_distance(location, position)
            # print (f'Difference to the plane world distance: {round( (dist - dist_old)*1000,1) } in meters')        
            
        distances_list.append(dist)
      
    nearest = min(distances_list)
               
    return min_idx


def transport(daten, transportmittel):
    """ Funktion erzeugt eine Liste und ein Dataframe, das die Informationen für
        die Kennung, die Bezeichnung den Haltestellenbereich und die Koordinaten der Haltestellen enthaelt. 
        
        Args: Der Name einer zu untersuchendenen Datei ohne die Endung .json
        
        Ausgabe: Die Liste und das Dataframe
        """
    # df = pd.DataFrame(columns=["Kennung", "Bezeichnung", "Haltestellenbereich", "Longitude", "Latitude"])
    data= []
    for feature in daten[transportmittel+".json"]["features"]:
        Kennung = feature["properties"]["Kennung"]
        Bezeichnung = feature["properties"]["Bezeichnung"]
        Haltestellenbereich = feature["properties"]["Haltestellenbereich"]  
        geometry = feature["geometry"]["coordinates"]    
        data.append({"Kennung": Kennung, "Bezeichnung": Bezeichnung, "Haltestellenbereich": Haltestellenbereich,
                     "Longitude": float(geometry[0]), "Latitude": float(geometry[1]),
                     "Index": transportmittel
                     })
    
    df = pd.DataFrame(data)

    return df, data


def dateneinlesen():
    """
    Diese Funktion liest die Daten aus den Json-Dateien im Ordner json ein.

    Alle Json-Dateien im aktuellen Ordner werden eingelesen und in einem
    Dictionary abgelegt. Der Key des Dictionarys ist der Dateiname der
    Json-Datei.
    
    Args: n.a.
    
    Returns: 
        daten (type: dictionary):  Dictionary with content of all json files
    
    """
    
    folderpath = setze_pfad()
    
    daten = {}
    for filename in os.listdir(folderpath):
        if filename.endswith(".json"):
            # print (filename)
            with open(filename, 'r', encoding='latin-1') as file:
                falsch_kodiert = file.read()
                try:
                    richtig_kodiert = falsch_kodiert.encode('latin-1').decode('utf-8')
                except:
                    richtig_kodiert = falsch_kodiert
               
                daten[filename] = json.loads(richtig_kodiert)

    return daten


def haltestellenbereichemitdfi(daten):
    """ function gets all haltestellenbereiche with dfi and generats a set
    
    Args:
        daten (type: dictionary):  Dictionary with content of all json files

    Returns:
        hb_mitdfi (type: set):     Set with all haltestellenbereiche with dfi        
    """
    
    hb_mitdfi = set()
    
    for item in daten['haltestellenbereichemitdfi.json']['features']:
        hb_mitdfi.add(item['properties'].get('Haltestellenbereich'))

    return hb_mitdfi


def check_defect(type_to_check, position, idx_nearest, nearest_item, df, df_defect):
    """ check if the nearest item is a defect item. If so, delete it from the dataframe and find the new nearest item. 
    
    Args:
        type_to_check (type: string): name of the transportmittel to check
        position (type: list): current position of the user
        idx_nearest (type: int): index of the nearest item        
        nearest_item (type: string): name of the nearest item
        df (type: df): dataframe with all stops
        df_defect (type: df): dataframe with all defects
        
    Returns:    
        no returns                             
        """
    nearest = df.iloc[idx_nearest]['Kennung']
    print(f"\nDer {type_to_check}, der am nächsten liegt:\n{df.iloc[idx_nearest][0:3]}")
    while nearest_item in df_defect["Kennung"].values:
        print(f"\n{type_to_check} is defect")
        
        # get the index of the row where 'Kennung' is the specified value
        index = df[df["Kennung"] == nearest].index
        
        # remove the row with the given index from the data frame
        df = df.drop(index)
        
        idx_nearest = search_nearest(position, df)
        nearest_item = df.iloc[idx_nearest]['Kennung']
        print(f"\ncheck next {type_to_check}:\n{df.iloc[idx_nearest][0:3]}")
    # refreh df_aufzuege dataframe


def split_linien_dict(dict):
    """ split the dictionary lines to Straßenbahnlinie and Buslinie
    
    Args:
        dict (type: dict): complete line dictionaey with all kind of lines 
        
    Returns:
        bus_dict (type: dict): dictionary with bus lines (subset of dict)
        strab_dict (type: dict): dictionary with straßenbahn lines (subset of dict)
               
    """
    strab_dict = {}
    bus_dict = {}
    for linie in dict.keys():
        if len(str(linie)) < 3:
            strab_dict.update({linie: dict[linie]})
        else:
            bus_dict.update({linie: dict[linie]})

    return strab_dict, bus_dict


def haversine_distance(pos1, pos2, unit="km", compare=False):
    """ calculate the distance between two position

    Args:
        pos1 (type: tuple): _description_
        pos2 (type: tuple): _description_
        unit (type: str, optional): unit of the distance. Defaults to "km".
        compare type: (bool, optional): flag to compare haversine with flat . Defaults to False.

    Returns:
        dist (type: float): distance between the two position
    """
    # Approximate radius of Earth in kilometers
    rad = 6371

    lat1, lon1 = pos1
    lat2, lon2 = pos2

    # Locations of Oslo and Vancouver
    phi1, lambda1 = radians(lat1), radians(lon1)
    phi2, lambda2 = radians(lat2), radians(lon2)

    # Distance between Oslo and Vancouver
    dist = 2 * rad * asin(sqrt(sin((phi2 - phi1) / 2) ** 2
                               + cos(phi1) * cos(phi2) * sin((lambda2 - lambda1) / 2) ** 2))

    simple_dist = calc_distance(pos1, pos2)
    if unit == "m":
        dist = dist * 1000
        simple_dist = simple_dist * 1000

    if compare:
        print(f'Haversine Distance [{unit}]: {dist:.3f}')
        print(f'Simple Distance [{unit}]: {simple_dist:.3f}')
        print(f'Difference [{unit}]: {(dist - simple_dist):.1f}\n')

    return dist


def stops_in_sequence(endhaltestelle, linie, df_hs, df_linien):
    """ determine the stops of a given line in sequence

    Args:
        endhaltestelle (type: str): name of one endhaltestelle
        linie (type: int):          the number of the line
        df_hs (type: df):           list of all stops with their averaged coordinates (and more)
        df_linien (type: df):       list of all lines with their unsorted stops

    Returns:(
        sorted_haltstellen (type: list):   sorted sequence of all stops from the the given linie
    """
    
    # get the coordinates of the endhaltestelle
    lat_end = df_hs.loc[df_hs["Haltestellennamen"] == endhaltestelle]["Latitude"].values[0].astype(object)
    lon_end = df_hs.loc[df_hs["Haltestellennamen"] == endhaltestelle]["Longitude"].values[0].astype(object)
    pos_endhaltestelle = (lat_end, lon_end)
    
    # get the coordinates of the first stop the search starts
    pos_last = pos_endhaltestelle

    # initealize the sorted list of the stops, starting with the endhaltestelle 
    sorted_haltestellen = [endhaltestelle]
    
    # get the stops of the given line and remove the endhaltestelle
    haltestellen = df_linien.loc[df_linien['Linie'] == linie]["Haltestellen"].tolist()[0]
    haltestellen.remove(endhaltestelle)
    
    # get the length of the haltestellen list (add +1 for the removed endhaltestelle)
    length_haltestellen = len(haltestellen)+1 
    
    # find the nearest haltestelle until the length of the sorted list is equal to the length of the haltestellen list
    while len(sorted_haltestellen) != length_haltestellen:
        
        # initealize the min_distance and min_idx
        min_distance = float('inf')
        min_idx = -1
        
        # iterate through the haltestellen list
        for idx, item in enumerate(haltestellen):

            lat = df_hs.loc[df_hs["Haltestellennamen"] == item]["Latitude"].values[0].astype(object)
            lon = df_hs.loc[df_hs["Haltestellennamen"] == item]["Longitude"].values[0].astype(object)
            pos_next = (lat, lon)

            # calculate the distance between the next haltestelle and the last haltestelle
            dist = haversine_distance(pos_next, pos_last, compare=False)
            
            # update the min_distance and min_idx
            if dist < min_distance:
                min_distance = dist
                min_idx = idx
  
        # get the nearest haltestelle from the haltestellen list
        nearest_haltestelle = haltestellen[min_idx]

        # remove the nearest haltestelle from the haltestellen list and add it to the sorted list
        haltestellen.remove(nearest_haltestelle)
        sorted_haltestellen.append(nearest_haltestelle)
        
        # update the position of the last haltestelle for the next iteration
        lat = df_hs.loc[df_hs["Haltestellennamen"] == nearest_haltestelle]["Latitude"].values[0].astype(object)
        lon = df_hs.loc[df_hs["Haltestellennamen"] == nearest_haltestelle]["Longitude"].values[0].astype(object)
        pos_last = (lat, lon)

    # return the sorted list
    return sorted_haltestellen
        
    
def find_stop_with_max_lines(df_haltestellen):
    """ Function to find the haltestelle with the most lines

    Args:
        df_haltestellen (type: dataframe): infos of the haltestellen incl. number of lines

    Returns:
        haltestellenname (type: string): 
        max_anz (type: int):
    """
    
    # group the dataframe by Haltestellennamen and add lines for one group
    df_temp = df_haltestellen.groupby('Haltestellennamen')['Linien'].agg(list)
    max_anz = 0
    for name, item in df_temp.items():
        all_items = set(list(itertools.chain(*item)))  # it groups all the iterables together and produces a single iterable as output
        if len(all_items) > max_anz:
            max_anz = len(all_items)
            haltestellenname = name
            
    return haltestellenname, max_anz


def get_position_from_df(df, haltestellenname):
    """ Function to get the coordinates of a haltestelle from a prepared dataframe.
        
        Args:    
            df_haltestellen (type: dataframe): infos incl. positions    
            haltestellenname (type: string): name of the haltestelle

        Returns:
            tuple with
            lat (type: float): latitude of the haltestelle
            lon (type: float): longitude of the haltestelle 
            
        """
    lat = df.loc[df["Haltestellennamen"] == haltestellenname]["Latitude"].values[0].astype(object)
    lon = df.loc[df["Haltestellennamen"] == haltestellenname]["Longitude"].values[0].astype(object)

    return (lat, lon)


def print_line_with_sorted_stops(sorted_haltestellen, linie, endhaltestelle, df_haltestellen, map = True):
    """
    Function to print the stops of a given line in sequence.
    
    Args:
        sorted_haltestellen (type: list): sorted sequence of all stops from the the given linie
        linie (type: int): the number of the line    
        endhaltestelle (type: string): the name of the endhaltestelle
        df_haltestellen (type: dataframe): infos incl. positions    
        map (type: boolean): if True, the map will be created

    Returns:
        None
    """   
    
    df_sequence = pd.DataFrame(columns= (spalten := ['Haltestellennamen', 'Latitude', 'Longitude', 'ASS', 'Linien']))
    
    print(f'\nThe stops of line {linie} in sequence, started with {endhaltestelle}: \n')
    previuos_item = endhaltestelle
    unit = "m"
    for idx, item in enumerate(sorted_haltestellen):
        pos_1 = get_position_from_df(df_haltestellen, item)
        pos_2 = get_position_from_df(df_haltestellen, previuos_item)
        dist =  haversine_distance(pos_1, pos_2, unit=unit, compare=False)
        print(f'{item}{" - Distance to previous stop ".rjust(60 -len(item))}{dist:.1f} [{unit}]')
        previuos_item = item
        # with additional information for map creation 
        _txt = 'Stop ' + str(idx) +' Distance to Stop ' + str(idx-1)+': '+ str(round(dist,1))+unit
        new_row = pd.DataFrame([[item, pos_1[0], pos_1[1], _txt, [str(linie)]]], columns= spalten)
        df_sequence = pd.concat([df_sequence, new_row], ignore_index=True)
    
    if map:
            create_html_map(df_sequence, "Linie_" + str(linie) + ".html")
                        
    return


def group_df_haltestellen(df_haltestellen):
    """ Function to group the dataframe by Haltestellennamen and add lines for one group
    
    Args:
        df_haltestellen (type: dataframe):  infos of the haltestellen incl. number of lines

    Returns:
        df_hs_grouped (type: dataframe):    dataframegrouped by Haltestellennamen 
    """
    
    df_hs_grouped= df_haltestellen.groupby('Haltestellennamen').agg({
    'Haltestellennamen': 'first',
    'Haltstellenbereichsnummer': 'first',
    'ASS': list,
    'Latitude': 'mean', 
    'Longitude': 'mean',
    'Aufzuege': 'first',
    'DFI': 'first',
    'Fahrtreppen': 'first',
    'Verkaufsorte': 'first',
    'Linien': lambda x: list(x.iloc[0]),
    'Anz Linien': 'first'   
    }).reset_index(drop=True)
    
    return df_hs_grouped


def find_haltestelle_with_max_ass(df_hs_grouped):
    """ Function to find the haltestelle with the most ASS
    
    Args:        
        df_hs_grouped (type: dataframe):    dataframegrouped by Haltestellennamen 

    Returns:
        haltestellenname (type: string):    name of the haltestelle with the most ASS
        max_ass_wert (type: int):           number of ASS of the haltestelle with the most ASS    
    """
    max_ass_wert = df_hs_grouped['ASS'].apply(len).max()
    haltestellenname = df_hs_grouped.loc[df_hs_grouped['ASS'].apply(len).idxmax()].Haltestellennamen

    return haltestellenname, max_ass_wert


def find_highest_value_of_feature(df_linien, feature):
    """ function findes the highest relative values of a given feature

    Args:
        df_linien (type: dataframe):    dataframe with the information for all lines 
        feature (type: string):         feature

    Returns:
        line_w_max_rel_feature (type: int):   number of line
        max_values (type: int):               highest number of feature
        rel (type: float ):                   highest relative number of feature                
        
    """
    
    # In case of multiple maxima, one should use the following code instead
    # max_idx = df_linien[rel_feature].eq(df_linien[rel_feature].max())
    # max_idx = max_idx.loc[max_idx].index

    
    rel_feature = "rel_" + feature
    line_w_max_rel_feature = df_linien.iloc[df_linien[rel_feature].idxmax()]["Linie"].astype(object)
    max_values = (_arg := df_linien.loc[df_linien["Linie"] == line_w_max_rel_feature]).iloc[0][feature].astype(object)
    rel = _arg.iloc[0][rel_feature].astype(object)
    
    return line_w_max_rel_feature, max_values, rel

# Dateiende