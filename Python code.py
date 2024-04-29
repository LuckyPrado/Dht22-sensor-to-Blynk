import time
import board
import adafruit_dht

import BlynkLib
import RPi.GPIO as GPIO
from BlynkTimer import BlynkTimer


#Sensor data pin is connected to GPIO 4
sensor = adafruit_dht.DHT22(board.D4, use_pulseio=False)

#Authentication code to connect with Blynk
BLYNK_AUTH_TOKEN = 'FhFUcnKpXU-QA5iLgTj2BQpysbRwOr9B'

# Initialize Blynk
blynk = BlynkLib.Blynk(BLYNK_AUTH_TOKEN)

# Create BlynkTimer Instance
timer = BlynkTimer()

# function to sync the data from virtual pins
@blynk.on("connected")
def blynk_connected():
    print("Hi, You have Connected to New Blynk2.0")
    print(".......................................................")
    print("................... By SME Dehradun ...................")
    time.sleep(2);

def TempHum():
    temperature = None
    humidity = None
    
    try:
    #Print the temperature and humidity
        temperature = sensor.temperature
        humidity = sensor.humidity
        print("Temp={0:.1f}C Humidity={1:0.1f}%".format(temperature, humidity))
    
    except RuntimeError as error:
        print(error.args[0])
        time.sleep(2.0)
    except Exception as error:
        sensor.exit()
        raise error

    time.sleep(2.0)
    
    blynk.virtual_write(0, humidity)
    blynk.virtual_write(1, temperature)
    print("Values sent to New Blynk Server!")

timer.set_interval(2, TempHum)


while True:
    blynk.run()
    timer.run()

