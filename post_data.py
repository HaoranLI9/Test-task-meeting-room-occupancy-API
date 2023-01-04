import requests


url = "http://127.0.0.1:5000/api/webhook"

data = {"sensor":"abc","ts":"2018-11-14T13:34:49Z","in":3,"out":2}
headers = {'Content-Type': 'application/json'}
print(url)
response = requests.post(url, json=data, headers=headers)
if response.status_code == 200:
  print("send data successfully")