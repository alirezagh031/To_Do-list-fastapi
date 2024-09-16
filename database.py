from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

SQLALCHEMY_DATABASE_URL = "postgresql://alireza_gh:Alireza81@localhost/alireza_gh"
engine = create_engine(SQLALCHEMY_DATABASE_URL)
sessionlocal = sessionmaker(bind=engine, autocommit=False, autoflush=False)
Base = declarative_base()