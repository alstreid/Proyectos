from flask import jsonify
from psycopg2 import connect, extras


host = 'localhost'
port = 5432
dbname = 'ProyectoAcademia'
user = 'postgres'
password = 1234


def get_connection():
    conn = connect(host=host, port=port, dbname = dbname, user=user, password=password )
    return conn 


class Cursos:
    def __init__(self, c_id, nombre, descripcion, estado,):
        self.c_id = c_id
        self.nombre = nombre
        self.descripcion = descripcion
        self.estado = estado

    def obtener_Cursos():

        conn = get_connection()
        cursor = conn.cursor(cursor_factory=extras.RealDictCursor)
        cursor.execute('SELECT * FROM cursos')
        cursos_lista = cursor.fetchall()
        cursor.close()
        conn.close()
        return cursos_lista
    
    def crear_Curso(nombre, descripcion):
        conn = get_connection()
        cursor = conn.cursor(cursor_factory=extras.RealDictCursor)
        cursor.execute('INSERT INTO cursos(c_nombre, c_descripcion, c_estado) VALUES (%s,%s,%s) RETURNING *' ,
                (nombre,descripcion, 'true'))

        curso_created = cursor.fetchone()
        conn.commit()
        cursor.close()
        conn.close()

        return curso_created
    

    def editar_Curso(nombre,descripcion,c_id):
        conn = get_connection()
        cursor = conn.cursor(cursor_factory=extras.RealDictCursor)
        cursor.execute('UPDATE cursos SET c_nombre=%s, c_descripcion=%s WHERE c_id=%s RETURNING *',
                (nombre,descripcion, c_id))

        curso_updated = cursor.fetchone()
        conn.commit()
        cursor.close()
        conn.close()

        return curso_updated
    
    def eliminar_Curso(c_id):
        conn = get_connection()
        cursor = conn.cursor(cursor_factory=extras.RealDictCursor)
        cursor.execute('DELETE FROM cursos  WHERE c_id=%s RETURNING *', (c_id,))

        cursos_deleted = cursor.fetchone()
    
        conn.commit()
        cursor.close()
        conn.close()

        return cursos_deleted
    

