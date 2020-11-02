import PySimpleGUI as sg
import pyautogui
import sys

sg.ChangeLookAndFeel('GreenTan')

# ------ Menu Definition ------ #
menu_def = [#['&File', '&Properties', '&Exit'],
            ['&Help', '&About...'], ]

layout = [  [sg.Menu(menu_def, tearoff=True)],
            [sg.Button('Zapisz', enable_events=True), sg.Button('Nagrywaj', enable_events=True)] ]

# Create the Window
window = sg.Window('TgRecorder', layout)
# Event Loop to process "events" and get the "values" of the inputs
while True:
    event, values = window.read()
    if event in (sg.WIN_CLOSED, 'Quit', 'Exit'): # if user closes window or clicks cancel
        break
    if event.startswith('About'):
        sg.Popup('For help: http://gpietrzak.pl/tgr')
    if event.startswith('Zapisz'):
        print("1. Kliknij w to okno")
        print("2. Najedź kursorem na wybrane miejsce")
        print("3. Kliknij Ctrl-C aby zapisać pozycję kursora.")
        #TODO: how to get mouse position?
        try:
            while True:
                x, y = pyautogui.position()
                positionStr = "X: " + str(x).rjust(4) + " Y: " + str(y).rjust(4)
                print(positionStr, end="")
                print('\b' * len(positionStr), end="", flush=True)
        except KeyboardInterrupt:
            print('Zapisane!')

        f = open("config.cfg", "w")
        f.write(str(x)+"\n"+str(y))
        f.close()

    if event.startswith('Nagrywaj'):
        f = open("config.cfg", "r")
        inputx = f.readline()
        inputy = f.readline()
        f.close()

        pyautogui.moveTo(int(inputx), int(inputy)) 
        pyautogui.click(clicks=2)
        pyautogui.mouseDown()