def divide_numbers():
    while True:
        try:
            numerator = float(input("Bitte gib den Zähler ein: "))
            denominator = float(input("Bitte gib den Nenner ein: "))
            
            result = numerator / denominator
            return result
            

        except (ValueError, ZeroDivisionError) as e:
            if isinstance(e, ValueError):
                print("Ungültige Eingabe: Bitte gib eine gültige Zahl ein.")
            elif isinstance(e, ZeroDivisionError):
                print("Fehler: Division durch Null ist nicht erlaubt.")

divide_numbers()