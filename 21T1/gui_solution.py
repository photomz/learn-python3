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
                userInput = None
        # When user does not input a number, a ValueError is raised
        except ValueError:
            if userInput == '':
                gPrint(
                    "Oops! Did you accidentally submit a blank text box?")
            else:
                gPrint(
                    "Oops! Did you accidentally type a string instead of an integer?")
            userInput = None
    return userInput


def maxIndex(array):
    duplicate = False
    maxIdx = -1e10
    for currentIdx in range(len(array)):
        if (array[currentIdx] > array[maxIdx]):
            maxIdx = currentIdx
            duplicate = False
        elif (array[currentIdx] == array[maxIdx]):
            duplicate = True
    if duplicate:
        return None
    return maxIdx


print("Math Engine roaring to life!")
player1 = gInput("Tell us your name, Player One -> ")
player2 = gInput("What about you, Player Two? -> ")
gPrint("Welcome to the maths quiz")
gPrint(f"Good luck {player1} and {player2}!\n")
names = (player1, player2)

difficulty = intInput(
    "We can do this easy (type '1') way, or the hard (type '2') way... -> ", (1, 2))
if difficulty == 1:
    gPrint("So you're a rookie, I see. Have no fear, for I'll go easy on you.", 2000)
# Difficulty can only be 1 or 2, so else can be used here
else:
    gPrint("So we're gonna do this the hard way.")
    gPrint("This quiz only stops in the event of emergency.")
    gPrint("Crying is not an emergency.", 2000)
wins = [0]*2
# Outer game loop
for roundIdx in range(2):
    scores = [0]*2
    # Round loop
    gPrint(f"Round {roundIdx+1}? Begin.")
    for questionIdx in range(3):
        # Player loop
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
            gPrint(f"Ready Player {playerIdx+1}: {names[playerIdx]}!")
            playerAnswer = intInput(f"{a} {operator} {b} = ")
            # Check whether the student-provided answer is correct
            if answer == playerAnswer:
                gPrint("Yea that's right :D")
            else:
                lowOrHigh = "low" if playerAnswer < answer else "high"
                gPrint(f"Oh no, ya got it wrong. You're too {lowOrHigh} :(")
                gPrint(f"The correct answer is {answer}...")
            isCorrect = playerAnswer == answer
            if isCorrect:
                scores[playerIdx] += 1
    # Score reporting loop
    for playerIdx in range(2):
        gPrint(
            f"{names[playerIdx]} scored {scores[playerIdx]} points in round {roundIdx+1}!")
    try:
        roundWinner = maxIndex(scores)
        gPrint(f"{names[roundWinner]}, nice. You won the round.")
        wins[roundWinner] += 1
    except ValueError:
        gPrint("It's a draw. Everyone's a winner!")

gPrint("Time's up! Let's tally it up, shall we?")
for playerIdx in range(2):
    gPrint(f"{names[playerIdx]} won {wins[playerIdx]} times.")
try:
    gameWinner = maxIndex(wins)
    gPrint(
        f"Wow {names[gameWinner]}, it's my honour to declare you, the Winner!", 4000)
except ValueError:
    gPrint("It's a...draw? Hats off to you two for pulling it off, do you know how rare that is?", 4000)
gPrint("Anyways, thanks for playing!")
gPrint("You'll come back...")
gPrint("...right?")
