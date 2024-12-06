import pyodbc
import os
from dotenv import load_dotenv

load_dotenv()

server = os.getenv('AZURE_SQL_SERVER')
database = os.getenv('AZURE_SQL_DATABASE')
username = os.getenv('AZURE_SQL_USER')
password = os.getenv('AZURE_SQL_PASSWORD')

print(f"Attempting to connect to server: {server}")
print(f"Database: {database}")
print(f"Username: {username}")

connection_string = (
    f"Driver={{ODBC Driver 18 for SQL Server}};"
    f"Server=tcp:{server},1433;"
    f"Database={database};"
    f"Uid={username};"
    f"Pwd={password};"
    "Encrypt=yes;"
    "TrustServerCertificate=yes;"
)

try:
    print("Attempting connection...")
    conn = pyodbc.connect(connection_string)
    print("Connected successfully!")
    conn.close()
except Exception as e:
    print(f"Error: {str(e)}")