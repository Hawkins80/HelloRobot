from gopigo import *
import time

def shimmy():
    for x in range(2):
        right()
        time.sleep(1)
        left()
        time.sleep(1)

def twirl():
    right_rot()
    time.sleep(3)
    left_rot()
    time.sleep(3)

shimmy()
twirl()
stop()
