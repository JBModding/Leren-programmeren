print("totaal prijs van de producten")
croissantjes = int(input("aantal croissantjes: "))
stokbroodjes = int(input("aantal stokbroden: "))
###############################################################
croissantjesprijs = 0.39
croissantjes = croissantjesprijs * croissantjes
croissantjes_af = round(croissantjes,2)
###############################################################
stokbroodprijsperstuk = 2.78
stokbroodprijs = stokbroodprijsperstuk * stokbroodjes
#################################################################
kortingsbon = 0.50

totaalprijs = (croissantjes + stokbroodprijs) - kortingsbon * 3
totaalprijs_af = round(totaalprijs,2)
##################################################################
print(f'''De feestlunch kost je bij de bakker {totaalprijs_af} euro voor de 17 croissantjes en de 2 stokbroden als de 3 kortingsbonnen nog geldig zijn!''')



