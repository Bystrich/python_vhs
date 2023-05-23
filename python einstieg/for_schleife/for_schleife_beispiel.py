meine_lieblingszahlen = [3, 11, 25, 100, 9, 5, 1, 23]

# z ist hierbei eine Laufvariable und durchläuft die ganze Liste, in dem sie zu dem jeweiligen Listeninhalt wird
for z in meine_lieblingszahlen:
    print("eine meiner Lieblingszahlen ist: " + str(z))

mein_name = "Valentin"


# Die range() Funktion erstellt eine Folge von Zahlen. Der erste Parameter gibt den Startwert an,
# und der zweite den Schlusswert (wird nicht mehr mitgenommen)
for i in range(0, len(mein_name)):
    print("der " + str(i) + "te Buchstabe in meinem Namen ist" + mein_name[i])
    print("eine meiner Lieblingszahlen ist: " + str(meine_lieblingszahlen[i]))

