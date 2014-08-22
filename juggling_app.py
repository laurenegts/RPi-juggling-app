#!/usr/bin/python
#above line makes the system think that the program is in python

import pibrella
import time
import subprocess

presstime = 0.

def button_changed(pin):
	global presstime
	if pin.read() == 1:
		presstime = time.time()
		#print(presstime)
		pibrella.light.green.on()
	else:
		releasetime = time.time()
		timedifference = releasetime - presstime #how long the button was pressed
		if timedifference < 3.:
			pibrella.light.green.off() #start off with green light off
			print("start pin sequence")
			#start pin sequence
			subprocess.call(["/home/pi/startall.sh"])
		else:
			pibrella.light.yellow.off() #light turns off when shutdown happens
			print("Shutdown!")
			#do the shutdown
			#subprocess.call(["echo", "shutdown -h now"])
			subprocess.call(["/usr/bin/shutdown", "-h", "now"])

def lighttransition():
	global presstime
	time.sleep(.1) #has the program wait
	if pibrella.button.read() == 1 or pibrella.input.a.read() == 1:
	#above line checks both of the buttons for changes
		time.sleep(.1)
		currenttime = time.time()
		timedifference = currenttime - presstime
		#print(timedifference, currenttime, presstime)
		if timedifference > 3.: #the transition between the lights to show what is going on
			pibrella.light.green.off()
			pibrella.light.yellow.on()

#turns red led on to show that the program is running
pibrella.light.red.on()

pibrella.button.changed(button_changed) #calling the functions
pibrella.input.a.changed(button_changed) #has it run the button changed function when the wired button is pressed
pibrella.loop(lighttransition)
pibrella.pause()

