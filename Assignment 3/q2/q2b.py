import requests
import nacl.secret
import nacl.utils
import base64
import simplejson as json

key = "52fc987da30724784fe7147c85a83cf7d193976c936201dc142d9080fcb4c546".decode("hex")


nonce = nacl.utils.random(nacl.secret.SecretBox.NONCE_SIZE)

box = nacl.secret.SecretBox(key)






message = {"api_token": "8de531a564e2cb932bf1382b964199ad5967f38fc76c6d366f9e0fa323ffb2e5",
"to": "nessie"}

headers1 = {'Content-type': 'application/json','Accept':'application/json'}

r= requests.post("https://whoomp.cs.uwaterloo.ca/458a3/api/psk/inbox",headers=headers1, json=message)
print(r.status_code)

str = json.loads(r.text)
cipher2 = str[0]['message']


ciphmsg = base64.standard_b64decode(cipher2)

ptext = box.decrypt(ciphmsg)

print ptext






