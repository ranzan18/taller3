 from taller_3_ORM.databse.connector import *
 from sqlalchemy import column, integer, string

 class animal(base)
 __tablename__="animal"
 animal= column(integer, primary_key=True, index=True)
 raza_canino = column(string(30))
 vacunas = column(string(30))
 cuentadebanco = column(string(30))

 class persona(base):
     __tablename__ ="animal"