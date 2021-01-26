#Auther : Ahmed Gamal
#led on off
#Date 15 Jen 2021
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(2,GPIO.OUT)

while True:
	x=str(input("please enter the value:"))
	if x=="ON":
		GPIO.output(2,GPIO.HIGH)
		
	elif x=="OFF":
		GPIO.output(2,GPIO.LOW)
			
	else:
		print("invallid value, try again")
