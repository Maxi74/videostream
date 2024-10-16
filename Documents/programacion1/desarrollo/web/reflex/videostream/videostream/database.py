import sqlite3

class Database():
    def __init__(self, db_name='videostream.db'):
        self.db_name = db_name
        self.crearTablas()

    def crearTablas(self):
        with sqlite3.connect(self.db_name) as conexion:
            cursor = conexion.cursor()
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS usuarios (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    nombre TEXT NOT NULL,
                    apellido TEXT NOT NULL,
                    dni TEXT NOT NULL,
                    email TEXT NOT NULL,
                    telefono TEXT NOT NULL,
                    direccion TEXT NOT NULL
                )
            ''')

            cursor.execute('''
                CREATE TABLE IF NOT EXISTS contenido (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    titulo TEXT NOT NULL,
                    genero TEXT NOT NULL,
                    ano INTEGER NOT NULL,
                    director TEXT NOT NULL,
                    protagonista TEXT NOT NULL,
                    tipo_contenido TEXT NOT NULL
                )
            ''')

            cursor.execute('''
                CREATE TABLE IF NOT EXISTS alquileres (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    usuario_id INTEGER NOT NULL,
                    contenido_id INTEGER NOT NULL,
                    fecha_alquiler TEXT NOT NULL,
                    fecha_devolucion TEXT NOT NULL,
                    importe REAL NOT NULL,
                    FOREIGN KEY (usuario_id) REFERENCES usuarios(id),
                    FOREIGN KEY (contenido_id) REFERENCES contenido(id)
                )
            ''')

            conexion.commit()



    def agregarUsuario(self, nombre, email):
        with sqlite3.connect(self.db_name) as conexion:
            cursor = conexion.cursor()
            cursor.execute("INSERT INTO usuarios (nombre, email) VALUES (?, ?)", (nombre, email))
            conexion.commit()

    def mostrarUsuarios(self):
        with sqlite3.connect(self.db_name) as conexion:
            cursor = conexion.cursor()
            cursor.execute("SELECT * FROM usuarios")
            return cursor.fetchall()

    def mostrarContenidos(self):
            with sqlite3.connect(self.db_name) as conexion:
                cursor = conexion.cursor()
                cursor.execute("SELECT * FROM contenido")
                return cursor.fetchall()


    def borrarUsuario(self, usuario_id):
        with sqlite3.connect(self.db_name) as conexion:
            cursor = conexion.cursor()
            cursor.execute("DELETE FROM usuarios WHERE id=?", (usuario_id,))
            conexion.commit()
