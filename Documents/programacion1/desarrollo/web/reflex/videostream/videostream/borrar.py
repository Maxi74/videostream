from .backend import *

def borrar():
    usuarios = db.mostrarUsuarios()
    lista_usuarios = [
        rx.text(f"Nro. {usuario[0]}, Nombre: {usuario[1]}, Email: {usuario[2]}") for usuario in usuarios
    ]
    page = rx.center(
        rx.vstack(
            rx.heading('Página para borrar usuarios'),
            rx.box(
                rx.vstack(*lista_usuarios) if usuarios else rx.text("No hay usuarios registrados."),
                padding_top='20px'
                ),
            rx.input(
                placeholder='Ingrese el ID del usuario a borrar', 
                on_blur=State.set_usuario_id
                ),
            rx.button('Borrar Usuario', 
                on_click=lambda: State.borrar_usuario
                ),
            rx.box(
                rx.link('Ir al menú principal', 
                    href='/',
                ),
                padding_top='20px',
            ),
        ),
        width='100%',
        height='100vh'
    )

    return page
