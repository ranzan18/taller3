 from taller_3_ORM.databse.connector import *
 from sqlalchemy import column, integer, string

 class cliente(base)
 __tablename__="cliente"
 codigo= column(integer, primary_key=True, index=True)
 direccion = column(string(30))
 telefono = column(string(30))
 cuentadebanco = column(string(30))

 class persona(base):
     __tablename__ ="cliente"