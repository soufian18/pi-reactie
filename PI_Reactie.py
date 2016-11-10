import time
import RPi.GPIO as GPIO
def checktrigger():
    if GPIO.input(11) == 1:
        print('input 11 wint!')
        return True
    if GPIO.input(13) == 1:
        print('input 13 wint!')
        return True
    else:
        return False
begin=input("Klik enter als je wil beginnen")
if begin:
    starttime = time.time()
    while GPIO.input(11) == 0 or GPIO.input(13)== 0:
        checktrigger()
        if checktrigger():
            break
        time.sleep(0.00001)
    elapsedtime = time.time() - starttime
    print(elapsedtime)
