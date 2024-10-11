number = input("Enter a number: ") #The user will be asked to give a number
result = number #The result variable will save the original number before
                #the variable number changes.

if len(number) == 1: #If the length of the number is one digit, it will print itself throught the following statment down below
    print("The multiplicative digital root of", number,"is", number)

elif len(number) == 2: #If the length of the number is two digits, it will go through the following loop.
    while True:
        n_one = number[0] #This will split the number into its two digits because 'number' is still a string. This is the first digit.
        n_two = number[1] #This is the second digit.
        number = int(n_one) * int(n_two) #The two seperated digits are now converted to integers, multiplied and formed a new number.
        number = str(number) #The new number is now back to the format string.
        if len(number) == 2: #If the length of the number is still two digits, the loop will continue
            continue 
        else:
            break #If it is one digit, the loop will break and the orginal number will be displayed along with the root.
    print("The multiplicative digital root of", result,"is", number)