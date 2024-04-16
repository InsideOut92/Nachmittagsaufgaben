# Import des random-Moduls, um zufällige Zahlen zu generieren
import random

# Funktion definieren, um zufällige Zahl zu generieren
def generate_random_number():
    """
    Diese Funktion generiert eine zufällige Zahl zwischen 0 und 99 und gibt sie zurück.
    """
    # Zufällige Zahl zwischen 0 und 99 generieren und zurückgeben
    return random.randint(0, 99)

# Aufruf der Funktion und Ausgabe des Ergebnisses
random_number = generate_random_number()
print("Die generierte Zahl ist:", random_number)
