# This is the main python file for the project. It serves as the entry point for the application and contains the main logic to run the program.
# We will import the necessary modules and classes, create instances of the NetworkDevice class, and call the methods to summarize and log the attributes of the network devices.

import logging
from network_device import NetworkDevice

def main():
    # Configure logging
    logging.basicConfig(filename='network_device.log', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

    # Create instances of NetworkDevice
    device1 = NetworkDevice("Router1", "192.168.1.1", "Router")
    device2 = NetworkDevice("Switch1", "192.168.1.2", "Switch")

    # Summarize and log attributes of the devices
    device1.summarize()
    device2.summarize()

if __name__ == "__main__":
    main()