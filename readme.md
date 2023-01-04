# Test task: meeting room occupancy API
This project is about an exercice for Square sense, it comes from https://jobs.square-sense.com/exercise/*****.pdf (not sure it' secret)

## Folder Structure

- `templates/`: This folder contains html
- `post_data.py`: This script helps to post data on the site http://hostname/api/webhook if u dont want to use commande
- `server.py` : This script constructs the server and APIS
- `test.py` : This script contains all of the unit tests

## Usage
Hostname defined is 127.0.0.1:5000, and the environement is Linux.
1. start the server and APIs
```
python3 server.py
```
2. Send data to the site http://hostname/api/webhook
you can use cmd like the following by 
```
curl --header "Content-Type: application/json" \
--request POST --data \
'{"sensor":"abc","ts":"2018-11-14T13:34:49Z","in":3,"out":2}' \
http://127.0.0.1:5000/api/webhook
```
Or you can use the script (you need to change the data to what you want):
```
python3 post_data.py
```

3. See the performance of APIs
      * you can go to this site or use the following command:
      ```
      curl --request GET http://127.0.0.1:5000/api/sensors
      ```
      you will get
      ```
        {"sensors":["abc"]}
      ```

      * you can go to this site or use the following command:
      ```
      curl --request GET http://127.0.0.1:5000/api/sensors/abc/occupancy
      ```
      you will get 
      ```
      {"inside":1,"sensor":"abc"}
      ```

      * you can go to this site or use the following command:
      ```
      curl --request GET http://127.0.0.1:5000/api/sensors/abc/occupancy?atInstant=2018-11-14T12:00:00Z  
      ```
      you will get 
      ```
      {"inside":0}
      ```
All of the results here are based on my data {"sensor":"abc","ts":"2018-11-14T13:34:49Z","in":3,"out":2}.  


## Test
Use the script
```
python3 test.py
```
You will see 6 tests succeed.



  


## Maintainers
[@Haoran LI](https://github.com/HaoranLI9)