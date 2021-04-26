import PySimpleGUI as sg

firstRow = [sg.Text('Welcome', key='_message', size=(40,1))]
secondRow = [sg.Input(key='_input'), sg.Button('Next', key=('_button'))]
layout = [firstRow, secondRow]

window = sg.Window('Square Root Calculator', layout, finalize=True)


def gPrint(message, sleepTime=1000):
    window.FindElement('_message').Update(message)
    window.Read(timeout=sleepTime)


def gInput(message):
    gPrint(message, 0)
    while True:
        event, values = window.Read()
        if event == None:
            raise SystemExit("Exit button clicked")
        if event == "_button":
            return values['_input']


def intInput(message, options=None):
    userInput = None
    while userInput == None:
        try:
            userInput = int(gInput(message))
            if options != None and userInput not in options:
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

while True:
	num = intInput("Enter a positive number")
	gPrint(f'Sqrt({num}) = {num**0.5}')