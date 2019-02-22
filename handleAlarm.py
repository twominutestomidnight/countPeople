import re
from lightON import light
from getValues import getEnter,getTime
import requests
from requests.auth import HTTPDigestAuth
import sys
import argparse
import json
def createParser ():
    parser = argparse.ArgumentParser()
    parser.add_argument('-c', '--config', default='config.json')
    return parser
parser = createParser()
namespace = parser.parse_args (sys.argv[1:])


with open(namespace.config) as config_file:
    config = json.load(config_file)


f = open(config['file_for_log'], "w")
f2 = open(config['file_for_alarm'], "w")
def alarm(startEnterValue):
    #str1 = "<eventState>active</eventState>"
    str2 = "<eventDescription>IO alarm</eventDescription>"
    srt3 = "<eventType>PeopleCounting</eventType>"
    str4 = "<eventType>videoloss</eventType>"
    #str5 = "<enter>0</enter>"
    count_enter = 0
    flag = False
    url_alert = 'http://{}/ISAPI/Event/notification/alertStream'.format(config['camera_ip'])

    #r = requests.get(url_alert, auth=HTTPDigestAuth('admin', 'Admin12345'), stream=True)
    r = requests.get(url_alert, auth=HTTPDigestAuth(config['login'], config['password']), stream=True)
    for line in r.iter_lines():
        line = line.decode("utf-8")
        f.write(line + "\n")
        #print(line)
        if line == str2:
            f2.write("io alarm : " + line + "\n")
            flag = True
            # startTime = re.findall(r'<dateTime>(.*?)</dateTime>', block, re.DOTALL)[0]
            # print(startTime)
            # print("IO alarm :", row)

        if flag == True:
            #enterValue = (int)(re.findall(r'<enter>(.*?)<\/enter>', block, re.DOTALL)[0])
            enterValue = getEnter(line)
            if enterValue != -1:
                #print("enterValue", enterValue)
                #print("startEnterValue", startEnterValue)
                f2.write("startEnterValue : "+ str(startEnterValue) + "\t" + "enterValue : "+ str(enterValue) +" \n")
                #logEnter.close()
                if enterValue > startEnterValue:
                    count_enter += 1
                    #print(count_enter)
                    f2.write("count_enter : " + str(count_enter) + "\n")
                    startEnterValue = enterValue
                    if count_enter > 1:
                        #timeAlarm = re.findall(r'<dateTime>(.*?)</dateTime>', block, re.DOTALL)[0]
                        #timeAlarm = getTime(line)
                        f2.write("alarm!, io count_enter : " + line + "\n")
                        #print("alarm!")
                        light(config['alarm_time'])


        if line == str4:
            flag = False
            count_enter = 0

