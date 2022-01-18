import requests
import datetime
import json
requests.packages.urllib3.disable_warnings()

print ("Current date and time: ")
print(datetime.datetime.now())


DNAC_scheme = 'https://'
DNAC_authority='sandboxdnac.cisco.com'
DNAC_port=':443'
DNAC_path_token='/dna/system/api/v1/auth/token'
DNAC_path='/dna/intent/api/v1/network-device'

DNAC_user = input("Username? ") 
DNAC_psw = input("Password? ")  

token_req_url = DNAC_scheme+DNAC_authority+DNAC_path_token
auth = (DNAC_user, DNAC_psw)
req = requests.post(token_req_url, auth=(DNAC_user, DNAC_psw), verify=False)
print("API Return Code: " + str(req.status_code))  
print('Request URI: ' + token_req_url)
print("Username: " + DNAC_user)
resp = req.text
token = req.json()['Token']
print("Received Token:")
print(token)
print("Length Token:")
print(len(token))

req_url = DNAC_scheme+DNAC_authority+DNAC_port+DNAC_path
print(req_url)
headers = {'X-auth-token': token}
resp_devices = requests.request('GET', req_url, headers=headers, verify=False)
print(resp_devices)
resp_devices_json = resp_devices.json()



for device in resp_devices_json['response']:
    if device['type'] != None:
        print('===')
        print('Hostname: ' + device['hostname'])
        print('Family: ' + device['family'])
        print('IP: ' + device['managementIpAddress'])
        print('MAC: '+ device['macAddress'])
        print('Software version: ' + device['softwareType'])
        print('Reachability: ' + device['reachabilityStatus'])
