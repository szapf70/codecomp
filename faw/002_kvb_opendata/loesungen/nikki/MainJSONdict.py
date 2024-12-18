import json, itertools

dict_all = "Dict_all_v3.json"


# read all data from Dict_all.json
def readDataFromJSON(filename): 

    with open (filename, "r") as file:
        json_data = json.load(file)
        return json_data


### Funktionen Leicht ###

# Leicht1:
# •	Wie viele Linien (Busse und Bahnen) und wie viele Haltestellenbereiche gibt es insgesamt?

def Leicht1(data):
    alle_linien = list()
    for key in data:
        hsb = data[key]
        Linien = hsb.get("Linien", "")
        lin_einzeln = Linien.split()
        alle_linien.extend(lin_einzeln)
    num_lin = len(set(alle_linien))

    nl = '\n'
    print ("Leicht 1:")
    print ("_________________")
    print(f"Es gibt {num_lin} Linien")
    print(f"Es gibt {len(data)} Haltestellenbereiche{nl}")
    # alle_linien.sort(key = int)
    return set(alle_linien)

# Leicht 2:
# •	Welcher Haltestellenbereich hat die meisten Haltestellen und an welchem Treffen sich die meisten Linien?

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

def Leicht4(data):  
    cnt_bus = 0
    cnt_strab = 0  
    cnt_both = 0
    for key in data:
        hsb = data[key]
        Betriebsbereich = hsb.get("Betriebsbereich", "")
        bb_einzeln = Betriebsbereich.split()
        if 'BUS' in bb_einzeln:
            if 'STRAB' in bb_einzeln:
                cnt_both += 1
            else:
                cnt_bus += 1
        elif 'STRAB' in bb_einzeln:
            cnt_strab += 1
    
    nl = '\n'
    print("Leicht 4:")
    print ("_________________")
    print(f"Bus: {cnt_bus}")
    print(f"STRAB: {cnt_strab}")
    print(f"Beides: {cnt_both}{nl}")

# Leicht 5
# •	Bestimme den nördlichsten, westlichsten, südlichsten und östlichsten Haltstellenbereich. 
# Wie kann man die Position eines Haltestellenbereichs berechnen?

def Leicht5(data):
    max_c1 = 0
    max_c2 = 0
    min_c1 = 100
    min_c2 = 100
    max_name_c1 = None
    max_name_c2 = None
    min_name_c1 = None
    min_name_c2 = None

    # for each hsb
    for key in data:
        hsb = data[key]    
        haltestellen = hsb.get("Haltestellen", "") 
        hsb_name = hsb["Haltestellenname"]

        max_coord1 = 0
        max_coord2 = 0
        min_coord1 = 100
        min_coord2 = 100

        # find max of all HS in 1 HSB
        for hs in haltestellen:
            if hs["coord1"] > max_coord1 or hs["coord1"] == max_coord1:
                max_coord1 = hs["coord1"]
            if hs["coord2"] > max_coord2 or hs["coord2"] == max_coord2:
                max_coord2 = hs["coord2"]
            if hs["coord1"] < min_coord1:
                min_coord1 = hs["coord1"]
            if hs["coord2"] < min_coord2:
                min_coord2 = hs["coord2"]
    
    
    # find name and max of all HSB
        if max_coord1 > max_c1 or max_coord1 == max_c1:
            max_c1 = max_coord1
            max_name_c1 = hsb_name
        if max_coord2 > max_c2 or max_coord2 == max_c2:
            max_c2 = max_coord2
            max_name_c2 = hsb_name
        if min_coord1 < min_c1:
            min_c1 = min_coord1
            min_name_c1 = hsb_name
        if min_coord2 < min_c2:
            min_c2 = min_coord2
            min_name_c2 = hsb_name

    nl = '\n'
    print("Leicht 5:")
    print ("_________________")
    print(f"Der Der am weitesten süd liegende Haltestellenbereich ist: {min_name_c1} ({min_c1})")
    print(f"Der Der am weitesten nördlichsten liegende Haltestellenbereich ist: {max_name_c2} ({max_c2})")
    print(f"Der östlichste Haltestellenbereich ist: {max_name_c1} ({max_c1})")
    print(f"Der wechstlichste Haltestellenbereich ist: {min_name_c2} ({min_c2}){nl}")



### Funktionen Mittel ###


# Mittel 1:
# •	Welche beiden Linien haben die größte Anzahl gemeinsamer Stationen?

def Mittel1(data):
    comb_dict = {}
    # berechne eine Kombo der 2 Linien für jeden Haltestellenbereich
    def findAllLinesCombinations(dict):
        for key in dict:
            hsb = dict[key]
            Linien_hsb = hsb.get("Linien", "")
            
            hsb_name = hsb["Haltestellenname"]
            lin_hsb_einzeln = Linien_hsb.split()
            combos_hsb = itertools.combinations(lin_hsb_einzeln, 2)

            for comb_hsb in combos_hsb:
                # print(comb_hsb)
                comb_dict[comb_hsb] = hsb_name
        return comb_dict
    
    comb_hsb_dict = findAllLinesCombinations(data)

        # gehe durch alle Kombinationenpaare aus HSB
        # check ob das Paar in HS_Linien ist
        # wenn ja, zähl die Haltestellen in diesem Bereich
    linien_cnt_dict = {}
    
    for lin_paar in comb_hsb_dict:
        # gehe durch alle Haltestellen in einem Haltestellenbereich
        cnt_hsb = 0
        for key in data:
            hsb = data[key]    
            Linien_hsb = hsb.get("Linien", "")
            lin_hsb_einzeln = Linien_hsb.split()

            if lin_paar[0] in lin_hsb_einzeln and lin_paar[1] in lin_hsb_einzeln:
                cnt_hsb += 1 
                linien_cnt_dict[lin_paar] = cnt_hsb
    # print(linien_cnt_dict)
    paar_max_hs = max(linien_cnt_dict, key = linien_cnt_dict.get)
    cnt_max_hs = int(linien_cnt_dict[paar_max_hs])
    nl = '\n' 
    print("Mittel 1:")
    print ("_________________")  
    print(f"Linienpaar mit meisten Haltestellenbereichen ist: {paar_max_hs} mit {cnt_max_hs} Haltestellenbereichen{nl}")
 

# Mittel 2:
# •	Welche Linie ist an all ihren Haltestellen prozentual am besten mit digitalen Fahrgastinformationsanzeigen ausgestattet? Das gleiche auch für Fahrtreppen und Aufzüge.

def Mittel2(data, lines):
    prozent_dfi_dict = {}
    prozent_auf_dict = {}
    prozent_ft_dict = {}
    
    # go through all lines
    for line in lines: 
        cnt_dfi = 0
        cnt_auf = 0
        cnt_ft = 0
        cnt_hsb = 0   
        
        # go through all hsb
        for key in data:           
            hsb = data[key]
            Linien_hsb = hsb.get("Linien", "")          
            lin_hsb_einzeln = Linien_hsb.split()
            
            # check if line is in hsb
            if line in lin_hsb_einzeln:
                # if line is in hsb, count hsb
                cnt_hsb += 1
                # if hsb has dfi, count dfi
                if hsb.get("DFI") != "":
                    cnt_dfi += 1
                if len(hsb.get("Aufzuege")) != 0:
                    cnt_auf += 1
                if len(hsb.get("Fahrtreppen")) != 0:
                    cnt_ft += 1

        # Prozent für eine Linie in einem HSB
        Prozent_dfi = round(cnt_dfi/cnt_hsb*100, 2)
        # Prozent_dict für alle Linien in allen HSB
        prozent_dfi_dict[line]= Prozent_dfi
        Prozent_auf = round(cnt_auf/cnt_hsb*100, 2)
        prozent_auf_dict[line]= Prozent_auf
        Prozent_ft = round(cnt_ft/cnt_hsb*100, 2)
        prozent_ft_dict[line]= Prozent_ft
    # print(prozent_dfi_dict)
    max_dfi_line = max(prozent_dfi_dict, key = prozent_dfi_dict.get)
    max_dfi_prozent = prozent_dfi_dict[max_dfi_line]
    max_auf_line = max(prozent_auf_dict, key = prozent_auf_dict.get)
    max_auf_prozent = prozent_auf_dict[max_auf_line]
    max_ft_line = max(prozent_ft_dict, key = prozent_ft_dict.get)
    max_ft_prozent = prozent_ft_dict[max_ft_line]
    nl = '\n' 
    print("Mittel 2:")
    print ("_________________")  
    print(f"Die höhste DFI Deckung hat die Linie {max_dfi_line} mit {max_dfi_prozent} %")
    print(f"Die höhste Aufzug Deckung hat die Linie {max_auf_line} mit {max_auf_prozent} %")
    print(f"Die höhste Fahrtreppe Deckung hat die Linie {max_ft_line} mit {max_ft_prozent} %{nl}")

# Mittel 3:
# •	Der Kölner weiß das eine zweistellige Nummer eine Straßenbahn und eine dreistellige Nummer ein Bus ist. Aber könnte man diese Information auch aus den Daten ziehen? Direkt angegeben ist es nicht.
# Wie genau soll man das beweisen? Nach Haltestellen mit einzelnen 1/2-stelligen Linien suchen und schauen ob sie nur STRAB sind?

def Mittel3(data, lines):
    linien_strab = []
    for line in lines: 
        if len(line) < 3:     
            for key in data:
                hsb = data[key]
                haltestellen = hsb.get("Haltestellen", "")
                
                for hs in haltestellen:
                    Linien_hs = hs.get("Linien", "")
                    lin_hs_einzeln = Linien_hs.split()
                    if line in lin_hs_einzeln and hs.get("Betriebsbereich") == "STRAB":
                        linien_strab.append(line)
    print("Mittel 3:")
    print ("_________________")  
    print(f"Linien {set(linien_strab)} sind eindeutig STRAB")


# Mittel 4:                           
# •	Liste alle Straßenbahnlinien jeweils mit allen Straßenbahnlinien in die man auf ihrem Weg direkt umsteigen kann auf.

def Mittel4(data, lines):
    line_set = set()
    line_list = []
    nl = '\n' 
    print("Mittel 4:")
    print ("_________________")  
    for line in lines: 
        line_strab_set = set()
        line_list = []
        line_strab_list = []
        if len(line) < 3:  
            for key in data:
                    hsb = data[key]
                    linien_hsb = hsb.get("Linien", "").split()
                    # haltestellen = hsb.get("Haltestellen", "")
                    # for hs in haltestellen:
                    #     Linien_hs = hs.get("Linien", "")
                    #     lin_hs_einzeln = Linien_hs.split()
                    if line in linien_hsb and len(linien_hsb)>1:
                        line_list.extend(linien_hsb)
                        line_list.remove(line)
                        line_strab_list = [x for x in line_list if len(x) < 3]
                        # line_strab_list.sort()
            line_strab_set = set(line_strab_list)
            # print(line)
            # print(line_strab_set)
            print(f"Linie {line} mmit direkter Umsteigemöglichkeit in die Linien {line_strab_set}{nl}")
    


# Mittel 5:                           
# •	Haben alle Straßenbahnlinien mindestens ein Kundencenter an einer ihrer Haltestellen?
# Und von welchen Linien ohne Kundencenter kann man mit einmal Umsteigen in eine andere Linie zu einem Kundencenter gelangen. 

def Mittel5(data, lines): 
    lines_with_kc = []
    lines_without_kc = []
    lines_alternative = []
    for line in lines:  
        # go through all STRAB lines
        if len(line) < 3:  
            for key in data:
                    hsb = data[key]
                    linien_hsb = hsb.get("Linien", "").split()
                    if line in linien_hsb:
                    # if line is in hsb, check if it has Verkaufsorte
                        verkaufsorte = hsb.get("Verkaufsorte")
                        if len(verkaufsorte) != 0:
                            #  if it has Verkaufsort, check if there is a Segment: KundenCenter in any of Verkaufsorte
                            for vo in verkaufsorte:
                                if vo.get("Segment") == "KundenCenter":
                                    lines_with_kc.append(line)
                          
            if line not in lines_with_kc:
                lines_without_kc.append(line)
                for key in data:
                    lines_hsb = []
                    hsb = data[key]
                    linien_hsb = hsb.get("Linien", "").split()
                    if line in linien_hsb and len(linien_hsb)>1:
                        lines_hsb.extend(linien_hsb)
                        for line_kc in lines_with_kc:
                            if line_kc in lines_hsb and len(line_kc)<3:
                                lines_alternative.append(line_kc)     
    lines_with_kc = set(lines_with_kc)  


    print("Mittel 5:")
    print ("_________________")                        
    print(f"Linien mit KundenCenter sind: {set(lines_with_kc)}")
    print(f"Linie/n ohne KundenCenter sind: {set(lines_without_kc)}")
    print(f"Umsteigemöglichkeit zum KundenCenter für Linie {set(lines_without_kc)} ist {set(lines_alternative)}")



def main():
    
    all_data = readDataFromJSON(dict_all)
    all_lines = Leicht1(all_data)
    # Leicht2(all_data)
    # Leicht3(all_data)
    # Leicht4(all_data)
    # Leicht5(all_data)

    # Mittel1(all_data)
    Mittel2(all_data, all_lines)
    Mittel3(all_data, all_lines)
    Mittel4(all_data, all_lines)
    Mittel5(all_data, all_lines)
    

    # # example for reading hs
    # haltestellen = ReadJSON.readVariables(prop, "Haltestellenname")
    # # print(hs)
    # # print(len(hs))

    # hsbereich = ReadJSON.readVariables(prop, "Haltestellenbereich")

    
    # print(Leicht1(lines, hsbereich))
    # print(prop)
    # print(type(hsbereich))
    # # Leicht2(prop)
        
if __name__ == "__main__":
    main()