# -*- coding: utf-8 -*-

from Unterricht.Fugger import product
class Kleidung(product.Product):
    def __init__(self, name, description, price, productnumber, discount,
                 manufacturinglocation, manufacturingtype, material, size,
                 brand):
        super().init(name, description, price, productnumber, discount,
                 manufacturinglocation, manufacturingtype)
        self.material = material
        self.size = size
        self.brand = brand

    def __str__(self):
        return (f"{self.name} kostet {self.price} Euro \n"
                f"Beschreibung: {self.description} \n"
                f"Produktnummer: {self.productnumber} \n"
                f"Aktuelle Rabatte: {self.discount} \n"
                f"Herstellungsort: {self.manufacturing_location} \n"
                f"Herstellungsart: {self.manufacturing_type}\n"
                f"Material: {self.material}"
                f"Groesse: {self.size}"
                f"Marke: {self.brand}")

if __name__ == '__main':
    kleidung = Kleidung("Hemd", "Ein roter Baumwoll-Pullover",
                         20.99, 6851681, None,
                         "Augsburg, Deutschland", "maschinell",
                         "Baumwolle", "L", "H&M")

    print(kleidung)