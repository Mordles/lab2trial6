import time
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)

GPIO.cleanup()

btn_input = 20;
LED_output = 21;

# GPIO btn_input set up as input.
GPIO.setup(btn_input, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(LED_output, GPIO.OUT)

# handle the button event
def buttonEventHandler_rising (pin):
    # turn LED on
    GPIO.output(LED_output,True)

	
GPIO.add_event_detect(btn_input, GPIO.FALLING, callback=buttonEventHandler_rising, bouncetime=100)

while True:
	print('Hello')
	time.sleep(0.1)
	
GPIO.cleanup()
 
