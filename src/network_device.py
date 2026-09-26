# In this file, we will create a class to show the attributes of a network device.
# We will also create a class method to show the attributes of a network device.
# Lastly, we will log the attributes of a network device to a log file.

import logging



class NetworkDevice:
    
    def __init__(self, name, ip_address, device_type):
        self.name = name
        self.ip_address = ip_address
        self.device_type = device_type

    def summarize(self):
        print(f"Device Name: {self.name}")
        print(f"IP Address: {self.ip_address}")
        print(f"Device Type: {self.device_type}")

    def log_attributes(self):
        msg = f"[DEVICE_SUMMARY]: {self.name} ({self.device_type}) - {self.ip_address}"
        print(msg)
        logging.info(f"LOG STRING: {msg}")