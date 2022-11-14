import time
import board
import adafruit_bmp280

i2c = board.I2C()

bmp280 = adafruit_bmp280.Adafruit_BMP280_I2C(i2c)
bmp280.sea_level_pressure = 1021.3


from digitalio import DigitalInOut, Direction, Pull

led1 = DigitalInOut(board.D17)
led2 = DigitalInOut(board.D27)
led3 = DigitalInOut(board.D22)
led1.direction = Direction.OUTPUT
led2.direction = Direction.OUTPUT
led3.direction = Direction.OUTPUT


while True:
    print("\nTemperature: %0.1f C" % bmp280.temperature)
    print("Pressure: %0.1f hPa" % bmp280.pressure)
    print("Altitude = %0.2f meters" % bmp280.altitude)
    time.sleep(1)
    if bmp280.temperature > 31:
        led1.value = False
        led2.value = False
        led3.value = True
    elif bmp280.temperature > 30:
        led1.value = True
        led2.value = False
        led3.value = False
    else:
        led1.value = False
        led2.value = True
        led3.value = False