from time import time, sleep
from random import randint, choice
import PySimpleGUI as sg

baseNumber = 8

layout = [[sg.Text('Welcome to the Math Quiz!', key='_message', size=(baseNumber*8, baseNumber))],
          [sg.showMessage(size=(baseNumber*6, baseNumber), do_not_clear=True,
                    justification='center', key='showMessage'), sg.Button('Next', size=(baseNumber*2, baseNumber), key=('_button'))]
        ]

window = sg.Window('Math Quiz', layout, auto_size_buttons=False, grab_anywhere=True)

def showMessage(message):
        window.Element('_message').Update(message)

def getInput(message):
    None

def getIntInput(message, domain=None, submitted=False):
    cin = None
    while cin == None:
        try:
            cin = int(getInput(message))
            if domain and cin not in domain: 
                showMessage("Oops! Did you accidentally type an invalid option?")
                cin = None
        except ValueError: 
            showMessage("Oops! Did you accidentally type a string instead of an integer?")
            cin = None
    return cin

def getDifficulty():
    cin = getIntInput("Please choose a difficulty (1=easy, 2=medium, 3=hard)", (1,2,3))
    wordDifficulty = "easy" if cin == 1 else "medium" if cin == 2 else "hard"
    showMessage("You have selected the {} quiz".format(wordDifficulty))
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
        showMessage("Correct")
    else: 
        showMessage("Sorry, you're too {} - the correct answer is {}.".format("low" if playerAnswer < answer else "high", answer))
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
    message = "Thanks for playing!\n"
    for i in range(len(players)): message += "{}, you won {} times.".format(players[i], wins[i])
    message += '\n\n'
    message += checkWins(wins, players)[1]
    message += "Thanks for playing!\nSee you soon!"
    return message



def getNames():
    player1 = getInput("Player 1, please enter your name")
    player2 = getInput("Player 2, please enter your name")
    showMessage("Welcome to the maths quiz\nGood luck {} and {}!".format(player1, player2))
    return [player1, player2]

def checkContinue(limit):
    # Vars available globally
    global gameIndex, playerIndex
    if playerIndex < limit-1: playerIndex += 1
    else: 
        playerIndex = 0
        gameIndex += 1

def checkPlayerRoundContinue(limit):
    global gameIndex, playerIndex, roundIndex
    if playerIndex < limit-1: playerIndex += 1
    else:
        playerIndex = 0
        roundIndex += 1

def checkRoundContinue(limit):

first,op,second,ans=None, None, None, None
gameIndex, playerIndex, roundIndex = 0,0,0
names, roundWins, difficulty = [],[0]*2,None

# Loop forever reading the window's values, updating the input field
while True:
    event, values = window.Read(timeout=10)  # read the window
    if event is None:  # if the X button clicked, just exit
        break
    assert isinstance(values[0], str) 
    userInput = values[0]

    if gameIndex == 0:
        if event == 'Next': 
            names.append(userInput)
            checkContinue(2)
        showMessage("Player {}, please enter your name".format(playerIndex))

    if gameIndex == 1:
        showMessage("Please choose a difficulty (1=easy, 2=medium, 3=hard)")
        if event == 'Next':
            if userInput not in (1,2,3): 
                showMessage("Oops! Invalid input. Please choose a difficulty (1=easy, 2=medium, 3=hard)", True)
            else:
                cin = int(userInput)
                wordDifficulty = "easy" if cin == 1 else "medium" if cin == 2 else "hard"
                showMessage("You have selected the {} quiz".format(wordDifficulty))
                checkContinue(1)
    
    if gameIndex == 2:
        if textUpdate: roundWins = [0]*2
        if playerIndex == 0: showMessage("\n\n\nRound {} is starting!!!".format(roundIndex+1))
        sleep(500)
        showMessage("{}, it's your turn!".format(names[playerIndex]))
        sleep(500)
        if event == 'Next':

        else: 
            first, op, second, ans = getQuestion(difficulty)
            
        
    


#   """//////////////////////////////////////////////////////////////////////"""      

names = getNames()
difficulty = getDifficulty()
wins = [0]*2
# Outer game loop
for i in range(2):
    scores = [0]*2
    # Round loop
    showMessage("\n\n\nRound {} is starting!!!".format(i+1))
    for j in range(3):
        # Player loop
        for k in range(2):
            showMessage("{}, it's your turn!".format(names[k]))
            first, op, second, ans = getQuestion(difficulty)
            playerAnswer = getIntInput("{} {} {} : ".format(first, op, second))
            if checkAnswer(playerAnswer, ans): scores[k]+=1
            showMessage('\n')
    # Score reporting loop
    for k in range(2): showMessage("{}, you got {} points!".format(names[k], scores[k]))
    winner, message = checkWins(scores, names)
    if winner != None: wins[winner] += 1
    showMessage(message)


showMessage(thanksForPlaying(names, wins))
