import json

class Config:
    def __init__(self, lines: list[str], options: list[str], file: str):
        self.lines = lines
        self.options = options
        self.file = file

def parse(config_path: str = "config.json") -> Config:
    with open(config_path, "r") as config_json:
        config = json.load(config_json)
        return Config(config["lines"], config["assessments"], config["file"])
