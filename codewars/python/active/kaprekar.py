start = int(input("Bitte ein Zahl zwischen 1 und 9998 (Ausnahme sind Zahlen mit vier gleichen Ziffern)"))

if start == 0 or start % 1111 == 0:
    print("Keine gültige Zahl")
else:
    versuche = 0
    while start != 6174:
        