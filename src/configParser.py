import json

class ConfigLine:
    __init__(self, dropDownOptions, label):
        self.label = label
        self.options = dropDownOptions

def parse():
    configLines = []
    with open("config.json", "r") as config_json:
        config = json.load(config_json)
        for line in config.lines:
            configLines.append(ConfigLine(config.Assessments, line))
    return configLines
