canada = 40.25 #Values of years and canada before code is executed.

years = 0

while canada < 100: #While the canada value is less than 100, it will constantly repeat until it has reached 100.
 canada = canada * 1.0184 #The value of canada will increase by 1.84% per year.
 years += 1 #While the canada value is increasing the years value will increase by 1 until the canada vaulue is 100.

print("It will take", years, "years to reach a population of 100 million.") #Statement showing the years needed to reach 100 million.
# Please, make sure to run these lines of code on a seperate program. Otherwise the program
# will give the wrong numbers.

while years < 10: #While the years are less than 10, the canadian pop will increase by the value underneath
    canada = canada + 40761460
    years += 1
print("By 2034, the population of Canada will be", canada, "millions") #Once the value of years reaches 10, then the statement will show the population of Canada in 10 years.