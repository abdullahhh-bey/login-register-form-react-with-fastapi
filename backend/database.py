from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import urllib

params = urllib.parse.quote_plus(
    "DRIVER={ODBC Driver 18 for SQL Server};"
    "SERVER=DESKTOP-JOGOILA\SQLEXPRESS01;"   
    "DATABASE=UserAuthDb;"
    "Trusted_Connection=yes;"
    "TrustServerCertificate=yes;"
)

#connection string
DATABASE_URL = f"mssql+pyodbc:///?odbc_connect={params}"

#created database setup path like DbCONTEXT
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

#Base class for creating tables by Models
Base = declarative_base()

#Dependency Function for services
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
