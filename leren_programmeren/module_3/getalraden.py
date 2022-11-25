import random



AANTAL_RONDES = 20
AANTAL_POGINGEN = 10
ronde = 0
score = 0
while ronde < AANTAL_RONDES:
    raden = input("Ben je er klaar voor om het getal te raden? ").lower()

    if raden == "nee":
        print(f"""Helaas!
        Uw score is {score} van de {AANTAL_RONDES} punten!""")
        exit()

    geheimgetal = random.randint(1, 1000)
#   print(geheimgetal)  # Deze print is er voor om te kijken of het script goed werkt en is dus niet noodzakelijk
    poging = 0
    while poging < AANTAL_POGINGEN:  # loop van het getal raden stopt na 10 pogingen
        while True:
            try:  # verplichting van cijfers
                antwoord = int(input("Raad het getal: "))
                break  # loop and a half
            except ValueError:
                print("Alleen cijfers invullen aub!")

        if antwoord == geheimgetal:
            print("Je heb het goede getal geraden!")
            score += 1
            break
        else:  # abs gebruiken
            verschil = abs(antwoord - geheimgetal)
            if verschil <= 20:  # berekent hier of het heel warm is of warm
                print("Je bent heel dichtbij!")
            elif verschil <= 50 and verschil >= 20:
                print("Je bent dichtbij!")
        poging += 1

    print(f"Je hebt {score} punt(en)!")
    ronde += 1
   


print(f"Uw score is {score} van de {AANTAL_RONDES} punten!")

