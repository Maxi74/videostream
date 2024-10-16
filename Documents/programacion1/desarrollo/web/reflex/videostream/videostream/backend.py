import reflex as rx
from .database import *

db = Database()

class State(rx.State):
    nombre: str
    email: str
    usuario_id: int
    mensaje: str

    def insertar_datos(self):
        db.agregarUsuario(self.nombre, self.email)
        self.mensaje = "Los datos se cargaron correctamente"
        self.nombre = ""
        self.email = "" 

    def borrar_usuario(self):
        db.borrarUsuario(self.usuario_id)
    
