from flask import Flask, jsonify, request, send_from_directory
from sensors import WasteBinSensor 

app = Flask(__name__, static_folder='dashboard')

sensor = WasteBinSensor()

@app.route('/')
def serve_dashboard():
    return send_from_directory('dashboard', 'index.html')

@app.route('/<path:path>')
def serve_static_files(path):
    return send_from_directory('dashboard', path)

@app.route('/api/bin_status', methods=['GET'])
def get_bin_status():

    fill_level = sensor.read_fill_level()
    return jsonify({"fill_level": fill_level}) 
if __name__ == '__main__':
    app.run(debug=True)