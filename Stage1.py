from gpiozero import LED, Button
from time import sleep
led = LED(4)
led.on()
sleep(5)
led.off()
