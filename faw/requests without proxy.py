import os
import requests
# für curl  ----  curl -v --noproxy localhost, http://localhost:8080

def send_get_request():
    try:
        # Sende eine GET-Anfrage an localhost:8080
        os.environ['NO_PROXY'] = '127.0.0.1'
        response = requests.get('http://127.0.0.1:8080')

        # Überprüfe, ob die Anfrage erfolgreich war
        if response.status_code == 200:
            print("Antwort erhalten:")
            print(response.text)
        else:
            print(f"Fehler: Status Code {response.status_code}")
    except requests.exceptions.RequestException as e:
        print(f"Anfrage fehlgeschlagen: {e}")

# Führe die Funktion aus
send_get_request()

