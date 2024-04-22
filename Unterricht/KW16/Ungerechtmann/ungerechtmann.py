import Pruefling

# Umgebungsvariable, Konstante
LISTE_PRUEFLING = []
# Leere Liste, die später mehrere Objekte der Klasse Prüfling aufnehmen soll.

# Rundungsfunktion
def round_to_half(grade):
    return round(grade * 2) / 2

# Berechnung der finalen Note für einen Prüfling basierend auf dem Wetter
def berechnung(pruefling, wetter):
    pruefung = pruefling.test_grade

    if pruefling.eye_color == "dunkel" and pruefling.hair_style == "lang":
        pruefling.final_grade = round_to_half(pruefling.test_grade * 1.1)
    elif pruefling.eye_color == "dunkel" and pruefling.hair_style == "kurz":
        pruefling.final_grade = round_to_half(pruefling.test_grade * 0.9)
    elif pruefling.eye_color == "hell" and pruefling.hair_style == "lang":
        pruefling.final_grade = round_to_half(pruefling.test_grade * 1.1)
    elif pruefling.eye_color == "hell" and pruefling.hair_style == "kurz":
        pruefling.final_grade = round_to_half(pruefling.test_grade * 0.9)
    else:
        print("Es ist ein Fehler aufgetreten")
        return

    if wetter == "schön":
        pruefling.final_grade -= 1

    # Stelle sicher, dass die Abschlussnote zwischen 1 und 6 liegt
    pruefling.final_grade = max(1, min(6, pruefling.final_grade))

    print(pruefling)
    print(f"Das Wetter war: {wetter}")

# Berechnung der finalen Noten für alle Prüflinge in der Liste
def final_grade_calculation(wetter):
    for pruefling in LISTE_PRUEFLING:
        # Berechne die Abschlussnote für jeden Prüfling
        berechnung(pruefling, wetter)
        print(pruefling)
        print(f"Das Wetter war: {wetter}")

# Prüfling hinzufügen
def add_pruefling():
    # Benutzereingabe mit Validierung für Augenfarbe
    eye_color = input("Augenfarbe (dunkel/hell): ").lower()
    while eye_color not in ["dunkel", "hell"]:
        print("Ungültige Eingabe! Bitte entweder 'dunkel' oder 'hell' eingeben: ")
        eye_color = input("Augenfarbe (dunkel/hell): ").lower()

    # Benutzereingabe mit Validierung für Haarlänge
    hair_style = input("Haarlänge, kurz oder lang: ").lower()
    while hair_style not in ["kurz", "lang"]:
        print("Ungültige Eingabe! Bitte entweder 'kurz' oder 'lang' eingeben: ")
        hair_style = input("Haarlänge, kurz oder lang: ").lower()

    # Benutzereingabe mit Validierung für Prüfungsnote
    while True:
        try:
            test_grade = float(input("Prüfungsnote (1.0 bis 6.0): "))
            if 1.0 <= test_grade <= 6.0:
                break
            else:
                print("Ungültige Eingabe! Bitte eine Note zwischen 1.0 und 6.0 ein: ")
        except ValueError:
            print("Ungültige Eingabe! Bitte eine gültige Zahl zwischen 1.0 und 6.0 eingeben: ")

    # Benutzereingabe Vorname und Nachname
    firstname = input("Vorname: ")
    lastname = input("Nachname: ")

    # Prüfling der Liste "LISTE_PRUEFLING" hinzufügen
    pruefling = Pruefling.Pruefling(eye_color, hair_style, test_grade, firstname, lastname,)
    LISTE_PRUEFLING.append(pruefling)

    print("Prüfling wurde erfolgreich hinzugefügt :)")

# Funktion zum Speichern der Prüflinge in einer Textdatei
def save_prueflinge():
    with open("prueflinge.txt", "w") as file:
        for pruefling in LISTE_PRUEFLING:
            file.write(f"{pruefling.firstname},{pruefling.lastname},{pruefling.eye_color},{pruefling.hair_style},{pruefling.test_grade}\n")
    print("Prüflinge erfolgreich gespeichert.")

# Funktion zum Laden der Prüflinge aus der Textdatei
def load_prueflinge():
    try:
        with open("prueflinge.txt", "r") as file:
            for line in file:
                data = line.strip().split(",")
                firstname, lastname, eye_color, hair_style, test_grade = data
                pruefling = Pruefling.Pruefling(eye_color, hair_style, float(test_grade), firstname, lastname)
                LISTE_PRUEFLING.append(pruefling)
        print("Prüflinge erfolgreich geladen.")
    except FileNotFoundError:
        print("Es wurden noch keine Prüflinge gespeichert.")

# Menü anzeigen
def show_menu():
    print("\nMenü:")
    print("1. Prüfling hinzufügen")
    print("2. Abschlussnoten berechnen")
    print("3. Programm beenden")

# Main-funktion
def main():
    while True:
        show_menu()
        choice = input("Bitte wähle eine Option zwischen 1 und 3: ")

        if choice == "1":
            add_pruefling()
        elif choice == "2":
            if not LISTE_PRUEFLING:
                print("Es wurden keine Prüflinge hinzugefügt.")
            else:
                wetter = input("Wetter 'schön' oder 'nicht schön' ?").lower()
                final_grade_calculation(wetter)
        elif choice == "3":
            # speichern der neu angelegten Prüflinge in .txt Datei
            save_prueflinge()
            print("Festplatte wird formatiert.")
            break
        else:
            print("Ungültige Eingabe! Bitte wähle eine Option zwischen 1 und 3.")

if __name__ == "__main__":
    main()
