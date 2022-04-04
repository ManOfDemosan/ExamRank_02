import os
import signal

fl = open("animationPid", "r")
pid = int(fl.readline())
fl.close()
os.kill(pid, signal.SIGUSR1)
