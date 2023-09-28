# Schreib ein kleines Programm, dass den Nutzer nach seinem Passwort fragt. Das Programm soll so lange fragen bis der
# Nutzer entweder das richtige Passwort oder drei mal ein falsches Passwort eingegeben hat
passwort = "qwertz123"

zähler = 1

max_versuche = 3

while zähler <= max_versuche:
    eingabe = input("Wie lautet ihr pw?")
    if eingabe == passwort:
        print("richtig")
        break
    else:
        print("falsch")
    zähler = zähler + 1

    if zähler > max_versuche:
        print("Ihre Versuche sind aufgebraucht!!!!!")