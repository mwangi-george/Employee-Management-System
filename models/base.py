from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from dotenv import load_dotenv
import os

# Load environment vars
load_dotenv()

# get postgres connection string from env vars
DB_URL = os.getenv("POSTGRES_DB_URL")

# if no connection found use a fallback sqlite db
FALL_BACK_DB_URL = "sqlite:///employees.db"

# define a connection engine based on available db
if DB_URL is not None:
    engine = create_engine(DB_URL)
else:
    engine = create_engine(FALL_BACK_DB_URL, connect_args={"check_same_thread": False})


# create a custom session class bound to the defined engine for interacting with the db later
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# create a base class for all the ORM models to be created in the application
Base = declarative_base()


def get_db():
    """A generator function to manage database sessions"""
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
