from flask import Flask, jsonify, request
from BACKEND.models.campeonato import Campeonato
from BACKEND import db

app = Flask(__name__)

@app.route('/getCampeonatos', methods=['GET'])
def getCampeonatos():
    campeonatos = db.session.query(Campeonato).all()
    campeonatosArr = []
    for c in campeonatos:
        campeonatosArr.append(c.toDict())
    return jsonify(campeonatosArr)

@app.route('/postCampeonato', methods=['POST'])
def postCampeonato():
    datosCampeonato = request.json
    nuevoCampeonato = Campeonato(
        id_deporte=datosCampeonato['id_deporte'],
        nombre=datosCampeonato['nombre'],
        temporada=datosCampeonato['temporada'],
        fecha_inicio=datosCampeonato['fecha_inicio'],
        fecha_fin=datosCampeonato['fecha_fin'],
        premio_total=datosCampeonato['premio_total']
    )
    db.session.add(nuevoCampeonato)
    db.session.commit()
    return jsonify({"Mensaje": "Campeonato creado correctamente"}), 201

@app.route('/putCampeonato', methods=['PUT'])
def putCampeonato():
    datosCampeonato = request.get_json()
    print(datosCampeonato)

    try:
        campeonato_actualizado = Campeonato(
            id_campeonato=datosCampeonato['id_campeonato'],
            id_deporte=datosCampeonato['id_deporte'],
            nombre=datosCampeonato['nombre'],
            temporada=datosCampeonato['temporada'],
            fecha_inicio=datosCampeonato['fecha_inicio'],
            fecha_fin=datosCampeonato['fecha_fin'],
            premio_total=datosCampeonato['premio_total']
        )
        db.session.merge(campeonato_actualizado)
        db.session.flush()
        db.session.commit()
        return jsonify({'statusCode': 200, 'message': 'Campeonato actualizado correctamente'})
    
    except Exception as e:
        return jsonify({'statusCode': 400, 'err': True, 'message': str(e)})

@app.route('/deleteCampeonato', methods=['DELETE'])
def deleteCampeonato():
    datosCampeonato = request.get_json()

    try:
        id_campeonato = datosCampeonato['id_campeonato']

        campeonato = db.session.query(Campeonato).filter_by(id_campeonato=id_campeonato).first()

        if campeonato:
            db.session.delete(campeonato)
            db.session.commit()
            return jsonify({'statusCode': 200, 'message': 'Campeonato eliminado correctamente'})
        else:
            return jsonify({'statusCode': 404, 'message': 'Campeonato no encontrado'})
    except Exception as e:
        return jsonify({'statusCode': 400, 'err': True, 'message': str(e)})

# Si quieres correrlo solo:
app.run("0.0.0.0",5000,debug=True)
