import time
import board
import busio
import digitalio
import adafruit_vl53l0x
import pwmio



i2c = busio.I2C(board.GP21, board.GP20)
distSense = adafruit_vl53l0x.VL53L0X(i2c)

led = digitalio.DigitalInOut(board.LED)
led.direction = digitalio.Direction.OUTPUT

motorPin = pwmio.PWMOut(board.GP29)

while True:
	led.value = True
	time.sleep(0.5)
	led.value = False
	time.sleep(0.5)
	print('Range: {}mm'.format(distSense.range))

	normDist = dist.Sense.range / 1211	
	dutyCycle = (1 - normDistance) * 65535
	motorPin.duty_cycle = dutyCycle
	print(dutyCycle)


