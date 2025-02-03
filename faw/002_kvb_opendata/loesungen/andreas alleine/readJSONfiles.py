import json

# read features from JSON

def readDataFromJSON(filename): 

    with open (filename, "r") as file:
        json_data = json.load(file)
        features = json_data["features"]
    return features

# read properties from features    
    
def readProperties(f):
    property_data = [ind_p ["properties"] for ind_p in f]
    return property_data

# read variables from properties with given key and get an empty string if key doesn't exsist
# (better solution than getting only those who exist because the length stays the same)
def readVariables(prop_list, prop_key):
    values = list()
    for dict in prop_list:
        values.append(dict.get(prop_key, ""))
    return values

# # read variables from properties with given key and check if key exists
# def readVariables(prop_list, prop_key):
#     values = list()
#     for dict in prop_list:
#         if prop_key in dict:
#             values.append(dict[prop_key])
#     return values