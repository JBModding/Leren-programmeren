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
print("croissantjes prijs: ", croissantjes)
print("stokbrood prijs: ", stokbroodprijs)
print("totaalprijs €", totaalprijs_af)



