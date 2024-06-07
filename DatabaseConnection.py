import cx_Oracle
import pyodbc

class DatabaseConnection:
    def __init__(self, db_config):
        self.db_config = db_config
        self.connection = self.connect()

    def connect(self):
        if self.db_config['type'] == 'oracle':
            return cx_Oracle.connect(self.db_config['user'], self.db_config['password'], self.db_config['dsn'])
        elif self.db_config['type'] == 'sql_server':
            return pyodbc.connect(f"DRIVER={{SQL Server}};SERVER={self.db_config['server']};DATABASE={self.db_config['database']};UID={self.db_config['user']};PWD={self.db_config['password']}")
        # Add more database types as needed

    def query(self, query):
        return pd.read_sql(query, self.connection)
