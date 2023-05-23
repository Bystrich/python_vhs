while True:
    print("ich laufe bis der User Stop sagt")
    antwort = input("? ")

    if antwort == "Stop" or antwort == "STOP" or antwort == "stop":
        break
    else:
        print("dann laufe ich wohl weiter")


andere_antwort = ""
while andere_antwort != "Halt":
    print("ich laufe bis der User Halt sagt")
    andere_antwort = input("? ")
