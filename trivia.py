# When you run this program, you will be given instructions on how the trivia program works

print("Welcome to my trivia program. Here, you will answer 5 random and unique questions. You will get a score out of 5. Good luck. You will need it.")

question_one = str(input("How many states are in the America? ")) #Each question will give a question and ask for an answer in the form of an input.

count = 0 #At the start, the counter variable starts at 0. Meaning that each player starts at 0 points.

if "50" == question_one:
    print("Correct! You have one point.")
    count = count + 1 #Every time you input the correct answer, the counter will add a point to your score. 

elif "50" != question_one:
    print("Incorrect. The answer is 50. No point.")#Every time you get an incorrect answer, you won't gain any points.

question_two = str(input("Name this class course code: "))
question_two = question_two.lower()

if "ic3su-04" == question_two:
    print("Correct! You have gained another point.")
    count = count + 1
    
elif "ic3su-04" != question_two:
    print("Incorrect. The answer is ic3su-04. No point.")

question_three = str(input("How many Diary of a Wimpy Kid books are there? "))

if "19" == question_three:
    print("Correct! You have gained another point.")
    count = count + 1

elif "19" != question_three:
    print("Incorrect. The answer is 19. No point.")

question_four = str(input("How many letters are in the alphabet? "))

if "26" == question_four:
    print("Correct. You have gained another point.")
    count = count + 1

elif "26" != question_four:
    print("Incorrect. The answer is 26. No point.")

question_five = str(input("How many planets do we have in the solar system? "))

if "8" == question_five:
    print("Correct. You have gained another point.")
    count = count + 1

elif "8" != question_five:
    print("Incorrect. The answer is 8. No point.")
    
#At the end of the trivia program, the program will calculate your score using the "Count" variable. It will divide your score by 5, and multiply it by 100 to give your score in percentage way.

print(f"Your score is: {count / 5 * 100 :.0f}%")