from handleAlarm import alarm
from getCurrentPeople import getStartPeopleValue


if __name__ == '__main__':
    startValue = getStartPeopleValue()
    print(startValue)
    alarm(startValue)