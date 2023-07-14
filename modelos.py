from app import db,app

class Disco(db.Model):  # Producto hereda de db.Model
    
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100))
    artista = db.Column(db.String(100))
    afecha = db.Column(db.Integer)
    imagen = db.Column(db.String(400))

    def __init__(self, nombre, artista, afecha, imagen):
        
        self.nombre = nombre
        self.artista = artista
        self.afecha = afecha
        self.imagen = imagen

    # Se pueden agregar más clases para definir otras tablas en la base de datos
    
class Video(db.Model):  # Producto hereda de db.Model
        
    id = db.Column(db.Integer, primary_key=True)     
    iddisco = db.Column(db.Integer)
    nombre = db.Column(db.String(100))
    videoclip = db.Column(db.String(400))

    def __init__(self, iddisco, nombre, videoclip):
            
        self.iddisco = iddisco
        self.nombre = nombre 
        self.videoclip = videoclip

with app.app_context():
    db.create_all()  # Crea todas las tablas en la base de datos


