from time import time, localtime, strftime, sleep
from syslog import syslog

strftime_format = "%a, %d %b %Y %H:%M:%S"

last_log = time()
syslog(f"Started sensor script at {strftime(strftime_format, localtime())}")

while True:
    # log alive messages every 5 minutes
    current = time()
    if current - last_log > 300:
        syslog(f"Alive at {strftime(strftime_format, localtime())}")

    sleep(60)


