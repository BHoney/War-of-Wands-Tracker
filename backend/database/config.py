import sqlalchemy
from config import configuration
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

#db setup
engine = sqlalchemy.create_engine(
    configuration.SQLALCHEMY_DATABASE_URL, connect_args={
        "check_same_thread": False
    }
)
SessionLocal = sessionmaker(bind=engine)
