#The program begins by asking the user the 
#amount of hours worked and the amount of money
#earned per hour

hrs = float(input("Enter amount of hours worked: "))#Enter your hours worked per week
#Enter your hours worked per week
pay = float(input("Enter amount of money earned per hour: "))#Enter hourly rate here

# These are the conditions where the program determines
# how much one user makes, overtime or not.

if hrs <= 40: #If hours are anything from 0 to 40, then you earned a regular pay.
    gross_pay = hrs * pay
    print(f"You just earned ${gross_pay:.2f} , Congratulations!")

if hrs > 40: #If hours are anything beyond 40, then you will earn overtime wages using the formula down below
    gross_pay = 40 * pay + (hrs - 40) * pay * 2
    print(f"You just earned ${gross_pay:.2f}, Congratulations!")

# These conditions here determines how much tax does the user
# have to pay using the tax bracket.

if gross_pay <= 100 and gross_pay >= 0: #Anything from 0 to 100 dollars, you pay no tax.
    tax = gross_pay * 0
    print(f"Your tax: ${tax:.2f}")

elif  gross_pay >= 100.01 and gross_pay <= 250: #Anything from 100.01 to 250 dollars, you pay 10% tax.
    tax = gross_pay * 0.10
    print(f"Your tax: ${tax:.2f}" )

elif gross_pay >= 250.01 and gross_pay <= 550: #Anything from 250.01 to 550 dollars, you pay 20% tax.
    tax = gross_pay * 0.20
    print(f"Your tax: ${tax:.2f}" )

elif gross_pay >= 550.01 and gross_pay <= 950: #Anything from 550.01 to 950, you pay 28% tax.
    tax = gross_pay * 0.28
    print(f"Your tax: ${tax:.2f}" )

else: #Anything beyond 950.01 dollars, you pay the highest tax. 35% tax.
    gross_pay >= 950.01
    tax = gross_pay * 0.35
    print(f"Your tax: ${tax:.2f}" )

# The user will then be given the option 
# to whether or not give a 10 dollar donation.

donation = input("Would you like to give a 10 dollar donation to United Way? (Enter either Y or N.): ")
if donation == "Y" or "y":
    donation_two = float(input("Enter your donation here: ")) #You enter your donation here.
    print(f"Donation: ${donation_two:.2f}, Thank you.")

elif donation == "N" or "n":
    donation_two = float(input("Enter your donation here: "))#Enter 0 for your donation and you will be charged nothing.
    print("Donation : $0.00. Thank you.")

# Here will determines the amount of money 
# the user will take home with him/her 

take_home_pay = gross_pay - tax - donation_two
print(f"Your take home pay: ${take_home_pay:.2f}")