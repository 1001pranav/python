from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, Session
from config.settings import settings


from motor.motor_asyncio import AsyncIOMotorClient
engine = create_engine(
    settings.get_database_url()      
)

Base = declarative_base()

# Create the database tables
Base.metadata.create_all(bind=engine)

SessionLocal = sessionmaker(autoflush=False, bind=engine)

session = Session() 

client = AsyncIOMotorClient(settings.get_mongo_url())
database = client.dbname

collection = database["users"]