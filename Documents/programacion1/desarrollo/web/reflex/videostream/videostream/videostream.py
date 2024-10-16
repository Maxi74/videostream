from .backend import *
from .cargarusuario import *
from .borrar import *
from .mostrar_usuarios import *
from .mostrar_contenido import *


def index():
    page = rx.center(
        rx.box(
            rx.heading('Bienvenido a VideoStream'),
            rx.divider(),
            rx.box(
                rx.vstack(
                    rx.button('Ir a página de cargar usuario', on_click=lambda: rx.redirect("/cargarUsuario")),
                    rx.button('Ir a menú de borrar usuario', on_click=lambda: rx.redirect("/borrar")),
                    rx.button('Ir a menú de mostrar usuario', on_click=lambda: rx.redirect("/mostrar")),
                    rx.button('Ir a menú de mostrar contenidos', on_click=lambda: rx.redirect("/mcontenido")),
                ),
                width='70%',
                height='80vh',
                padding_top='40px',
            ),
        ),
    )
    return page

app = rx.App()
app.add_page(index, route="/")
app.add_page(cargarUsuario, route="/cargarUsuario")
app.add_page(borrar, route="/borrar")
app.add_page(mostrar, route="/mostrar")
app.add_page(mcontenido, route="/mcontenido")