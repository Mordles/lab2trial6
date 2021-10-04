import time
import RPi.GPIO as GPIO
GPIO.cleanup()
GPIO.setmode(GPIO.BCM)

btn_input = 20;
LED_output = 21;

# GPIO btn_input set up as input.
GPIO.setup(btn_input, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(LED_output, GPIO.OUT)

GPIO.remove_event_detect(btn_input)

# handle the button event
def buttonEventHandler_rising (pin):
    # turn LED on
    GPIO.output(LED_output,True)

	
GPIO.add_event_detect(btn_input, GPIO.RISING, callback=buttonEventHandler_rising, bouncetime=100) 
 
try:  
    while True : pass  
except:
    GPIO.cleanup()      
