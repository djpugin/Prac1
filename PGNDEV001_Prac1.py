 #!/usr/bin/python3
"""
Python Practical Template
Keegan Crankshaw
Readjust this Docstring as follows:
Names: Devon Pugin
Student Number: PGNDEV001
Prac: 1
Date: 24/07/2019
"""

# import Relevant Librares
import RPi.GPIO as GPIO
import time
#set mode of pin layout
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
global LEDS
#sets LEDs to the correct channels
LEDS = [6,5,4]
global buttons
#set buttons  to correct channels
buttons = [12,13]
GPIO.setup(buttons, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(LEDS, GPIO.OUT, initial=GPIO.LOW)
GPIO.output(LEDS, GPIO.LOW)
i = 0

# Logic that you write

GPIO.add_event_detect(13, GPIO.RISING, bouncetime=200)
GPIO.add_event_detect(12, GPIO.RISING,bouncetime=200)


def set_mode(j):
        #takes value between 0 and 7 and outputs the binary version of that number
        vals = ["000","001","010","011","100","101","110","111"]
        lst = [0,0,0]
        for i in range(3):
 		lst[i] = int(vals[j][i])
        
	return lst

def count_up(j):
#if leds are all lit, turn them off
        if j == 7:
           j = 0
#count up in the LEDS
        else:
           j +=1

        return j

def count_down(j):
#if LEDS are all off turn them all on
        if j == 0:
           j = 7

        else:
# count down on the LEDS
           j -= 1

        return j

def main():
   global i


   x = [0,0,0]
   if GPIO.event_detected(13):
#count up if button 0 is pressed
        time.sleep(0.1)
        print("up button pressed")
        if i ==  7:
           i = 0
        else:
           i +=1

        print(i)
 	x = set_mode(i)
        print(x)
        GPIO.output(LEDS, x)


   elif GPIO.event_detected(12):
        time.sleep(0.1)
        print("down button pressed")
        if i==0:
           i = 7
        else:
           i-=1
        print(i)


        x = set_mode(i)
        print(x)
        GPIO.output(LEDS,x)


# Only run the functions if
if __name__ == "__main__":
    # Make sure the GPIO is stopped correctly
    try:
        while True:
            main()
    except KeyboardInterrupt:
        print("Exiting gracefully")
        # Turn off your GPIOs here
        GPIO.cleanup()
    except Exception as e:
        GPIO.cleanup()
        print("Some other error occurred")
        print(e.message)
