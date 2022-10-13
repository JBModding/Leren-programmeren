# Setup
speler_antwoord = ["ja", "nee", "Ja", "Nee", "Yes", "No", "yes", "no"]
routes = ["links", "rechts", "vooruit", "achteruit"]

# Introduction
naam = input("Welkom avonturier, wat is uw naam?\n")
print(f"""Van harte welkom {naam} 
laten we beginnen met het verhaal""")
print(f"""Je bevind je in een donkere straat
maar {naam} let op! in deze straat kunnen enge figuren rondlopen""")
print('------------------------------------------------------------')
print("De straat heeft meerdere manieren om eruit te komen maar kies je de verkeerde weg...... dan ben je helaas dood")
print("Het is dus aan jou om de goeie manier te vinden om er veilig uit te komen")
# Start van het spel

def vraagAntwoord(prompt: str, opties: list) -> str:
    antwoord = ""
    while antwoord not in opties:
        antwoord = input(prompt+"\n")
        if antwoord not in opties:
            print('Dat snap ik niet probeer het op een andere manier!')
    return antwoord

antwoord = vraagAntwoord("Weet je zeker dat je de straat in wil gaan? \nja/nee",speler_antwoord)

if antwoord == "ja":
    print("Je loopt de straat in, in de verte zie je een lamp knipperen daar moet je veilg aankomen\n")
elif antwoord == "nee":
    print("jij bent niet klaar voor dit avontuur. tot ziens , " + naam + ".")
    quit()
# het volgende gedeelte van de game
 aan je rechter kant loopt de straat verder af, recht voot je staat een muur waar je niet overheen kan en achter je verlaat je de game
print("Aan je linker kant zie je een groep jongeren met zwarte kleren, \n aan je rechter kant , loopt de bos verder af\n Er is een muur recht voor je \n achter je is het uitgang van de bos .\n")
antwoord1 = vraagAntwoord ("welke route zou je kiezen ?\nlinks/rechts/vooruit/achteruit", routes)
if antwoord1 == "links":
    print(" De beer eet je op . Rip, " + naam + ".")
    quit()

elif antwoord1 == "rechts":
    print("Je gaat dieper het bos in \n aan je linker kant , je ziet een slang \n aan je rechter kant , je ziet een waterval \n als je vooruit gaat dan loop je de bos dieper in \n achter je is het uitgang van de bos \n ")
    antwoord3 = vraagAntwoord('waar ga je naar toe?\nlinks/rechts/vooruit/achteruit' , routes)
elif antwoord1 == "vooruit":
    print("je kunt de muur niet breken .\n je bent stapje terug gegaan \n aan je linker kant , je ziet een beer \n aan je rechter kant , loopt de bos verder af \n achter je is het uitgang van de bos \n ")
    antwoord2 = vraagAntwoord('waar ga je naar toe?\nlinks/rechts/vooruit/achteruit' , routes)
    if antwoord2 == "achteruit":
        print(" je verlaat de bos . Tot ziens , " + naam + ".")
        quit()
    elif antwoord2 == "rechts":
        print("Je gaat dieper het bos in.\n aan je linker kant , je ziet een slang \n aan je rechter kant , je ziet een waterval \n als je vooruit gaat is er een kans dat je uit de bos kan ontsnappen maar ook weer niet \n achter je is het uitgang van de bos \n ")
        antwoord3 = vraagAntwoord('waar ga je na toe?\nlinks/rechts/vooruit/achteruit' , routes)
    elif antwoord2 == "links":
        print(" De beer eet je op . Rip, " + naam + ".")
        quit()

elif antwoord1 == "achteruit":
    print(" je verlaat de bos . Tot ziens , " + naam + ".")
    quit()
else:
    print(" ik begrijp dat niet .\n")
if antwoord3 == "links":
    print(" Je wordt gebeten door de slang . Rip, " + naam + ".")
    quit()
elif antwoord3 == "rechts":
    print("Het is jou gelukt om uit de bos te komen . \n")
elif antwoord3 == "vooruit":
    print("je hebt de juiste keuze genomen je hebt t overleeft . \n")
    antwoord3 = "vooruit"
elif antwoord3 == "achteruit":
    print(" je verlaat de bos . Tot ziens , " + naam + ".")
    quit()

