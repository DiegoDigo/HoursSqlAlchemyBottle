from datetime import datetime
from sqlalchemy import (create_engine, Column, String, Integer, DateTime, ForeignKey)
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker

engine = create_engine('postgresql+psycopg2://postgres:261216@localhost:5432/hour')

Base = declarative_base()

Session = sessionmaker(bind=engine)

session = Session()


class User(Base):
    __tablename__ = 'usuario'
    user_id = Column(Integer, primary_key=True, autoincrement=True)
    username = Column(String(20), nullable=False, unique=True, index=True)
    password = Column(String, nullable=False)
    email = Column(String, unique=True, nullable=False)
    created = Column(DateTime(), default=datetime.now)
    update_on = Column(DateTime(), default=datetime.now, onupdate=datetime.now())


class Perfil(Base):
    __tablename__ = 'perfil'
    perfil_id = Column(Integer, primary_key=True, autoincrement=True)
    fisrt_name = Column(String(20), nullable=False)
    last_name = Column(String(50), nullable=False)
    office = Column(String)
    user_id = Column(Integer, ForeignKey('usuario.user_id', ondelete='CASCADE'), nullable=False)
    user = relationship("User", backref='usuario')


Base.metadata.create_all(engine)

