# Definition der Klasse für die Benutzerinteraktion und -eingabe
from Unterricht.KW16.Ungerechtmann.Fitnessstudio.FitnessstudioPreisgestaltung import FitnessstudioPreisgestaltung
from Unterricht.KW16.Ungerechtmann.Fitnessstudio.Hauptmenü import Hauptmenu
from Unterricht.KW16.Ungerechtmann.Fitnessstudio.Mitgliederdatenverwaltung import Mitgliederdatenverarbeitung


class Benutzerinteraktion:
    @staticmethod
    def calculate_new_member_price():
        basispreis = float(input("Bitte geben Sie den Basispreis ein: "))
        altersgruppe = int(input("Bitte geben Sie die Altersgruppe ein: "))
        geschlecht = input("Bitte geben Sie das Geschlecht ein (m/w): ")
        bmi = float(input("Bitte geben Sie den BMI ein: "))
        soziale_netzwerke = input("Hat die Person soziale Netzwerke (ja/nein): ").lower() == "ja"
        freunde_anzahl = int(input("Bitte geben Sie die Anzahl der Freunde ein: "))
        bild_post_anzahl = int(input("Bitte geben Sie die Anzahl der Bildposts ein: "))
        trainingstage = int(input("Bitte geben Sie die Anzahl der Trainingstage ein: "))

        preisgestaltung = FitnessstudioPreisgestaltung(basispreis, altersgruppe, geschlecht, bmi, soziale_netzwerke,
                                                       freunde_anzahl, bild_post_anzahl, trainingstage)
        preis = preisgestaltung.preis_berechnen()
        print("Der Mitgliedsbeitrag beträgt:", preis, "Euro")

    @staticmethod
    def update_existing_member_price():
        mitglieds_id = input("Bitte geben Sie die Mitglieds-ID des zu aktualisierenden Mitglieds ein: ")

    @staticmethod
    def add_member_data(members):
        neue_daten = input(
            "Bitte geben Sie die Daten des neuen Mitglieds ein (Format: 'Name, Alter, Geschlecht, BMI, Freunde, Bildposts, Trainingstage'): ")
        neue_daten_liste = neue_daten.split(',')
        members.append(neue_daten_liste)

    @staticmethod
    def display_member_data(members):
        print("Mitgliedsdaten:")
        for mitglied in members:
            print("Name:", mitglied['name'])
            print("Alter:", mitglied['age'])
            print("Geschlecht:", mitglied['gender'])
            print("BMI:", mitglied['bmi'])
            print("Freunde:", mitglied['social_friends'])
            print("Bildposts:", mitglied['posts_per_week'])
            print("Trainingstage:", mitglied['training_frequency'])
            print("\n")


# Hauptprogramm
if __name__ == "__main__":
    members = Mitgliederdatenverarbeitung.process_member_data('example_data.txt')
    print("Extrahierte Mitgliederdaten:")
    print(members)

    benutzeraktion = Benutzerinteraktion()
    while True:
        Hauptmenu.main_menu()
        choice = input("Bitte geben Sie Ihre Auswahl ein: ")

        if choice == "1":
            benutzeraktion.calculate_new_member_price()
        elif choice == "2":
            benutzeraktion.update_existing_member_price()
        elif choice == "3":
            benutzeraktion.add_member_data(members)
        elif choice == "4":
            benutzeraktion.display_member_data(members)
        elif choice == "5":
            print("Das Programm wird beendet.")
            break
        else:
            print("Ungültige Auswahl. Bitte geben Sie eine der angegebenen Nummern ein.")