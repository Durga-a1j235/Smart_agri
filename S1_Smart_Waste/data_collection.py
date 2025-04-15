import json
from datetime import datetime
class DataCollection:
    def __init__(self, file_path="waste_data.json"):
        self.file_path = file_path

    def save_data(self, data):
        with open(self.file_path, "a") as file:
            json.dump(data, file)
            file.write("\n")

    def collect_data(self, sensor):
        data = {
            "timestamp": datetime.now().isoformat(),
            "fill_level": sensor.read_fill_level()
        }
        self.save_data(data)
        return data