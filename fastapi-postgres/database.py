from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
import os

DB_URL = "postgresql://neondb_owner:npg_6LrCk2DtnhMd@ep-floral-firefly-a1z55hid-pooler.ap-southeast-1.aws.neon.tech/neondb?sslmode=require"

engine = create_engine(DB_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
