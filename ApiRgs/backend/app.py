from flask import Flask, request, jsonify, Response, session
from flask_pymongo import PyMongo
from bson import json_util, ObjectId
from usersModel import Users
from Authenticated import Authenticated
from Security import Security
import jwt
from decouple import config
from flask_cors import CORS

app = Flask(__name__)
app.config['MONGO_URI'] = 'mongodb://localhost/rgtmongodb'
mongo = PyMongo(app)

CORS(app)

has_access = []
# encoded_token = []
# print (encoded_token)


# ruta de tokenvalidate
@app.route('/token', methods=['GET'])
def obtener_datos_protegidos():
    # Obtener el token de los encabezados de la solicitud
    token = request.headers.get('Authorization')
    
    
    if token and token.startswith('Bearer '):

        token = token[len('Bearer '):]
        global has_access
        has_access = token
        return jsonify({'mensaje': 'Datos protegidos'})
    else:
        # Si no se proporciona un token válido, devolver una respuesta de error
        return jsonify({'error': 'No se proporcionó un token válido'}), 401



#Ruta login
@app.route('/prueba', methods=['GET'])
def prueba():
    return jsonify({"prueba": "existosa"})

@app.route('/auth', methods=['POST'])
def login():
    username = request.json['username']
    password = request.json['password']
    
    # _user = (username,password)
    # print (_user)
    authenticated_user = Authenticated.login_auth(username, password)
    # print (authenticated_user)
    if (authenticated_user != None):
        encoded_token = Security.generate_token(authenticated_user)
        
        return jsonify({'success':True, 'token':encoded_token})
    else:
        return jsonify({'success':False})
        
        # global encoded_token 
        # encoded_token = Security.generate_token(authenticated_user)
        # # print (encoded_token)
        
        # return encoded_token
 

#Rutas
@app.route('/consulta/<d_i>', methods=['GET'])
def login_client(d_i):
    login_client = Users.identify_client(d_i)
    if login_client:
        return jsonify({'mensaje':'Cliente encontrado',
                    'datos': login_client})
    else:
        return not_found()

@app.route('/clients', methods=['POST'])
def create_client():

    # has_access=Security.validate_token(request.headers)
    if has_access: 
        try:
            name = request.json['name']
            lastname = request.json['lastname']
            d_i = request.json['d_i']
            cel = request.json['cel']
            email = request.json['email']
            address = request.json['address']
            acceptPromotions = request.json['acceptPromotions']
  
            if name and lastname and d_i and cel and email and address:
                response = Users (name, lastname, d_i, cel, email, address,acceptPromotions)
                client_creado = response.crear_client()
                
                return jsonify({'mensaje':'Cliente Creado',
                            'data': client_creado})
            else: 
                return not_found()
        except: 
            return not_found()
    else: 
        return jsonify({'mensaje': 'No autorizado'})

@app.route('/clients', methods=['GET'])
def show_clients():

    # has_access=Security.validate_token(request.headers)

    if has_access:
        
        clients_list = Users.get_clients()

        return jsonify({'mensaje':'Lista de clientes',
                        'datos': clients_list})
    else:
        return jsonify({'mensaje': 'No autorizado'}), 401

@app.route('/clients/<id>', methods=['GET'])
def show_client(id):

        client = Users.get_client(id)
        
        return jsonify({'mensaje':'Cliente por su ID',
                        'datos': client})
# Consulta por numero de cédula
# @app.route('/clients/<d_i>', methods=['GET'])
# def identify_client(d_i):

#         client = Users.get_client(d_i)
        
#         return jsonify({'mensaje':'Cliente por su ID',
#                         'datos': client})


@app.route('/clients/<id>', methods=['DELETE'])
def drop_client(id):
    # has_access=Security.validate_token(request.headers)
    if has_access:
        del_client = Users.delete_client(id)
        
        return jsonify({'Cliente borrado': del_client})
    else: 
        return jsonify({'mensaje': 'No autorizado'})

@app.route('/clients/<id>', methods=['PUT'])
def update_client(id):
    # has_access=Security.validate_token(request.headers)

    if has_access:
        response = Users.put_client(id)
        return jsonify({'Cliente':response,
                        'Estado': 'ha sido actualizado'})
    else: 
        return jsonify({'mensaje': 'No autorizado'})
        
    
@app.errorhandler(404)
def not_found(error=None):
    response = jsonify ({
        'message': 'Resource Not Found: ' + request.url,
        'status': 404
    })
    response.status_code = 404
    return response

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)