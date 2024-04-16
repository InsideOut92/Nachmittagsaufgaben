class Auto:
    def __init__(self, kennzeichen, passengers, consumption, driver):
        self.kennzeichen = kennzeichen
        self.passengers = passengers
        self.consumption = consumption
        self.maxTank = 60.0
        self._speed = 0.0
        self.driver = driver

    def __str__(self):
        return (f"Das Auto hat das Kennzeichen {self.kennzeichen}, darin dürfen "
                f"{self.passengers} Personen sitzen.\n"
                f"Und das Auto verbraucht {self.consumption} Liter pro Kilometer.")

    def beschleunigung(self, t):
        for i in range(t):
            self._speed += 1.5
            print(f"Beschleunigung um 1.5 km/h, Geschwindigkeit: {self._speed} km/h")

    def bremsen(self, t):
        for i in range(t):
            if self._speed > 0:
                self._speed -= 1.0
                print(f"Bremsen um 1.0 km/h, Geschwindigkeit: {self._speed} km/h")
            else:
                print("Das Auto steht bereits.")


if __name__ == '__main__':
    print("Ausgabe die immer kommt!")
    print("Ich bin die Main-Datei!")
    auto = Auto("SJ-a 642", 5, 5.6, "Justin")
    auto2 = Auto("K-OEL 456", 2, 34.2, "Sebi")

    autoListe = [auto, auto2]

    for car in autoListe:
        print(car)
        car.beschleunigung(10)  # Beschleunigung um 10 Zeiteinheiten
        print(car)
        car.bremsen(5)  # Bremsen um 5 Zeiteinheiten
        print(car)
        if isinstance(car, Auto):
            car.beschleunigung(30)
            print(car)
        elif isinstance(car, int):  # Du hattest hier car**(car*2), das korrigiere ich zu car**2
            print(car**2)  # Berechne das Quadrat von car
        else:
            print("Ich heiße Marvin")
