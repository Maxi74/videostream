import reflex as rx
from .database import *

db = Database()

class State(rx.State):
    nombre: str
    dni: str
    email: str
    telefono: str
    direccion: str
    usuario_id: int
    contenido_id: int
    mensaje: str
    titulo: str
    genero: str
    ano: int
    director: str
    protagonista: str
    tipo_contenido: str

    def insertar_datos(self):
        db.agregarUsuario(self.nombre, self.dni, self.email, self.telefono, self.direccion)
        self.mensaje = "Los datos se cargaron correctamente"
        self.nombre = ""
        self.email = "" 
        self.direccion = ""
        self.telefono = ""
        self.dni = ""
        

    def insertar_contenido(self):
        db.agregarUsuario(self.nombre, self.email)
        self.mensaje = "Los datos se cargaron correctamente"
        self.nombre = ""
        self.email = "" 

        
    def borrar_usuario(self):
        db.borrarUsuario(self.usuario_id)
    
    def borrar_contenido(self):
        db.borrarContenidos(self.contenido_id)
