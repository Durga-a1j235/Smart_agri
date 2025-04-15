class WasteBinActuator:
    def __init__(self):
        self.alert_status = False

    def trigger_alert(self, status):
        self.alert_status = status
        if status:
            print("Alert: Bin is full!")
        else:
            print("Alert cleared.")