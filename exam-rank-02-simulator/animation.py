import time
import signal
import os
import sys

global run
fl = open("animationPid", "w")
fl.write(str(os.getpid()))
fl.close()

def animationHadler(signum, frame):
    global run
    run = False
    sys.exit(0)

signal.signal(signal.SIGUSR1, animationHadler)

def animate():
    animation = "|/-\\"
    idx = 0
    global run
    run = True
    while run:
        print(animation[idx % len(animation)],end="\r")
        idx += 1
        time.sleep(0.1)
animate()
