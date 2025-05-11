import mysql.connector
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import declarative_base

#engine = create_engine(mysql.connector.connect(user="root", password="1234", host="localhost", database="agenda", port="3306"))
connection_string = "mysql+mysqlconnector://root:0311@localhost:3306/betpoli"
engine = create_engine(connection_string, echo=True)

Session = sessionmaker(bind=engine)
session = Session()

Base = declarative_base()