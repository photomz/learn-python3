import pandas
import csv
import random  # import the random library to allow the use of random.randint & random.choice


print("Welcome to the maths quiz")
print("*********************************")
# initialise name variable to hold users name input
name = input("Please enter your name: ")
print("*********************************")
# initialise variable to store difficulty selected

difficulty = int(input("Please choose a difficulty 1=easy, 2=hard "))
if difficulty == 1:
    print("You have selected the easy quiz")
else:
    print("You have selected the hard quiz")

print("*********************************")
print("Good luck " + name + "!")
# initialise score variable, set score to 0
print("*********************************")
score = 0
# LOOP STARTS HERE use x as loop total and i as loop start point. After each loop/question, i will grow until it reaches x
x = 10
i = 0

while i < x:
    # initialise two variables to be set to a random value between 1 and 10, these will form the two numbers for each question
    if difficulty == 1:
        val1 = random.randint(1, 10)
        val2 = random.randint(1, 10)
    else:
        val1 = random.randint(1, 100)
        val2 = random.randint(1, 100)
    # the op list stores the values for possible operators for the questions
    op = ("+", "-", "*")
    # random.choice will randomly select one of the ops from the ops list
    operator = random.choice(op)
    # the question will then be made up of these 3 random variables
    question = str(val1) + operator + str(val2)
    print(question)
    print("*********************************")
    # increment i by 1 to log that a question has been asked
    i = i + 1
    # work out the correct answer to the Q depending on which operator was randomly selected for this question.
    if operator == "+":
        # this will need to change with each question (randomised)
        answer = val1 + val2
    elif operator == "-":
        answer = val1 - val2
    else:
        answer = val1 * val2
    playerAnswer = int(input("What is the answer?"))
    # check whether the answer input is correct
    print("*********************************")
    if answer == playerAnswer:  # this still does not work here yet
        print("Correct")
        # increase score for a correct answer
        score = score + 1
    elif playerAnswer > answer:
        # if wrong answer, work out whether too high or too low
        print("Sorry, you are incorrect, you are too high")
        x = playerAnswer - answer
    else:
        y = answer - playerAnswer
        print("Sorry, you are incorrect, you are too low")
        print("You are too low by... " + str(y))
    print("*********************************")

# LOOP STOPS HERE
# output name and final score
print("Thanks for playing " + name)
print("Your score is: " + str(score))
print("*************END*****************")

with open('scores.csv', mode='a') as csv_file:
    fieldnames = ['Name', 'Score', 'Difficulty']
    writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

    # writer.writeheader()
    writer.writerow({'Name': name, 'Score': score, 'Difficulty': difficulty})
# this will output the full scores list in a nicer format after each quiz result by reading in the scores csv file
f = pandas.read_csv('scores.csv')
# this will query the csv data so only easy levels are displayed
f.query('Difficulty == 1', inplace=True)
# this will sort by score in descending order
f.sort_values(["Score"], axis=0,
              ascending=False, inplace=True)
print(f)
