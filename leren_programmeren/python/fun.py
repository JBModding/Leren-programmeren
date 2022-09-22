bedrag = float(input("wat is het totaal bedrag: "))

def BerekenBtw(bedrag_ex: float) -> float:
    bedragincl = bedrag / 100
    totaal = bedragincl * 121
    return totaal

def btwwaarde(bedrag: float) -> float:
    bedragincl = bedrag / 100
    btw = bedragincl * 21
    return btw

totaal = BerekenBtw(bedrag)
btw = btwwaarde(bedrag)
print(f"Dit is de incl prijs: €{totaal}")
print(f"btw:  €{btw}")