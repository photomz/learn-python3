# Import the random library to allow the use of randint() & choice()
from random import randint, choice


def intInput(message, options=None):
    userInput = None
    while userInput == None:
        try:
            userInput = int(input(message))
            if options is not None and userInput not in options:
                print(f"Oops! What you typed isn't in {options}")
                userInput = None
        # When user does not input a number, a ValueError is raised
        except ValueError:
            if userInput == '':
                print("Oops! Did you accidentally submit a blank text box?")
            else:
                print("Oops! Did you accidentally type a string instead of an integer?")
            userInput = None
    return userInput


def maxIndex(array):
    duplicate = False
    maxIdx = 0
    for currentIdx in range(len(array)):
        if (array[currentIdx] > array[maxIdx]):
            maxIdx = currentIdx
            duplicate = False
        elif (array[currentIdx] == array[maxIdx]):
            duplicate = True
    if duplicate:
        return None
    return maxIdx


numRounds = 2
numQuestions = 3

print("Math Engine roaring to life!")
player1 = input("Tell us your name, Player One --> ")
player2 = input("What about you, Player Two? --> ")
print("Welcome to the maths quiz")
print(f"Good luck {player1} and {player2}!\n")
# Initialise names list to hold users name input for both players
names = (player1, player2)

# Initialise variable to store difficulty selected
difficulty = intInput(
    "We can do this easy (type '1') way, or the hard (type '2') way...", (1, 2))
if difficulty == 1:
    print("So you're a rookie, I see. Have no fear, for I'll go easy on you.")
# Difficulty can only be 1 or 2, so else can be used here
else:
    print("Okkk so we're gonna do this the hard way.")


# OUTER GAME LOOP STARTS HERE
# Use numRounds as loop total and roundIdx as loop start point.
# After each loop/question, roundIdx will grow until it reaches numRounds
wins = [0, 0]
for roundIdx in range(numRounds):
    scores = [0, 0]
    # OUTER ROUND LOOP STARTS HERE
    # Use numQuestions as loop total and roundIdx as loop start point.
    # After each loop/question, roundIdx will grow until it reaches numQuestions
    # Asks "numQuestions" questions to both players in a single round.
    print(f"Round {roundIdx+1}? Begin.")
    for questionIdx in range(numQuestions):
        # INNER PLAYER LOOP STARTS HERE
        # Asks a question to each player, use playerIdx to know which player.
        for playerIdx in range(2):
            # Set two variables to a random integer, these will form the two numbers for each question
            # Select integer from 1 to 10 if player selected easy level
            if difficulty == 1:
                a = randint(1, 10)
                b = randint(1, 10)
            else:
                # Select integer from 1 to 100 if player selected hard level
                a = randint(1, 100)
                b = randint(1, 100)
            # The possibleOperators list stores the values for possible operators for the questions
            # Test players on addition, subtraction, or multiplication
            possibleOperators = ("+", "-", "*")
            # choice() will randomly select one operator from the possibleOperators list
            operator = choice(possibleOperators)
            # Calculate the correct answer depending on the randomly selected operator.
            # Answer is recalculated with each question
            if operator == '+':
                answer = a+b
            elif operator == '-':
                answer = a-b
            elif operator == '*':
                answer = a*b
            print(
                f"Question {questionIdx+1}. Ready Player {playerIdx+1}: {names[playerIdx]}!")
            playerAnswer = intInput(f"{a} {operator} {b} = ")
            # Check whether the student-provided answer is correct
            if answer == playerAnswer:
                print("Yea that's right :D")
                # Increment score for current player by 1, since they got it correct
                scores[playerIdx] += 1
            else:
                # Calculate absolute difference between correct answer and actual answer: how much is the player off by?
                absoluteDifference = abs(answer - playerAnswer)
                # If wrong answer, work out whether too high or too low
                if playerAnswer < answer:
                    reason = "low"
                else:
                    reason = "high"
                print(
                    f"Oh no, ya got it wrong. You're too {reason} by {absoluteDifference} :(")
                print(f"The correct answer is {answer}...")
        # INNER PLAYER LOOP STOPS HERE
    # OUTER ROUND LOOP ENDS HERE
    # Report points earned for each player in round with loop
    for playerIdx in range(2):
        print(
            f"{names[playerIdx]} scored {scores[playerIdx]} points in round {roundIdx+1}!")
    try:
        roundWinner = maxIndex(scores)
        print(f"{names[roundWinner]}, nice. You won the round.")
        wins[roundWinner] += 1
    except TypeError:
        print("It's a draw. Everyone's a winner!")
# OUTER GAME LOOP ENDS


print("Time's up! Let's tally it up, shall we?")
for playerIdx in range(2):
    print(f"{names[playerIdx]} won {wins[playerIdx]} times.")
try:
    gameWinner = maxIndex(wins)
    print(
        f"Wow {names[gameWinner]}, it's my honour to declare you, the Winner!")
except TypeError:
    print("It's a...draw? Hats off to you two for pulling it off, do you know how rare that is?")
print("Anyways, thanks for playing!")
print("You'll come back...")
print("...right?")
