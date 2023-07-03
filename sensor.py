from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

sensor_value = 0

@app.route('/')
def index():
    return render_template('index.html', sensor_value=sensor_value)

@app.route('/api/sensor', methods=['POST', 'PUT'])
def update_sensor():
    global sensor_value
    sensor_value = request.get_json().get('value')
    return '', 204

@app.route('/api/sensor', methods=['GET'])
def get_sensor():
    global sensor_value
    # Return the sensor value as a JSON response
    return jsonify({'value': sensor_value})

if __name__ == '__main__':
    app.run(debug=True)
