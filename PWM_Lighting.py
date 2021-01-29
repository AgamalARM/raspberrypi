#Ahmed Gamal>>>> buzzer tone -->pwm 
import RPi.GPIO as GPIO
import tkinter
def init():
	GPIO.cleanup()
	GPIO.setmode(GPIO.BCM)
	GPIO.setup(2,GPIO.OUT)
	GPIO.output(2,GPIO.LOW)
def Tone_one():
	PwmCh.ChangeDutyCycle(10)
def Tone_two():
	PwmCh.ChangeDutyCycle(50)
def Tone_three():
	PwmCh.ChangeDutyCycle(100)	
init()
#generate PWM on channel 2 with freq=100 hz
PwmCh=GPIO.PWM(2,100)
PwmCh.start(100)
window=tkinter.Tk()
window.title("tones")  
window.geometry("300x200")
Tone_one_Button= tkinter.Button( window , text = "Tone One" , command = Tone_one)
Tone_one_Button.pack()
Tone_Two_Button= tkinter.Button( window , text = "Tone Two" , command = Tone_two)
Tone_Two_Button.pack()
Tone_Three_Button= tkinter.Button( window , text = "Tone Three" , command = Tone_three)
Tone_Three_Button.pack()
tkinter.mainloop()
