print("totaal prijs van de producten")
croissantjesaantal = int(input("aantal croissantjes: "))
stokbroodjes = int(input("aantal stokbroden: "))
###############################################################
croissantjesprijs = 0.39
croissantjes = croissantjesprijs * croissantjesaantal 
croissantjes_af = round(croissantjes,0)
###############################################################
stokbroodprijsperstuk = 2.78
stokbroodprijs = stokbroodprijsperstuk * stokbroodjes 
#################################################################
kortingsbon = 0.50

totaalprijs = (croissantjes + stokbroodprijs) - kortingsbon * 3
totaalprijs_af = round(totaalprijs,0)  * 100
##################################################################
print(f'De feestlunch kost je bij de bakker {totaalprijs_af} cent voor de {croissantjesaantal} croissantjes en de {stokbroodjes} stokbroden als de 3 kortingsbonnen nog geldig zijn!')



