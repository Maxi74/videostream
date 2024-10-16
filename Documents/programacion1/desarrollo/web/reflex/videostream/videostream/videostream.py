from .backend import *
from .cargar import *
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
                        rx.link('Ir a pagina de cargas',
                            href='/cargar'
                            ),
                        rx.link('Ir a menu de borrar',
                                href='/borrar'
                            ),
                        rx.link('Ir a menu de mostrar usuario',
                                href='/mostrar'
                                ),
                        rx.link('Ir a menu de mostrar contenidos',
                                href='/mcontenido'
                                ),
                        ),
                        width='70%',
                        height='80vh',
                        padding_top = '40px',
                    ),
                ),
            ),    
    return page

app = rx.App()
app.add_page(index)
app.add_page(cargar)
app.add_page(borrar)
app.add_page(mostrar)
app.add_page(mcontenido)