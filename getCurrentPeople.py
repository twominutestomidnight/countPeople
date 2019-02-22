import requests
import datetime
from requests.auth import HTTPDigestAuth
from xml.dom import minidom


def getStartPeopleValue():
    url = 'http://192.168.30.50/ISAPI/System/Video/inputs/channels/1/counting/search/'
    #now = datetime.datetime.now()
    st = "{}-{}-{}".format(datetime.datetime.now().year, datetime.datetime.now().month, datetime.datetime.now().day)

    payload = """
    <?xml version="1.0" encoding="utf-16"?>
    <countingStatisticsDescription
    	xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
    	xmlns:xsd="http://www.w3.org/2001/XMLSchema">
    	<reportType>weekly</reportType>
    	<timeSpanList>
    		<timeSpan>
    			<startTime>{}T00:00:00</startTime>
    			<endTime>{}T23:59:59</endTime>
    		</timeSpan>
    	</timeSpanList>
    </countingStatisticsDescription>
    """.format(st, st)

    r = requests.get(url, auth=HTTPDigestAuth('admin', 'Admin12345'), data=payload)

    xmldoc = minidom.parseString(r.text)
    itemlist = xmldoc.getElementsByTagName('enterCount')
    # for i in itemlist:
    #    print(i.firstChild.nodeValue)
    day = datetime.datetime.today().weekday()
    startEnterValue = (int)(itemlist[day].firstChild.nodeValue)
    # print("Len : ", itemlist)

    return startEnterValue