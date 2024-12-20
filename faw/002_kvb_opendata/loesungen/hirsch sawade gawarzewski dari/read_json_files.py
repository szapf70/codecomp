# Isabell Hirsch
# Alfred Sawade
# Axel Gawarzewski
# Ali Dari

#Daten einlesen

import json
from pathlib import Path
import os

folder_path = (str(Path(__file__).parent.absolute()) + os.sep + "json" + os.sep)


def read_aufzuege():
    """
    read aufzuege.json file from json folder

    :return: dict with data of aufzuege.json
    """
    file_path = folder_path + "aufzuege.json"
    with open(file_path, 'r') as file:
        aufzuege = json.load(file)
        #TODO: unbekannte Zeichen und Umlaute herausfiltern
    return aufzuege


def read_aufzugstoerungen():
    """
    read aufzugstoerungen.json file from json folder

    :return: dict with data of aufzugstoerungen.json
    """
    file_path = folder_path + "aufzugstoerungen.json"
    with open(file_path, 'r') as file:
        aufzugstoerungen = json.load(file)
        #TODO: unbekannte Zeichen und Umlaute herausfiltern
    return aufzugstoerungen


def read_fahrtreppen():
    """
    read fahrtreppen.json file from json folder

    :return: dict with data of fahrtreppen.json
    """
    file_path = folder_path + "fahrtreppen.json"
    with open(file_path, 'r') as file:
        fahrtreppen = json.load(file)
        #TODO: unbekannte Zeichen und Umlaute herausfiltern
    return fahrtreppen 


def read_fahrtreppenstoerungen():
    """
    read fahrtreppenstoerungen.json file from json folder

    :return: dict with data of fahrtreppenstoerungen.json
    """
    file_path = folder_path + "fahrtreppenstoerungen.json"
    with open(file_path, 'r') as file:
        fahrtreppenstoerungen = json.load(file)
        #TODO: unbekannte Zeichen und Umlaute herausfiltern
    return fahrtreppenstoerungen


def read_haltestellen():
    """
    read haltestellen.json file from json folder

    :return: dict with data of haltestellen.json
    """
    file_path = folder_path + "haltestellen.json"
    with open(file_path, 'r') as file:
        haltestellen = json.load(file)
        #TODO: unbekannte Zeichen und Umlaute herausfiltern
    return haltestellen


def read_haltestellenbereiche():
    """
    read haltestellenbereiche.json file from json folder

    :return: dict with data of haltestellenbereiche.json
    """
    file_path = folder_path + "haltestellenbereiche.json"
    with open(file_path, 'r') as file:
        haltestellenbereiche = json.load(file)
        #TODO: unbekannte Zeichen und Umlaute herausfiltern
    return haltestellenbereiche


def read_haltestellenbereichemitdfi():
    """
    read haltestellenbereichemitdfi.json file from json folder

    :return: dict with data of haltestellenbereichemitdfi.json
    """
    file_path = folder_path + "haltestellenbereichemitdfi.json"
    with open(file_path, 'r') as file:
        haltestellenbereichemitdfi = json.load(file)
        #TODO: unbekannte Zeichen und Umlaute herausfiltern
    return haltestellenbereichemitdfi


def read_verkaufsorte():
    """
    read verkaufsorte.json file from json folder

    :return: dict with data of verkaufsorte.json
    """
    file_path = folder_path + "verkaufsorte.json"
    with open(file_path, 'r') as file:
        verkaufsorte = json.load(file)
        #TODO: unbekannte Zeichen und Umlaute herausfiltern
    return verkaufsorte


def add_coordinates_for_station_areas(station_areas, stations):
    """
    For each station area the coordinates are added to the dictionary. 
    For calculation the balance point of the coordinates of the single stations 
    in the station area is used.

    :param station_areas: dict with station area data
    :param stations: dict with stations to read out the koordinates

    :return: station_areas dict with 'koordinaten' for the stations added
    """
    vrsnr_by_short_name = get_station_area_vrsnr_by_short_name(station_areas)
    for station_area in station_areas:
        coordinates = list()
        for station in stations:
            if station_areas[vrsnr_by_short_name[stations[station]['kurzname']]]['haltestellenbereich'] == station_areas[station_area]['haltestellenbereich']:
                coordinates.append(stations[station]['koordinaten'])
        coordinates_count = len(coordinates)
        x_value = sum(x for x,y in coordinates)/coordinates_count
        y_value = sum(y for x,y in coordinates)/coordinates_count
        station_areas[station_area]['koordinaten'] = x_value, y_value


def get_data_for_stations():
    """
    Prepare dict with station releated data. 

    :return: dict with data for stations (by ass:int), properites: "name":str,"kurzname":str,
             "bus":bool (True for bus, False for train),"linien":set of ints,
             "koordinaten":2-value tuple,"fahrtreppen":bool,"Aufzuge":bool, "haltestellenbereich":str
    """ 
    station = {}
    try:
        jason_data=read_haltestellen()
    except Exception as e:
        return f"Ein Fehler ist aufgetreten: {e}"

    for area_data in jason_data['features']:
        station[area_data["properties"]['ASS']]={'name':area_data['properties']['Name'],
        'kurzname':area_data['properties']['Kurzname'],'koordinaten':tuple(area_data['geometry']['coordinates']),
        'linien':set()}

        if area_data['properties'].get('Linien'):
            station[area_data['properties']['ASS']]['linien']=set(area_data['properties']['Linien'].split())


        if 'bus' in area_data['properties']['Betriebsbereich'].lower():
            station[area_data['properties']['ASS']]['bus']=True
        else:
            station[area_data['properties']['ASS']]['bus']=False  
    
    return station


def get_station_areas_with_customer_service():
    """
    Prepare set with station area that have a customer service point. 

    :return: set with station area that have a customer service point
    """       
    try:
        json_data=read_verkaufsorte()
    except Exception as e:
        return f"Ein Fehler ist aufgetreten: {e}"
    
    customer_service = set()
    for store_data in json_data['features']:
        if store_data["properties"]["Segment"] == "KundenCenter":
            customer_service.add(store_data["properties"]["haltestellenbereich"])

    return customer_service


def get_data_for_station_areas():
    """
    Prepare dict with station area releated data. 

    :return: dict with data for station areas (by vrsnummer:int), 
             properites: "haltestellenbereich": int, "haltestellenname":str,
             "kurzname":str, "linien": set of ints, "bus":bool, "strassenbahn":bool,
             "fahrtreppen":bool, "aufzuge":bool, "koordinaten": 2-value tuple,
             "kundencenter":bool, "digitalanzeige":bool, "lageplan":str, 
             "umgebungsplan":str
    """
    station_area = {}

    try:
        jason_data=read_haltestellenbereiche()
        jason_datamitdfi=read_haltestellenbereichemitdfi()
        jason_datamitfahrtreppe = read_fahrtreppen()
        jason_datamitaufzug = read_aufzuege()
        customer_service = get_station_areas_with_customer_service()
    except Exception as e:
        return f"Ein Fehler ist aufgetreten: {e}"

    dfi_set= set()
    fahrtreppen_set = set()
    aufzug_set = set()
    
    for dfi_data in jason_datamitdfi['features']:
        dfi_set.add(dfi_data['properties']['Haltestellenbereich'])

    for fahrtreppen_data in jason_datamitfahrtreppe['features']:
        fahrtreppen_set.add(fahrtreppen_data['properties']['Haltestellenbereich'])

    for aufzug_data in jason_datamitaufzug['features']:
        aufzug_set.add(aufzug_data['properties']['Haltestellenbereich'])

    for area_data in jason_data['features']:
        #TODO: VRSNummer seems not to be unique --> add or replace by Haltestellenbereich? 
        station_area[area_data["properties"]['VRSNummer']]={'haltestellenbereich':area_data['properties']['Haltestellenbereich'],
        'haltestellenname':area_data['properties']['Haltestellenname'],'kurzname':area_data['properties']['kurzname'],'linien':[]}
        if area_data['properties'].get('Linien'):
            station_area[area_data['properties']['VRSNummer']]['linien'] = set(area_data['properties']['Linien'].split())
        if 'bus' in area_data['properties']['Betriebsbereich'].lower():
            station_area[area_data['properties']['VRSNummer']]['bus'] = True
        else:
            station_area[area_data['properties']['VRSNummer']]['bus'] = False
        if 'strab' in area_data['properties']['Betriebsbereich'].lower():
            station_area[area_data['properties']['VRSNummer']]['strassenbahn'] = True
        else:
            station_area[area_data['properties']['VRSNummer']]['strassenbahn'] = False
        if area_data['properties']['Haltestellenbereich'] in dfi_set:
            station_area[area_data['properties']['VRSNummer']]['digitalanzeige']=True
        else:
            station_area[area_data['properties']['VRSNummer']]['digitalanzeige']=False

        if area_data['properties']['Haltestellenbereich'] in fahrtreppen_set:
            station_area[area_data['properties']['VRSNummer']]['fahrtreppen']=True
        else:
            station_area[area_data['properties']['VRSNummer']]['fahrtreppen']=False

        if area_data['properties']['Haltestellenbereich'] in aufzug_set:
            station_area[area_data['properties']['VRSNummer']]['aufzuge']=True
        else:
            station_area[area_data['properties']['VRSNummer']]['aufzuge']=False

        if area_data['properties']['Haltestellenbereich'] in customer_service:
            station_area[area_data['properties']['VRSNummer']]['kundencenter']=True
        else:
            station_area[area_data['properties']['VRSNummer']]['kundencenter']=False

    # TODO: nur da wo daten vorhanden sind einfügen: 'lageplan':area_data['properties']['Lageplan'], 'umgebungsplan':area_data['properties']['Umgebungsplan'],
    return station_area


def get_station_area_vrsnr_by_short_name(station_area_data):
    """
    Link station area short name to the related VRSNumber 

    :param dataset: station area data in a dict with vrsnummer as key, by default data 
    is read fron .json file

    :return: dict with station area short name as key:str and VRSNummer:str as value
    """
    station_area_nr_by_short_name = {}
    for area_data in station_area_data:
        station_area_nr_by_short_name[station_area_data[area_data]['kurzname']]=area_data

    return station_area_nr_by_short_name

def get_station_area_vrsnr_by_area_number(station_area_data):
    """
    Link station area short name to the related VRSNumber 

    :param dataset: station area data in a dict with vrsnummer as key, by default data 
    is read fron .json file

    :return: dict with station area number as key:str and VRSNummer:str as value
    """
    station_area_nr_by_short_name = {}
    for area_data in station_area_data:
        station_area_nr_by_short_name[station_area_data[area_data]['haltestellenbereich']]=area_data

    return station_area_nr_by_short_name

def get_lines_for_buses_and_trains(station_data):
    """
    Prepare dict with lines listed seperatelly for busses and trains.

    :param station_data: data for stations (by ass:int)

    :return: dict with lines devied by keys 'bus' and 'train' 
    """
    lines_for_buses_and_trains = {'bus':set(), 'train':set()}
    for station in station_data:
        if station_data[station]['bus']:
            lines_for_buses_and_trains['bus'].update(station_data[station]['linien'])
        else:
            lines_for_buses_and_trains['train'].update(station_data[station]['linien'])

    return lines_for_buses_and_trains

def get_train_line_data(station_area_data):
    """
    Prepare dict with train line releated data. 

    :param dataset: station area data in a dict with vrsnummer as key, by default data
                    is read from .json file

    :return: dict with train line number as key:str 
             properites: "umsteige_linien":set of str, 
             "kundencenter": set of releated station areas (verkaufsort:int)
             "haltestellen": set of releated station areas (vrsnummer:int)
             "kundenenter_mit_einmal_umsteigen": set of releated lines station areas (vrsnummer:int)
    """
    train_line_data = {}
    for station_area in station_area_data:
        for line in station_area_data[station_area]['linien']:
            crossing_lines = station_area_data[station_area]['linien'].copy()
            crossing_lines.remove(line)
            if not train_line_data.get(line):
                train_line_data[line] = {'umsteige_linien':set(),'kundencenter':False,'haltestellen':set(),'kundenenter_mit_einmal_umsteigen':set()}
            if crossing_lines != None:
                train_line_data[line]['umsteige_linien'].update(crossing_lines,)
            train_line_data[line]['haltestellen'].add(station_area)
        if station_area_data[station_area]['kundencenter']:
            train_line_data[line]['kundencenter']= True

    for line in train_line_data:
        for linie in train_line_data[line]['umsteige_linien']:
            if train_line_data[linie]['kundencenter']:
                train_line_data[line]['kundenenter_mit_einmal_umsteigen'].update(linie)    
    
    #tbd: use a list for "haltestellen" being ordered by distance (--> for task 'schwer')
    return train_line_data

def get_escalator_incidents(station_area_data):
    """
    Prepare dict with train line releated data. 

    :param dataset: station area data in a dict with vrsnummer as key, by default data
                    is read fron .json file

    :return: dict with escalator incidents data for station areas (by vrsnumber:str), 
             value is a dict with escalator 'kennung':str as key and properties 
             'bezeichnung':str, incident 'timestamp':str
    """

    try:
        json_data = read_fahrtreppenstoerungen()
    except Exception as e:
        return f"Ein Fehler ist aufgetreten: {e}"

    escalator_incidents = {}
    vrsnumbers = get_station_area_vrsnr_by_area_number(station_area_data)

    for escalator_data in json_data['features']:
        escalator_incidents[vrsnumbers[escalator_data["properties"]['Haltestellenbereich']]]={'kennung':escalator_data['properties']['Kennung'],
        'bezeichnung':escalator_data['properties']['Bezeichnung'],'timestamp':escalator_data['properties']['timestamp']}
    return escalator_incidents


def get_elevator_incidents(station_area_data):
    """
    Prepare dict with train line releated data. 

    :param dataset: station area data in a dict with vrsnummer as key, by default data
                    is read from .json file

    :return: dict with elevator incidents data for station areas (by vrsnumber:str), 
             value is a dict with elevator 'kennung':str as key and properties 
             'bezeichnung':str, incident 'timestamp':str
    """
    try:
        json_data = read_aufzugstoerungen()
    except Exception as e:
        return f"Ein Fehler ist aufgetreten: {e}"
    
    elevator_incidents = {}
    vrsnumbers = get_station_area_vrsnr_by_area_number(station_area_data)

    for elevator_data in json_data['features']:
        elevator_incidents[vrsnumbers[elevator_data["properties"]['Haltestellenbereich']]]={'kennung':elevator_data['properties']['Kennung'],
        'bezeichnung':elevator_data['properties']['Bezeichnung'],'timestamp':elevator_data['properties']['timestamp']}
    return elevator_incidents