import product

class Bestellung:
    def __init__(self):
        self.products = []

    def produkt_hinzufuegen(self, product):
        self.products.append(product)

    def produkt_entfernen(self, product):
        self.products.remove(product)

    def gesamtpreis_berechnen(self):
        gesamtpreis = sum(product.price for product in self.products)
        return gesamtpreis

    def bestellung_anzeigen(self):
        for product in self.products:
            print(product)
