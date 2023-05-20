import time
import board
import busio
import digitalio
import adafruit_vl53l0x


i2cSCL = digitalio.DigitalInOut(board.GP21)
i2cSDA = digitalio.DigitalInOut(board.GP20)
i2cSCL.pull = digitalio.Pull.UP
i2cSDA.pull = digitalio.Pull.UP
#i2cSCL.direction = digitalio.Direction.OUTPUT
#i2cSDA.direction = digitalio.Direction.OUTPUT
i2cSCL.drive_mode = digitalio.DriveMode.OPEN_DRAIN
i2cSDA.drive_mode = digitalio.DriveMode.OPEN_DRAIN



i2c = busio.I2C(board.GP21, board.GP20)
distSense = adafruit_vl53l0x.VL53L0X(i2c)

led = digitalio.DigitalInOut(board.LED)
led.direction = digitalio.Direction.OUTPUT


while True:
	led.value = True
	time.sleep(0.5)
	led.value = False
	time.sleep(0.5)
	print('Range: {}mm'.format(distSense.range))