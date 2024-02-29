# Schreibe eine Funktion die ein Quadrat beliebiger Größe aus einem gewählten Zeichen ausgibt

def quadrat_aus_zeichen(groesse, zeichen):
  reihe = 1

  while reihe <= groesse:
    print(groesse * zeichen)
    reihe = reihe + 1

# Schreibe eine Funktion die überprüft ob zwei bestimmte Buchstaben in einem Wort gleich sind. So sollte z.B. print(gleiche_buchstaben("programmierer", 6, 7)) True ausgeben

def gleiche_buchstaben(wort, b_1, b_2):
  antwort = wort[b_1] == wort[b_2]
  return antwort


#quadrat_aus_zeichen(10, "a")
#quadrat_aus_zeichen(12, "p")

print (gleiche_buchstaben("test", 0 , 3))
print (gleiche_buchstaben("Valentin", 4 , 6))