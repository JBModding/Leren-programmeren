# from decimal import ROUND_DOWN
# from tokenize import group


# #inhoudzwem = 8*3*1.5
# #uitgraven = inhoudzwem*25
# #voorrij = 250
# #grond = inhoudzwem*32.50
# #totaal = uitgraven+voorrij+grond


# ###########################################################
# #print(inhoudzwem, "m3")
# #print(f""" Offerte voor een zwembad van 8 bij 3 bij 1.5:
# #Uitgraven: €{uitgraven}
# #Voorrijkosten: €{voorrij}
# #Afvoeren grond: €{grond}
# #Totaalprijs: \033[1m€{totaal}\033[0m
# #""")
# #############################################################

hoogte = float(input("wat is de Hoogte van uw zwembad: "))
lengte = float(input("hoe lang is uw zwembad vloer: "))
Breedte = float(input("Wat is d breedte van uw zwembad: "))
Diepte = float(input("Wat is de diepte van uw zwembad: "))



kubieke = hoogte*Breedte*Diepte
uitgraven1 = kubieke*25
opp1 = lengte*Diepte*2
opp2 = Breedte*Diepte*2
opp3 = lengte*Breedte
oppall = opp1+opp2+opp3
grond1 = kubieke*32.503
voorrij1 = 250
beton = lengte*Breedte*250
rood = beton*25
kleur = beton*125
totaal1 = grond1+uitgraven1+voorrij1+beton
totaal1_af = round(totaal1,2)
totaal2 = grond1+uitgraven1+voorrij1+rood
totaal2_af = round(totaal2,2)
totaal3 = grond1+uitgraven1+voorrij1+kleur
totaal3_af = round(totaal3,2)

print(oppall)

print(kubieke, "m3")
print("--------------------------------------")
afwerking = input(""" Welke kleur tegens had u gewilt?
standaard = geen meerprijs
rood = €20>
kleur naar keuze = €100>
""")



if afwerking == "standaard":
     print(f"""Offerte voor een zwembad van {hoogte} bij {Breedte} bij {Diepte} meter totaal van {kubieke}:
     uitgraven: €{uitgraven1}
     afvoeren grond: €{grond1}
     voorrijkosten: €{voorrij1}
     oppervlakte: {oppall} vierkante meter
     beton + tegels: {beton}
     totaalprijs: \033[1m€{totaal1_af}\033[0m
     """)
 elif afwerking == "rood":
     print(f"""Offerte voor een zwembad van {hoogte} bij {Breedte} bij {Diepte} meter totaal van {kubieke}:
     uitgraven: €{uitgraven1}
     afvoeren grond: €{grond1}
     voorrijkosten: €{voorrij1}
     oppervlakte: {oppall} vierkante meter
     beton + tegels: {rood}
     totaalprijs: \033[1m€{totaal2_af}\033[0m
     """)
 else:
     print(f"""Offerte voor een zwembad van {hoogte} bij {Breedte} bij {Diepte} meter totaal van {kubieke}:
     uitgraven: €{uitgraven1}
     afvoeren grond: €{grond1}
     voorrijkosten: €{voorrij1}
     oppervlakte: {oppall} vierkante meter
     beton + tegels: {kleur}
     totaalprijs: \033[1m€{totaal3_af}\033[0m
     """)