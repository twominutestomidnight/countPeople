import os
import threading

def printit():
    threading.Timer(120, printit).start()
    print("Hello, World!")
    os.system('taskkill /IM "curl.exe" /F')
printit()



#os.system('taskkill /IM "curl.exe" /F')

#print(date+1)
