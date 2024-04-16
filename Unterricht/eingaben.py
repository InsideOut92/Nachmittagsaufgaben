name = input("Bitte geben Sie ihren Namen ein: ")
print("Hallo " + name)

alter = input("Bitte geben Sie ihr Alter ein: ")
try:
    alter = int(alter)
    alter = alter + 1
    print(f"Sie werden nächstes Jahr {alter} Jahre alt sein")
    # formatiere String
    print("Sie werden nächstes Jahr " + str(alter) + " Jahre alt.")
    # explizite Umwandlung von int in String

except:
    print("Es wurden keine Zahlen eingegeben!")
else:
    print("Ich werde ausgeführt, wenn alles korrekt verlaufen ist!")



try:
    division = 4 / 0
    print(x)
except NameError:
    print("Variable x ist noch nicht definiert")
except ZeroDivisionError:
    print("One does not simply divide by 0.")
except:
    print("Ein Affe ist aufgetaucht und frisst deine Eier.")
finally:
    print("Ich werde definitiv ausgeführt!")



try:
    #with open("datentypen.py") as f:
        #print(f.readline())

        #Modi:
        # "r" - Lesen
        # "a" - anhängen
        # "w" - schreiben
        # "x" - erstellen der Datei - wirft Fehler, wenn Datei bereits existiert


        f = open("datentypen.py", "rt")
        for line in f:
            print(line)
except:
    print("Datei konnte nicht gefunden werden!")
finally:
    f.close()


try:
    with open("textdatei.txt", "a") as f:
        f.write(name + " " + str(alter) + "\n")
except:
    print("Du bisch doof!")
finally:
    f.close()