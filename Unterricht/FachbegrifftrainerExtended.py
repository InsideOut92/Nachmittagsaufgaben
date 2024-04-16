import random
import json

class Fachbegrifftrainer:
    """Eine Klasse zum Verwalten und Üben von Fachbegriffen."""

    def __init__(self):
        """Initialisiert einen leeren Fachbegrifftrainer."""
        self.fachbegriffe = {}

    def add_fachbegriff(self, fachbegriff, definition):
        """Fügt einen Fachbegriff und seine Definition hinzu."""
        self.fachbegriffe[fachbegriff] = definition

    def remove_fachbegriff(self, fachbegriff):
        """Entfernt einen Fachbegriff aus der Liste."""
        if fachbegriff in self.fachbegriffe:
            del self.fachbegriffe[fachbegriff]
            print(f"{fachbegriff} wurde erfolgreich entfernt.")
        else:
            print(f"{fachbegriff} ist nicht in der Liste der Fachbegriffe.")

    def practice(self):
        """Übt die Fachbegriffe."""
        if not self.fachbegriffe:
            print("Die Liste der Fachbegriffe ist leer. Fügen Sie zuerst Fachbegriffe hinzu.")
            return

        print("Willkommen zum Fachbegrifftraining!")
        fachbegriffe_list = list(self.fachbegriffe.items())
        random.shuffle(fachbegriffe_list)  # Zufällige Reihenfolge der Fachbegriffe
        for fachbegriff, definition in fachbegriffe_list:
            print(f"Fachbegriff: {fachbegriff}")
            try:
                input("Drücken Sie Enter, um die Definition anzuzeigen: ")
                print(f"Definition: {definition}")
                input("Drücken Sie Enter, um zum nächsten Fachbegriff zu gelangen: ")
            except KeyboardInterrupt:
                print("\nTraining abgebrochen.")
                return
        print("Das Training ist abgeschlossen.")

    def repeat_training(self):
        """Startet das Training erneut."""
        while True:
            self.practice()
            while True:
                repeat = input("Möchten Sie das Training wiederholen? (ja/nein): ").lower()
                if repeat in ('ja', 'nein'):
                    break
                else:
                    print("MÖP! Ungültige Eingabe! Bitte gib 'ja' oder 'nein' ein.")
            if repeat != 'ja':
                print("Auf Wiedersehen!")
                break

    def save_to_file(self, filename):
        """Speichert die Fachbegriffe in einer JSON-Datei."""
        with open(filename, 'w') as file:
            json.dump(self.fachbegriffe, file)
        print("Fachbegriffe erfolgreich in die Datei gespeichert.")

    def load_from_file(self, filename):
        """Lädt die Fachbegriffe aus einer JSON-Datei."""
        with open(filename, 'r') as file:
            self.fachbegriffe = json.load(file)
        print("Fachbegriffe aus der Datei geladen.")
        # Fachbegriffe zur Liste hinzufügen
        for fachbegriff, definition in self.fachbegriffe.items():
            self.add_fachbegriff(fachbegriff, definition)

    def menu(self):
        """Zeigt das Menü und führt die ausgewählte Funktion aus."""
        while True:
            print("\n*** Menü ***")
            print("1. Fachbegriff hinzufügen")
            print("2. Fachbegriff entfernen")
            print("3. JSON-Datei laden")
            print("4. Training starten")
            print("5. Beenden")

            choice = input("Wählen Sie eine Option (1-5): ")
            if choice == '1':
                fachbegriff = input("Geben Sie den Fachbegriff ein: ")
                definition = input("Geben Sie die Definition ein: ")
                self.add_fachbegriff(fachbegriff, definition)
            elif choice == '2':
                fachbegriff = input("Geben Sie den zu entfernenden Fachbegriff ein: ")
                self.remove_fachbegriff(fachbegriff)
            elif choice == '3':
                filename = input("Geben Sie den Dateinamen ein: ")
                self.load_from_file(filename)
            elif choice == '4':
                self.repeat_training()
            elif choice == '5':
                print("Auf Wiedersehen!")
                break
            else:
                print("Ungültige Eingabe! Bitte wählen Sie eine Option zwischen 1 und 5.")

# Erstellen einer Instanz des Fachbegrifftrainers
trainer = Fachbegrifftrainer()

# Laden der Fachbegriffe aus einer JSON-Datei oder Erstellen neuer Fachbegriffe
try:
    trainer.load_from_file("fachbegriffe.json")
    print("Fachbegriffe erfolgreich aus der Datei geladen.")
except FileNotFoundError:
    print("Die Datei wurde nicht gefunden. Es werden neue Fachbegriffe erstellt.")

# Menü anzeigen und Funktionen ausführen
trainer.menu()
