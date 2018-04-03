import requests

message = {"api_token": "8de531a564e2cb932bf1382b964199ad5967f38fc76c6d366f9e0fa323ffb2e5",
"to": "nessie", 
"message": "SGVsbG8sIHdvcmxkIQ=="}

headers1 = {'Content-type': 'application/json','Accept':'application/json'}

r= requests.post("https://whoomp.cs.uwaterloo.ca/458a3/api/plain/send",headers=headers1, json=message)
print(r.status_code)


