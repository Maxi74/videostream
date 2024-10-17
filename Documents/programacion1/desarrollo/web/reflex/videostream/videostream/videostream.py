from .backend import *
from .cargarusuario import *
from .borrarusuario import *
from .mostrar_usuarios import *
from .mostrar_contenido import *
from .usuarios import menusuarios
from .contenidos import menucontenidos
from .cargarcontenido import altacontenido
from .borrarcontenido import bajacontenido


def index():
    page = rx.center(
        rx.box(
            rx.heading('Bienvenido a VideoStream'),
            rx.divider(),
            rx.vstack(
                rx.button('Ir a Usuarios', on_click=lambda: rx.redirect("/menusuarios")),  
                rx.button('Ir a Contenidos', on_click=lambda: rx.redirect("/menucontenidos")), 
            ),
            width='70%',
            height='80vh',
            padding_top='40px',
        ),
    )
    return page

app = rx.App()
app.add_page(index, route="/")
app.add_page(menusuarios, route="/menusuarios")
app.add_page(menucontenidos, route="/menucontenidos")
app.add_page(cargarusuario, route="/cargarUsuario")
app.add_page(borrarusuario, route="/borrarusuario")
app.add_page(verusuario, route="/verusuario")
app.add_page(vercontenido, route="/vercontenido")
app.add_page(altacontenido, route="/altacontenido")
app.add_page(bajacontenido, route="/bajacontenido")