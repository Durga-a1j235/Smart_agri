from sensors import Sensors
from actuators import Actuators
from data_collection import DataCollection
from communication import Communication
from ui import UserInterface

def main():
    sensors = Sensors()
    actuators = Actuators()
    data_collector = DataCollection()
    communication = Communication()
    ui = UserInterface()

    data = data_collector.collect_data(sensors)

    
    ui.display_data(data)

    
    if data["soil_moisture"] < 30:  
        actuators.control_irrigation(True)
    else:
        actuators.control_irrigation(False)

    
    communication.transmit_data(data)

if __name__ == "__main__":
    main()