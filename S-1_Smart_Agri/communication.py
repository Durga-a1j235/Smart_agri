class Communication:
    def __init__(self, protocol="LoRaWAN"):
        self.protocol = protocol

    def transmit_data(self, data):
        print(f"Transmitting data using {self.protocol}: {data}")