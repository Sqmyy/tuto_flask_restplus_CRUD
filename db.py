from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from db_cred import DB_URI

Session = sessionmaker(autocommit=False, autoflush=False, bind=create_engine(DB_URI))
session = scoped_session(Session)
