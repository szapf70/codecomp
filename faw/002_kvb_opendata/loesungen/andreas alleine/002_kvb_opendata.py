import readJSONfiles, pprint


def main():
    fileName = "haltestellenbereiche.json"

    # features
    feat = readJSONfiles.readDataFromJSON(fileName)
    # properties
    prop = readJSONfiles.readProperties(feat)

#----------- Liste der Haltestellen an der sich zwei Linien treffen --------------------------------------------------------
    # Define the lines to compare
    line_a = (3) # Replace with actual line identifier
    line_b = (5)  # Replace with actual line identifier

    # Sets to store stops for each line
    ges_linie = set()
    ges_linie2 = set()

    for stop_info in prop:
        # Get the lines serving this stop
        linie = stop_info.get("Linien", "")
        linien = linie.split()

        # Check if the stop is part of line_a or line_b
        if line_a in linien:
            ges_linie.add(stop_info.get("Haltestellenname", ""))
        if line_b in linien:
            ges_linie2.add(stop_info.get("Haltestellenname", ""))

    # Find common stops
    meisten_treffen = ges_linie.intersection(ges_linie2)

    if meisten_treffen:
        print(f"Die meisten gemeinsamen Stationen haben {line_a} und {line_b}: {list(meisten_treffen)}")
    else:
        print(f"{line_a} und {line_b} haben keine gemeinsamen Haltestellen.")

if __name__ == "__main__":
    main()