import requests
import nacl.secret as secret
import nacl.utils as utils
import nacl.pwhash as pwhash
import base64
import simplejson as json
import nacl.encoding as encoding
import nacl.signing as signing
import nacl as nacl




privatefile = open("privatekey","r")
key = privatefile.read()
# Serialize the verify key to send it to a third party

sign_key = nacl.signing.SigningKey(key, encoder=encoding.HexEncoder)
signed = sign_key.sign("Attack at Dawn")


signedmsg = base64.standard_b64encode(signed)

print signedmsg
message = {"api_token": "8de531a564e2cb932bf1382b964199ad5967f38fc76c6d366f9e0fa323ffb2e5",
"to" :"nessie", "message" : signedmsg}

headers1 = {'Content-type': 'application/json','Accept':'application/json'}


r= requests.post("https://whoomp.cs.uwaterloo.ca/458a3/api/signed/send",headers=headers1, json=message)
print(r.status_code)
#print r.text






