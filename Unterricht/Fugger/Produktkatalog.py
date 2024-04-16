# -*- coding: utf-8 -*-

from product import Product
from Stoff import Stoff


class Produktkatalog:
    def __init__(self):
        self.produkte = {}

    def produkt_hinzufuegen(self, product):
        self.produkte[product.productnumber] = product
        print("Produkt erfolgreich hinzugefügt!")

    def produkt_entfernen(self, productnumber):
        if productnumber in self.produkte:
            del self.produkte[productnumber]
            print("Produkt erfolgreich entfernt!")
        else:
            print("Das Produkt ist nicht im Katalog.")

    def produktkatalog_anzeigen(self):
        if self.produkte:
            print("Produktkatalog:")
            for productnumber, product in self.produkte.items():
                print(f"Produktnummer: {productnumber}")
                print(product)
                print()
        else:
            print("Der Produktkatalog ist leer.")

    def produktkatalog_speichern(self, file):
        try:
            with open(file, 'w') as f:
                for productnumber, product in self.produkte.items():
                    if isinstance(product, Stoff):
                        f.write(
                            f"{product.name},{product.description},{product.price},{product.productnumber},"
                            f"{','.join(product.discount)},{product.manufacturing_location},{product.manufacturing_type},"
                            f"{product.length},{product.width},{product.color},{product.material}\n")
                    else:
                        f.write(
                            f"{product.name},{product.description},{product.price},{product.productnumber},"
                            f"{','.join(product.discount)},{product.manufacturing_location},{product.manufacturing_type}\n")
            print("Produktkatalog erfolgreich gespeichert!")
        except IOError:
            print("Fehler beim Speichern des Produktkatalogs.")

    @classmethod
    def produktkatalog_laden(cls, file):
        try:
            produktkatalog = cls()
            with open(file, 'r') as f:
                for line in f:
                    product_info = line.strip().split(',')
                    name = product_info[0]
                    description = product_info[1]
                    price = float(product_info[2])
                    productnumber = int(product_info[3])
                    discount = product_info[4].split('|')
                    manufacturing_location = product_info[5]
                    manufacturing_type = product_info[6]
                    if len(product_info) > 7:
                        length = int(product_info[7])
                        width = int(product_info[8])
                        color = product_info[9]
                        material = product_info[10]
                        product = Stoff(name, description, price, productnumber, discount, manufacturing_location,
                                        manufacturing_type, length, width, color, material)
                    else:
                        product = Product(name, description, price, productnumber, discount, manufacturing_location,
                                          manufacturing_type)
                    produktkatalog.produkt_hinzufuegen(product)
            print("Produktkatalog erfolgreich geladen!")
            return produktkatalog
        except IOError:
            print("Fehler beim Laden des Produktkatalogs.")


def main():
    print("Willkommen im Produktkatalog-Programm!")
    katalog = Produktkatalog()

    while True:
        print("\nBitte wählen Sie eine Option:")
        print("1. Produkt hinzufügen")
        print("2. Produkt entfernen")
        print("3. Produktkatalog anzeigen")
        print("4. Produktkatalog speichern")
        print("5. Produktkatalog laden")
        print("6. Beenden")

        choice = input("Ihre Auswahl: ")

        if choice == "1":
            name = input("Bitte geben Sie den Produktnamen ein: ")
            description = input("Bitte geben Sie die Produktbeschreibung ein: ")
            price = float(input("Bitte geben Sie den Preis ein: "))
            productnumber = int(input("Bitte geben Sie die Produktnummer ein: "))
            discount = input("Bitte geben Sie die Rabatte ein (getrennt durch Kommas): ").split(',')
            manufacturing_location = input("Bitte geben Sie den Herstellungsort ein: ")
            manufacturing_type = input("Bitte geben Sie die Herstellungsart ein: ")
            length = int(input("Bitte geben Sie die Länge ein: "))
            width = int(input("Bitte geben Sie die Breite ein: "))
            color = input("Bitte geben Sie die Farbe ein: ")
            material = input("Bitte geben Sie das Material ein: ")
            product = Stoff(name, description, price, productnumber, discount, manufacturing_location,
                            manufacturing_type, length, width, color, material)
            katalog.produkt_hinzufuegen(product)

        elif choice == "2":
            productnumber = int(input("Bitte geben Sie die Produktnummer des zu entfernenden Produkts ein: "))
            katalog.produkt_entfernen(productnumber)

        elif choice == "3":
            katalog.produktkatalog_anzeigen()

        elif choice == "4":
            filename = input("Bitte geben Sie den Dateinamen für die Speicherung ein: ")
            katalog.produktkatalog_speichern(filename)

        elif choice == "5":
            filename = input("Bitte geben Sie den Dateinamen für das Laden ein: ")
            katalog = Produktkatalog.produktkatalog_laden(filename)

        elif choice == "6":
            print("Das Programm wird beendet.")
            break

        else:
            print("Ungültige Auswahl!")


if __name__ == "__main__":
    main()
