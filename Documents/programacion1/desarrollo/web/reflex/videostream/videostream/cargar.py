from .backend import *

def cargar():
    page = rx.center(
        rx.vstack(
            rx.heading('Página para cargar los datos'),
            rx.box(
                rx.text('Nombre: '),
                rx.input(
                    placeholder='Ingrese el nombre',
                    on_blur=State.set_nombre, 
                ),
                rx.text('email: '),
                rx.input(
                    placeholder='Ingrese el email',
                    on_blur=State.set_email, 
                ),
                padding_top='20px'
                ),
            rx.button('Cargar', on_click=lambda: State.insertar_datos
                ),
            rx.text(State.mensaje, color="green"),
            rx.box(
                rx.link('Ir a menú principal', href='/'),
                padding_top='20px',
                ),
            ),
        width='100%',
        height='100vh'
    )

    return page
