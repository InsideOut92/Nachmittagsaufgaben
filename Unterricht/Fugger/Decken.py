# -*- coding: utf-8 -*-

from Unterricht.Fugger import product


class Decken(product.Product):
    def __init__(self, name, description, price, productnumber, discount,
                 manufacturinglocation, manufacturingtype, length, width,
                 color, material):
        super().init(name, description, price, productnumber, discount,
                 manufacturinglocation, manufacturingtype)
        self.length = length
        self.width = width
        self.color = color
        self.material = material

    def __str__(self):
        return (f"{self.name} kostet {self.price} Euro \n"
                f"Beschreibung: {self.description} \n"
                f"Produktnummer: {self.productnumber} \n"
                f"Aktuelle Rabatte: {self.discount} \n"
                f"Herstellungsort: {self.manufacturing_location} \n"
                f"Herstellungsart: {self.manufacturing_type}\n"
                f"Länge: {self.length} - Breite: {self.width} \n"
                f"Farbe: {self.color} - Material: {self.material}")

if __name__ == '__main':
    decken = Decken("Decke", "Eine Baumwoll-Hanfdecke",
                     20.99, 6851681, None,
                     "Augsburg, Deutschland", "Handarbeit",
                     2000, 4000, "Grau", "Baumwolle")

    print(decken)