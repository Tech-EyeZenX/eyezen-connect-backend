from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declartive_base
from sqlalachemy.orm import sessionmaker

from src.config.settings import settings


# create the database engine using the DATABASE_URL from settings

engine = create_engine(settings.DATABASE_URL)

sessionLocal = sessionmaker(autocommit = False, autoflush = False, bind = engine)

Base = declartive_base()

def get_db():
    db = sessionLocal()

    try:
        yield db
    finally:
        db.close()