import db
from sqlalchemy import Column,Integer,String,Float,Date
from sqlalchemy.orm import relationship


class Partidos (db.Base):

    __tablenmae__ = 'partidos'
    id_partido = Column(Integer,primary_key=True)
    id_campeonato = Column(Integer)
    equipo_local = Column(String)
    equipo_visitante = Column(String)
    fecha_partido = Column(Date)
    marcador_equipo_local = Column(Integer)
    marcador_equipo_visitante = Column(Integer)
    estado = Column(String)

    def __init__ (self, id_partido,id_campeonato,equipo_local,equipo_visitante,fecha_partido,marcador_equipo_local,marcador_equipo_visitante,estado):
        self.id_partido = id_partido
        self.c
