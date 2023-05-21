import time
import board
import busio
import digitalio
import adafruit_vl53l0x
import pwmio
import math

maxDistVal = 1211 #max recorded valid value so far

i2c = busio.I2C(board.GP21, board.GP20)
distSense = adafruit_vl53l0x.VL53L0X(i2c)

led = digitalio.DigitalInOut(board.LED)
led.direction = digitalio.Direction.OUTPUT

motorPin = pwmio.PWMOut(board.GP22)

while True:
	led.value = True
	time.sleep(0.5)
	led.value = False
	time.sleep(0.5)
	print('Range: {}mm'.format(distSense.range))
	
	# distSense is ALWAYS 0 to 8192
	distSenseRange = distSense.range
	if (distSenseRange > maxDistVal):
		distSenseRange = maxDistVal

	normDist = distSenseRange / maxDistVal
	dutyCycle = (1 - normDist) * 65535
	motorPin.duty_cycle = math.floor(dutyCycle)
	print(dutyCycle)


