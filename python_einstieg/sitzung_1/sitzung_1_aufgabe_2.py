# Schreiben sie ein Programm, dass ihren Namen erfragt, unter der Variable -mein_name- speichert und diesen dann
# ausgibt:
mein_name = input("Wie ist dein Name?")
print(mein_name)
# Schreiben sie ein Programm, dass nach ihrer Adresse fragt, unter der Variable -meine_adresse- speichert und diese
# dann ausgibt:
meine_adresse = input("Wie ist deine Adresse?")
print(meine_adresse)

# Schreiben sie ein Programm, dass noch einmal nach einer neuen Adresse fragt und die unter der Variable
# -meine_adresse- speichert. Geben sie nachher die neue und die alte Adresse aus:

'''
meine_alte_adresse = meine_adresse
meine_adresse = input("Wie ist deine neue Adresse?")
print(meine_adresse)
print("Meine alte Adresse war " + meine_alte_adresse)
'''

# Schreiben sie ein Programm, dass nach zwei (ganzen) Zahlen fragt und die summe dieser beiden Zahlen ausgibt:
zahl_1 = input("Zahl 1?")
zahl_2 = int(input("Zahl 2?"))
print(int(zahl_1) + zahl_2)