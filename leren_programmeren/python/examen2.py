print('Justin Boom 99064305')
print('Welkom bij het keuze menu dit menu helpt u om een keuze te maken tussen 2 producten')
#####
######
max = int(input("Hoeveel wilt u maximaal uitgeven aan de telefoons?" ))
I13 = int(input("Vul de prijs is van de Iphone: "))
S22 = int(input("Vul de prijs is van de Samsung: "))
print('========================================================')
##
gelijk = I13==S22
verschil1 = S22 - I13 
verschil2 = I13 - S22
teduurS = S22 > max
teduurI = I13 > max

##

if teduurS and teduurI:
    print('De telefoons zijn te duur voor uw budget.')

if I13 > S22: #als de iphone duurder is dan de samsung word de samsung aangeboden bij de klant
          print('De Iphone 13 is duurder dan de Samsung S22')
          print('========================================================')
          print(f'Het duurste toestel is de Iphone 13 met een prijs van €{I13}')
          print('========================================================')
          print(f'Het goedkoopste toestel is de Samsung S22 met een prijs van €{S22}')
          print('========================================================')
#
elif gelijk: #omdat beide toestellen even duur zijn word de Iphone 13 aangeboden omdat dit de voorkeur is van de klant
    print('Beide toestellen zijn even duur, ons advies gaat dus uit naar de Iphone 13')


else: # als de Samsung duurder is dan de iphone word de iphone aangeboden bij de klant
    print('De Samsung S22 is duurder dan de Iphone 13')
    print('========================================================')
    print(f'Het duurste toestel is de Samsung S22 met een prijs van €{S22}')
    print('========================================================')
    print(f'Het goedkoopste toestel is de Iphone 13 met een prijs van €{I13}')
    print('========================================================')


if verschil2 <= 50:
        print(f'Het advies is dus de Iphone 13 te kopen. Deze is namelijk €{verschil1} goedkoper dan de Samsung S22')
else:
        print(f'Het advies is dus de Samsung S22 te kopen. Deze is namelijk €{verschil2} goedkoper dan de Iphone 13')

# if I13 > 900:
#     print(f'de Iphone is het duurste, de telefoon kost {I13}')
#     print(f'De samsung is het goedkoopst, de telefoon kost {S22}')
#     print('Het advies is dus om geen telefoon te kopen, ze zijn te duur.')

# # else S22 > 900:
# #     print(f'de Samsung is het duurste, de telefoon kost {S22}')
# #     print(f'De Iphone is het goedkoopst, de telefoon kost {I13}')
# #     print('Het advies is dus om geen telefoon te kopen, ze zijn te duur.')

