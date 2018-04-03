import requests
import nacl.secret as secret
import nacl.utils as utils
import nacl.pwhash as pwhash
import base64
import simplejson as json
import nacl.encoding as encoding
import nacl.signing as signing
import nacl as nacl

from nacl.public import PrivateKey, Box

import nacl.hash
from nacl.public import PrivateKey
HASHER = nacl.hash.blake2b





message = {"api_token": "8de531a564e2cb932bf1382b964199ad5967f38fc76c6d366f9e0fa323ffb2e5",
"user" :"nessie"}
headers1 = {'Content-type': 'application/json','Accept':'application/json'}
r= requests.post("https://whoomp.cs.uwaterloo.ca/458a3/api/pke/get-key",headers=headers1, json=message)
print(r.status_code)
str= r.text.split(":")[2]


Str1 = str.split("\"")[1]

msg = base64.standard_b64decode(Str1)
hashmsg =HASHER(msg, encoder=nacl.encoding.HexEncoder)
#get hash
print "hash:" + hashmsg

#part 2
#generate a public and private key and upload the public key
key = nacl.utils.random(nacl.secret.SecretBox.KEY_SIZE)
sk = PrivateKey.generate()
pk = sk.public_key
basekey = pk.encode(encoder=nacl.encoding.Base64Encoder)
message2 = {"api_token": "8de531a564e2cb932bf1382b964199ad5967f38fc76c6d366f9e0fa323ffb2e5",
"public_key" : basekey}
r2= requests.post("https://whoomp.cs.uwaterloo.ca/458a3/api/pke/set-key",headers=headers1, json=message2)
print(r2.status_code)

#part 2b
nessiekey = nacl.public.PublicKey(Str1, encoder=nacl.encoding.Base64Encoder)
box = Box(sk, nessiekey)
secret = "take a walk"
cipher = box.encrypt(secret)
cipherbase64 = base64.standard_b64encode(cipher)
message2 = {"api_token": "8de531a564e2cb932bf1382b964199ad5967f38fc76c6d366f9e0fa323ffb2e5",
"to" :"nessie", "message": cipherbase64}
r= requests.post("https://whoomp.cs.uwaterloo.ca/458a3/api/pke/send",headers=headers1, json=message2)
print(r.status_code)


#part 3
message2 = {"api_token": "8de531a564e2cb932bf1382b964199ad5967f38fc76c6d366f9e0fa323ffb2e5"}
r= requests.post("https://whoomp.cs.uwaterloo.ca/458a3/api/pke/inbox",headers=headers1, json=message2)

str = json.loads(r.text)
str2 = str[0]['message']
print str2

ciphmsg = base64.standard_b64decode(str2)
lastmsg = box.decrypt(ciphmsg)

print lastmsg

