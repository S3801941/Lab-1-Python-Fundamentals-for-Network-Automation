# In this file, we will create a class that will parse the attributes of a network device from a data file.
# To do this we will create a class method that will read the data from the file.
# Then we will have a method to parse the data depending on the type of data that is being read.
# We will also be making these methods capable of handling errors and exceptions that may occur during the parsing process.
# Lastly, we will log the results of the parsing process to a log file.

# Try to import logging, csv, json, os, xml.etree.ElementTree, and yaml and have a catch all error except statment.
try:
    import logging
    import csv
    import json
    import os
    import xml.etree.ElementTree as ET
    import yaml
    print("Import Successful")
except ImportError:
    print("Unable to import one or more imports")        

class parser_utils:

    # This module will be for trying to opening up and reading the file from the data folder.
    def __init__(self, yellow_brick_road):
        self.yellow_brick_road = yellow_brick_road
        try:
            with open(yellow_brick_road, 'r') as brick_road:
                road_brick = brick_road.read()
        except FileExistsError:
            msg = f"[Error]: The file {yellow_brick_road} does not exist."
            print(msg)
            logger.info(f"LOG STRING: {msg}")
            return None

    # This methode will parse JSON files.
    def parse_JSON

        