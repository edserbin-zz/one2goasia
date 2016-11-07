import os

import xml.etree.ElementTree as ET

path = os.path.dirname(__file__)

file_name1 = path + '/personal_data.xml'


def return_command_executer():
    tree = ET.parse(file_name1)
    root = tree.getroot()
    command_executer = root.find('command_executer').text
    return command_executer
