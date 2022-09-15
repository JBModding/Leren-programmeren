#Justin Boom 99064305

Geel = input("Heeft u een gele kaas? (Y/N)")

if Geel == "n":
    schimmel = input("Heeft u kaas blauwe schimmel plekken? (Y/N)")

    if schimmel == "y":
        korst = input("Heeft u kaas een zichtbare korst? (Y/N)")

        if korst == "y":
            print("Blue De Rochbaron")

        else: 
            print("Foume D'Ambert")
    
    else:
        korstg = input("Heeft uw kaas een zichbare korst? (Y/N)")

        if korstg == "y":
            print("Camenbert")
        
        else:
            print("Mozzarella")

if Geel == "y":
    gaten = input("Zitten er gaten in uw kaas? (Y/N)")

    if gaten == "y":
        prijs = input("Is de prijs hoog? (Y/N)")

        if prijs == "y":
            print("Emmenthaler")

        else:
            print("Leerdamer")

    else:
        steen = input("Is de kaas zo hard als steen? (Y/N)")

        if steen == "y":
            print("Paramigiano Reggiano")

        else:
            print("Goudse kaas")
            

print("Auther: Justin Boom")