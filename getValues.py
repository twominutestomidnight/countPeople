import re

def getEnter(block):
    try:
        enterValue = (int)(re.findall(r'<enter>(.*?)<\/enter>', block, re.DOTALL)[0])
        return enterValue
    except:
        #print("wrong reg rx")
        return -1


def getTime(block):
    try:
        timeAlarm = re.findall(r'<dateTime>(.*?)<\/dateTime>', block, re.DOTALL)[0]
        return timeAlarm
    except:
        #print("wrong reg rx")
        return -1