from flask import Flask, jsonify, request
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from flask_cors import CORS 

app = Flask(__name__)

app.config['MONGO_DBNAME'] = 'Laboratorios_Departamentales'
app.config['MONGO_URI'] = 'mongodb://localhost:27017/Laboratorios_Departamentales'

mongo = PyMongo(app)
CORS(app)

Dict={"Nombre": "",
      "Ano": "",
      "Descripcion": "",
      "NIT": "",
      "Municipio": "",
      "Gerente": "",
      "Telefono": "",
      "Area": "",
      "Pruebas": "",
      "Profesional": "",
      "Imagen": "",
      "Estado": "",
      "Certificaciones": ""    
}
      
@app.route('/api/Laboratorios', methods=['GET'])
def get_all_labs():
    Laboratorios = mongo.db.Laboratorios 
    result = []
    for field in Laboratorios.find():
        result.append({'_id': str(field['_id']),  
                       'Nombre': field['Nombre'], 
                       'Ano': field['Ano'], 
                       'Descripcion': field['Descripcion'], 
                       'NIT': field['NIT'], 
                       'Municipio': field['Municipio'], 
                       'Gerente': field['Gerente'], 
                       'Telefono': field['Telefono'],
                       'Area': field['Area'], 
                       'Pruebas': field['Pruebas'], 
                       'Profesional': field['Profesional'], 
                       'Imagen': field['Imagen'],  
                       'Estado': field['Estado'], 
                       'Certificaciones': field['Certificaciones']})
    return jsonify(result)

@app.route('/api/Ingresar_Lab', methods=['POST'])
def add_task():
            labs = mongo.db.Laboratorios
            data = request.get_json()
            The_Dict=Dict.copy()
            NIT=data['NIT']
            The_Dict["NIT"]=NIT
            Nombre=data['Nombre']
            The_Dict['Nombre']=Nombre
            Ano = data['Ano']
            The_Dict['Ano'] = Ano
            Descripcion = data['Descripcion']
            The_Dict['Descripcion'] = Descripcion
            Municipio=data['Municipio']
            The_Dict['Municipio']=Municipio
            Telefono=data['Telefono']
            The_Dict['Telefono']=Telefono
            N_Coor=data['Gerente']
            The_Dict['Gerente']=N_Coor
            Area = data['Area']
            The_Dict['Area'] = Area
            Pruebas = data['Pruebas']
            The_Dict['Pruebas'] = Pruebas
            Est_Func=data['Estado']
            The_Dict['Estado']=Est_Func
            Profesional = data['Profesional']
            The_Dict['Profesional'] = Profesional
            Imagen = data['Imagen']
            The_Dict['Imagen'] = Imagen
            Certificaciones = data['Certificaciones']
            The_Dict['Certificaciones'] = Certificaciones
            El_id=labs.insert_one(The_Dict).inserted_id
            return jsonify({'result': str(El_id)})

@app.route('/api/lab/<id>', methods=['DELETE'])
def delete_task(id):
    Laboratorios = mongo.db.Laboratorios

    response = Laboratorios.delete_one({'_id': ObjectId(id)})

    if response.deleted_count == 1:
        result = {'message': 'record deleted'}
    else: 
        result = {'message': 'no record found'}
    
    return jsonify({'result': result})            

if __name__ == '__main__':
    app.run(debug=True)