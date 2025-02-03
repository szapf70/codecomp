import json, pprint

#-------- Auslesen der Haltestellen und der Linien ----------------------------------------------------------
"""
Funktion gibt die Anzal und Namen der Haltestellen einer Linie an.
Parameter:  Liste der Haltestellenbereiche im json-Format
Output:     Liste aller Haltestellen (haltestellen) und die Anzahl
            ein dictinary (haltestellenbereichs_info) mit den Informationen der Haltestellenbereiche
"""

filename = "haltestellenbereiche.json"
with open(filename, "r") as file:
    haltestellen_data = json.load(file)

haltestellenname = [feature["properties"]["Haltestellenname"] for feature in haltestellen_data["features"]]
haltestellenbereichs_info = [feature["properties"] for feature in haltestellen_data["features"]]

#----------- Liste der Haltestellen nach den einzelnen Linien --------------------------------------------------------
"""
Funktion gibt eine Liste aus in der die Haltestellen der gesuchten Line stehen.
Input:      Die Linen-Nr.:
output:     Liste der Haltestellen der gesuchten Linie
"""

ges_linie = input('Welche Linie soll abgefragt werden: ')

liste_ges_haltestellen = []

for stop_info in haltestellenbereichs_info:
    linien = stop_info.get("Linien", "")
    if ges_linie in linien.split():
        liste_ges_haltestellen.append(stop_info["Haltestellenname"])

if not liste_ges_haltestellen:
    print("Diese Linie gibt es nicht oder hat keine zugeordnete Haltestelle.")

print(f"Anzahl der Haltestellen für Linie {ges_linie}: {len(liste_ges_haltestellen)}")
print(liste_ges_haltestellen)