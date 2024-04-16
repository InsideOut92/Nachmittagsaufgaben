from product import Product
from Stoff import Stoff

class Produktkatalog:
    def __init__(self):
        self.produkte = []

    def produkt_hinzufuegen(self, product):
        self.produkte.append(product)

    def produkt_entfernen(self, product):
        self.produkte.remove(product)

    def produktkatalog_anzeigen(self):
        for product in self.produkte:
            print(product)

    def produktkatalog_speichern(self, file):
        with open(file, 'w') as f:
            for product in self.produkte:
                if isinstance(product, Stoff):
                    f.write(
                        f"{product.name},{product.description},{product.price},{product.productnumber},"
                        f"{','.join(product.discount)},{product.manufacturing_location},{product.manufacturing_type},"
                        f"{product.length},{product.width},{product.color},{product.material}\n")
                else:
                    f.write(
                        f"{product.name},{product.description},{product.price},{product.productnumber},"
                        f"{','.join(product.discount)},{product.manufacturing_location},{product.manufacturing_type}\n")

    @classmethod
    def produktkatalog_laden(cls, file):
        produktkatalog = cls()
        with open(file, 'r') as f:
            for line in f:
                product_info = line.strip().split(',')
                name = product_info[0]
                description = product_info[1]
                price = float(product_info[2])
                productnumber = int(product_info[3])
                discount = product_info[4].split('|')
                manufacturing_location = ','.join(product_info[5:-5])
                manufacturing_type = product_info[-5]
                if len(product_info) > 7:
                    length = int(product_info[-4])
                    width = int(product_info[-3])
                    color = product_info[-2]
                    material = product_info[-1]
                    product = Stoff(name, description, price, productnumber, discount, manufacturing_location,
                                    manufacturing_type, length, width, color, material)
                else:
                    product = Product(name, description, price, productnumber, discount, manufacturing_location,
                                      manufacturing_type)
                produktkatalog.produkt_hinzufuegen(product)
        return produktkatalog


if __name__ == '__main__':
    # Erstellen eines Produktkatalogs
    katalog = Produktkatalog()

    # Hinzufügen eines Stoffprodukts zum Katalog
    stoff1 = Stoff("Baumwolle Rot", "Ein roter Wollstoff.", 28.99, 1565168, ["10%", "24%"],
                  "Rottendorf, Deutschland", "maschinell", 2000, 4000, "Rot", "Baumwolle")
    katalog.produkt_hinzufuegen(stoff1)

    # Anzeigen des Produktkatalogs
    print("Produktkatalog:")
    katalog.produktkatalog_anzeigen()

    # Speichern des Produktkatalogs in einer Datei
    katalog.produktkatalog_speichern("produktkatalog.txt")

    # Laden des Produktkatalogs aus der Datei
    neuer_katalog = Produktkatalog.produktkatalog_laden("produktkatalog.txt")
    print("\nNeu geladener Produktkatalog:")
    neuer_katalog.produktkatalog_anzeigen()
