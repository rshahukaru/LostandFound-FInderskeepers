import os
from dotenv import load_dotenv

basedir = os.path.abspath(os.path.dirname(__file__))
load_dotenv()

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'dev-key-placeholder'
    
    # Azure SQL Database configuration
    DB_SERVER = os.environ.get('AZURE_SQL_SERVER')
    DB_NAME = os.environ.get('AZURE_SQL_DATABASE')
    DB_USER = os.environ.get('AZURE_SQL_USER')
    DB_PASS = os.environ.get('AZURE_SQL_PASSWORD')
    
    SQLALCHEMY_DATABASE_URI = (
        f"mssql+pyodbc://{DB_USER}:{DB_PASS}@{DB_SERVER}"
        f"/{DB_NAME}?driver=ODBC+Driver+18+for+SQL+Server"
        "&encrypt=yes&TrustServerCertificate=yes"
    )
    SQLALCHEMY_TRACK_MODIFICATIONS = False