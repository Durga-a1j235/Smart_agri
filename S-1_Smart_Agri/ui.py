class UserInterface:
    def display_data(self, data):
        print("\n--- Sensor Data ---")
        for key, value in data.items():
            print(f"{key}: {value}")
        print("-------------------")