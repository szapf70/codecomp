import json, pprint,ReadJSON


filename= ("haltestellenbereiche.json")
filename1=("haltestellen.json") 
filename2=("Dict_all_v3.json") 
#filename3=("aufzuege.json") 

# features
feat = ReadJSON.readDataFromJSON(filename)
# properties
prop = ReadJSON.readProperties(feat)

#-------------------------------------------------------------------------------------------------------------
#download oof the files from Haltestellenbereich
#-----------------------------------------------
with open(filename, 'r') as file:
 KVB_1 = json.load(file)
#download oof the files from Haltestellen
#-----------------------------------------------
with open(filename1, 'r') as file:
 KVB_2 = json.load(file) 


#------------------------------------------------------------------------------------------------------------ 
 # Zugriff auf die Liste der Haltestellenbereiche Features
features = KVB_1['features']
# -------------------------------Liste der Namen Haltestellenbereiche extrahieren-------------------------------------------------
HSname = [feature['properties']['Haltestellenname'] for feature in features]
Kname = [feature['properties']["kurzname"] for feature in features]
Betriebsbereiche = [feature['properties']['Betriebsbereich'] for feature in features]
VRSnum= [feature['properties']["VRSNummer"] for feature in features]
lines = ReadJSON.readVariables(prop, "Linien")


 # ----------------------------Zugriff auf die Liste der Haltestellen Features
features1 = KVB_2['features']
# Liste der Namen extrahieren
Kname1 = [feature['properties']["Kurzname"] for feature in features1]


#---------Wie viele Linien (Busse und Bahnen) und wie viele Haltestellenbereiche gibt es insgesamt?-----
lines_new=list()
for l in lines:
    lines_new.extend(l.split())
#print(lines_new)

print("Es gibt insgesamt",len(set(lines_new)), "Vekehrslinien und ", (len(Betriebsbereiche)),"Haltestellen")

#-------Welcher Haltestellenbereich hat die meisten Haltestellen und an welchem treffen sich die meisten Linien?-----
Kname_new=list()

for l in Kname1:
   Kname_new.extend(l.split())

haeufigkeit_dict = {}

for element in Kname_new:
    if element in haeufigkeit_dict:
        haeufigkeit_dict[element] += 1
    else:
        haeufigkeit_dict[element] = 1
 
    
Max_halt=max(haeufigkeit_dict,key=haeufigkeit_dict.get)         
f= Kname1.count(Max_halt)


print("Chorweiler hat mit",f, "Haltestellen die meisten Haltestellen in Köln")
#print(lines_new)


# Wir wollen die Längen der Listen unter dem Schlüssel 'Linien' vergleichen
key_to_compare = 'Linien'

# Initialisierung für das Speichern des längsten Listeneintrags
max_length = 0
max_key = None

for key, sub_dict in KVB_1.items():
    # Holen Sie sich die Liste unter dem spezifischen Schlüssel
    if key_to_compare in sub_dict:
        current_length = len(sub_dict[key_to_compare])
        
        # Vergleichen der aktuellen Länge mit der maximalen Länge
        if current_length > max_length:
            max_length = current_length
            max_key = key

print(f"Der Schlüssel mit der längsten Liste unter '{key_to_compare}' ist '{max_key}' mit {max_length} Elementen.")

'''
lines_new=list()
for l in lines:
    lines_new.extend(l.split())
print(lines_new)
haeufigkeit_dict1 = {}

for i in Kname_new:
   pprint.pprint(i)
   key=Kname
   for a in lines_new:
        num_lin_hsb = len(set(lines_new))
        break
pprint.pprint(i)     
print(i,a)       
   

   
#haltestellen = Kname_new
#lin_einzeln = lines_new
#num_lin_hsb = len(lin_einzeln)
#num_hs = len(haltestellen)
#print(haltestellen,num_lin_hsb )



#-----------------------------------Anzahl der Busse ,Strassenbahnen und beides gemeinsam---------------

bus= Betriebsbereiche.count("BUS")
Strab= Betriebsbereiche.count("STRAB")
Beides= Betriebsbereiche.count("BUS ""STRAB")

print("Es sind insgesamt", bus, "Busse",Strab, "Strassenbahnen und ",Beides, "Gesamtzahl der Verkehsrmittel")

#----Wieviel Haltestellenbereiche haben Fahrtreppen, Aufzüge, beides oder keines von beidem?---
'''