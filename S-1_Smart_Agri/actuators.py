class Actuators:
    def __init__(self):
        self.irrigation_status = False

    def control_irrigation(self, status):
        self.irrigation_status = status
        if status:
            print("Irrigation system turned ON.")
        else:
            print("Irrigation system turned OFF.")