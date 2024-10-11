#Using string manipulation, I created the following table listed on 
#the assignment page.

print(8 * "-", "Welcome to www.amazon.ca", 12 * "-")
print("\t1. Fortnite tips and tricks", 4 * ".","12.49")
print("\t2. Xbox controller charger", 5 * ".", " 7.59")
print("\t3. Android collectible robot", 4 * ".","6.99")
print("\t4. Cell phone case", 14 * ".", "8.99")
print("\t5. Selfie stick", 16 * ".", "11.39")
print("\t6. Exit")

subtotal = 0 #I set the subtotal, tax and shipping at zero, as it will change
shipping = 0 #throughout the program.
tax = 0

while True:
    question = int(input("What would you like? (Choose an option from 1-6): "))
    #The user will then be asked what products would they like as the loop
    #will keep asking until they enter 6 to exit the selection page.
    if question == 1:
        subtotal += 12.49 #If the user enters a certain number, the price
    elif question == 2:   #will then be added along the subtotal varaible
        subtotal += 7.59  #(before taxes)
    elif question == 3:
        subtotal += 6.49
    elif question == 4:
        subtotal += 8.99
    elif question == 5:
        subtotal += 11.39
    elif question == 6: #Once the user enters six, the program will then go
                        #through the following conditons, to see what to do next.
        if subtotal == 0:
            print("Total: $0.00. Have a nice day") #If the user ordered nothing,
            break                                  #the loop will break and display a total of 0 dollars.

        elif subtotal > 0 and subtotal <=34.99:  #If the subtotal is between 0 to 34.99 dollars, the user will then ask
            member = input("Are you Amazon Prime member? [y/n]: ")#if the user is an Amazon Prime member.
            member = member.lower()
            if member == "y": #If the user says yes, there will be no shipping.
                shipping = 0
            
            elif subtotal >= 35: #If the user has a cost of beyond 35 dollars, there will be no shipping
                shipping = 0
            
            elif member == "n": #If the user says no, then 4.50 dollars worth of shipping will be added to the total cost.
                shipping += 4.50
        
        tax = subtotal * 0.13 #Whatever the subtotal ends up to be, there will be 13% tax on the subtotal.
                
        print(f"Subtotal: ${subtotal:.2f}.") #This will display the subtotal rounded to 2 decimals
        print(f"Tax: (13%) ${subtotal * 0.13:.2f}.") #This will display the tax rounded to 2 decimals
        print(f"Shipping: ${shipping:.2f}.") #This will display the shipping rounded to 2 decimals.
    
        total = subtotal + tax + shipping #The total includes the subtotal, the tax, and the shipping
    
        print(19 * "=")
    
        print(f"Total: ${total:.2f}")#This will display the total rounded to 2 decimals.
        
        break #Once everyting is executed, the loop will break and end the code.