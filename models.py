#!/usr/bin/python
from json import JSONEncoder
from sqlalchemy import Column, Integer, String, Boolean, create_engine
from sqlalchemy.ext.declarative import declarative_base
from db_cred import DB_URI

Base = declarative_base()


class Task(Base):
    __tablename__ = 'tasks'

    t_id = Column(Integer, primary_key=True)
    t_title = Column(String(127))
    t_description = Column(String(255))
    t_done = Column(Boolean)

    def __init__(self, t_id, t_title, t_description, t_done):
        self.t_id = t_id
        self.t_title = t_title
        self.t_description = t_description
        self.t_done = t_done

    def setTitle(self, title):
        self.t_title = title

    def setDescription(self, description):
        self.t_description = description

    def setStatus(self, done):
        self.t_done = done

    def display(self):
        return "{id: " + str(self.t_id) + "; title: " + self.t_title + "; description: " + self.t_description + "; done: " + str(self.t_done) + "}"


if __name__ == "__main__":
    engine = create_engine(DB_URI)
    Base.metadata.drop_all(engine)
    Base.metadata.create_all(bind=engine)