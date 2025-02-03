import readJSONfiles


def main():
    fileName = "haltestellenbereiche.json"

    # features
    feat = readJSONfiles.readDataFromJSON(fileName)
    # properties
    prop = readJSONfiles.readProperties(feat)

    liste_ges_haltestellen = []
    liste_bus_haltestellen = []
    liste_strb_haltestellen = []
    liste_both_haltestellen = []

    for stop_info in prop:
        betriebsbereich = stop_info.get("Betriebsbereich", "")
        liste_ges_haltestellen.append(betriebsbereich)


        #if "BUS" in betriebsbereich:
        if betriebsbereich == "BUS":
            liste_bus_haltestellen.append(betriebsbereich)
        if betriebsbereich == "STRAB":
            liste_strb_haltestellen.append(betriebsbereich)
        if betriebsbereich != "BUS" and betriebsbereich != "STRAB":
            liste_both_haltestellen.append(betriebsbereich)

    #print("Bus Stops:", liste_bus_haltestellen)
    #print("Straßenbahn Stops:", liste_strb_haltestellen)
    #print("Straß/Bus Stops:", liste_both_haltestellen)

    print(f"Haltestellen nur für Busse: {len(liste_bus_haltestellen)}, Haltestellen nur für Straßenbahnen: {len(liste_strb_haltestellen)} und beide Arten : {len(liste_both_haltestellen)}")



if __name__ == "__main__":
    main()
