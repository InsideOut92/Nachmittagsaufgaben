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
        for fachbegriff, definition in self.fachbegriffe.items():
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
                if repeat == 'ja' or repeat == 'nein':
                    break
                else:
                    print("MÖP! Ungültige Eingabe! Bitte gib 'ja' oder 'nein' ein.")
            if repeat != 'ja':
                print("Auf Wiedersehen!")
                break


# Erstellen einer Instanz des Fachbegrifftrainers
trainer = Fachbegrifftrainer()

# Hinzufügen der heute verwendeten Fachbegriffe und ihrer Definitionen
trainer.add_fachbegriff("Klasse", "Eine Vorlage zur Erzeugung von Objekten.")
trainer.add_fachbegriff("Objekt", "Eine Instanz einer Klasse.")
trainer.add_fachbegriff("Dynamische Typisierung", "Der Typ einer Variablen wird zur Laufzeit bestimmt und ist an das Objekt gebunden, nicht an die Variable selbst.")
trainer.add_fachbegriff("Klassenattribute", "Attribute, die in der Methode/Konstruktor '__init__()' definiert sind, um auf Klassenebene Daten zu speichern.")
trainer.add_fachbegriff("Datenstrukturen",
                        "Verschiedene Strukturen zur Speicherung von Werten: Listen, Dicts, Sets, Tuples.")
trainer.add_fachbegriff("Listen", "Geordnete, veränderbare Datenstruktur, die Duplikate erlaubt.")
trainer.add_fachbegriff("Dicts", "Geordnete, veränderbare Datenstruktur, die keine Duplikate erlaubt.")
trainer.add_fachbegriff("Sets", "Ungeordnete, veränderbare Datenstruktur, die keine Duplikate erlaubt.")
trainer.add_fachbegriff("Tuples", "Geordnete, unveränderbare Datenstruktur, die Duplikate erlaubt.")
trainer.add_fachbegriff("Überschreiben", "Das Ersetzen einer Methode in einer Unterklasse durch eine gleichnamige Methode der Oberklasse.")

# Training starten
trainer.repeat_training()
