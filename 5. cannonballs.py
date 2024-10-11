cannon = int(input("Enter number of cannons: ")) #The program will ask the user for the amount of cannonballs desired

levels = 0 #The number of levels being made.

total = 0 #Total amount of cannoballs used in the structure/pyramid.

while True:
    levels += 1 #The levels will increase by 1 when running the loop

    amount = levels ** 2 #For each level the number of cannon balls in that level is that number of levels multiplied by itself (ex: the fourth level has 16 cannon balls or 4^2)

    if total  + amount > cannon: #If the program is higher than than the amount of cannons, 
        levels -= 1              #The levels will decrease by 1 and the loop will break

        break

    total = total + amount #This add amount to total

remainder = cannon - total #formula to calculate the remainder after cannonballs levels are made.

print("There will be", levels, "levels made") #Statement showing the levels made.

print("There will be", remainder,"leftover.") #Statement showing the leftover cannonballs after structure is made