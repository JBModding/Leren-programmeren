print("""
Er wordt u een aantal vragen gesteld die relevant zijn aan de solicitatie voor 'Circusdirecteur voor Circus HotelDeBotel'
Gelieve deze vragen eerlijk en serieus in te vullen.
Als blijkt dat u aan de criteria voldoet dan komt u in aanmerking voor een solicitatie gesprek!
Hier komen de vragen, veel succes!!!
""")

ervaring = (input('Heeft u praktijk ervaring in Dieren-dresuur, jongleren of acrobatiek? ')) 

if (ervaring == 'ja'): 
     soort_ervaring = int(input('''Waar heeft u ervaring in?
                    1: dieren-dresuur
                    2: jongleren
                    3: acrobatiek
                    '''))

     jaren_ervaring = int (input('Hoeveel jaar praktijk ervaring heeft u daar in? '))

if ((soort_ervaring == 1) and (int(jaren_ervaring) > 4)) or ((soort_ervaring == 2) and (int(ervaring) > 5)) or ((soort_ervaring == 3) and (int(ervaring) > 3)):
      ervaring = True
else:
     ervaring = False

vraag2_diploma = input('Heeft u een MBO diploma in ondernemen? ')

if vraag2_diploma == 'ja':
       antwoord_diploma = int(input("Welk niveau diploma heeft u?"))
    


vraag3_vrachtwagen = input('Heeft u een geldig vrachtwagen rijbewijs? ')

vraag4_hoed = input('Heeft u een hoge hoed? ')

vraag5_manOfVrouw = input('Bent u een man of een vrouw? ')

if vraag5_manOfVrouw == 'man': 
     vraag6_snor = input("Heeft u een snor?")
     if vraag6_snor == "ja":
          vraag7_breedte = int (input('Hoe groot is uw snor in centimeters? '))
          raise NameError("nope")
    

if vraag5_manOfVrouw == 'vrouw':
     vraag6_krulhaar = input("Heeft u rood krullend haar?")
     if vraag6_krulhaar == 'ja':
         vraag7_lengte = int (input('Hoe lang is uw haar in centimeters? '))
     

     

vraag8_lengte = int (input('Hoelang bent u in centimeters? '))

vraag9_gewicht = int (input('Hoe zwaar bent u in kg? '))

vraag10_certificaat = input('Heeft u een certificaat "overleven met gevaarlijk personeel"? ')

if ((ervaring == True) and (vraag2_diploma =='ja'and antwoord_diploma > 3) and (vraag3_vrachtwagen == 'ja') and (vraag4_hoed == 'ja') and (vraag5_manOfVrouw == "man" and vraag6_snor == "ja" and vraag7_breedte > 10) and (int(vraag8_lengte) > 150) and (int(vraag9_gewicht) < 90) and (vraag10_certificaat == 'ja') or (vraag5_manOfVrouw == "vrouw" and vraag6_krulhaar == "ja" and vraag7_lengte > 20) and (int(vraag8_lengte) > 150) and (int(vraag9_gewicht) < 90) and (vraag10_certificaat == 'ja')):   
     print('Gefeliciteerd, u komt in aanmerking voor een solicitatie gesprek!')

else:
     print('Jammer joh, u bent niet geschikt voor deze positie')