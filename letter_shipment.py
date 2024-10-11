# The user will input the weight of the 
# letter/parcel they would like to ship

weight = float(input("Enter weight of letter in grams: ")) # Enter the weight of the letter here.

# The program will then use the conditions listed below to 
# calculate the cost of the letter

if weight <= 40: #Anything from 0 to 40 grams is 70 cents with this condition.
    cost = 0.70

elif weight <= 100: 
    cost = 1.25 #Anything from 40.1 to 100 is 1.25 dollars


else: #Anything greater than 100 will be executed with this condition here.
    add_weight = weight - 100
    extra = (add_weight // 50) + 1
    cost = 1.25 + (extra * 0.3)
    
# Here you will then get the final amount here,
# rounded to two decimals

print(f"The cost of the postage is : ${cost:.2f}")