print('Welkom bij het keuze menu dit menu helpt u om een keuze te maken tussen 2 producten')
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
####