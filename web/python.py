from flask import Flask, request, session, g, redirect, url_for, abort, render_template, flash
import requests
import json
from keystoneclient.auth.identity import v2
from keystoneclient import session
from ceilometerclient import client

app = Flask(__name__)

@app.route("/")
def main():
	return render_template('index.html')

@app.route("/coba")
def coba():
	userid = "demo"
	password = "stack"
	tenatid = "2bfcfea32f4949d9af6e0f3cc52373af"
	#token id
	url = 'http://172.16.160.115:5000/v2.0/tokens'
	headers = {'content-type': 'application/json'}
	payload = {'auth':{'passwordCredentials':{'username':userid, 'password':password},          'tenantId':tenatid}}    
	r = requests.post(url, data=json.dumps(payload), headers=headers)
	#print r.headers.get('content-type')
	#print json.dumps(r.json(), sort_keys=True, indent=4, separators=(',', ': '))
	json_data = r.json()
	r.close()
	tokens = json.loads(json.dumps(json_data))
	#print tokens
	tokenid = tokens['access']['token']['id']
	#server list
	url = 'http://172.16.160.115:8774/v2/servers/detail'
	headers = {'X-Auth-Token':str(tokenid)}
	r = requests.get(url, headers=headers)
	json_data = r.json()
	print json.dumps(r.json(), sort_keys=True, indent=4, separators=(',', ': '))
	json_data = r.json()
	r.close()
	return render_template('coba.html', json_data = json_data)

@app.route("/metering")
def metering():
	userid = "demo"
	password = "stack"
	tenatid = "2bfcfea32f4949d9af6e0f3cc52373af"
	#token id
	url = 'http://172.16.160.115:5000/v2.0/tokens'
	headers = {'content-type': 'application/json'}
	payload = {'auth':{'passwordCredentials':{'username':userid, 'password':password},          'tenantId':tenatid}}    
	r = requests.post(url, data=json.dumps(payload), headers=headers)
	#print r.headers.get('content-type')
	#print json.dumps(r.json(), sort_keys=True, indent=4, separators=(',', ': '))
	json_data = r.json()
	r.close()
	tokens = json.loads(json.dumps(json_data))
	#print tokens
	tokenid = tokens['access']['token']['id']
	#ceilometer metering total
	url = 'http://172.16.160.115:8777/v2/meters/instance/statistics'
	headers = {'X-Auth-Token':str(tokenid)}
	r = requests.get(url, headers=headers)
	json_data = r.json()
	print json.dumps(r.json(), sort_keys=True, indent=4, separators=(',', ': '))
	json_data = r.json()
	r.close()
	return render_template('metering.html', json_data = json_data)

@app.route("/monitordisk")
def monitordisk():
	userid = "demo"
	password = "stack"
	tenatid = "2bfcfea32f4949d9af6e0f3cc52373af"
	#token id
	url = 'http://172.16.160.115:5000/v2.0/tokens'
	headers = {'content-type': 'application/json'}
	payload = {'auth':{'passwordCredentials':{'username':userid, 'password':password},          'tenantId':tenatid}}    
	r = requests.post(url, data=json.dumps(payload), headers=headers)
	#print r.headers.get('content-type')
	#print json.dumps(r.json(), sort_keys=True, indent=4, separators=(',', ': '))
	json_data = r.json()
	r.close()
	tokens = json.loads(json.dumps(json_data))
	#print tokens
	tokenid = tokens['access']['token']['id']
	#ceilometer metering disk usage
	url = 'http://172.16.160.115:8777/v2/meters/disk.device.usage/statistics'
	headers = {'X-Auth-Token':str(tokenid)}
	r = requests.get(url, headers=headers)
	json_data = r.json()
	print json.dumps(r.json(), sort_keys=True, indent=4, separators=(',', ': '))
	json_data = r.json()
	r.close()
	return render_template('monitordisk.html', json_data = json_data)

@app.route("/memory")
def memory():
	userid = "demo"
	password = "stack"
	tenatid = "2bfcfea32f4949d9af6e0f3cc52373af"
	#token id
	url = 'http://172.16.160.115:5000/v2.0/tokens'
	headers = {'content-type': 'application/json'}
	payload = {'auth':{'passwordCredentials':{'username':userid, 'password':password},          'tenantId':tenatid}}    
	r = requests.post(url, data=json.dumps(payload), headers=headers)
	#print r.headers.get('content-type')
	#print json.dumps(r.json(), sort_keys=True, indent=4, separators=(',', ': '))
	json_data = r.json()
	r.close()
	tokens = json.loads(json.dumps(json_data))
	#print tokens
	tokenid = tokens['access']['token']['id']
	#ceilometer metering memory usage
	url = 'http://172.16.160.115:8777/v2/meters/memory.usage/statistics'
	headers = {'X-Auth-Token':str(tokenid)}
	r = requests.get(url, headers=headers)
	json_data = r.json()
	print json.dumps(r.json(), sort_keys=True, indent=4, separators=(',', ': '))
	json_data = r.json()
	r.close()
	return render_template('memory.html', json_data = json_data)

@app.route("/monitorcpu")
def monitorcpu():
	userid = "demo"
	password = "stack"
	tenatid = "2bfcfea32f4949d9af6e0f3cc52373af"
	#token id
	url = 'http://172.16.160.115:5000/v2.0/tokens'
	headers = {'content-type': 'application/json'}
	payload = {'auth':{'passwordCredentials':{'username':userid, 'password':password},          'tenantId':tenatid}}    
	r = requests.post(url, data=json.dumps(payload), headers=headers)
	#print r.headers.get('content-type')
	#print json.dumps(r.json(), sort_keys=True, indent=4, separators=(',', ': '))
	json_data = r.json()
	r.close()
	tokens = json.loads(json.dumps(json_data))
	#print tokens
	tokenid = tokens['access']['token']['id']
	#ceilometer metering cpu usage
	url = 'http://172.16.160.115:8777/v2/meters/cpu_util/statistics'
	headers = {'X-Auth-Token':str(tokenid)}
	r = requests.get(url, headers=headers)
	json_data = r.json()
	print json.dumps(r.json(), sort_keys=True, indent=4, separators=(',', ': '))
	json_data = r.json()
	r.close()
	return render_template('monitorcpu.html', json_data = json_data)

@app.route("/vm1")
def vm1():
	userid = "demo"
	password = "stack"
	tenatid = "2bfcfea32f4949d9af6e0f3cc52373af"
	#token id
	url = 'http://172.16.160.115:5000/v2.0/tokens'
	headers = {'content-type': 'application/json'}
	payload = {'auth':{'passwordCredentials':{'username':userid, 'password':password},          'tenantId':tenatid}}    
	r = requests.post(url, data=json.dumps(payload), headers=headers)
	#print r.headers.get('content-type')
	#print json.dumps(r.json(), sort_keys=True, indent=4, separators=(',', ': '))
	json_data = r.json()
	r.close()
	tokens = json.loads(json.dumps(json_data))
	#print tokens
	tokenid = tokens['access']['token']['id']
	#ceilometer detail  vm 1
	url = 'http://172.16.160.115:8777/v2/resources/0bfa5f3b-7393-40ee-bab3-aa64df3bda98'
	headers = {'X-Auth-Token':str(tokenid)}
	r = requests.get(url, headers=headers)
	json_data = r.json()
	print json.dumps(r.json(), sort_keys=True, indent=4, separators=(',', ': '))
	json_data = r.json()
	r.close()
	return render_template('vm1.html', json_data = json_data)

@app.route("/vm2")
def vm2():
	userid = "demo"
	password = "stack"
	tenatid = "2bfcfea32f4949d9af6e0f3cc52373af"
	#token id
	url = 'http://172.16.160.115:5000/v2.0/tokens'
	headers = {'content-type': 'application/json'}
	payload = {'auth':{'passwordCredentials':{'username':userid, 'password':password},          'tenantId':tenatid}}    
	r = requests.post(url, data=json.dumps(payload), headers=headers)
	#print r.headers.get('content-type')
	#print json.dumps(r.json(), sort_keys=True, indent=4, separators=(',', ': '))
	json_data = r.json()
	r.close()
	tokens = json.loads(json.dumps(json_data))
	#print tokens
	tokenid = tokens['access']['token']['id']
	#ceilometer detail  vm 2
	url = 'http://172.16.160.115:8777/v2/resources/7810e1ae-8f5a-4421-aa5c-c26526cb8fce'
	headers = {'X-Auth-Token':str(tokenid)}
	r = requests.get(url, headers=headers)
	json_data = r.json()
	print json.dumps(r.json(), sort_keys=True, indent=4, separators=(',', ': '))
	json_data = r.json()
	r.close()
	return render_template('vm2.html', json_data = json_data)


if __name__ == "__main__":
    app.run()







