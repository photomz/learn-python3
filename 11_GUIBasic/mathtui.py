from random import randint, choice

def getIntInput(message, domain=None):
    cin = None
    while cin == None:
        try:
            cin = int(input(message))
            if domain and cin not in domain: cin = None
        except ValueError: 
            print("Oops! Did you accidentally type a string instead of an integer?")
            cin == None
    return cin


def getNames():
    player1 = input("Player 1, please enter your name: ")
    player2 = input("Player 2, please enter your name: ")
    print("\nWelcome to the maths quiz")
    print("Good luck {} and {}!\n".format(player1, player2))
    return [player1, player2]


def getDifficulty():
    cin = getIntInput("Please choose a difficulty (1=easy, 2=medium, 3=hard): ", (1,2,3))
    wordDifficulty = "easy" if cin == 1 else "medium" if cin == 2 else "hard"
    print("You have selected the {} quiz".format(wordDifficulty))
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
        print("Correct")
    else: 
        print("Sorry, you're too {} - the correct answer is {}.".format("low" if playerAnswer < answer else "high", answer))
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

names = getNames()
difficulty = getDifficulty()
wins = [0]*2
# Outer game loop
for i in range(2):
    scores = [0]*2
    # Round loop
    print("\n\n\nRound {} is starting!!!".format(i+1))
    for j in range(3):
        # Player loop
        for k in range(2):
            print("{}, it's your turn!".format(names[k]))
            first, op, second, ans = getQuestion(difficulty)
            playerAnswer = getIntInput("{} {} {} : ".format(first, op, second))
            if checkAnswer(playerAnswer, ans): scores[k]+=1
            print('\n')
    # Score reporting loop
    for k in range(2): print("{}, you got {} points!".format(names[k], scores[k]))
    winner, message = checkWins(scores, names)
    if winner != None: wins[winner] += 1
    print(message)


print(thanksForPlaying(names, wins))
