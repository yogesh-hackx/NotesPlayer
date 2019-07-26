import pyautogui as pgui
import pyxhook
import threading
import keyboard  # using module keyboard
import re
import time

notes = open("notes.txt")
m = True

pgui.PAUSE = 0.03

def noteLine():
    m = True
    while(m):
        m = notes.readline()
        if "#" in m:
            return (m)
def keyPressed():
    while True: 
        try: 
            if keyboard.is_pressed('right'):  # if key 'q' is pressed 
                return False
            else:
                return True
        except:
            break

pattern = re.compile(r'(?![EB]#)[A-G](\#|b|\+)?')

matches = pattern.finditer(noteLine())

# for match in matches:
#     print(match.group())
sleepSec = 0
while matches:

    for match in matches:
            
            keyboard.wait('right')
            
            if "A" in match.group():
                pgui.press("y")
                time.sleep(sleepSec)
                # if "+" in match.group():
                    
                
            if "B" in match.group():
                pgui.press("u")
                time.sleep(sleepSec)
                # if "+" in match.group():
                    
                
            if "C" in match.group():
                pgui.press("i")
                time.sleep(sleepSec)
                # if "+" in match.group():
                    

            if "C#" in match.group():
                pgui.press("h")
                time.sleep(sleepSec)
                # if "+" in match.group():
                    

            if "E" in match.group():
                pgui.press("e")
                time.sleep(sleepSec)
                # if "+" in match.group():
                    

            if "D" in match.group():
                pgui.press("o")
                time.sleep(sleepSec)
                # if "+" in match.group():
                    

            if "D#" in match.group():
                pgui.press("j")
                time.sleep(sleepSec)
                # if "+" in match.group():
                    
                
            if "F" in match.group():
                pgui.press(",")
                time.sleep(sleepSec)
                # if "+" in match.group():
                    
                
            if "F#" in match.group():
                pgui.press("l")
                time.sleep(sleepSec)
                # if "+" in match.group():
                    

            if "G" in match.group():
                pgui.press("t")
                time.sleep(sleepSec)
                # if "+" in match.group():
                    

            if "G#" in match.group():
                pgui.press(";")
                time.sleep(sleepSec)
                # if "+" in match.group():
                    

            if "Bb" in match.group():
                pgui.press("'")
                time.sleep(sleepSec)
                # if "+" in match.group():
    matches = pattern.finditer(noteLine())
            

            


'''if __name__ == "__main__": 
    # creating thread 
    t1 = threading.Thread(target= eachNote) 
    t2 = threading.Thread(target=keyDetect) 
  
    # starting thread 1 
    t1.start() 
    # starting thread 2 
    t2.start()
'''


        