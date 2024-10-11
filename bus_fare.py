## Table using string manipulation 
print(60 * "=") # multiplies the "=" by 60
print("Category\t\t1 ticket\t\t5 tickets\t\tmonthly")# \t will apply the tab between table lines
print(60 * "=")
print("Adult\t\t\t$3.00\t\t\t$12.65\t\t\t$95.70")
print(60 * "=")
print("Senior\t\t\t$2.00\t\t\t$9.90\t\t\t$48.40")
print(60 * "=")
print("Student\t\t\t$2.20\t\t\t$9.90\t\t\t$66.00")
print(60 * "=")

#Here, the user will input what category the belong to 
#and how many tickets they want.

category = str(input("Choose a category: (Enter either Adult, Student or Senior.): "))#Enter which catergory you belong.
ticket = str(input("How many tickets do you want? (Enter either 1, 5, m): "))#Enter the amount of tickets you would like to purchase.
category = category.lower() #This will convert any input the user enter to all lowercased letters. (Ex. ADulT -> adult. )

#The following "if" statements are the nine possiblites the user might enter. 

if "adult" == category and "1" == ticket: 
    print("You owe $3.00. Have a nice day.")
if "adult" == category and "5" == ticket:
    print("You owe $12.65, Have a nice day.")
if "adult" == category and "m" == ticket:
    print("You owe $95.70. Have a nice day.")
if "senior" == category and "1" == ticket:
    print("You owe $2.00. Have a nice day.")
if "senior" == category and "5" == ticket:
    print("You owe $9.90. Have a nice day.")
if "senior" == category and "m" == ticket:
    print("You owe $48.40. Have a nice day.")
if "student" == category and "1" == ticket:
    print("You owe $2.20. Have a nice day.")
if "student" == category and "5" == ticket:
    print("You owe $9.90. Have a nice day.")
if "student" == category and "m" == ticket:
    print("You owe $66.00. Have a nice day.")

