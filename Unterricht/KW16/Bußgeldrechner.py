def berechne_basisbusgeld(ort, geschwindigkeitsueberschreitung):
    if ort == "innerorts":
        if 1 <= geschwindigkeitsueberschreitung <= 10:
            return 30
        elif 11 <= geschwindigkeitsueberschreitung <= 20:
            return 60
        elif 21 <= geschwindigkeitsueberschreitung <= 30:
            return 120
    elif ort == "außerorts":
        if 1 <= geschwindigkeitsueberschreitung <= 10:
            return 20
        elif 11 <= geschwindigkeitsueberschreitung <= 20:
            return 50
        elif 21 <= geschwindigkeitsueberschreitung <= 30:
            return 100
    return 0  # Standardwert, wenn keine Bedingung erfüllt ist

def berechne_aufschlaege_rabatte(wetterbedingungen, fahrzeugzustand, unfallbeteiligung, teilschuld, wiederholungstaeter):
    aufschlag_wetter = 0
    aufschlag_zustand = 0
    aufschlag_unfall = 0
    aufschlag_wiederholung = 0

    if wetterbedingungen.lower() in ['regen', 'schnee']:
        aufschlag_wetter = 0.20

    if fahrzeugzustand.lower() == 'mängel':
        aufschlag_zustand = 0.10

    if unfallbeteiligung.lower() == 'ja':
        aufschlag_unfall = 0.30
        if teilschuld.lower() == 'ja':
            aufschlag_unfall *= 0.5  # Reduzierung um 15%

    if wiederholungstaeter.lower() == 'ja':
        aufschlag_wiederholung = 0.10

    return aufschlag_wetter, aufschlag_zustand, aufschlag_unfall, aufschlag_wiederholung

def berechne_endgueltiges_bussgeld(basisbussgeld, aufschlag_wetter, aufschlag_zustand, aufschlag_unfall, aufschlag_wiederholung):
    endgueltiges_bussgeld = basisbussgeld + (basisbussgeld * (aufschlag_wetter + aufschlag_zustand + aufschlag_unfall + aufschlag_wiederholung))
    endgueltiges_bussgeld = round(endgueltiges_bussgeld)
    return endgueltiges_bussgeld


def anzeigen_bussgeldkatalog():
    print("Bußgeldkatalog:")
    print("Innerorts:")
    print("- 1-10 km/h: 30€")
    print("- 11-20 km/h: 60€")
    print("- 21-30 km/h: 120€")
    print("Außerorts:")
    print("- 1-10 km/h: 20€")
    print("- 11-20 km/h: 50€")
    print("- 21-30 km/h: 100€")


def main():
    while True:
        print("\n--- Menü ---")
        print("1. Bußgeld berechnen")
        print("2. Bußgeldkatalog anzeigen")
        print("3. Beenden")

        choice = input("Bitte wählen Sie eine Option (1-3): ")

        if choice == "1":
            # Bußgeld berechnen
            ort = input("Bitte geben Sie den Ort des Verstoßes ein (innerorts/außerorts): ")
            geschwindigkeitsueberschreitung = int(
                input("Bitte geben Sie die Geschwindigkeitsüberschreitung in km/h ein: "))
            wetterbedingungen = input("Bitte geben Sie die Wetterbedingungen ein (klar, Regen, Schnee): ")
            fahrzeugzustand = input("Bitte geben Sie den Fahrzeugzustand ein (in Ordnung, Mängel): ")
            unfallbeteiligung = input("Gab es eine Unfallbeteiligung? (ja/nein): ")
            teilschuld = input("Hat ein anderer Fahrer Teilschuld am Unfall? (ja/nein): ")
            wiederholungstaeter = input("Ist der Fahrer ein Wiederholungstäter? (ja/nein): ")

            basisbussgeld = berechne_basisbusgeld(ort, geschwindigkeitsueberschreitung)
            aufschlag_wetter, aufschlag_zustand, aufschlag_unfall, aufschlag_wiederholung = berechne_aufschlaege_rabatte(
                wetterbedingungen, fahrzeugzustand, unfallbeteiligung, teilschuld, wiederholungstaeter)
            endgueltiges_bussgeld = berechne_endgueltiges_bussgeld(basisbussgeld, aufschlag_wetter, aufschlag_zustand,
                                                                   aufschlag_unfall, aufschlag_wiederholung)
            print("Das berechnete Bußgeld beträgt:", endgueltiges_bussgeld, "Euro")

        elif choice == "2":
            # Bußgeldkatalog anzeigen
            anzeigen_bussgeldkatalog()

        elif choice == "3":
            # Beenden
            print("Programm wird beendet.")
            break

        else:
            print("Ungültige Eingabe. Bitte wählen Sie eine der angegebenen Optionen.")


if __name__ == "__main__":
    main()
