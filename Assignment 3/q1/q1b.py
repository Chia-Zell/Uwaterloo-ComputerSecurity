import requests
import json
import base64

message = {"api_token": "8de531a564e2cb932bf1382b964199ad5967f38fc76c6d366f9e0fa323ffb2e5",
"to": "nessie", 
"message": "SGVsbG8sIHdvcmxkIQ=="}

headers1 = {'Content-type': 'application/json','Accept':'application/json'}

r= requests.post("https://whoomp.cs.uwaterloo.ca/458a3/api/plain/inbox",headers=headers1, json=message)
print(r.status_code)
print(r.text)


str = json.loads(r.text)
str2 = str[0]['message']
print base64.standard_b64decode(str2)

