from machine import Pin, SoftI2C
from time import sleep_ms

from hcsr04 import HCSR04
from VL53L0X import VL53L0X

pin_led=Pin(16, Pin.OUT)

senzor_hcsr04=HCSR04(trigger_pin=18, echo_pin=19, echo_timeout_us=1000000)

i2c_vl53=SoftI2C(sda=Pin(8), scl=Pin(9), freq=1000000)
senzor_vl53=VL53L0X(i2c_vl53)

while True:
    distanta1=senzor_hcsr04.distance_cm()
    """
    if distanta1<10:
        pin_led.on()
    else:
        pin_led.off()
    """    
    senzor_vl53.start()
    distanta2=senzor_vl53.read()/10-5
    senzor_vl53.stop()
    
    if distanta2<10:
        pin_led.on()
    else:
        pin_led.off()
        
    print("Distanta 1 = ", round(distanta1,2)," ","Distanta 2 = ", round(distanta2,2),"        ", end="\r")
    
    sleep_ms(1000)