import json

haltestellenbereiche = "json/haltestellenbereiche.json"
haltestellen = "json/haltestellen.json"
fahrtreppen = "json/fahrtreppen.json"
haltestellen_dfi = "json/haltestellenbereichemitdfi.json"
aufzuege = "json/aufzuege.json"
verkaufsorte = "json/verkaufsorte.json"

def readDataFromJSON(filename): 

    with open (filename, "r") as file:
        json_data = json.load(file)
        features = json_data["features"]
        return features

hsb_f = readDataFromJSON(haltestellenbereiche)
hs_f = readDataFromJSON(haltestellen)
ft_f = readDataFromJSON(fahrtreppen)
dfi_f = readDataFromJSON(haltestellen_dfi)
lift_f = readDataFromJSON(aufzuege)   
vo_f = readDataFromJSON(verkaufsorte)

property_hsb = [ind_p ["properties"] for ind_p in hsb_f]
property_hs = [ind_p ["properties"] for ind_p in hs_f]
geometry_hs = [ind_g ["geometry"] for ind_g in hs_f]
property_dfi = [ind_p ["properties"] for ind_p in dfi_f]
property_lift = [ind_p["properties"] for ind_p in lift_f]
geometry_lift = [ind_g["geometry"] for ind_g in lift_f]
property_ft = [ind_p["properties"] for ind_p in ft_f]
geometry_ft = [ind_g["geometry"] for ind_g in ft_f]
property_vo = [ind_p["properties"] for ind_p in vo_f]
    
# print(hsb["kurzname"])

def createDictAll(hsb, hs, ft, dfi, lift, vo):
    # result dictionary with all necessary data
    dict_all = {} 
    # dictionary where the values for the result dictionary will be added
    dict_values = {} 
    #  property_hsb is a list, p_hsb is a dict 
    for p_hsb in property_hsb: 
        # function to add keys defined in keepKeys from hsb for each hsb and
        # to add coordinates from geometry of hsb to each hsb
        def addPropCoord(searchKey_xx, keepKeys, res_key_xx, xx_f):
            values_list = []
            for el in xx_f:
                el_p = el["properties"]
                
                if el_p[searchKey_xx] == res_key_xx:
                    dict_from_hs = dict((key, el_p[key]) for key in keepKeys if key in el_p) 
                    # values_list = []
                    el_g = el.get("geometry", "")

                    dict_from_hs.update({"coord1": el_g["coordinates"][0]})
                    dict_from_hs.update({"coord2": el_g["coordinates"][1]})

                    values_list.append(dict_from_hs.copy())

            return values_list
        
        res_key_kurzname = p_hsb["kurzname"]
        res_key_hsb = p_hsb["Haltestellenbereich"]

        # add Haltestellenbereich, Haltestellenname, Linien and Betriebsbereich 
        dict_values = dict((key, p_hsb[key]) for key in {"Haltestellenbereich", "Haltestellenname", "Linien", "Betriebsbereich"} if key in p_hsb)
           
        # find Haltestellen for each kurzname and add them as a list of dictionaries
        values_hs_list = addPropCoord("Kurzname", {"Betriebsbereich", "Linien"}, res_key_kurzname, hs_f)
        dict_values["Haltestellen"] = values_hs_list

        # find Aufzuege
        values_lift_list = addPropCoord("Haltestellenbereich", {"Kennung", "Bezeichnung"}, res_key_hsb, lift_f)
        dict_values["Aufzuege"] = values_lift_list

        # find fahrtreppen
        values_ft_list = addPropCoord("Haltestellenbereich", {"Kennung", "Bezeichnung"}, res_key_hsb, ft_f)
        dict_values["Fahrtreppen"] = values_ft_list 

        # find verkaufsorte
        values_vo_list = addPropCoord("haltestellenbereich", {"Segment"}, res_key_hsb, vo_f)
        dict_values["Verkaufsorte"] = values_vo_list 
    
        # find dfi
        dict_values["DFI"] = ""
        for p_dfi in property_dfi:
            if p_dfi["Haltestellenbereich"] == res_key_hsb:
                dict_values["DFI"] = res_key_hsb
            

        dict_all[res_key_kurzname] = dict_values  
                # dict_all["Haltestellen"] = p_hs
                # dict_all.update(p_hs)
        # print(dict_values)
        
    
    
        

    return dict_all

dict_all_data = createDictAll(hsb_f, hs_f, ft_f, dfi_f, lift_f, vo_f)
# print(dict_all_data)

with open("Dict_all_v3.json", 'w', encoding = 'utf-8') as file:
        json.dump(dict_all_data, file, indent=4)