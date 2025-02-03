import ReadJSON, pprint

fileName = "haltestellenbereiche.json"


feat = ReadJSON.readDataFromJSON(fileName)
prop = ReadJSON.readProperties(feat)


# example for reading line
lines = ReadJSON.readVariables(prop, "Linien")
# print(lines)
# print(len(lines))

# example for reading names
names = ReadJSON.readVariables(prop, "Haltestellenname")
# print(names)
# print(len(names))

hsbereich = ReadJSON.readVariables(prop, "Haltestellenbereich")

### Funktionen Leicht ###

def counting(l, hsb):
    cnt = 0
    all_lines = list()
    for lin in l:
        # print(lin)
        # lin = lin.split(',')
        lin_einzeln = lin.split()
        # print(type(lin_einzeln))
        # print(lin_einzeln)
        all_lines.extend(lin_einzeln)
    # print(all_lines)
    # print(len(all_lines))
    # # print(set(all_lines))
    # print(len(set(all_lines)))

    # # print(l)
    # # print(len(l))
    # # print(hsb)
    # print(len(set(hsb)))
    return len(set(all_lines)), len(set(hsb))

print(counting(lines, hsbereich))