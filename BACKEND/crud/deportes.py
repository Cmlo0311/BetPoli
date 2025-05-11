from flask import Flask, jsonify, request, make_response
from BACKEND.models.deportes import Deporte

from BACKEND import db

app = Flask(__name__)

@app.route('/getDeportes',methods=['GET'])
def getDeportes():
    misD = db.session.query(Deporte).all()
    deportesArr = []
    for d in misD:
        deportesArr.append(d.toDict())
    return jsonify(deportesArr)

@app.route('/postDeporte',methods=['POST'])
def postDeporte():
    datosDeporte=request.json
    nuevoDeporte=Deporte(
        id_deporte=datosDeporte['id_deporte'],
        nombre=datosDeporte['nombre'],
        descripcion=datosDeporte['descripcion']
    )
    db.session.add(nuevoDeporte)
    db.session.commit()
    return jsonify({"Mensaje":"Deporte creado correctamente"}), 201

@app.route('/putDeporte',methods=['PUT'])
def putDeporte():
    datosDeporte=request.get_json()
    print(datosDeporte)

    try:
        deporte_actualizado = Deporte(
            id_deporte=datosDeporte['id_deporte'],
            nombre=datosDeporte['nombre'],
            descripcion=datosDeporte['descripcion']
        )
        db.session.merge(deporte_actualizado)
        db.session.flush()
        db.session.commit()
        return jsonify({'statusCode': 200, 'message': 'Success'})
    
    except Exception as e:
        return jsonify({'statusCode': 400, 'err': True, 'message': str(e)})

@app.route('/deleteDeporte',methods=['DELETE'])
def  deleteDeporte():
    datosDeporte = request.get_json()

    try:
        id_deporte = datosDeporte['id_deporte']

        deporte = db.session.query(Deporte).filter_by(id_deporte=id_deporte).first()

        if deporte:
            db.session.delete(deporte)
            db.session.commit()
            return jsonify({'statusCode': 200, 'message': 'Deporte eliminado correctamente'})
        else:
            return jsonify({'statusCode': 404, 'message': 'Deporte no encontrado'})
    except Exception as e:
            return jsonify({'statusCode': 400, 'err': True, 'message': str(e)})
    
app.run("0.0.0.0",5000,debug=True)