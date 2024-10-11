# The loop will be able to ask the user 
# repeatedly until the user has enough credits
while True:
    number = int(input("How many credits do you have?"))
    if number < 30: # Condition when the user doesn't have 30 credits to graduate.
        total = 30 - number #This will calculate how many credits the user will need to reach 30.
        print("You are not able to graduate.")
        print("You need",total,"more credits to graduate")
    elif number >= 30: # Condition when the user has 30 or more credits
        print("Congratulations.") # The user will then get a message saying congrats
        break                     # before the loop will break. (The requirement has   
                                  # been satisfied)