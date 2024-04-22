import ast

# Definition der Klasse für die Preisgestaltung im Fitnessstudio
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

        # Auf zwei Dezimalstellen runden
        return round(preis, 2)