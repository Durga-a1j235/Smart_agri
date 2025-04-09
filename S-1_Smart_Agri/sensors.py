import random

class Sensors:
    def __init__(self):
        pass

    def read_soil_moisture(self):
        
        return random.uniform(10, 100)  

    def read_temperature(self):
        
        return random.uniform(20, 40)  

    def read_humidity(self):
        
        return random.uniform(30, 90)  

    def read_rainfall(self):
        
        return random.uniform(0, 50)  