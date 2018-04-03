import requests
import nacl.secret as secret
import nacl.utils as utils
import nacl.pwhash as pwhash
import base64
import simplejson as json

passw = "instructional dance"
salt = "bbec7a7c2f37eccc19684c5e9a0b19e5d9dfc31b2b78e3cd4fe346b39b3b8f72".decode("hex")


oplimit = 524288

memlimit1 = 16777216



kdf = pwhash.scrypt.kdf
dev_key = kdf(secret.SecretBox.KEY_SIZE, passw, salt,
                 opslimit=oplimit, memlimit=memlimit1)
dev_box = secret.SecretBox(dev_key)
nonce = utils.random(secret.SecretBox.NONCE_SIZE)



message = {"api_token": "8de531a564e2cb932bf1382b964199ad5967f38fc76c6d366f9e0fa323ffb2e5",
"to": "nessie",}

headers1 = {'Content-type': 'application/json','Accept':'application/json'}

r= requests.post("https://whoomp.cs.uwaterloo.ca/458a3/api/psp/inbox",headers=headers1, json=message)
print(r.status_code)



cipher = r.text.split(",")

str = json.loads(r.text)
cipher2 = str[0]['message']
ciphmsg = base64.standard_b64decode(cipher2)

print dev_box.decrypt(ciphmsg)









