from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
import pymysql

engine = create_engine(
    "mysql+pymysql://root@localhost:3306/facturapp_25t2_py?charset=utf8mb4"
)


Session = sessionmaker(bind=engine)

session = Session()

Base = declarative_base()

