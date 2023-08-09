from flask import jsonify
from psycopg2 import connect, extras


host = 'localhost'
port = 5432
dbname = 'ProyectoAcademia'
user = 'postgres'
password = '1234'


def get_connection():
    conn = connect(host=host, port=port, dbname = dbname, user=user, password=password )
    return conn 


class Profesor:
    def __init__(self, prof_id ,nombre, apellido, celular, fecha_nacimiento,):
        self.prof_id = prof_id
        self.nombre = nombre
        self.apellido = apellido
        self.celular = celular
        self.fecha_nacimiento = fecha_nacimiento

    def obtener_Profesores():

        conn = get_connection()
        cursor = conn.cursor(cursor_factory=extras.RealDictCursor)
        cursor.execute('SELECT * FROM profesor')
        profesor_list = cursor.fetchall()
        cursor.close()
        conn.commit()

        return profesor_list
    
    def crear_Profesor(nombres,apellidos,celular,fecha_nacimiento):
        conn = get_connection()
        cursor = conn.cursor(cursor_factory=extras.RealDictCursor)
        cursor.execute('INSERT INTO profesor(prof_nombres, prof_apellidos, prof_celular, prof_fecha_nacimiento) VALUES (%s,%s,%s,%s) RETURNING *' ,
                (nombres,apellidos,celular,fecha_nacimiento,))

        profesor_created = cursor.fetchone()
        conn.commit()
        cursor.close()
        conn.close()

        return profesor_created
    

    def editar_Profesor(nombres,apellidos,celular,prof_id):
        conn = get_connection()
        cursor = conn.cursor(cursor_factory=extras.RealDictCursor)
        cursor.execute('UPDATE profesor SET prof_nombres=%s, prof_apellidos=%s, prof_celular=%s WHERE prof_id = %s RETURNING *' ,
                        (nombres, apellidos, celular, prof_id))


        profesor_updated = cursor.fetchone()
        conn.commit()
        cursor.close()
        conn.close()

        return profesor_updated
    
    def eliminar_Profesor(prof_id):
        conn = get_connection()
        cursor = conn.cursor(cursor_factory=extras.RealDictCursor)
        cursor.execute('DELETE FROM profesor WHERE prof_id = %s RETURNING *',(prof_id,))   
        profesor_deleted = cursor.fetchone()
        conn.commit()
        cursor.close()
        conn.close()

        return profesor_deleted
    
