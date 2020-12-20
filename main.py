from taller_3_ORM.database.connector import*
from taller_3_ORM.model.cliente import cliente

if __name__== '__main__':
    print ("taller 3")

    #crear todo en la base de datos
    Base.metabase-create_all(engine)

    cl1= cliente (direccion="panama", telefono="12345678",cuentadebanco="123445678910")
     
     print(cl1)
     #agregar los insert a la sesion
     sesion.add(cl1)

     #ejecutaer la conuslta
    session.commit()

    print(cl1)




    if __name__== '__main__':
    print ("taller 3")

    #crear todo en la base de datos
    Base.metabase-create_all(engine)

    ani = (animal="canino", raza_canino="perro_callejero",vacunas="todas_puestas")
     
     print(ani)
     #agregar los insert a la sesion
     sesion.add(ani)

     #ejecutaer la conuslta
    session.commit()

    print(ani)
