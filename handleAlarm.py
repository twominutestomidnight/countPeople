import re
from lightON import light
from getValues import getEnter,getTime


#rint(dataSplit[1])

def alarm(startEnterValue):
    #str1 = "<eventState>active</eventState>"
    str2 = "<eventDescription>IO alarm</eventDescription>"
    srt3 = "<eventType>PeopleCounting</eventType>"
    str4 = "<eventType>videoloss</eventType>"
    #str5 = "<enter>0</enter>"
    log = open("ll.log", "a")
    logEnter = open("llEnter.log", "a")
    count_enter = 0
    flag = False
    i = 0
    #while(True):

    #f = open("test2.log", "r")
    while True:
        #f = open("test2.log", "r")
        #f = open("19022019v3.txt", "r")
        f = open(r"19022019v3.txt", "r")
        dataFull = f.read()
        dataSplit = dataFull.split('\n\n')
        for block in dataSplit:
            small_block = block.split('\n')
            for row in small_block:
                if row == str2:
                    flag = True
                    # startTime = re.findall(r'<dateTime>(.*?)</dateTime>', block, re.DOTALL)[0]
                    # print(startTime)
                    # print("IO alarm :", row)
                    break
                if row == srt3 and flag == True:
                    #enterValue = (int)(re.findall(r'<enter>(.*?)<\/enter>', block, re.DOTALL)[0])
                    enterValue = getEnter(block)
                    print("enterValue", enterValue)
                    print("startEnterValue", startEnterValue)

                    #logEnter.close()
                    if enterValue > startEnterValue:
                        count_enter += 1
                        logEnter.write("enter : " + str(enterValue) + "\t StartEnterValue : " + str(startEnterValue) + "\n")
                        startEnterValue = enterValue
                        if count_enter > 1:
                            #timeAlarm = re.findall(r'<dateTime>(.*?)</dateTime>', block, re.DOTALL)[0]
                            timeAlarm = getTime(block)
                            log.write("alarm!, people in : "+ str(count_enter) + "\t" + timeAlarm + "\n")
                            logEnter.write("alarm!, enter : " + str(enterValue) + "\t StartEnterValue : " + str(startEnterValue) + "\n")
                            print("alarm!")
                            light(10)
                    else:
                        break

                if row == str4:
                    flag = False
                    count_enter = 0

                i += 1

        print("count_enter: ", count_enter)
        #open("llEnter.log", 'w').close()
        #f.close()
        #open(r'C:\Users\User\PycharmProjects\bitrate\19022019v3.txt', 'w').close()