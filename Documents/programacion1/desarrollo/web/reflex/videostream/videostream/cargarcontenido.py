from .backend import *

def altacontenido():
    page = rx.center(
        rx.vstack(
            rx.heading('Página para cargar los datos de los contenidos'),
            rx.box(
                rx.text('Nombre: '),
                rx.input(
                    placeholder='Ingrese el nombre',
                    on_blur=State.set_nombre, 
                ),
                rx.text('DNI: '),
                rx.input(
                    placeholder='Ingrese el DNI',
                    on_blur=State.set_dni, 
                ),
                rx.text('Email: '),
                rx.input(
                    placeholder='Ingrese el email',
                    on_blur=State.set_email, 
                ),
                rx.text('Teléfono: '),
                rx.input(
                    placeholder='Ingrese el número telefónico:',
                    on_blur=State.set_telefono, 
                ),
                rx.text('Dirección: '),
                rx.input(
                    placeholder='Ingrese la dirección:',
                    on_blur=State.set_direccion, 
                ),
                padding_top='20px'
            ),
            rx.button('Cargar', on_click=lambda: State.insertar_datos()), 
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
