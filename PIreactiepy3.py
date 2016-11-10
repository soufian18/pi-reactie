import time
import RPi.GPIO as GPIO
import random
import csv
GPIO.setmode(GPIO.BOARD)
GPIO.setup(11,GPIO.IN)
GPIO.setup(7,GPIO.IN)
GPIO.setup(13,GPIO.OUT)
GPIO.setup(15,GPIO.OUT)
winner='onduidelijk'
player1=str(input('Speler 1 voer uw naam in: '))
player2=str(input('Speler 2 voer uw naam in: '))
randomnumber=random.randrange(2,7)
def checktrigger():
    global winner
    if GPIO.input(11) == 1:
        winner=player1
        return True
    if GPIO.input(7) == 1:
        winner=player2
        return True
    else:
        return False

time.sleep(randomnumber)
if GPIO.input(11) == 1 or GPIO.input(7)== 1:
    print('Valsspeler!')
starttime = time.time()
GPIO.output(13,True)
while GPIO.input(11) == 0 or GPIO.input(7)== 0:
    if checktrigger():
        break
    time.sleep(0.00001)
elapsedtime = time.time() - starttime
print('de winnaar is '+winner+' met een tijd van: '+str(elapsedtime))
GPIO.output(13,False)

with open('highscores.csv','a') as highscores:
    writer= csv.writer(highscores,delimiter=';')
    writer.writerow(('naam','score'))
    writer.writerow((winner,elapsedtime))
GPIO.cleanup()

