# Importieren der ast-Bibliothek für die Auswertung von Python-Ausdrücken aus einer Datei
import ast

# Definition der Klasse FitnessstudioPreisgestaltung
class FitnessstudioPreisgestaltung:
    def __init__(self, basispreis, altersgruppe, geschlecht, bmi, soziale_netzwerke, freunde_anzahl, bild_post_anzahl,
                 trainingstage):
        self.basispreis = basispreis
        self.altersgruppe = altersgruppe
        self.geschlecht = geschlecht
        self.bmi = bmi
        self.soziale_netzwerke = soziale_netzwerke
        self.freunde_anzahl = freunde_anzahl
        self.bild_post_anzahl = bild_post_anzahl
        self.trainingstage = trainingstage

    # Methode zur Berechnung des Mitgliedsbeitrags
    def preis_berechnen(self):
        preis = self.basispreis

        # Rabatte basierend auf Altersgruppe
        if 20 <= self.altersgruppe <= 60:
            preis *= 0.9  # 10% Rabatt für Frauen zwischen 20 und 60 Jahren
        elif self.altersgruppe < 20:
            if 18.5 <= self.bmi <= 24.9:
                preis *= 0.8  # 20% Rabatt für Personen unter 20 Jahren mit normalem BMI

        # Rabatt für Personen über 60 Jahren mit sozialen Aktivitäten
        if self.altersgruppe > 60 and self.soziale_netzwerke and self.freunde_anzahl >= 50 and self.bild_post_anzahl >= 3:
            preis *= 0.7  # 30% Rabatt für Personen über 60 Jahren mit sozialen Aktivitäten

        # Rabatt für Sommertraining
        if 3 <= self.trainingstage <= 6:
            preis *= 0.95  # 5% Rabatt für Sommertraining

        return round(preis, 2)  # Auf zwei Dezimalstellen runden

# Funktion zur Verarbeitung der Mitgliederdaten
def process_member_data(file_path):
    members = []
    try:
        with open(file_path, 'r') as file:
            # Lese den Inhalt der Datei
            content = file.read()
            # Entferne das Präfix "members = " aus dem Inhalt
            content = content.replace("members =", "")
            # Verwende ast.literal_eval, um den Inhalt als Python-Code zu interpretieren
            parsed_content = ast.literal_eval(content.strip())
            if isinstance(parsed_content, list):
                members = parsed_content
            else:
                print("Die Datei enthält keine Liste von Mitgliedern.")
    except Exception as e:
        print(f"Fehler beim Verarbeiten der Datei: {e}")
    return members

# Beispielaufruf der Funktion
file_path = 'example_data.txt'
members = process_member_data(file_path)
print("Extrahierte Mitgliederdaten:")
print(members)

# Hauptmenüfunktion
def main_menu():
    print("Willkommen zum Fitnessstudio-Preisgestaltungsprogramm!")
    print("Bitte wählen Sie eine Option:")
    print("1. Mitgliedsbeitrag für neues Mitglied berechnen")
    print("2. Mitgliedsbeitrag für vorhandene Mitglieder aktualisieren")
    print("3. Mitgliedsdaten hinzufügen")
    print("4. Mitgliedsdaten anzeigen")
    print("5. Beenden")

# Funktion zur Berechnung des Mitgliedsbeitrags für ein neues Mitglied
def calculate_new_member_price():
    basispreis = float(input("Bitte geben Sie den Basispreis ein: "))
    altersgruppe = int(input("Bitte geben Sie die Altersgruppe ein: "))
    geschlecht = input("Bitte geben Sie das Geschlecht ein (m/w): ")
    bmi = float(input("Bitte geben Sie den BMI ein: "))
    soziale_netzwerke = input("Hat die Person soziale Netzwerke (ja/nein): ").lower() == "ja"
    freunde_anzahl = int(input("Bitte geben Sie die Anzahl der Freunde ein: "))
    bild_post_anzahl = int(input("Bitte geben Sie die Anzahl der Bildposts ein: "))
    trainingstage = int(input("Bitte geben Sie die Anzahl der Trainingstage ein: "))

    preisgestaltung = FitnessstudioPreisgestaltung(basispreis, altersgruppe, geschlecht, bmi, soziale_netzwerke, freunde_anzahl, bild_post_anzahl, trainingstage)
    preis = preisgestaltung.preis_berechnen()
    print("Der Mitgliedsbeitrag beträgt:", preis, "Euro")

# Funktion zur Aktualisierung des Mitgliedsbeitrags für ein vorhandenes Mitglied
def update_existing_member_price():
    mitglieds_id = input("Bitte geben Sie die Mitglieds-ID des zu aktualisierenden Mitglieds ein: ")

# Funktion zur Hinzufügung von Mitgliedsdaten
def add_member_data():
    neue_daten = input("Bitte geben Sie die Daten des neuen Mitglieds ein (Format: 'Name, Alter, Geschlecht, BMI, Freunde, Bildposts, Trainingstage'): ")
    neue_daten_liste = neue_daten.split(',')
    members.append(neue_daten_liste)

# Funktion zur Anzeige der Mitgliedsdaten
def display_member_data():
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

# Main-Programm
if __name__ == "__main__":
    while True:
        main_menu()
        choice = input("Bitte geben Sie die Nummer Ihrer Auswahl ein: ")

        if choice == "1":
            calculate_new_member_price()
        elif choice == "2":
            update_existing_member_price()
        elif choice == "3":
            add_member_data()
        elif choice == "4":
            display_member_data()
        elif choice == "5":
            print("Das Programm wird beendet.")
            break
        else:
            print("Ungültige Auswahl. Bitte geben Sie eine der angegebenen Nummern ein.")
