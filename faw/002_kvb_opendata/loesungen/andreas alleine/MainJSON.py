import readJSONfiles, pprint

### Funktionen Leicht ###

# Leicht1:
# •	Wie viele Linien (Busse und Bahnen) und wie viele Haltestellenbereiche gibt es insgesamt?

def Leicht1(l, hsb):
    all_lines = list()
    for lin in l:
        # split string with lines in a list into single strings separated with blank
        lin_einzeln = lin.split()
        # print(lin_einzeln)

        # add list with single strings in list with all lines as elements (not as list like with append)
        all_lines.extend(lin_einzeln)
    # remove all duplicates with set
    return len(set(all_lines)), len(set(hsb))

# # Leicht 2:
# # •	Welcher Haltestellenbereich hat die meisten Haltestellen und an welchem Treffen sich die meisten Linien?
# def Leicht2(hs, hsb, l):

#     for haltestellenbereich in hsb:
#         hsb_keys = haltestellenbereich.keys()
#         print(hsb_keys)

# # Leicht 3:
# # •	Wieviel Haltestellenbereiche haben Fahrtreppen, Aufzüge, beides oder keines von beidem?
# def Leicht3(hs, hsb, l):
    
  


def main():
    fileName = "haltestellenbereiche.json"

    # features
    feat = readJSONfiles.readDataFromJSON(fileName)
    # properties
    prop = readJSONfiles.readProperties(feat)


    # example for reading line
    lines = readJSONfiles.readVariables(prop, "Linien")
    # print(lines)
    # print(len(lines))

    # example for reading hs
    haltestellen = readJSONfiles.readVariables(prop, "Haltestellenname")
    # print(hs)
    # print(len(hs))

    hsbereich = readJSONfiles.readVariables(prop, "Haltestellenbereich")

    print(Leicht1(lines, hsbereich))
    print(prop)

    # Leicht2(prop)
        
if __name__ == "__main__":
    main()

def Leicht2(data):
    max_lin = 0
    max_hs = 0
    for key in data:
        hsb = data[key]
        Linien = hsb.get("Linien", "")
        Haltestellen = hsb.get("Haltestellen", "")
        lin_einzeln = Linien.split()
        num_lin_hsb = len(lin_einzeln)
        num_hs = len(Haltestellen)
        if num_lin_hsb > max_lin:
            max_lin = num_lin_hsb
            key_lin = key
        if num_hs > max_hs:
            max_hs = num_hs
            key_hs = key
    hsb_hs= data[key_hs]["Haltestellenname"]
    hsb_lin = data[key_lin]["Haltestellenname"]

    nl = '\n'
    print("Leicht 2:")
    print ("_________________")
    print(f"Haltestellenbereich mit meisten Haltestellen ist: {hsb_hs} mit {max_hs} Haltestellen")
    print(f"Haltestellenbereich mit meisten Linien ist: {hsb_lin} mit {max_lin} Linien{nl}")

    # Leicht 3   
# •	Wieviel Haltestellenbereiche haben Fahrtreppen, Aufzüge, beides oder keines von beidem?

def Leicht3(data):

    Aufzuege = [d["Aufzuege"] for d in data.values()] 
    num_aufzuege = len(list(filter(None, Aufzuege)))
    Fahrtreppen = [d["Fahrtreppen"] for d in data.values()] 
    num_ft = len(list(filter(None, Fahrtreppen)))
    both = len([d for d in data.values() if bool(d["Aufzuege"]) & bool(d["Fahrtreppen"])])
    # warum funktioniert das nicht?
    keiner = len([d for d in data.values() if len(d["Aufzuege"]) == 0 & len(d["Fahrtreppen"]) == 0])
    nur_auf = num_aufzuege-both
    nur_ft = num_ft - both
    keiner = len(data) - both - nur_auf - nur_ft

    nl = '\n'
    print("Leicht 3:")
    print ("_________________")
    # print(f"Insgesamt {num_aufzuege} Haltestellenbereiche haben Aufzüge")
    print(f"{nur_auf} Haltestellen haben nur Aufzüge")
    # print(f"Insgesamt {num_ft} Haltestellenbereiche haben Fahrtreppen")
    print(f"{nur_ft} Haltestellen haben nur Fahrtreppen")
    print(f"{both} Haltestellenbereiche haben beides")
    print(f"{keiner} Haltestellenbereiche haben weder Aufzüge noch Fahrtreppen{nl}")

# Leicht 4   
# •	Wieviel Haltestellenbereiche decken jeweils die Betriebsbereich „BUS“, „STRAB“ oder beides ab?