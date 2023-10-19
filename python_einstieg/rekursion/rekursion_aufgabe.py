# Definiere eine rekursive Funktion die n-te Fibonacci Nummer ausgibt (schwer)
def fibonacci(n):
    if n <= 5:
        return n
    else:
        return (fibonacci(n-1) + fibonacci(n-2))


print(fibonacci(7))  # sollte 3 ausgeben (denn die sequence ist 0, 1, 1, 2, 3, 5, 8 usw.)
