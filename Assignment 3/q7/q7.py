import requests
import json
import base64
import nacl.encoding
import nacl.signing
import nacl.utils
from nacl.hash import blake2b
from nacl.public import PrivateKey, Box
from binascii import unhexlify

signing_key = nacl.signing.SigningKey.generate()
verify_key = signing_key.verify_key

verify_key64 = verify_key.encode(encoder=nacl.encoding.Base64Encoder)

message = {"api_token": "8de531a564e2cb932bf1382b964199ad5967f38fc76c6d366f9e0fa323ffb2e5",
"public_key" : verify_key64}

headers = {
  "content-type": "application/json",
  "accept": "application/json"
}
r = requests.post("https://whoomp.cs.uwaterloo.ca/458a3/api/prekey/set-identity-key", json=message, headers=headers)

print(r.status_code)

sk = PrivateKey.generate()
pk = sk.public_key
pk64 = pk.encode(encoder=nacl.encoding.RawEncoder)

signed = signing_key.sign(pk64)

pkey64 = base64.b64encode(signed)

message1 = {
  "api_token": "8de531a564e2cb932bf1382b964199ad5967f38fc76c6d366f9e0fa323ffb2e5", "public_key": pkey64}
r1 = requests.post("https://whoomp.cs.uwaterloo.ca/458a3/api/prekey/set-signed-prekey", json=message1, headers=headers)


print(r1.status_code)


message2 = {
  "api_token": "8de531a564e2cb932bf1382b964199ad5967f38fc76c6d366f9e0fa323ffb2e5", "user": "nessie"}
r2 = requests.post("https://whoomp.cs.uwaterloo.ca/458a3/api/prekey/get-identity-key", json = message2, headers=headers)

print(r2.status_code)
pubkey = json.loads(r2.text)['public_key']

print(pubkey)
verifykey = nacl.signing.VerifyKey(pubkey, encoder=nacl.encoding.Base64Encoder)
print(verifykey)

message3 = {
  "api_token": "8de531a564e2cb932bf1382b964199ad5967f38fc76c6d366f9e0fa323ffb2e5",
  "user": "nessie"}
r3 = requests.post("https://whoomp.cs.uwaterloo.ca/458a3/api/prekey/get-signed-prekey", json=message3, headers=headers)
print(r3.status_code)
print r3.text
item = verifykey.verify(base64.b64decode(json.loads(r3.text)['public_key']))
nessiepk = nacl.public.PublicKey(item, encoder=nacl.encoding.RawEncoder)

msg = "need to work please"
box = Box(sk, nessiepk)

encrypted = box.encrypt(msg)
enc64 = base64.b64encode(encrypted)
message4 = {
  "api_token": "8de531a564e2cb932bf1382b964199ad5967f38fc76c6d366f9e0fa323ffb2e5","to": "nessie",
  "message": enc64}
r4 = requests.post("https://whoomp.cs.uwaterloo.ca/458a3/api/prekey/send", json=message4, headers=headers)

print(r4.text)
print(r4.status_code)

message5 = {"api_token": "8de531a564e2cb932bf1382b964199ad5967f38fc76c6d366f9e0fa323ffb2e5",}
r5 = requests.post("https://whoomp.cs.uwaterloo.ca/458a3/api/prekey/inbox", json=message5, headers=headers)

print(json.loads(r5.text)[0]['message'])
print(r5.status_code)

finalmessage = base64.b64decode(json.loads(r5.text)[0]['message'])
print(box.decrypt(finalmessage))
