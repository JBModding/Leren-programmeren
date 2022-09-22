print('Justin Boom 99064305')
print('Welkom bij het keuze menu dit menu helpt u om een keuze te maken tussen 2 producten')
#####
I13 = 900
S22 = 900
######
I13 = int(input("Vul de prijs is van de Iphone: "))
S22 = int(input("Vul de prijs is van de Samsung: "))
print('========================================================')
##
eindprijs1 = S22 - I13 
eindprijs2 = I13 - S22
##

if I13 > S22:
          print('De Iphone 13 is duurder dan de Samsung S22')
          print('========================================================')
          print(f'Het duurste toestel is de Iphone 13 met een prijs van €{I13}')
          print('========================================================')
          print(f'Het goedkoopste toestel is de Samsung S22 met een prijs van €{S22}')
          print('========================================================')
          print(f'Het advies is dus de Samsung S22 te kopen. Deze is namelijk €{eindprijs2} goedkoper dan de Iphone 13')


elif (S22 == I13):
    print('Beide toestellen zijn even duur, ons advies gaat dus uit naar de Iphone 13')


else:
    print('De Samsung S22 is duurder dan de Iphone 13')
    print('========================================================')
    print(f'Het duurste toestel is de Samsung S22 met een prijs van €{S22}')
    print('========================================================')
    print(f'Het goedkoopste toestel is de Iphone 13 met een prijs van €{I13}')
    print('========================================================')
    print(f'Het advies is dus de Iphone 13 te kopen. Deze is namelijk €{eindprijs1} goedkoper dan de Samsung S22')

# if I13 > 900:
#     print(f'de Iphone is het duurste, de telefoon kost {I13}')
#     print(f'De samsung is het goedkoopst, de telefoon kost {S22}')
#     print('Het advies is dus om geen telefoon te kopen, ze zijn te duur.')

# # else S22 > 900:
# #     print(f'de Samsung is het duurste, de telefoon kost {S22}')
# #     print(f'De Iphone is het goedkoopst, de telefoon kost {I13}')
# #     print('Het advies is dus om geen telefoon te kopen, ze zijn te duur.')

