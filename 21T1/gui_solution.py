# Import the random library to allow the use of randint() & choice()
from random import randint, choice
import PySimpleGUI as sg


baseNumber = 4
firstRow = [sg.Text('Welcome to the Math Quiz!', key='_message', size=(
    baseNumber*8, baseNumber), font=('Helvetica', 30))]
secondRow = [sg.Input(size=(baseNumber*6, baseNumber*2), do_not_clear=False,
                      justification='center', key='input', font=('Helvetica', 20)),
             sg.Button('Next', size=(baseNumber*2, baseNumber*2), font=('Helvetica', 20), key=('_button'))]
layout = [firstRow, secondRow]
global window
window = sg.Window('Math Quiz', layout,
                   auto_size_buttons=False, grab_anywhere=True)


def gSleep(sleepTime=1000):
    window.Read(timeout=sleepTime)


def gPrint(message, sleepTime=1000):
    window.Finalize()
    window.FindElement('_message').Update(message)
    gSleep(sleepTime)


def gInput(message):
    gPrint(message, 0)
    while True:
        event, values = window.Read()
        if event == None:
            raise SystemExit("Exit button clicked")
        if event == "_button":
            return values['input']


def intInput(message, options=None):
    userInput = None
    while userInput == None:
        try:
            userInput = int(gInput(message))
            if options is not None and userInput not in options:
                gPrint(f"Oops! What you typed isn't in {options}")
                userInput = None
        # When user does not input a number, a ValueError is raised
        except ValueError:
            if userInput == '':
                gPrint("Oops! Did you accidentally submit a blank text box?")
            else:
                gPrint(
                    "Oops! Did you accidentally type a string instead of an integer?")
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
player1 = gInput("Tell us your name, Player One")
player2 = gInput("What about you, Player Two?")
gPrint("Welcome to the maths quiz")
gPrint(f"Good luck {player1} and {player2}!\n")
# Initialise names list to hold users name input for both players
names = (player1, player2)

# Initialise variable to store difficulty selected
difficulty = intInput(
    "We can do this easy (type '1') way, or the hard (type '2') way...", (1, 2))
if difficulty == 1:
    gPrint("So you're a rookie, I see. Have no fear, for I'll go easy on you.", 2000)
# Difficulty can only be 1 or 2, so else can be used here
else:
    gPrint("Okkk so we're gonna do this the hard way.", 2000)


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
    gPrint(f"Round {roundIdx+1}? Begin.")
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
            gPrint(
                f"Question {questionIdx+1}. Ready Player {playerIdx+1}: {names[playerIdx]}!")
            playerAnswer = intInput(f"{a} {operator} {b} = ")
            # Check whether the student-provided answer is correct
            if answer == playerAnswer:
                gPrint("Yea that's right :D")
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
                gPrint(
                    f"Oh no, ya got it wrong. You're too {reason} by {absoluteDifference}:(")
                gPrint(f"The correct answer is {answer}...")
        # INNER PLAYER LOOP STOPS HERE
    # OUTER ROUND LOOP ENDS HERE
    # Report points earned for each player in round with loop
    for playerIdx in range(2):
        gPrint(
            f"{names[playerIdx]} scored {scores[playerIdx]} points in round {roundIdx+1}!")
    try:
        roundWinner = maxIndex(scores)
        gPrint(f"{names[roundWinner]}, nice. You won the round.")
        wins[roundWinner] += 1
    except TypeError:
        gPrint("It's a draw. Everyone's a winner!")
# OUTER GAME LOOP ENDS


gPrint("Time's up! Let's tally it up, shall we?")
for playerIdx in range(2):
    gPrint(f"{names[playerIdx]} won {wins[playerIdx]} times.")
try:
    gameWinner = maxIndex(wins)
    gPrint(
        f"Wow {names[gameWinner]}, it's my honour to declare you, the Winner!", 4000)
except TypeError:
    gPrint("It's a...draw? Hats off to you two for pulling it off, do you know how rare that is?", 4000)
gPrint("Anyways, thanks for playing!")
gPrint("You'll come back...")
gPrint("...right?")
