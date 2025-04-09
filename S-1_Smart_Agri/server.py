from flask import Flask, jsonify, request, send_from_directory
from sensors import Sensors  

app = Flask(__name__, static_folder='dashboard')


sensors = Sensors()


@app.route('/')
def serve_dashboard():
    return send_from_directory('dashboard', 'index.html')


@app.route('/<path:path>')
def serve_static_files(path):
    return send_from_directory('dashboard', path)


@app.route('/api/sensors', methods=['GET'])
def get_sensor_data():
 
    data = {
        "soil_moisture": sensors.read_soil_moisture(),
        "temperature": sensors.read_temperature(),
        "humidity": sensors.read_humidity(),
        "rainfall": sensors.read_rainfall()
    }
    return jsonify(data)


@app.route('/api/irrigation', methods=['POST'])
def control_irrigation():
    status = request.json.get('status', False)
    
    if status:
        print("Irrigation system turned ON.")
    else:
        print("Irrigation system turned OFF.")
    return jsonify({"message": "Irrigation status updated", "status": status})

if __name__ == '__main__':
    app.run(debug=True)