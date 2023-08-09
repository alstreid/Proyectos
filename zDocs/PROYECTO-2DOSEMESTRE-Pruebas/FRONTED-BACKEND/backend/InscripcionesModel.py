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


class Inscripciones:
    def __init__(self, cedula_participante,fecha_inscripcion, programacion_id, estado_inscripcion):
        self.cedula_participante = cedula_participante
        self.fecha_inscripcion = fecha_inscripcion
        self.programacion_id = programacion_id
        self.estado_inscripcion = estado_inscripcion

    def obtener_Inscripciones():

        conn = get_connection()
        cursor = conn.cursor(cursor_factory=extras.RealDictCursor)
        cursor.execute('SELECT * FROM inscripcion')
        inscripciones_list = cursor.fetchall()
        cursor.close()
        conn.commit()

        return inscripciones_list
    
    def inscripcion_programacion(prog_id):

        conn = get_connection()
        cursor = conn.cursor(cursor_factory=extras.RealDictCursor)
        cursor.execute("""SELECT i_id, p_nombres, p_apellidos, i_fecha_inscripcion, ei.ei_id, ei_descripcion, prog_id, i.p_cedula 
                            FROM inscripcion as i, participante, estado_inscripcion as ei
                            WHERE participante.p_cedula = i.p_cedula AND  i.ei_id = ei.ei_id AND  prog_id= %s""", prog_id)
        i_p_list = cursor.fetchall()
        cursor.close()
        conn.commit()

        return i_p_list
    
    def crear_Inscripcion(cedula_participante,fecha_inscripcion,programacion,estado_inscripcion):
        conn = get_connection()
        cursor = conn.cursor(cursor_factory=extras.RealDictCursor)
        cursor.execute('INSERT INTO inscripcion(p_cedula, i_fecha_inscripcion, prog_id, ei_id) VALUES(%s, %s, %s, %s) RETURNING *',
                (cedula_participante,fecha_inscripcion,programacion,estado_inscripcion,))

        inscripcion_created = cursor.fetchone()
        conn.commit()
        cursor.close()
        conn.close()

        return inscripcion_created
    

    def editar_Inscripcion(ei_id,i_id ):
        conn = get_connection()
        cursor = conn.cursor(cursor_factory=extras.RealDictCursor)
        cursor.execute('UPDATE inscripcion SET ei_id=%s WHERE i_id=%s RETURNING *',
                (ei_id,i_id ,))

        inscripciones_updated = cursor.fetchone()
        conn.commit()
        cursor.close()
        conn.close()

        return inscripciones_updated
    
    def eliminar_Inscripcion(self):
        conn = get_connection()
        cursor = conn.cursor(cursor_factory=extras.RealDictCursor)
        cursor.execute('DELETE FROM inscripcion WHERE i_id = %s RETURNING *', (self.i_id,))

        inscripciones_deleted = cursor.fetchone()

        conn.commit()
        cursor.close()
        conn.close()

        return inscripciones_deleted