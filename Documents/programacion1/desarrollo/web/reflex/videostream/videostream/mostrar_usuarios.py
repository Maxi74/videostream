from .backend import *
from .database import *

def mostrar():
    usuarios = db.mostrarUsuarios()
    lista_usuarios = [
        rx.text(f"Nro. {usuario[0]}, Nombre: {usuario[1]}, Email: {usuario[3]}") for usuario in usuarios
    ]
    page = rx.center(
                rx.box(
                    rx.heading('Datos Usuarios '),
                    rx.box(
                        rx.vstack(*lista_usuarios) if usuarios else rx.text("No hay usuarios registrados."),
                        padding_top='20px'
                        ),
                    rx.box(
                        rx.vstack(
                            rx.link('Ir a menu principal',
                                    href='/'
                                    ),
                            ),
                            width='100%',
                            height='40vh',
                            padding_top = '10px',
                        ),
                ),
            ),    
    return page