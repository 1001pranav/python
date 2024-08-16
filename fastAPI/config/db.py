from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, Session
from config.settings import settings

engine = create_engine(
    settings.get_database_url()      
)
print(settings.get_database_url())
Base = declarative_base()

# Create the database tables
Base.metadata.create_all(bind=engine)

SessionLocal = sessionmaker(autoflush=False, bind=engine)

session = Session()