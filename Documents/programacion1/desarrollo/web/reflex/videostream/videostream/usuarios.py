from .backend import *

def menusuarios():
    page = rx.center(
        rx.box(
            rx.heading('Menú de Usuarios'),
            rx.divider(),
            rx.vstack(
                rx.button('Ir a página de cargar usuario', on_click=lambda: rx.redirect("/cargarUsuario")),
                rx.button('Ir a menú de borrar usuario', on_click=lambda: rx.redirect("/borrarusuario")),
                rx.button('Ir a menú de mostrar usuario', on_click=lambda: rx.redirect("/verusuario")),
                ),
            width='70%',
            height='80vh',
            padding_top='40px',
            ),
        )
    return page