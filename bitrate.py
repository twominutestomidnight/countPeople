import os
import time
def getStreamAlert():
#os.system("curl http://igor_test:233Wedf8!@192.168.40.39/ISAPI/Event/notification/alertStream > qwe.txt")

#os.system("curl --digest --user admin:admin12345 192.168.40.176/ISAPI/Event/triggers > qweqwe.txt")
#os.system("curl --digest --user admin:admin12345 192.168.40.176/ISAPI/Event/notification/alertStream > tt.txt")\
    fileName = "19022019v3.txt"

    command = "curl --digest --user admin:Admin12345 192.168.30.50/ISAPI/Event/notification/alertStream > {}".format(fileName)
    os.system(command)
    return fileName
getStreamAlert()





#os.system("curl --digest --user admin:admin12345 192.168.40.176/ISAPI/Event/notification/alertStream > full_full.txt")

'''
import requests
from requests.auth import HTTPDigestAuth

url = 'http://192.168.40.176/ISAPI/Event/triggers'
url2 = 'http://192.168.40.176/ISAPI/Event/notification/alertStream'
r = requests.get(url, auth=HTTPDigestAuth('admin', 'admin12345'))
print("status : ", r.status_code, " text: ", r.text)
print("==================================== ")
r = requests.get(url2, auth=HTTPDigestAuth('admin', 'admin12345'))
'''