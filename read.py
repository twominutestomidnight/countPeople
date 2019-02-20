from getCurrentPeople import getStartPeopleValue
from handleAlarm import alarm
#from bitrate import getStreamAlert
'''
from threading import Thread

class Waiter(Thread):
    def run(self):
        startValue = getStartPeopleValue()
        # startValue = 358
        print(startValue)
        alarm(startValue)



class Worker(Thread):
    def run(self):
        getStreamAlert()

'''
if __name__ == '__main__':

    startValue = getStartPeopleValue()
    #startValue = 358
    print(startValue)
    alarm(startValue)
    '''
    Worker().start()
    Waiter().start()
    '''