# config.py
import urllib.parse

class Config:
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    @staticmethod
    def get_db_uri():
        # CAMBIA ESTO CON TUS DATOS
        server = '(localdb)\SistemasAlex'           # o 'localhost\SQLEXPRESS'
        database = 'users_db'
        username = 'charlie'                
        password = 'Sistemas2020'   

        params = urllib.parse.quote_plus(
            f"DRIVER={{ODBC Driver 17 for SQL Server}};"
            f"SERVER={server};"
            f"DATABASE={database};"
            f"UID={username};"
            f"PWD={password};"
            f"TrustServerCertificate=yes;"
        )
        return f"mssql+pyodbc:///?odbc_connect={params}"