#python
import json
import pprint
import numpy
import scipy
import math

def Data_manage(file,mykey,myvalue):
    '''
    The main funtion to handel different input files;
    Only targeted items are stored in the dictionary ;
    Data are stored in a dictionary and returned;
    
    file - file name, all json files are got from a sub-dir called "json";
    mykey - parameter for getting the key of the dict, read from file;
    myvalue - parameter(s) for the value the the dict, read from file
    
    '''

    with open(file, 'r') as inp:
        data = json.load(inp)

    mydict = {}
    for feature in data.get('features', []):
        geometry = feature.get('geometry', {})
        properties = feature.get('properties', {})
        Data = {
            "coordinates" : geometry.get('coordinates', []),
            "Kennung" : properties.get('Kennung',""),
            "Haltestellenbereich" : properties.get('Haltestellenbereich',""),
            "haltestellenbereich" : properties.get('haltestellenbereich',""),
            "timestamp" : properties.get('timestamp' ,""),
            "Name" : properties.get('Name',""),
            "Betriebsbereich" : properties.get('Betriebsbereich' ,""),
            "Linien" : properties.get('Linien',""),
            "Haltestellenname" : properties.get('Haltestellenname' ,""),
            "ASS" : properties.get('ASS' ,""),
            "Segment" : properties.get('Segment',"")
        }
        mylist = []
        for item in myvalue:
            mylist.append(Data.get(item))
        mydict.setdefault(Data.get(mykey),[]).extend(mylist)
    return mydict

aufzuege_dict=Data_manage('aufzuege.json', "Haltestellenbereich", ("coordinates","Kennung"))
aufzugstoerungen_dict=Data_manage('aufzugstoerungen.json', "Haltestellenbereich", ("Kennung","timestamp"))
fahrtreppen_dict=Data_manage('fahrtreppen.json', "Haltestellenbereich", ("coordinates","Kennung"))
fahrtreppenstoerungen_dict=Data_manage('fahrtreppenstoerungen.json', "Haltestellenbereich", ("Kennung","timestamp"))
haltestellen_dict=Data_manage('haltestellen.json', "Name", ("Betriebsbereich","ASS","Linien","coordinates"))
haltestellenbereiche_dict=Data_manage('haltestellenbereiche.json', "Haltestellenname", ("Haltestellenbereich","Betriebsbereich","Linien","VRSNummer"))
haltestellenbereichemitdfi_dict=Data_manage('haltestellenbereichemitdfi.json', "Haltestellenbereich", ())
verkaufsorte_dict=Data_manage('verkaufsorte.json', "haltestellenbereich", ("Segment",))
# coordinates_halt_dict=Data_manage('haltestellen.json', "coordinates", ("Name","Betriebsbereich","ASS","Linien"))
# verkaufsorte_kundercenter_set={key for key, value in verkaufsorte_dict.items() if "KundenCenter" in value}

# pprint.pprint(haltestellen_dict)

# =========================================================================================================

def Linien(dict):
    """
    Linien Funtion:     filter all the Linien and seperate them into STRB and BUS

    Input:              haltestellenbereiche_dict (ouput from Data_manage function)

    return:             STRB_Linien - [list] / Bus_Linien - [list]  
    """

    linienList_all = []
    STRB_Linien = []
    Bus_Linien = []

    linienList = []
    for key in dict.keys():
        linienList.append(dict[key][2].strip().split(" "))

    for item in linienList:
        for i in item:
            if i:
                linienList_all.append(int(i))
                
    linienList_all = set(linienList_all) 

    for item in linienList_all:
        if item < 100:
            STRB_Linien.append(item)
        if item >= 100:
            Bus_Linien.append(item)


    return linienList_all, STRB_Linien, Bus_Linien

# =========================================================================================================

def Haltestellenbereich_meisten_Haltestellen (dict):
    """
    function:   find which "Haltestellenbereich" has most "Haltestellen"
    input:      haltestellen_dict
    output:     Haltestellenbereich which has most "Haltestellen"
    """

    Haltestellenbereich_Haltestellen_sum = []
    for key in haltestellen_dict.keys():
        sub_dict = []
        sub_dict.append(int(len(haltestellen_dict[key])/4))
        sub_dict.append(key)
        Haltestellenbereich_Haltestellen_sum.append(sub_dict)

    Haltestellenbereich_Haltestellen_sum = sorted(Haltestellenbereich_Haltestellen_sum)

    return Haltestellenbereich_Haltestellen_sum[-1]

# =========================================================================================================

def Haltestellenbereich_meisten_Linien (dict):
    """
    function:   find which "Haltestellenbereich" has most "Linien"
    input:      haltestellen_dict
    output:     Haltestellenbereich which has most "Linien"
    """

    Haltestellenbereich_Haltestellen_sum = []
    for key in dict.keys():
        dict[key][2] = dict[key][2].strip().split(" ")

    max_key = 'Köln'
    max_length = 1
    max_length_key_list = []
    for key in dict.keys():
        if len(dict[key][2]) > max_length:
            max_length = len(dict[key][2])
            max_key = key
            max_length_key_list.append(key)
            max_length_key_list.append(len(dict[key][2]))
        if len(dict[key][2]) == max_length:
            max_length_key_list.append(key)
            max_length_key_list.append(len(dict[key][2]))


    # print(max_key)
    # print(max_length)
    # print(max_length_key_list)

    return max_key, max_length, dict

# if __name__ == '__Haltestellenbereich_meisten_Linien__':
#     Haltestellenbereich_meisten_Linien (haltestellenbereiche_dict)

# =========================================================================================================

def report(list, fileName, fileFormat = ".txt"):
    """
    function:   generate report
    input:      list, filename, default report in ".txt" format
    output:     report
    
    """
    fileName = fileName+fileFormat
    with open(fileName, 'w', encoding="utf-8") as f:
        f.write("\n".join(list))

# =========================================================================================================
# cos(d/R) = sin(φ₁)sin(φ₂) + cos(φ₁)cos(φ₂)cos(θ₂ - θ₁)
# d = R * arccos[sin(φ₁)sin(φ₂) + cos(φ₁)cos(φ₂)cos(θ₂ - θ₁)]
# θ :   longitude   (east-west) 
# φ :   latitude    (north-south)


def distance_two_positions_haversine(latitude1,longitude1,latitude2, longitude2,R = 6371000):
    """
    
    d = 2R * sin⁻¹(√[sin²((θ₂ - θ₁)/2) + cosθ₁ * cosθ₂ * sin²((φ₂ - φ₁)/2)])

        where:  θ₁, φ₁ - First point latitude and longitude coordinates;
                θ₂, φ₂ - Second point latitude and longitude coordinates;
                R -  Earth's radius (R = 6371 km); and
                d - Distance between them along Earth's surface.

    input:      latitude1,longitude1,latitude2, longitude2
                R = 6371000 (default)

    return:     distance between point 1 and 2
    """

    latitude1_rad = math.radians(latitude1)
    longitude1_rad = math.radians(longitude1)

    latitude2_rad = math.radians(latitude2)
    longitude2_rad = math.radians(longitude2)

    distance = 2*R*math.asin(((math.sin((latitude2_rad-latitude1_rad)/2))**2 + math.cos(latitude1_rad)*math.cos(latitude2_rad)*(math.sin((longitude2_rad-longitude1_rad)/2))**2)**(1/2))

    return distance


# ========================================================================================================
def max_min_dict_finder(dict,parameter):
    """
    function: max_min_dict_finder   finde the max or min value in a dictionary and return the key of it

    input:                          dictionary
                                    parameter: choose between "max" and "min"

    return:                         max_value_key, 
                                    max_value, 
                                    min_value_key, 
                                    min_value
    """

    return_dict = {"max_value_key": None, "max_value":None, "min_value_key":None, "min_value":None}
    
    max_value = None
    min_value = None
    max_value_key = None
    min_value_key = None

    if parameter == "max":
        return_dict = {"max_value_key": None, "max_value":None}
        max_value = max(list(dict.values()))
        for key, value in dict.items():
            if value == max_value:
                max_value_key = key
        return_dict["max_value_key"] = max_value_key
        return_dict["max_value"] = max_value

    if parameter == "min":
        return_dict = {"min_value_key":None, "min_value":None}
        min_value = min(list(dict.values()))
        for key, value in dict.items():
            if value == min_value:
                min_value_key = key
        return_dict["min_value_key"] = min_value_key
        return_dict["min_value"] = min_value

    return return_dict 
