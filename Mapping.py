class Mapping:
    def __init__(self, mappings_file):
        with open(mappings_file, 'r') as file:
            mappings = json.load(file)
        self.src_table = mappings['source']['table']
        self.dest_table = mappings['destination']['table']
        self.src_columns = mappings['source']['columns']
        self.dest_columns = mappings['destination']['columns']
        self.key_columns = mappings['key_columns']
