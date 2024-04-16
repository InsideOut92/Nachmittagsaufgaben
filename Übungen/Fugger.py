import json

class Produkt:
    def __init__(self, name, produkt_nr, preis, fertigungsort):
        self.name = name
        self.produkt_nr = produkt_nr
        self.preis = preis
        self.fertigungsort = fertigungsort

class Kleidungsstueck(Produkt):
    def __init__(self, name, produkt_nr, preis, fertigungsort, groessen):
        super().__init__(name, produkt_nr, preis, fertigungsort)
        self.groessen = groessen

class Textilunternehmen:
    def __init__(self):
        self.produkte = []

    def neues_produkt(self, produkt):
        self.produkte.append(produkt)

    def produkt_bearbeiten(self, produkt_nr, attribut, wert):
        for produkt in self.produkte:
            if produkt.produkt_nr == produkt_nr:
                setattr(produkt, attribut, wert)
                break

    def produkt_loeschen(self, produkt_nr):
        for produkt in self.produkte:
            if produkt.produkt_nr == produkt_nr:
                self.produkte.remove(produkt)
                break

    def produkt_katalog_speichern(self, datei):
        with open(datei, 'w') as f:
            produkte_json = [vars(produkt) for produkt in self.produkte]
            json.dump(produkte_json, f)

    def produkt_katalog_laden(self, datei):
        with open(datei, 'r') as f:
            produkte_json = json.load(f)
            for produkt in produkte_json:
                if 'groessen' in produkt:
                    neues_produkt = Kleidungsstueck(**produkt)
                else:
                    neues_produkt = Produkt(**produkt)
                self.neues_produkt(neues_produkt)

# Beispiel zur Nutzung:
if __name__ == "__main__":
    textilunternehmen = Textilunternehmen()

    decke = Produkt("Decke", "1001", 29.99, "Deutschland")
    kleid = Kleidungsstueck("Kleid", "2001", 49.99, "Italien", {"International": "M", "US": "8", "Europa": "38"})
    hose = Produkt("Hose", "3001", 39.99, "China")
    hemd = Produkt("Hemd", "4001", 34.99, "Indien")

    textilunternehmen.neues_produkt(decke)
    textilunternehmen.neues_produkt(kleid)
    textilunternehmen.neues_produkt(hose)
    textilunternehmen.neues_produkt(hemd)

    textilunternehmen.produkt_katalog_speichern("produkte.json")

    # Änderungen am Produktkatalog vornehmen
    textilunternehmen.produkt_bearbeiten("2001", "preis", 59.99)
    textilunternehmen.produkt_loeschen("3001")

    textilunternehmen.produkt_katalog_speichern("produkte_geaendert.json")

    # Laden des geänderten Produktkatalogs
    textilunternehmen_neu = Textilunternehmen()
    textilunternehmen_neu.produkt_katalog_laden("produkte_geaendert.json")

    for produkt in textilunternehmen_neu.produkte:
        print(vars(produkt))
