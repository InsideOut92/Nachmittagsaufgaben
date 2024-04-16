import os

if os.path.exists("textdatei.txt"):
    try:
        os.remove("textdatei.txt")
        print("Die Datei wurde gelöscht :)")
    except:
        print("Datei konnte nicht gelöscht werden! \n Zugriffsrechte prüfen!")
else:
    print("Die Datei existiert nicht oder wurde bereits gelöscht!")