from .backend import *
from .database import *


def mcontenido():
    contenidos = db.mostrarContenidos()
    lista_contenidos = [
        rx.text(f"Nro. {contenido[0]}, Titulo: {contenido[1]}, Genero: {contenido[2]}, Año: {contenido[3]}") for contenido in contenidos
    ]
    page = rx.center(
                rx.box(
                    rx.heading('Datos Contenido '),
                    rx.box(
                        rx.vstack(*lista_contenidos) if contenidos else rx.text("No hay contenidos registrados."),
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