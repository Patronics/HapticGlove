import time
import board
import busio
import digitalio
import analogio
import pwmio
import adafruit_vl53l0x
import math

maxDistVal = 1270 #max recorded valid value so far
minPotVal = 300
maxPotVal = 65535


i2c = busio.I2C(board.GP21, board.GP20)
distSense = adafruit_vl53l0x.VL53L0X(i2c)

led = digitalio.DigitalInOut(board.LED)
led.direction = digitalio.Direction.OUTPUT

pot = analogio.AnalogIn(board.GP26_A0)

motorPin = pwmio.PWMOut(board.GP16)

while True:
	led.value = True
	time.sleep(0.1)
	led.value = False
	time.sleep(0.1)
	print('Range: {}mm'.format(distSense.range))
	

	# distSense is ALWAYS 0 to 8192
	distSenseRange = distSense.range
	potVal = pot.value
	if (potVal < minPotVal):
		potVal = 0
	else:
		potVal = potVal/maxPotVal
	
	if (distSenseRange > (maxDistVal*potVal)):
		distSenseRange = maxDistVal
	
	print('Pot: {}'.format(potVal))
	normDist = distSenseRange / maxDistVal
	dutyCycle = (1 - normDist) * 65535
	motorPin.duty_cycle = math.floor(dutyCycle)
	print('Duty Cycle: {}'.format(dutyCycle))


