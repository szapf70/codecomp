import json, pprint, os

def load_geo_Data(filename, key_prompt, key_prompt2):

    filename = os.path.join("json", filename)

    with open (filename, "r") as file:
        haltestellen_data = json.load(file)
        features = haltestellen_data ["features"]
        prop_list = [idx["properties"] for idx in features]   
        geo_list = [idx["geometry"] for idx in features]
        
        return ( [idx[key_prompt] for idx in prop_list],[idx[key_prompt2] for idx in geo_list])
    
def load_Data(filename):

    filename = os.path.join("json", filename)

    with open (filename, "r") as file:
         haltestellen_data = json.load(file)
         features = haltestellen_data ["features"]
         prop_list = [idx["properties"] for idx in features]
         return (prop_list)

# ------------- generiert ein Dict mit Linien als int (linien_int) ------------------------

filename_2 = "json/haltestellenbereiche.json"

with open (filename_2, "r") as file:
    haltestellen_data = json.load(file)
    features = haltestellen_data ["features"]
    prop_list = [idx["properties"] for idx in features]  

numbers = []
dat = {}
for dat in prop_list:
    
    if "Linien" in dat:
        number = dat["Linien"].split()
        numbers = []
        for element in number:
            elint = int(element)
            numbers.append(elint)
    else:   
        numbers = [0]
    dat["linien_int"] = numbers

linien_int = [idx.get("linien_int", 0) for idx in prop_list]            # legt eine Variabele mit den Listen von Linien als int an

def func_all_lines_list ():
        all_lines_list =[]                                                      # legt eine Variabele mit EINER Lister aller Linien als int an.
        linien_int = [idx.get("linien_int", 0) for idx in prop_list]
        for list in linien_int:
                for element in list:                                            # entfernt die aufgefüllte 0 für die fehlende Linie
                        if element > 0:
                                all_lines_list = all_lines_list + list
                                
        return (all_lines_list)
# ------------------ Einlesen von Aufzug u. Fahrtreppen Informaionen ------------
def aufz_trpp_data():
    filename = "json/aufzuege.json"

    with open (filename, "r") as file:
            aufz_data = json.load(file)
            aufzuege_list = aufz_data ["features"]
            #aufzug_hsb = aufzuege_list[2]["Haltestellenbereich"]

    aufzug_liste=[]
    for i in range(len(aufzuege_list)):
            a = (aufzuege_list[i]["properties"]["Haltestellenbereich"])
            aufzug_liste.append(a)   
    aufzug_liste = (set(aufzug_liste))                                                     # Liste aller Haltestellenbereiche mit Aufzug

    filename = "json/fahrtreppen.json"

    with open (filename, "r") as file:
            fahrt_data = json.load(file)
            trepp_list = fahrt_data ["features"]
            
    fahrtreppen_liste=[]
    for i in range(len(trepp_list)):
            a = (trepp_list[i]["properties"]["Haltestellenbereich"])
            fahrtreppen_liste.append(a)   
    fahrtreppen_liste = (set(fahrtreppen_liste))                                # Liste aller Haltestellenbereiche mit Fahrtreppen

    return aufzug_liste,fahrtreppen_liste
