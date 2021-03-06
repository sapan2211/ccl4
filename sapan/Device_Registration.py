import requests
import logging

LOG_FILENAME = "pi_logs.txt"
logging.basicConfig(filename=LOG_FILENAME, level=logging.DEBUG,format='%(asctime)s %(message)s')

Email = "sapan2211@yahoo.com"
DeviceId="88521B7AD79BE277"
payload= {'Email':Email,'DeviceId': DeviceId}
import json

body = {'Email':Email,'DeviceId':DeviceId}
header = {'Content-Type':'application/json', 'Accept':'application/json'}
response = requests.post('http://35.162.32.72:8005/registerpi/registerdevice', headers = header, data = json.dumps(body), verify = False)
if response.status_code == 200:
	print "Registered"
	logging.debug("PI_Registered with ID"+ DeviceId)
else:
	print "Please re-run Get_DeviceId.py and enter proper email and ID above"
	logging.debug("PI registration Failed")
