# config.py
import urllib.parse

class Config:
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    @staticmethod
    def get_db_uri():
        server = 'localhost'           # o 'localhost\\SQLEXPRESS'
        database = 'users_db'

        params = urllib.parse.quote_plus(
            f"DRIVER={{ODBC Driver 17 for SQL Server}};"
            f"SERVER={server};"
            f"DATABASE={database};"
            f"Trusted_Connection=yes;"  # ← USA TU CUENTA DE WINDOWS
            f"TrustServerCertificate=yes;"
        )
        return f"mssql+pyodbc:///?odbc_connect={params}"