from time import time, sleep
from random import randint, choice
import PySimpleGUI as sg

# //////// START GUI CHANGES ///////////
baseNumber = 4
sleepTime =0.5

layout = [[sg.Text('Welcome to the Math Quiz!', key='_message', size=(baseNumber*8, baseNumber), font=('Helvetica', 30))],
          [sg.Input(size=(baseNumber*6, baseNumber*2), do_not_clear=False,
                    justification='center', key='input', font=('Helvetica', 20)), sg.Button('Next', size=(baseNumber*2, baseNumber*2), font=('Helvetica', 20), key=('_button'))]
        ]

window = sg.Window('Math Quiz', layout, auto_size_buttons=False, grab_anywhere=True)
def customSleep(sleepTime=500):
    window.Read(timeout=sleepTime)

def customPrint(message, sleepTime=500):
    window.Finalize()
    window.FindElement('_message').Update(message)
    customSleep(sleepTime)

def customInput(message):
    customPrint(message, 0)
    while True:
        event, values = window.Read();
        if event == None:
            raise SystemExit("Exit button clicked")
        if event == "_button":
            return values['input']

# /////// END GUI CHANGES /////////////

def getIntInput(message, domain=None):
    cin = None
    while cin == None:
        try:
            cin = customInput(message)
            cin=int(cin)
            if domain and cin not in domain: cin = None
        except ValueError: 
            if cin == '': customPrint("Oops! Did you accidentally submit a blank text box?")
            else: customPrint("Oops! Did you accidentally type a string instead of an integer?")
            cin = None
    return cin


def getNames():
    player1 = customInput("Player 1, please enter your name")
    player2 = customInput("Player 2, please enter your name")
    customPrint("Welcome to the maths quiz")
    customPrint("Good luck {} and {}!\n".format(player1, player2))
    return [player1, player2]


def getDifficulty():
    cin = getIntInput("Please choose a difficulty (1=easy, 2=medium, 3=hard): ", (1,2,3))
    wordDifficulty = "easy" if cin == 1 else "medium" if cin == 2 else "hard"
    customPrint("You have selected the {} quiz".format(wordDifficulty))
    return cin


def getQuestion(difficulty):
    assert difficulty == 1 or difficulty == 2 or difficulty == 3
    firstRange = 10 if difficulty == 1 else 100
    secondRange = 100 if difficulty == 3 else 10
    operator = choice(("+", "-", "*"))
    firstNumber = randint(1, firstRange)
    secondNumber = randint(1, secondRange)
    a, b = firstNumber, secondNumber
    assert operator in ('+', '-', '*')
    if operator == '+':
        answer = a+b
    elif operator == '-':
        answer = a-b
    elif operator == '*':
        answer = a*b
    return (firstNumber, operator, secondNumber, answer)

def checkAnswer(playerAnswer, answer):
    if answer == playerAnswer:  # this now works again!!!
        customPrint("Correct")
    else: 
        customPrint("Sorry, you're too {} - the correct answer is {}.".format("low" if playerAnswer < answer else "high", answer))
    return answer == playerAnswer

def uniqueMax(arr):
    maybeMax = max(arr)
    if len([item for item in arr if item == maybeMax]) > 1:
        return None
    else: return maybeMax

def checkWins(scores, names):
    trueMax = uniqueMax(scores)
    if trueMax == None:
        return (None, "This match was a draw! Everyone's a winner!")
    else:
        playerIndex = scores.index(trueMax)
        return (playerIndex, "Well done {} you are the winner of this game!".format(names[playerIndex]))

def thanksForPlaying(players, wins):
    customPrint("Thanks for playing!")
    for i in range(len(players)):
        customPrint("{}, you won {} times.".format(players[i], wins[i]))
    customPrint(checkWins(wins, players)[1])
    customPrint("Thanks for playing! See you soon!")

print("Math Engine roaring to life!")
names = getNames()
difficulty = getDifficulty()
wins = [0]*2
# Outer game loop
for i in range(2):
    scores = [0]*2
    # Round loop
    customPrint("Round {} is starting!!!".format(i+1))
    for j in range(3):
        # Player loop
        for k in range(2):
            first, op, second, ans = getQuestion(difficulty)
            playerAnswer = getIntInput("{}, it's your turn!\n{} {} {} : ".format(names[k], first, op, second))
            if checkAnswer(playerAnswer, ans): scores[k]+=1
    # Score reporting loop
    for k in range(2): 
        customPrint("{}, you got {} points!".format(names[k], scores[k]))
    winner, message = checkWins(scores, names)
    if winner != None: wins[winner] += 1
    customPrint(message)


thanksForPlaying(names, wins)
