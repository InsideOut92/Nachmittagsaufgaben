# -*- coding: utf-8 -*-

import product

class Stoff(product.Product):
    def __init__(self, name, description, price, productnumber, discount,
                 manufacturing_location, manufacturing_type, length, width,
                 color, material):
        super().__init__(name, description, price, productnumber, discount,
                         manufacturing_location, manufacturing_type)
        self.length = length
        self.width = width
        self.color = color
        self.material = material

    def __str__(self):
        return (f"{self.name} kostet {self.price} \n"
                f"Beschreibung: {self.description} \n"
                f"Produktnummer: {self.productnumber} \n"
                f"Aktuelle Rabatte: {self.discount} \n"
                f"Herstellungsort: {self.manufacturing_location} \n"
                f"Herstellungsart: {self.manufacturing_type} \n"
                f"Länge: {self.length} - Breite: {self.width} \n"
                f"Farbe: {self.color} - Material: {self.material} \n")

if __name__ == '__main__':
    stoff = Stoff("Baumwolle Rot", "a roter Wollstoff, ge.",
                  28.99, 1565168, ["10%", "24%"],
                  "Rottendorf, Deutschland",
                  "maschinell", 2000, 4000,
                  "Rot", "Baumwolle" )

    print(stoff)
    print(isinstance(stoff, product.Product))
    print(isinstance(stoff, Stoff))