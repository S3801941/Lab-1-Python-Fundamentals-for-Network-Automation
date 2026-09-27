# This is the main python file for the project. It serves as the entry point for the application and contains the main logic to run the program.
# We will import the necessary modules and classes, create instances of the NetworkDevice class, and call the methods to summarize and log the attributes of the network devices.

import logging
from network_device import NetworkDevice

def main():
    # Configure logging
    logging.basicConfig(filename='logs/lab.log', level=logging.INFO)

    pass



if __name__ == "__main__":
    main()