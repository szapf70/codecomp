import functions_loader, itertools
#********************************************************************************************************
# ------------------- Schwierigkeitsgrad – leicht -------------------------------------------------------
#********************************************************************************************************
#
# --- Welcher Haltestellenbereich hat die meisten Haltestellen? -----------------------------------------
def hstb_max_hast():
    prop_list = (functions_loader.load_Data("haltestellen.json"))
    hstb = [idx["Name"] for idx in prop_list]                       # liest die Haltestellennamen ein

    count_befor = 0
    for hst in set(hstb):
            count = hstb.count(hst)                                 # zählt die Haltestellenbereichs Namen
            if count > count_befor:
                rehst = hst
                max_count= count
                count_befor = count
    return (rehst, max_count)                                       # gibt den Namen der Haltestelle mit der Anzahl ihrer Bereiche zurück
    
#
# --- an welcher Haltestelle Treffen sich die meisten Linien? -------------------------------------------
def hst_max_linien():
    max_lint = 0
    anz_lin_dict ={}
    name_hst = ""
    prop_list = (functions_loader.load_Data("haltestellenbereiche.json"))
    for i in range(len(prop_list)):
        hst_list = prop_list[i]["Haltestellenname"]                # holt sich die Haltestelle für den Durchlauf
        lin_list = prop_list[i].get("Linien", "0").split()
        anz_lin = len(lin_list)
                       
        if anz_lin > max_lint:                                     #-----------------------------------------------
            name_hst = hst_list                                    # prüft ob die Anzahl der Linien an der Station
            max_lint = anz_lin                                     # maximal, gleich oder geringer ist 
            continue                                               # damit auch mehrer Haltestellen mit gleicher maximalen Linien gelistet werden können
        if anz_lin == max_lint:                                    #
                name_hst = name_hst +","+ hst_list                 #
                continue                                           #
        if anz_lin < max_lint:                                     #
                continue                                           #-----------------------------------------------

    return (name_hst,max_lint)                                     # gibt den Namen und die Anzahl an Linien zurück
#
# --- Wieviel Haltestellenbereiche haben Fahrtreppen, Aufzüge, beides oder keines von beidem? ----------
def aufz_trpp():
    prop_list = (functions_loader.load_Data("haltestellenbereiche.json"))
    haltestellenbereich = [idx["Haltestellenbereich"] for idx in prop_list]                                         # lädt Haltestellenbereichs-Liste aus Haltestenbereich
    Betriebsbereich = [idx["Betriebsbereich"] for idx in prop_list]                                                 # lädt Betriebsbereichs-Liste aus Haltestenbereich 

    aufzug_liste,fahrtreppen_liste = functions_loader.aufz_trpp_data()

    hstb_mit_rollt_und_aufz = [x for x in haltestellenbereich if x in fahrtreppen_liste and x in aufzug_liste]      # lädt Haltestellenbereichs in neue Liste wenn if Bedingung stimmt
    hstb_mit_aufz = [x for x in haltestellenbereich if x in aufzug_liste and x not in fahrtreppen_liste]            #
    hstb_mit_rollt = [x for x in haltestellenbereich if x in fahrtreppen_liste and x not in aufzug_liste]           #-----------------------------------------------------------------
    #
# --- Wieviel Haltestellenbereiche decken jeweils die Betriebsbereich „BUS“, „STRAB“ oder beides ab? ---
    #
    bus = Betriebsbereich.count("BUS")                                                                              # zählt BUS, STRAB oder
    strab = Betriebsbereich.count("STRAB")                                                                          # BUS STRAB aus Betriebsbereich
    bus_strab = Betriebsbereich.count("BUS STRAB")                                                                  #------------------------------

    return (hstb_mit_rollt_und_aufz, hstb_mit_aufz,hstb_mit_rollt,bus,strab,bus_strab)                              # gibt alle Werte zurück
#
#********************************************************************************************************
# ------------------- Schwierigkeitsgrad – mittel -------------------------------------------------------
#********************************************************************************************************
# --- Welche beiden Linien haben die größte Anzahl gemeinsamer Stationen? -------------------------------
# ----------------- (big thank you to Nikki for her help) ------------------------------------------------
def common_stations ():
    comb_dict = {}
    prop_dict =  functions_loader.load_Data("haltestellenbereiche.json")
    
    for hsb_dict in prop_dict:
        linien = hsb_dict.get("Linien", "").split()                                 # lädt Linien aus Datenset hsb_dict
        hst_name = hsb_dict.get("Haltestellenname", "")                             # lädt Haltestellennamen aus Datenset hsb_dict
        combs_hsb = itertools.combinations(linien, 2)                               # Funktion bildet all möglichen Lininepaare

        for comb_hsb in combs_hsb:                                                  # iteriert über die einzelnen Linienpaare 
            comb_dict[comb_hsb] = hst_name                                          # weist dem Tuple Linienpaar den Haltestellennamen zu
    
    linien_cnt_dict = {}
    for lin_paar in comb_dict:                                                      # iteriert über das Dictionaries der Linienpaare 
        cnt_hsb = 0 
        
        for hsb_dict in prop_dict:                                                  # iteriert über die Datensätze der Haltestellen
            linien = hsb_dict.get("Linien", "").split()                             # generiert eine bereinigte Liste der Linien

            if lin_paar[0] in linien and lin_paar[1] in linien:                     # prüft ob die erste und die zweite Linie des Linienpaares in diesem Datensat der Haltestelle vorkommt
                cnt_hsb +=1                                                         # zählt die Stationen hoch wo diese Linienpaar vorkommt
                linien_cnt_dict[lin_paar] = cnt_hsb                                 # weist dem Linienpaar die Anzahl an gemeinsamer Stationen zu
    paar_max_hs = max(linien_cnt_dict, key = linien_cnt_dict.get)                   # gibt das Linienpaar mit dem höstem Anzahl zurück
    cnt_max_hs = int(linien_cnt_dict[paar_max_hs])                                  # gibt den Wert des Linienpaares als int zurück

    return (paar_max_hs, cnt_max_hs)                                                # gibt das Linienpaar und die Anzahl gemeinsamer Stationen zurück
#
# --- eine zweistellige Nummer steht für eine Straßenbahn ------------------------------------------------
# --- und eine dreistellige Nummer für ein Bus -----------------------------------------------------------
#
def bus_strab_digits():
    prop_dict =  functions_loader.load_Data("haltestellen.json")
    
    bus_list = []
    strab_list =[]
    for hst_dict in prop_dict:                                                      # iteriert über die Datensätze der Haltestellen
            linien = hst_dict.get("Linien", "").split()                             # weist die Linien aus einem Datensatz einer Liste zu
            hst_bet_ber = hst_dict.get("Betriebsbereich", "")                       # weist die Betriebsbereichsbezeichnung aus einem Datensatz einer Liste zu
            if hst_bet_ber == "BUS":
                for linie in linien:
                    bus_list.append(linie)                                          # wenn Betriebsbereich = "BUS" wird die Linien Nr. der Liste bus_list zugefügt
            if hst_bet_ber == "STRAB":
                for linie in linien:
                    strab_list.append(linie)                                        # wenn Betriebsbereich = "BSTRAB" wird die Linien Nr. der Liste strab_list zugefügt

    bus_numbers = set(bus_list)                                                     # weist das Set der bus_list der Liste bus_numbers zu    
    strab_numbers = set(strab_list)                                                 # weist das Set der strab_list der Liste strab_numbers zu 

    return (bus_numbers,strab_numbers)                                              # gibt eine Liste mir Bus Nr. und eine mit Straßenbahn Nr. zurück
#
# --- Liste alle Straßenbahnlinien jeweils mit allen Straßenbahnlinien in die man auf ihrem Weg direkt umsteigen kann auf ---
#
def strab_umst ():

    prop_dict =  functions_loader.load_Data("haltestellenbereiche.json")
    
    ges_linie_list =[]
    for hsb_dict in prop_dict:                                                          #iteriert über die Datensätze bis zu den einzelnen Linien Nr.
        linien = hsb_dict.get("Linien", "").split()
        for linie in linien:
            linie_int = int(linie)  	                                                # wandelt die Linie Nr von einem str in ein int um
            if linie_int < 100:                                                         # prüft ob es eine Straßenbahnlinie ist
                ges_linie_list.append(linie)
    ges_linien = set(ges_linie_list)                                                    # erstellt eine Liste mit Straßenbahnlinen die gesucht werden sollen.

    umstig_in_dict2 = {}
    for ges_linie in ges_linien:                                                        # iteriert über die Liste der gesuchten Linien
            umstig_in_list = []
            umstig_in_end = []
            for hsb_dict in prop_dict:
                linien_u = hsb_dict.get("Linien", "").split()                           #iteriert über die Datensätze bis zu den einzelnen Linien Nr.   
                if ges_linie in linien_u:                                               # prüft ob die gesucht Linie in den Linien an den HSB vorkommt
                    for linie in linien_u:
                        linie_u = int(linie)                                            # gibt die Linien aus dem HSB einzeln weiter
                        if linie_u < 100 and linie != ges_linie and linie_u != 0:       # prüft ob die Linie ein Bus (>100), selbst die gesuchte Zahl oder eine aufgefüllte 0 ist
                            umstig_in_list.append(linie_u)                              # fügt nur Straßenbahnlinien der Liste zu
                            umstig_in_end = sorted(set(umstig_in_list))                 # entfernt doppelte Linien und sortiert die Liste
                            umstig_in_dict2.update({ges_linie: umstig_in_end})          # fügt die Liste einem Dictionary mit dem Key der gesuchten Linie an
                            
    return (umstig_in_dict2)                                                            # gibt ein Dictionary mit den Straßenbahnlinien als Key und Listen der Umstigsmöglickeiten zurück
