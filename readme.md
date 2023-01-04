# Test task: meeting room occupancy API
This project is about an exercice for Square sense, it comes from https://jobs.square-sense.com/exercise/*****.pdf (not sure it' secret)

## Folder Structure

- `templates/`: This folder contains html
- `post_data.py`: This script helps to post data on the site http://hostname/api/webhook if u dont want to use commande
- `server.py` : This script constructs the server and APIS
- `test.py` : This script contains all of the unit tests

## Usage
Hostname defined is 127.0.0.1:5000, and the environement is Linux.
1. start the server and APIS
```
python3 server.py
```
2. Send data to the site http://hostname/api/webhook
U can use cmd like the following by 
```
curl --header "Content-Type: application/json" \
--request POST --data \
'{"sensor":"abc","ts":"2018-11-14T13:34:49Z","in":3,"out":2}' \
http://127.0.0.1:5000/api/webhook
```
Or u can use the script (U need to change data to what u wanted)
```
python3 post_data.py
```