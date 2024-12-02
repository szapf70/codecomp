import random
from datetime import datetime, timedelta

def generiere_liste():
    startzeit = datetime.strptime("06:00:00", "%H:%M:%S")
    endzeit = datetime.strptime("14:00:00", "%H:%M:%S")
    zeit_intervall = timedelta(seconds=5)

    aktuelle_zeit = startzeit
    daten_liste = []

    while aktuelle_zeit <= endzeit:
        # Formatieren der aktuellen Zeit als String
        zeit_string = aktuelle_zeit.strftime("%H:%M:%S")

        # Generierung der normalverteilten Zufallswerte
        wert1 = str(round(random.gauss(80, 1),2))  # Mittelwert 80, Standardabweichung 1.05
        wert2 = str(round(random.gauss(10, 1),2))    # Mittelwert 10, Standardabweichung 1.2
        wert3 = str(round(random.gauss(50, 1),2))    # Mittelwert 50, Standardabweichung 1.03
        
        
        # Hinzufügen des Datensatzes zur Liste
        daten_liste.append([zeit_string, wert1, wert2, wert3])

        # Erhöhung der aktuellen Zeit um das Intervall
        aktuelle_zeit += zeit_intervall

    return daten_liste

# Generierung und Anzeige der Liste
liste = generiere_liste()

with open('station_16.log', 'w') as l:
    for eintrag in liste:
        l.write(";".join(eintrag)+'\n')
