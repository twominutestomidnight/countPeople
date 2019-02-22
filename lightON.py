import time
import requests
from requests.auth import HTTPDigestAuth


def light(timeLight):
    url = 'http://192.168.30.50/ISAPI/System/IO/outputs/1/trigger'
    #url = 'http://192.168.30.50/ISAPI/System/IO/outputs/1/trigger'
    payloadOn = """
    <IOPortData>
    	<outputState>high</outputState>
    </IOPortData>
    """

    payloadOnOff = """
    <IOPortData>
    	<outputState>low</outputState>
    </IOPortData>
    """
    r = requests.put(url, auth=HTTPDigestAuth('admin', 'Admin12345'), data = payloadOn)
    time.sleep(timeLight)
    r = requests.put(url, auth=HTTPDigestAuth('admin', 'Admin12345'), data = payloadOnOff)





