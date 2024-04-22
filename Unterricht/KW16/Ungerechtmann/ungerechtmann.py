import Pruefling

# Umgebungsvariable, Konstante
LISTE_PRUEFLING = []
# Leere Liste, die später mehrere Objekte der Klasse Prüfling aufnehmen soll.

def berechnung(pruefling, wetter):
    pruefung = pruefling.test_grade

    if pruefling.eye_color == "dunkel" or pruefling.eye_color == 0:
        if pruefling.hair_style == "lang" or pruefling.hair_style == 1:
            pruefling.final_grade = pruefling.test_grade * 0.9
        else:
            pruefling.final_grade = pruefling.test_grade * 1.1
    elif (pruefling.eye_color == 1 or pruefling.eye_color == "hell") and (pruefling.hair_style == "kurz" or pruefling.hair_style == 0):
        pruefling.final_grade = pruefling.test_grade * 0.9
    elif ((pruefling.eye_color == 1 or pruefling.eye_color == 0) and (pruefling.hair_style == "lang" or pruefling.hair_style == 1)):
        pruefling.final_grade = pruefling.test_grade * 1.1
    else:
        print("Es ist ein Fehler aufgetreten")
        return

    if wetter == "schön":
        pruefling.final_grade -= 1

    if pruefling.final_grade > 6.0:
        pruefling.final_grade = 6.0
    elif pruefling.final_grade < 1.0:
        pruefling.final_grade = 1.0
    else:
        pruefling.final_grade = round(pruefling.final_grade * 2) / 2

def final_grade_calculation():
    i = 0
    count_prueflinge = len(LISTE_PRUEFLING)

    while i < count_prueflinge:
        berechnung(LISTE_PRUEFLING[i], wetter)
        print(LISTE_PRUEFLING[i])
        print("Das Wetter war: {wetter}")
        i = i + 1
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

# Funktion zum berechnen der Anschlussnoten
def calculate_final_grades():
    wetter = input("Wetter 'schön' oder 'nicht schön' ?").lower()
    for pruefling in LISTE_PRUEFLING:
        # Berechne die Abschlussnote für jeden Prüfling
        berechnung(pruefling, wetter)
        print(pruefling)
        print(f"Das Wetter war: {wetter}")

def show_menu():
    print("\nMenü:")
    print("1. Prüfling hinzufügen")
    print("2. Abschlussnoten berechnen")
    print("3. Programm beenden")



print(len(LISTE_PRUEFLING))

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
                calculate_final_grades()
        elif choice == "3":
            # speichern der neu angelegten Prüflinge in .txt Datei
            save_prueflinge()
            print("Festplatte wird formatiert.")
            break
        else:
            print("Ungültige Eingabe! Bitte wähle eine Option zwischen 1 und 3.")

if __name__ == "__main__":
    main()