import json
from datetime import datetime

class DataCollection:
    def __init__(self, file_path="data.json"):
        self.file_path = file_path

    def save_data(self, data):
        with open(self.file_path, "a") as file:
            json.dump(data, file)
            file.write("\n")

    def collect_data(self, sensors):
        data = {
            "timestamp": datetime.now().isoformat(),
            "soil_moisture": sensors.read_soil_moisture(),
            "temperature": sensors.read_temperature(),
            "humidity": sensors.read_humidity(),
            "rainfall": sensors.read_rainfall(),
        }
        self.save_data(data)
        return data