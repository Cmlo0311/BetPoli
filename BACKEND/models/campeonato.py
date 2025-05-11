from BACKEND.db import Base
from sqlalchemy import Column,Integer,String,Float,Date,DECIMAL,ForeignKey
from sqlalchemy.orm import relationship

class Campeonato(Base):
    __tablename__ = 'campeonatos'
    id_campeonato = Column(Integer, primary_key=True, autoincrement=True)
    id_deporte    = Column(Integer, ForeignKey('deportes.id_deporte'))
    nombre        = Column(String(100))
    temporada     = Column(String(50))
    fecha_inicio  = Column(Date)
    fecha_fin     = Column(Date)
    premio_total  = Column(DECIMAL(10,2))
    deportes      = relationship("Deporte", back_populates="campeonatos")
    partidos      = relationship("Partido", back_populates="campeonato")

    
    def __init__(self, id_deporte, nombre, temporada, fecha_inicio, fecha_fin, premio_total):
        self.id_deporte = id_deporte
        self.nombre = nombre
        self.temporada = temporada
        self.fecha_inicio = fecha_inicio
        self.fecha_fin = fecha_fin
        self.premio_total = premio_total

    def __repr__(self):
        return (f"Campeonato(id_campeonato={self.id_campeonato}, id_deporte={self.id_deporte}, "
                f"nombre='{self.nombre}', temporada='{self.temporada}', "
                f"fecha_inicio={self.fecha_inicio}, fecha_fin={self.fecha_fin}, "
                f"premio_total={self.premio_total})")
    
    def __str__(self):
        return str(self.id_campeonato)
    
    def toDict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}
    
    def json(self):
        return {
            'ID_Campeonato': self.id_campeonato,
            'ID_Deporte': self.id_deporte,
            'Nombre': self.nombre,
            'Temporada': self.temporada,
            'Fecha_Inicio': str(self.fecha_inicio),
            'Fecha_Fin': str(self.fecha_fin),
            'Premio_Total': float(self.premio_total) if self.premio_total else None
        } 