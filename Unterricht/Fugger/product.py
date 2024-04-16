class Product:
    def __init__(self, name, description, price, productnumber, discount, manufacturing_location, manufacturing_type):
        self.name = name
        self.description = description
        self.price = price
        self.productnumber = productnumber
        self.discount = discount
        self. manufacturing_location = manufacturing_location
        self.manufacturing_type = manufacturing_type

    def __str__(self):
        return (f"{self.name} kostet {self.price} \n"
                f"Beschreibung: {self.description} \n"
                f"Produktnummer: {self.productnumber} \n"
                f"Aktuelle Rabatte: {self.discount} \n"
                f"Herstellungsort: {self.manufacturing_location} \n"
                f"Herstellungsart: {self.manufacturing_type} \n")

if __name__ == '__main__':
    product = Product("Lampe", "leuchtet", 19.99, 98745, None,
                      "Berlin, Deutschland", "Handarbeit")
    print(product)
    