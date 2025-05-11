from BACKEND.db import Base
from sqlalchemy import Column,Integer,String,Float,Date
from sqlalchemy.orm import relationship

class Usuario(Base):
    __tablename__='Usuarios'
    NombreUsuario = Column(String, primary_key=True,)
    Nombre = Column(String)
    Apellido = Column(String)
    Identificacion = Column(Integer)
    CorreoElectronico = Column(String)
    FechaNacimiento = Column(Date)
    Contrasena = Column(String)

    def __init__(self,NombreUsuario,Nombre,Apellido,Identificacion,CorreoElectronico,FechaNacimiento,Contrasena):
        self.NombreUsuario=NombreUsuario
        self.Nombre=Nombre
        self.Apellido=Apellido
        self.Identificacion=Identificacion
        self.CorreoElectronico=CorreoElectronico
        self.FechaNacimiento=FechaNacimiento
        self.Contrasena=Contrasena

    def __repr__(self):
        return f"Usuarios({self.NombreUsuario},{self.Nombre},{self.Apellido},{self.Identificacion},{self.CorreoElectronico},{self.FechaNacimineto},{self.Contrasena})"
    
    def __str__(self):
        return self.NombreUsuario
    
    def toDict (self):
        return {c.name:getattr(self,c.name) for c in self.__table__.columns}
    
    def json(self):
        return {'NombreUsuario': self.NombreUsuario,'Nombre':self.Nombre,'Apellido':self.Apellido,'Identificacion':self.Identificacion,
                'Correo Electronico':self.CorreoElectronico,'Fecha de nacimiento':self.FechaNacimiento,'Contrasena':self.Contrasena}
    