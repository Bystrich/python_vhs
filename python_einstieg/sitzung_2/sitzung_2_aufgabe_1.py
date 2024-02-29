# Warum funktioniert den Code nicht? Versuche ihn zu fixen.
neue_nummer = int(input("Bitte geben sie eine nummer ein: "))

if neue_nummer > 0:
    if neue_nummer % 2 == 0:
        print("Die Nummer ist gerade")
else:
    print("Die Nummer ist ungerade")
else:
    print("Die Nummer ist null oder negativ")


# Schreibe Code, der nach dem Alter des Benutzers fragt und durch EINE If-Anweisung überprüft ob das genannte Alter sinnvoll ist (z.B. zwischen 5 und 100 Jahren)


# Ändere den Code so, dass die If-Anweisung wahr ist, wenn die Zahl nicht zwischen 5 und 8 liegt. Tip: dafür muss nur ein Wort hinzugefügt werden!
nummer = int(input("Bitte geben sie eine nummer ein: "))
if (nummer >= 5 and nummer <= 8):
    print("Die eingebene nummer ist nicht zwischen 5 und 8")
