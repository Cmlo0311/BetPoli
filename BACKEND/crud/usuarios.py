from flask import Flask, jsonify, request, make_response
from BACKEND.models.usuarios import Usuario

from BACKEND import db

from flask_cors import CORS

app = Flask(__name__)
CORS(app)


@app.route('/getUsuario',methods=['GET'])
def getUsuario():

    misP = db.session.query(Usuario).all()
    usuarioArr = []
    for p in misP:
        usuarioArr.append(p.toDict())
    return jsonify(usuarioArr)


@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    NombreUsuario = data.get('NombreUsuario')
    Contrasena = data.get('Contrasena')
    print("JSON recibido:", data)

    usuario = db.session.query(Usuario).filter_by(NombreUsuario=NombreUsuario).first()

    if usuario and usuario.Contrasena == Contrasena:
        return jsonify({"mensaje": "Login exitoso", "usuario": usuario.toDict()}), 200
    else:
        return make_response(jsonify({"mensaje": "Usuario o contraseña incorrecta"}), 401)



@app.route('/postUsuario',methods=['POST'])
def postUsuario():
    datosUsuario=request.json
    nuevo_usuario= Usuario(
        NombreUsuario = datosUsuario['NombreUsuario'],
        Nombre=datosUsuario['Nombre'],
        Apellido=datosUsuario['Apellido'],
        Identificacion=datosUsuario['Identificacion'],
        CorreoElectronico=datosUsuario['CorreoElectronico'],
        FechaNacimiento=datosUsuario['FechaNacimiento'],
        Contrasena=datosUsuario['Contrasena']
    )
    db.session.add(nuevo_usuario)
    db.session.commit()
    return jsonify({"Mensaje":"Usuario creado correctamente"}), 201
    
    
@app.route('/putUsuario',methods=['PUT'])
def putUsuario():
    datosUsuario=request.get_json()

    print(datosUsuario)

    try:
        usuario_actualizado = Usuario(
            NombreUsuario=datosUsuario['NombreUsuario'],
            Nombre=datosUsuario['Nombre'],
            Apellido=datosUsuario['Apellido'],
            Identificacion=datosUsuario['Identificacion'],
            CorreoElectronico=datosUsuario['CorreoElectronico'],
            FechaNacimiento=datosUsuario['FechaNacimiento'],
            Contrasena=datosUsuario['Contrasena']
        )
        db.session.merge(usuario_actualizado)
        db.session.flush()
        db.session.commit()
        return jsonify({'statusCode': 200, 'message': 'Success'})


    except Exception as e:
        return jsonify({'statusCode': 400, 'err': True, 'message': str(e)})

@app.route('/deleteUsuario', methods=['DELETE'])
def deleteUsuario():
    datosUsuario=request.get_json()

    try:
        NombreUsuario = datosUsuario['NombreUsuario']

        usuario = db.session.query(Usuario).filter_by(NombreUsuario=NombreUsuario).first()

        if usuario:
            db.session.delete(usuario)
            db.session.commit()
            return jsonify({'statusCode': 200, 'message': 'Usuario eliminado correctamente'})
        else:
            return jsonify({'statusCode': 404, 'message': 'Usuario no encontrado'})

    except Exception as e:
            return jsonify({'statusCode': 400, 'err': True, 'message': str(e)}) 

app.run("0.0.0.0",5000,debug=True)