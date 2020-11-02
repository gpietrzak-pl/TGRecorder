import pyautogui
import sys
pyautogui.FAILSAFE = True
j = 0
i = 1
screenWidth, screenHeight = pyautogui.size()
while int(j) < 1:   
    j = pyautogui.confirm(text='1 TO START      0 TO USTAWIENIE KURSORA', title='Autoclicker Telegram by Ares Neptuno', buttons=['1', '0'])
    if int(j) < 1:
        print('Kliknij Ctrl-C aby ustawić punkt.')
        try:
            while True:
                x, y = pyautogui.position()
                positionStr = 'X: ' + str(x).rjust(4) + ' Y: ' + str(y).rjust(4)
                print(positionStr, end='')
                print('\b' * len(positionStr), end='', flush=True)
        except KeyboardInterrupt:
            print('\n')

        f = open("x.txt", "w")
        f.write(str(x))
        f.close()
        f = open("y.txt", "w")
        f.write(str(y))
        f.close()

       

 
while int(i) > 0:   
    i = pyautogui.confirm(text='1 TO START      0 TO STOP', title='Autoclicker Telegram by Ares Neptuno', buttons=['1', '0'])
    if int(i) > 0:
        f = open('x.txt', 'r')
        inputx = f.readline()
        f.close()
        print(inputx)
        f = open('y.txt', 'r')
        inputy = f.readline()
        f.close()
        print(inputy)
        pyautogui.moveTo(int(inputx), int(inputy)) 
        pyautogui.click(clicks=2)
        pyautogui.mouseDown()    
            

 
