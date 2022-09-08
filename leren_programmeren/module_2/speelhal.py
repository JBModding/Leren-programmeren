print("totaal prijs voor aantal personen")
tickets = int(input("aantal tickets: "))
#######################################
ticketprijspp = 7.45
tickets = tickets * ticketprijspp
tickets_af = round(tickets,2)
########################################
vipvr = int(input("aantal minuten: "))
########################################
vipvrprijs = 0.37 / 5
vrprijs = vipvr * vipvrprijs 
vip_af = round(vrprijs,2)
########################################
print("ticket totaalprijs: ", tickets)
print("vr totaalprijs: ", vip_af)
#######################################
eindprijs = tickets + vip_af
#######################################
print(f'''Dit geweldige dagje-uit met 4 mensen in de Speelhal met 45 minuten VR kost je maar {eindprijs} euro''')