from sqlalchemy import create_engine 
from sqlalchemy. ext.declarative import declarative_base
from sqlalchemy.orm import sessionmarker

#conectores de base datos

#base datos local

#engine = create_engine (' sqlite:///mydb.db')

#base datos relacional
engine = create_engine('mysql+pymysql://root:root@base_datos/clase')

base = declarative_base()

# manejo de las sesiones 
sesion = sessionmarker(bind=engine)
session = sesion()