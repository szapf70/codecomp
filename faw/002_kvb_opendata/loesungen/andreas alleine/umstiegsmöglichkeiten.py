import readJSONfiles, pprint


def main():
    fileName = "haltestellenbereiche.json"

    # features
    feat = readJSONfiles.readDataFromJSON(fileName)
    # properties
    prop = readJSONfiles.readProperties(feat)

#----------- Liste der Haltestellen an der sich zwei Linien treffen --------------------------------------------------------

    ges_linie = input('Sie wollen umsteigen? Mit welcher Linie kommen sie: ')
    ges_linie2 = input('Und in welche Linie wollen sie umsteigen: ')

    liste_ges_haltestellen = []

    for stop_info in prop:
        linien = (stop_info.get("Linien", ""))
        if ges_linie in linien.split() and ges_linie2 in linien.split():
            liste_ges_haltestellen.append(stop_info["Haltestellenname"])

    if not liste_ges_haltestellen:
        print("Diese Linie gibt es nicht oder hat keine zugeordnete Haltestelle.")

    print(f"Der Übergang der Linie: {ges_linie} und der Linie: {ges_linie2} ")
    print(liste_ges_haltestellen)

if __name__ == "__main__":
    main()