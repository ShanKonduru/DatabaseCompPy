import json

class Config:
    def __init__(self, config_file):
        with open(config_file, 'r') as file:
            config = json.load(file)
        self.source_db = config['source_db']
        self.destination_db = config['destination_db']
