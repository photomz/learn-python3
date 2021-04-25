from random import randint, choice # Import the random library to allow the use of randint() & choice()
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


# Custom sleep function.
def gSleep(sleepTime=1000):
		window.Read(timeout=sleepTime)

# Print to GUI.
def gPrint(message, sleepTime=1000):
		window.Finalize()
		window.FindElement('_message').Update(message)
		gSleep(sleepTime)

# Get input from GUI.
def gInput(message):
		gPrint(message, 0)
		while True:
				event, values = window.Read()
				if event == None:
						raise SystemExit("Exit button clicked")
				if event == "_button":
						return values['input']

# Get integer input from GUI.
# Keeps trying until it gets valid input that satisfies options (if given)
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
								gPrint("Oops! Did you accidentally type a string instead of an integer?")
						userInput = None
		return userInput

# Finds the index where the maximum array value is
# If there are duplicate maximum values, returns None. Maximum must be unique.
def maxIndex(array):
		duplicate = False
		maxIdx = 0
		for currentIdx in range(len(array)):
			if (array[currentIdx] > array[maxIdx]): 
				maxIdx = currentIdx
				duplicate = False
			elif (array[currentIdx] == array[maxIdx]):
				duplicate = True
		if duplicate: return None
		return maxIdx

numRounds = 2
numQuestions = 3

print("Math Engine roaring to life!")


# Initialise names list to hold users name input for both players

# Initialise variable to store difficulty selected

# OUTER GAME LOOP STARTS HERE
# Use numRounds as loop total and roundIdx as loop start point. 
# After each loop/question, roundIdx will grow until it reaches numRounds
wins = (0, 0)
for roundIdx in range(numRounds):
		scores = (0, 0)
		# OUTER ROUND LOOP STARTS HERE
		# Use numQuestions as loop total and roundIdx as loop start point. 
		# After each loop/question, roundIdx will grow until it reaches numQuestions
		# Asks "numQuestions" questions to both players in a single round.
		for questionIdx in range(numQuestions):
				# INNER PLAYER LOOP STARTS HERE
				# Asks a question to each player, use playerIdx to know which player.
				for playerIdx in range(2):

						# Set two variables to a random integer, these will form the two numbers for each question
					
						# Test players on addition, subtraction, or multiplication

						# Calculate the correct answer depending on the randomly selected operator.

						# Check whether the student-provided answer is correct

				# INNER PLAYER LOOP STOPS HERE
		# OUTER ROUND LOOP ENDS HERE

		# Report points earned for each player in round


# OUTER GAME LOOP ENDS


# Report rounds won by each player
