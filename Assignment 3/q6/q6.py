import requests
import nacl.secret as secret
import nacl.utils as utils
import nacl.pwhash as pwhash
import base64
import simplejson as json
import nacl.encoding as encoding
import nacl.signing as signing
import nacl as nacl
import binascii
from nacl.public import PrivateKey, Box


key = nacl.utils.random(nacl.secret.SecretBox.KEY_SIZE)
sk = PrivateKey.generate()
pk = sk.public_key
basekey = pk.encode(encoder=nacl.encoding.Base64Encoder)
message2 = {"api_token": "8de531a564e2cb932bf1382b964199ad5967f38fc76c6d366f9e0fa323ffb2e5",
"public_key" : basekey}
headers1 = {'Content-type': 'application/json','Accept':'application/json'}
r2= requests.post("https://whoomp.cs.uwaterloo.ca/458a3/api/surveil/set-key",headers=headers1, json=message2)
print(r2.status_code)



message = {"api_token": "8de531a564e2cb932bf1382b964199ad5967f38fc76c6d366f9e0fa323ffb2e5",
"user" :"nessie"}
r= requests.post("https://whoomp.cs.uwaterloo.ca/458a3/api/surveil/get-key",headers=headers1, json=message)
print(r.status_code)
str= r.text.split(":")[2]
Str1 = str.split("\"")[1]
msg = "test"
nessiekey = nacl.public.PublicKey(Str1, encoder=nacl.encoding.Base64Encoder)
key = nacl.utils.random(nacl.secret.SecretBox.KEY_SIZE)
normalBox = nacl.secret.SecretBox(key)
ciphertext = normalBox.encrypt(msg)
governkey64 = "+HxegzAtmr5sBBAUVDQu4KKwGvVVnCeOtOoU68PyCGk="
governkey = nacl.public.PublicKey(governkey64, encoder=nacl.encoding.Base64Encoder)
nessiebox = Box(sk, nessiekey)
governbox = Box(sk, governkey)
nessiecipher = nessiebox.encrypt(key)
governcipher = governbox.encrypt(key)
finalmsg =nessiecipher + governcipher + ciphertext
base64finalmsg = base64.standard_b64encode(finalmsg)

message = {"api_token": "8de531a564e2cb932bf1382b964199ad5967f38fc76c6d366f9e0fa323ffb2e5",
"to": "nessie", 
"message": base64finalmsg}
r2= requests.post("https://whoomp.cs.uwaterloo.ca/458a3/api/surveil/send",headers=headers1, json=message)
print(r2.status_code)






##receive and decrypt
message = {"api_token": "8de531a564e2cb932bf1382b964199ad5967f38fc76c6d366f9e0fa323ffb2e5",
"to": "nessie"}
r2= requests.post("https://whoomp.cs.uwaterloo.ca/458a3/api/surveil/inbox",headers=headers1, json=message)
str = json.loads(r2.text)
str2 = str[0]['message']
print str2
encryptedpublicall = base64.standard_b64decode(str2)
nessienewkey = nessiebox.decrypt(encryptedpublicall[:72])
nessiebox2 = nacl.secret.SecretBox(nessienewkey)
encryptedpublic = encryptedpublicall[144:]
encrypted  =  nessiebox2.decrypt(encryptedpublic)
print encrypted 

