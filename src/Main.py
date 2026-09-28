# This is the main python file for the project. It serves as the entry point for the application and contains the main logic to run the program.
# We will import the necessary modules and classes, create instances of the NetworkDevice class, and call the methods to summarize and log the attributes of the network devices.

import logging
import network_device
import parser_utils

# Configure logging
logging.basicConfig(filename='logs/lab.log', level=logging.INFO)

# Initial Log message for starting the lab.
msg = 'LAB1-START'
print(msg)
logging.info(msg)


def main():

    # Parsing JSON files to get device summaries.
    stawman = parser_utils.parser_utils('data/devices.json')
    straw = stawman.parse_json()
    brain_1 = network_device.NetworkDevice(
        name = straw [0]['hostname'],
        ip_address = straw[0]['ip'],
        device_type = straw[0]['type']
    )
    brain_2 = network_device.NetworkDevice(
        name = straw [1]['hostname'],
        ip_address = straw[1]['ip'],
        device_type = straw[1]['type']
    )

    brain_1.summarize()
    brain_2.summarize()

    brain_1.log_attributes()
    brain_2.log_attributes()


    # Parsing YAML files to get device information.
    lion = parser_utils.parser_utils('data/interfaces.yaml')
    courage = lion.parse_yaml()
    lionheart_1 = f"Interface {courage['interfaces'][0]['name']} is {courage['interface'][0]['status']}"
    lionheart_2 = f"Interface {courage['interfaces'][1]['name']} is {courage['interface'][1]['status']}"
    print("Interface Information")
    print("="*50)
    print(lionheart_1)
    print(lionheart_2)
    print("="*50)
    print()

    # Logging YAML information
    msg = 'INTERFACE_STATUS_LOGGED'
    print(msg)
    logging.info(f"INTERFACE_MSG: {msg}")


    #Parsing CSV files for inventory information.
    tin_man = parser_utils.parser_utils('data/inventory.csv')
    new_heart = tin_man.parse_csv()
    heart_1 = f"Device {new_heart[1][0]} is a {new_heart[1][1]}{new_heart[1][2]}"
    heart_2 = f"Device {new_heart[2][0]} is a {new_heart[2][1]}{new_heart[2][2]}"
    print("Inventory Information")
    print("="*50)
    print(heart_1)
    print(heart_2)
    print("="*50)
    print()

    # Logging CSV information
    msg = 'DEVICE_INFO_LOGGED'
    print(msg)
    logging.info(f"DEVICE_MSG: {msg}")


    #Parsing XML file for vlan information.
    dorothy = parser_utils.parser_utils('data/vlan.xml')
    home = dorothy.parse_xml()
    print("VLAN Information")
    print("="*50)
    for family_member in home:
        family = f"VLAN {family_member['id']} is the {family_member['name']}"
        print("VLAN Information")
        print(family)
    print("="*50)
    print()

    # logging VLAN information
    msg = 'VLAN_INFO_LOGGED'
    print(msg)
    logging.info(f"VLAN_MSG: {msg}")


# This will run the main function
if __name__ == "__main__":
    main()


# Final log message indicating the end of the script
msg = '[LAB1-END]'
print(msg)
logging.info(msg)