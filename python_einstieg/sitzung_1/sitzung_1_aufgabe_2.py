# Schreibe ein Programm, dass deinen Namen erfragt, unter der Variable -mein_name- speichert und diesen dann
# ausgibt:
mein_name = input("Name? ")
print(mein_name)
# Schreibe ein Programm, dass nach deiner Adresse fragt, unter der Variable -meine_adresse- speichert und diese
# dann ausgibt:

meine_adresse = input("Adresse? ")
print("Meine Adresse: " + meine_adresse)

# Schreibe ein Programm, dass noch einmal nach einer neuen Adresse fragt und die unter der Variable
# -meine_adresse- speichert. Gebe nachher die neue und die alte Adresse aus:

meine_alte_adresse = meine_adresse
meine_adresse = input("Neue Adresse?")

print("Meine neue Adresse: " + meine_adresse)
print("Meine alte Adresse: " + meine_alte_adresse)

# Schreibe ein Programm, dass nach zwei (ganzen) Zahlen fragt und die summe dieser beiden Zahlen ausgibt:
zahl_1 = int(input("Zahl 1? "))
zahl_2 = int(input("Zahl 2? "))

print(zahl_1+zahl_2)