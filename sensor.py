from time import time, localtime, strftime, sleep
from syslog import syslog
from gpiozero import DistanceSensor, Buzzer, LED
import os

strftime_format = "%a, %d %b %Y %H:%M:%S"

last_log = time()
syslog(f"Started sensor script at {strftime(strftime_format, localtime())}")


# Blink the activity led to show that the script is active
led_cmd = 'echo none | sudo tee /sys/class/leds/led0/trigger'
os.system(led_cmd)
activity = LED(47)
activity.blink()


max_distance = 0.5
sensor = DistanceSensor(echo=23, trigger=24, max_distance=max_distance,
        threshold_distance=0.05)
# buz = Buzzer(17)
led = LED(17)

while True:
    dist = sensor.distance
    current = time()
    if dist < max_distance:
        led.on()
        sleep(dist)
        led.off()
        sleep(dist)

        if current - last_log > 10:
            syslog(f"Alive at {strftime(strftime_format, localtime())}. Distance {dist}")
            last_log = time()
    else:
        # log alive messages every 5 minutes
        if current - last_log > 300:
            syslog(f"Alive at {strftime(strftime_format, localtime())}. Distance {dist}")
            last_log = time()
        sleep(10)


