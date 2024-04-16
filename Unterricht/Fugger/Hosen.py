# -*- coding: utf-8 -*-


from Kleidung import Kleidung

class Hosen(Kleidung):
    def __init__(self, name, description, price, productnumber, discount,
                 manufacturing_location, manufacturing_type, material, size,
                 brand, color, type, eu_size, us_size, leg_length):
        super().__init__(name, description, price, productnumber, discount,
                 manufacturing_location, manufacturing_type, material, size,
                 brand, color)
        self.type = type
        self.eu_size = eu_size
        self.us_size = us_size
        self.leg_length = leg_length

    def __str__(self):
        return (f"{self.name} \nkostet {self.price} Euro \n"
                f"Beschreibung: {self.description} \n"
                f"Produktnummer: {self.productnumber} \n"
                f"Aktuelle Rabatte: {self.discount} \n"
                f"Herstellungsort: {self.manufacturing_location} \n"
                f"Herstellungsart: {self.manufacturing_type}\n"
                f"Material: {self.material}"
                f"\nGroesse: {self.size}"
                f"\nMarke: {self.brand}"
                f"\nFarbe: {self.color}"
                f"\nTyp: {self.type}"
                f"\nGroesse EU: {self.eu_size}"
                f"\nGroesse US: {self.us_size}"
                f"\nBeinlaenge: {self.leg_length}")

if __name__ == '__main__':
    hosen = Hosen("Jeans", "Eine blaue Jeanshose",
                         35.99, 6851681, None,
                         "Nürnberg, Deutschland", "Maschinell",
                         "Denim", "XXL", "H&M", "Blau", "Jeans",
                         60, 62, 84)

    print(hosen)