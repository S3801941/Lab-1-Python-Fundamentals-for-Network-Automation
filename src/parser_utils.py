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
                road = brick_road.read()
        except FileExistsError:
            msg = f"[Error]: The file {yellow_brick_road} does not exist."
            print(msg)
            logging.info(f"LOG STRING: {msg}")
            return None
        else:
            self.road = road

    # This methode will parse JSON files.
    def parse_json(self):
        try:
            red_slippers = json.load(self.road)
        except json.JSONDecodeError as e:
            msg = 'PARSING_JSON_ERROR'
            print(msg)
            logging.info(f"LOG STRING: {msg}")
            return None
        else:
            msg = 'PARSING_JSON_SUCCESS'
            logging.info(f"LOG STRING: {msg}")
            return red_slippers

    # This method will parse YAML files.
    def parse_yaml(self):
        try:
            red_slippers = yaml.safe_load(self.road)
        except yaml.YAMLError as e:
            msg = 'PARSE_YAML_ERROR'
            print(msg)
            logging.info(f"LOG STRING: {msg}")
            return None
        else:
            msg = 'PARSING_YAML_SUCCESS'
            print(msg)
            logging.info(f"LOG STRING: {msg}")
            return red_slippers

    # This method will parse XML files.
    def parse_xml(self):
        try:
            wizard = ET.parse(self.yellow_brick_road)
            oz = wizard.getroot()
            red_slippers = []
            for dorothy in oz:
                tornado = {}
                for toto in dorothy:
                    tornado[toto.tag] = toto.text
                red_slippers.append(tornado)
        except ET.ParseError as e:
            msg = 'PARSING_XML_ERROR'
            print(msg)
            logging.info(f"LOG STRING: {msg}")
            return None
        else:
            msg = 'PARSING_XML_SUCCESS'
            print(msg)
            logging.info(f"LOG STRING: {msg}")
            return red_slippers

    # This method will parse CSV files.
    def parse_csv(self):
        try:
            red_slippers = []
            oz = csv.reader(self.yellow_brick_road.splitlines())
            for munchkins in oz:
                red_slippers.append(munchkins)
        except csv.Error as e:
            msg = 'PARSING_CSV_ERROR'
            print(msg)
            logging.info(f"LOG STRING: {msg}")
            return None
        else:
            msg = 'PARSING_CSV_SUCCESS'
            logging.info(f"LOG STRING: {msg}")
            return red_slippers