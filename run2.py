import os
import threading

def printit():
    threading.Timer(121, printit).start()
    print("Hello, World!")
    os.system('python bitrate.py')

printit()