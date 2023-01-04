from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

webhooks = []
sensor_ids = set()

@app.route('/api/webhook', methods=['GET','POST'])
def webhook_listener():
  if request.method == 'GET':
    # return a list of all webhooks
    return jsonify(webhooks)
  elif request.method == 'POST':
    # create a new webhook
    data = request.get_json()
    webhook = {
        "sensor" : data['sensor'],
        "ts" : data['ts'],
        "in_count" : data['in'],
        "out_count" : data['out']
    }
    webhooks.append(webhook)
    sensor_ids.add(data['sensor'])
    # return the new webhook
    return jsonify(webhook)

@app.route('/api/sensors', methods=['GET'])
def get_sensors():
  if request.method == 'GET':
    # return a list of all sensors
    return jsonify({"sensors" : list(sensor_ids)})


@app.route('/api/sensors/<sensor_id>/occupancy', methods=['GET'])
def get_sensor_occupancy(sensor_id):
  # get the sensor data for the given sensor id
  if sensor_id in sensor_ids:
      sum_inside = 0
      # create a response with the sensor data
      for w in  webhooks:
        if w['sensor'] == sensor_id:
          sum_inside += (w["in_count"] - w["out_count"])
      response = {
        "sensor" : sensor_id,
        "inside" : sum_inside
      }
  else:
    response = {
        "error": "Sensor not found"
      }                
  return jsonify(response)

@app.route('/sensors/<sensor_id>/occupancy', methods=['GET'])
def get_sensor_occupancy_atInstant(sensor_id):
  # get the sensor data for the given sensor id
  if sensor_id in sensor_ids:
    atInstant = request.args.get('atInstant')
    if atInstant:
      sum_inside = 0
      # create a response with the sensor data
      for w in  webhooks:
        if w['sensor'] == sensor_id and w['ts'] <= atInstant:
          sum_inside += (w["in_count"] - w["out_count"])
      response = {
        "inside" : sum_inside
      }
    else:
      sum_inside = 0
      # create a response with the sensor data
      for w in  webhooks:
        if w['sensor'] == sensor_id:
          sum_inside += (w["in_count"] - w["out_count"])
      response = {
        "inside" : sum_inside
      }
  else:
    response = {
        "error": "Sensor not found"
      }                
  return jsonify(response)
@app.route('/api/occupancy', methods=['GET'])
def get_ccupancy():
    sensor = request.args.get('sensor')
    if sensor in sensor_ids:
      sum_inside = 0
      # create a response with the sensor data
      for w in  webhooks:
        if w['sensor'] == sensor:
          sum_inside += (w["in_count"] - w["out_count"])
      response = {"inside" : sum_inside}
      return jsonify(response)
    else:
      response = {
        "error": "Sensor not found"
      }              
      return jsonify(response)

@app.route('/home')
def home():
    return render_template('home.html')

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000)
