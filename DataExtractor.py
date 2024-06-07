import pandas as pd

class DataExtractor:
    def __init__(self, db_connection, table, columns):
        self.db_connection = db_connection
        self.table = table
        self.columns = columns

    def extract(self):
        query = f"SELECT {', '.join(self.columns)} FROM {self.table}"
        return self.db_connection.query(query)
