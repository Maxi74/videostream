from .backend import *

def menucontenidos():
    page = rx.center(
        rx.box(
            rx.heading('Menú de Contenidos'),
            rx.divider(),
            rx.vstack(
                rx.button('Ir a visualización', on_click=lambda: rx.redirect("/vercontenido")),
                rx.button('Ir a altas', on_click=lambda: rx.redirect("/altacontenido")),
                rx.button('Ir a bajas', on_click=lambda: rx.redirect("/bajacontenido")),
            ),
            width='70%',
            height='80vh',
            padding_top='40px',
        ),
    )
    return page