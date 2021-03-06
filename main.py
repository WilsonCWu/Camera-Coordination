import ball_tracking
import threading
import time
import smbus

# for RPI version 1, use “bus = smbus.SMBus(0)”
bus = smbus.SMBus(1)

# This is the address we setup in the Arduino Program
address = 0x04

def writeNumber(value):
	bus.write_byte(address, value)
	# bus.write_byte_data(address, 0, value)
	return -1

while True:
	writeNumber(6)
	print ("RPI: Hi Arduino, I sent you ", var)
	# sleep one second
	time.sleep(1)

#Create a ball tracker, and start the thread
cameraThread = ball_tracking.BallTracker()
cameraThread.start()

FPS = 30
delay = 1.5/FPS
pctOn = 1

prevAngle = 0

def reduceSpeed():
	time.sleep(pctOn*delay)
	motorDriver.motorsOff()
	time.sleep((1-pctOn)*delay)

#Loop a couple of times
while True:
        time.sleep(1)
	#Get the new camera update from the 
	info = cameraThread.getBallInfo()
	if (info):
		if (not info == True):
		#so that we can break at any point
			x = 640 - info[0] ##flip across x axis
			y = info[1]
			realX = -7 + (float)(x-38)*(15)/558
			realY = 14 + (float)(y-40)*(5)/188
			print("Location: "+str(640-x)+"\t"+str(y)+"\nLocationReal: "+str(realX)+"\t"+str(realY))
##			#print(x)
##			radius = info[2]
##			theta = info[3] - 5
##			topTheta = info[4]
##			bottomTheta = 2*theta - topTheta
##			print(str(theta)+","+str(topTheta))
##
##			#If the ball is off center left, spin that way
##			if (x < (cameraThread.width/2 - 50)):
##				motorDriver.right(False)
##				motorDriver.left(True)
##				reduceSpeed()
##
##			#If the ball is off center right, spin that way
##			elif (x > (cameraThread.width/2 + 50)):
##				motorDriver.right(True)
##				motorDriver.left(False)
##				reduceSpeed()
##
##			# For now, if the ball is centered, charge it head on
##			else:
##				if (not (prevAngle > bottomTheta and prevAngle < topTheta)) and (abs(prevAngle - theta) > 2):
##					servo.setServoPos(theta, 10)
##					prevAngle = theta
##				#motorDriver.forward()
##				
##				
##		else:
##			motorDriver.left(True)
##			motorDriver.right(False)
##			reduceSpeed()
