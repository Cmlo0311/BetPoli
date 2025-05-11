from BACKEND.db import Base
from sqlalchemy import Column,Integer,String,Float,Date
from sqlalchemy.orm import relationship

class Deporte (Base):
    __tablename__ = 'deportes'
    id_deporte = Column(Integer,primary_key=True)
    nombre = Column(String,nullable=False)
    descripcion = Column(String, nullable=True)

    def __init__(self,id_deporte,nombre,descripcion):
        self.id_deporte=id_deporte
        self.nombre = nombre
        self.descripcion = descripcion

    def __repr__(self):
        return f"Deporte({self.id_deporte},{self.nombre},{self.descripcion})"
    
    def __str__(self):
        return self.id_deporte
    
    def toDict(self):
        return {c.name:getattr(self,c.name) for c in self.__table__.columns}
    
    def json(self):
        return {'ID_Deporte': self.id_deporte,'Nombre': self.nombre,'Descripcion': {self.descripcion}}


