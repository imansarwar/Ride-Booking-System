#Project Lab Task2
#UberRidingSystem

#Login Details
name=input("Enter Your Name:")
password=input("Enter Your Password:")

if name==name:
    print("................Welcome",name,"................\n")
else:
    print("Incorrect Username")

#Variables and Riding Service Details
ride1="Car"
ride2="Bike"
ride3="AC car"
ride4="Rickshaw"
print("Ride1. Car")
print("Ride2. Bike")
print("Ride3. AC Car")
print("Ride4. Rickshaw")
chooseride=input("Please select any ride:")
if chooseride==ride1 or chooseride=='car' or 'Car':
    print("You have selected your ride as: ",ride1,"\n")
elif chooseride==ride2 or chooseride=='bike' or 'Bike':
    print("You have selected your ride as: ",ride2,"\n")
elif chooseride==ride3 or chooseride=='ac car' or 'AC Car':
    print("You have selected your ride as: ",ride3,"\n")
elif chooseride==ride4 or chooseride=='rickshaw' or 'Rickshaw':
    print("You have selected your ride as: ",ride4,"\n")
else:
    print("Your selected ride is not available")

#Selection of Areas
area1="Gulshan"
area2="Sirsyed Uni"
area3="Defence"
print("Area1. Gulshan")
print("Area2. Sirsyed Uni")
print("Area3. Defence")
choosearea=input("Please select any area:")
if choosearea==area1 or choosearea=='gulshan' or 'Gulshan':
    print("You have selected your area as: ",area1,"\n")
elif choosearea==area2 or choosearea=='sirsyed uni' or 'Sirsyed uni':
    print("You have selected your area as: ",area2,"\n")
elif choosearea==area3 or choosearea=='defence' or 'Defence':
    print("You have selected your area as: ",area3,"\n")
else:
    print("Your selected area is not available")

#Bill and use of IF Condition
print("..................................................")
print("Your Booking Details Are: \n")
print("Name:",name)

if chooseride=='1' and choosearea=='1':
    print("Your selected ride is:",ride1,"\nYour selected destiny is:",area1)
elif chooseride=='1' and choosearea=='2':
    print("Your selected ride is:",ride1,"\nYour selected destiny is:",area2)
elif chooseride=='1' and choosearea=='3':
    print("Your selected ride is:",ride1,"\nYour selected destiny is:",area3)
elif chooseride=='2' and choosearea=='1':
    print("Your selected ride is:",ride2,"\nYour selected destiny is:",area1)
elif chooseride=='2' and choosearea=='2':
    print("Your selected ride is:",ride2,"\nYour selected destiny is:",area2)
elif chooseride=='2' and choosearea=='3':
    print("Your selected ride is:",ride2,"\nYour selected destiny is:",area3)
elif chooseride=='3' and choosearea=='1':
    print("Your selected ride is:",ride3,"\nYour selected destiny is:",area1)
elif chooseride=='3' and choosearea=='2':
    print("Your selected ride is:",ride3,"\nYour selected destiny is:",area2)
elif chooseride=='3' and choosearea=='3':
    print("Your selected ride is:",ride3,"\nYour selected destiny is:",area3)
elif chooseride=='4' and choosearea=='1':
    print("Your selected ride is:",ride4,"\nYour selected destiny is:",area1)
elif chooseride=='4' and choosearea=='2':
    print("Your selected ride is:",ride4,"\nYour selected destiny is:",area2)
elif chooseride=='4' and choosearea=='3':
    print("Your selected ride is:",ride4,"\nYour selected destiny is:",area3)
else:
    print("Sorry no booking can be done")
print("\nTotal Bill: $100")
