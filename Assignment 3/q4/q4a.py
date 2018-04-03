import requests
import nacl.secret as secret
import nacl.utils as utils
import nacl.pwhash as pwhash
import base64
import simplejson as json
import nacl.encoding as encoding
import nacl.signing as signing




signing_key = signing.SigningKey.generate()

verify_key = signing_key.verify_key
pfile = open("verificationkey","w")
privatefile = open("privatekey","w")

# Serialize the verify key to send it to a third party
verify_key_hex = verify_key.encode(encoder=encoding.Base64Encoder)
pfile.write(verify_key_hex)

sign_key_hex = signing_key.encode(encoder=encoding.HexEncoder)
privatefile.write(sign_key_hex)
message = {"api_token": "8de531a564e2cb932bf1382b964199ad5967f38fc76c6d366f9e0fa323ffb2e5",
"public_key": verify_key_hex}

headers1 = {'Content-type': 'application/json','Accept':'application/json'}

r= requests.post("https://whoomp.cs.uwaterloo.ca/458a3/api/signed/set-key",headers=headers1, json=message)
print(r.status_code)
#print r.text

pfile.close()
privatefile.close()






