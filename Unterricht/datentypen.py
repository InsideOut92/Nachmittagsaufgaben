liste = [0, 1, 2, 3, 4, 5, 6, 33]

dictionary = {
    0: "Null",
    1: "Eins",
    2: "Zwei",
    3: "Drei",
    4: "Vier",
    5: "Fünf",
    12 : "Zwölf",
    12 : "12"
}

print(dictionary.get(2, "Nicht gefunden"))  # Verwende dictionary.get(), um einen Standardwert zurückzugeben, falls der Schlüssel nicht vorhanden ist
dictionary[2] = "Zwo"  # Ändere den Wert für den Schlüssel 2
print(dictionary[2])
print(liste[2])
liste.append(6)
dictionary[6] = "Sechs"
print(liste)
print(dictionary)

# Eine Liste, um zu verfolgen, welche Elemente bereits ausgegeben wurden
ausgegeben = []

# Iteriere über die Liste und prüfe, ob das Element im Wörterbuch vorhanden ist
for i in liste:
    if i in dictionary:
        if i not in ausgegeben:  # Prüfe, ob das Element bereits ausgegeben wurde
            print(dictionary[i])
            ausgegeben.append(i)  # Füge das Element zur Liste der ausgegebenen Elemente hinzu
    else:
        print("Kenn ich nicht!")


sets = {"milch", "zucker", "mehl", "eier", "safran"}
print(sets)
sets.add("pfeffer")
sets.pop()
print(sets)

print("zucker" in sets)
sets.remove("zucker")
print("zucker" in sets)


tuples = ("milch" , "mehl", "zucker", "salz", "safran", "eier", "eier", "mehl")
print(tuples)
print(tuples[2])

#Python hat 4 Datenstrukturen um mehrere werte zu speichern.
# -Liste- geordnet, veränderbar und erlaubt Duplikate
# -Dictionary- geordnet, veränderbar, aber keine Duplikate
# -Sets- ungeordnet, "veränderbar" und erlauben KEINE Duplikate (Add+Remove)

