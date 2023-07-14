from flask import Flask ,jsonify ,request
from app import app,ma
from modelos import *


# Definición del esquema para la clase Producto
class DiscoSchema(ma.Schema):
   
    class Meta:
        fields = ("id", "nombre", "artista", "afecha", "imagen")

disco_schema = DiscoSchema()  # Objeto para serializar/deserializar un producto
discos_schema = DiscoSchema(many=True)  # Objeto para serializar/deserializar múltiples productos

@app.route("/discos", methods=["GET"])
def get_Discos():
    
    all_discos = Disco.query.all()  # Obtiene todos los registros de la tabla de productos
    result = discos_schema.dump(all_discos)  # Serializa los registros en formato JSON
    return jsonify(result)  # Retorna el JSON de todos los registros de la tabla

@app.route("/discos/<id>", methods=["GET"])
def get_disco(id):
    
    disco = Disco.query.get(id)  # Obtiene el producto correspondiente al ID recibido
    return disco_schema.jsonify(disco)  # Retorna el JSON del producto

@app.route("/discos/<id>", methods=["DELETE"])
def delete_disco(id):
    
    disco = Disco.query.get(id)  # Obtiene el producto correspondiente al ID recibido
    db.session.delete(disco)  # Elimina el producto de la sesión de la base de datos
    db.session.commit()  # Guarda los cambios en la base de datos
    return disco_schema.jsonify(disco)  # Retorna el JSON del producto eliminado

@app.route("/discos", methods=["POST"])  # Endpoint para crear un producto
def create_disco():
    
    nombre = request.json["nombre"]  # Obtiene el nombre del producto del JSON proporcionado
    artista = request.json["artista"]  # Obtiene el precio del producto del JSON proporcionado
    afecha = request.json["afecha"]  # Obtiene el stock del producto del JSON proporcionado
    imagen = request.json["imagen"]  # Obtiene la imagen del producto del JSON proporcionado
    new_disco = Disco(nombre, artista, afecha, imagen)  # Crea un nuevo objeto Producto con los datos proporcionados
    db.session.add(new_disco)  # Agrega el nuevo producto a la sesión de la base de datos
    db.session.commit()  # Guarda los cambios en la base de datos
    return disco_schema.jsonify(new_disco)  # Retorna el JSON del nuevo producto creado

@app.route("/discos/<id>", methods=["PUT"])  # Endpoint para actualizar un producto
def update_disco(id):
    
    disco = Disco.query.get(id)  # Obtiene el producto existente con el ID especificado

    # Actualiza los atributos del producto con los datos proporcionados en el JSON
    disco.nombre = request.json["nombre"]
    disco.artista = request.json["artista"]
    disco.afecha = request.json["afecha"]
    disco.imagen = request.json["imagen"]

    db.session.commit()  # Guarda los cambios en la base de datos
    return disco_schema.jsonify(disco)  # Retorna el JSON del producto actualizado


# Definición del esquema para la clase Producto
class VideoSchema(ma.Schema):
    
    class Meta:
        fields = ("id", "iddisco", "nombre", "videoclip")

video_schema = VideoSchema()  # Objeto para serializar/deserializar un producto
videos_schema = VideoSchema(many=True)  # Objeto para serializar/deserializar múltiples productos

@app.route("/videos", methods=["GET"])
def get_Videos():
    
    all_videos = Video.query.all()  # Obtiene todos los registros de la tabla de productos
    result = videos_schema.dump(all_videos)  # Serializa los registros en formato JSON
    return jsonify(result)  # Retorna el JSON de todos los registros de la tabla

@app.route("/videos/<id>", methods=["GET"])
def get_Video(id):
   
    video = Video.query.get(id)  # Obtiene el producto correspondiente al ID recibido
    return video_schema.jsonify(video)  # Retorna el JSON del producto

@app.route("/videos/<id>", methods=["DELETE"])
def delete_video(id):
    
    video = Video.query.get(id)  # Obtiene el producto correspondiente al ID recibido
    db.session.delete(video)  # Elimina el producto de la sesión de la base de datos
    db.session.commit()  # Guarda los cambios en la base de datos
    return video_schema.jsonify(video)  # Retorna el JSON del producto eliminado

@app.route("/videos", methods=["POST"])  # Endpoint para crear un producto
def create_video():
    
    iddisco = request.json["iddisco"]  # Obtiene el nombre del producto del JSON proporcionado
    nombre = request.json["nombre"]  # Obtiene el precio del producto del JSON proporcionado
    videoclip = request.json["videoclip"]  # Obtiene el stock del producto del JSON proporcionado
    new_video = Video(iddisco, nombre, videoclip)  # Crea un nuevo objeto Producto con los datos proporcionados
    db.session.add(new_video)  # Agrega el nuevo producto a la sesión de la base de datos
    db.session.commit()  # Guarda los cambios en la base de datos
    return video_schema.jsonify(new_video)  # Retorna el JSON del nuevo producto creado

@app.route("/videos/<id>", methods=["PUT"])  # Endpoint para actualizar un producto
def update_video(id):
    
    video = Video.query.get(id)  # Obtiene el producto existente con el ID especificado

    # Actualiza los atributos del producto con los datos proporcionados en el JSON
    video.iddisco = request.json["iddisco"]
    video.nombre = request.json["nombre"]
    video.videoclip = request.json["videoclip"]
    #video.imagen = request.json["imagen"]

    db.session.commit()  # Guarda los cambios en la base de datos
    return video_schema.jsonify(video)  # Retorna el JSON del producto actualizado
