#in this all types are used like if/else , elif, Multiple if, Logocal Operators

print("Welcome to the Rollercoster")
height = int(input("What is your height in cm? "))
bill = 0

if height >= 120:
    print("You can ride the Rollercoster!")
    age = int(input("What is your age? "))
    if age < 12:
        bill = 5
        print("The fare is $5")
    elif age <= 18:
        bill = 7
        print("The fare is $7")

    # Logical operator. one false condition in (and) it will give you a result as false. 
    # One true condition in (or) it will give you a result as true 
    elif age >= 45 and age <= 55:
        print("Everything is going to be ok. Have a free ride on us!")

    else:
        bill = 12
        print("The fare is $12")


    want_photo = input("Do you want a photo taken? Y or N. ")
    if want_photo =="Y":
        
    #Add $3 in their bill. it can be done +=
        bill += 3
        print(f"Your Final Bill is ${bill}.")
else:
    print("Sorry, you have to grow taller before you can ride.")