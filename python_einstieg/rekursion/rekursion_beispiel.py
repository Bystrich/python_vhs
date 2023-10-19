# Rekursion erlaubt es einem den Aufruf einer Funktion in der Funktion selber anzuwenden.
# Dazu wird ein Rekursionsanker benötigt (in diesem Beispiel in Zeile 5)
def factorial(n):
    if n < 2:
        return 1  # Anker
    else:
        return n * factorial(n - 1)  # Rekursiver Aufruf: 6! = 6 * 5!


print(factorial(3))
