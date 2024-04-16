# -*- coding: utf-8 -*-

from product import Product
from Unterricht.Fugger.Stoff import Stoff


class Textilien(Product):
    def __init__(self, name, description, price, productnumber, discount,
                 manufacturing_location, manufacturing_type, stoff_list):
        super().__init__(name, description, price, productnumber, discount,
                         manufacturing_location, manufacturing_type)

        self.stoff_list = stoff_list
        # kann Liste oder ein einzelnes Objekt sein

    def print_Material(self):
        for stoff in self.stoff_list:
            print(stoff)

    def __str__(self):
        return (f"{self.name} kostet {self.price} Euro\n"
                f"Beschreibung: {self.description} \n"
                f"Produktnummer: {self.productnumber} \n"
                f"Aktuelle Rabatte: {self.discount} \n"
                f"Herstellungsort: {self.manufacturing_location} \n"
                f"Herstellungsart: {self.manufacturing_type} \n"
                f"Stoffliste: {self.print_Material()}")

if __name__ == '__main__':
    baumwolle = Stoff("Baumwolle Rot", "a roter Wollstoff, ge.",
                      28.99, 1565168, ["10%", "24%"],
                      "Rottendorf, Deutschland",
                      "maschinell", 2000, 4000,
                      "Rot", "Baumwolle")
    polyester = Stoff("Polyester Grau", "Ein grauer Polyesterstoff", 29.99,
                      1565167, None, "Shenzen, China", "maschinell",
                      1000, 1000, "Grau", "Polyester")
    hanf = Stoff("Hanf braun", "Brauner Hanfstoff", 12.99, 684175,
                 ["45%", "10%", "15%", "20%"], "Hamburg, Deutschland",
                 "maschinell", 3000, 4000, "Braun", "Hanf")
    textil1 = Textilien("Hanfdecke", "eine gut duftende Decke aus Hanf",
                        99.99, 123456, None,
                        "Würzburg, Deutschland", "hanfarbeit",
                        [baumwolle, hanf])
    textil2 = Textilien("Abendkleid", "das schicke schwarze", 129.99,
                        123457, None, "Würzburg, Deutschland",
                        "maschinell", [baumwolle, polyester, polyester, polyester])

    this_set = {textil1, textil2, textil1}
    for textil in this_set:
        print(textil)

