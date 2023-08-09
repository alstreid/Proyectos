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


class Programacion:
    def __init__(self, prog_id ,fecha_inicio, fecha_fin, duracion, horario_id, profesor_id , curso_id ,):
        self.prog_id = prog_id
        self.fecha_inicio = fecha_inicio
        self.fecha_fin = fecha_fin
        self.duracion = duracion
        self.horario_id = horario_id
        self.profesor_id = profesor_id
        self.curso_id = curso_id

    def obtener_Programaciones():

        conn = get_connection()
        cursor = conn.cursor(cursor_factory=extras.RealDictCursor)
        cursor.execute("""SELECT prog_id,c_nombre, c_descripcion, prog_fecha_inicio, prog_fecha_fin, prog_duracion, 
                        h_dia, h_hora_inicio, h_hora_cierre, prof_nombres, prof_apellidos
                        FROM programacion, cursos, horario, profesor WHERE programacion.c_id = cursos.c_id AND 
                        programacion.h_id = horario.h_id AND programacion.prof_id = profesor.prof_id ORDER BY prog_id """)
        programacion_list = cursor.fetchall()
        cursor.close()
        conn.close()

        return programacion_list
    
    def obtener_Programacion_Detalle(prog_id):
        conn = get_connection()
        cursor = conn.cursor(cursor_factory=extras.RealDictCursor)
        cursor.execute("""SELECT prog_id,c_nombre, c_descripcion, prog_fecha_inicio, prog_fecha_fin, prog_duracion, h_dia,
                        h_hora_inicio, h_hora_cierre, prof_nombres, prof_apellidos FROM programacion, cursos, horario, profesor
                        WHERE programacion.c_id = cursos.c_id AND programacion.h_id = horario.h_id AND programacion.prof_id = profesor.prof_id AND prog_id = %s""",
                        (prog_id,))
        programacion_detalle = cursor.fetchone()
        cursor.close()
        conn.commit()

        return programacion_detalle
    def crear_Programacion(fecha_inicio, fecha_fin, duracion, horario, profesor,curso):
        conn = get_connection()
        cursor = conn.cursor(cursor_factory=extras.RealDictCursor)
        cursor.execute('INSERT INTO programacion(prog_fecha_inicio, prog_fecha_fin, prog_duracion, h_id, prof_id,c_id) VALUES (%s,%s,%s,%s,%s,%s) RETURNING *' ,
                (fecha_inicio,fecha_fin, duracion, horario, profesor, curso))

        programacion_created = cursor.fetchone()
        conn.commit()
        cursor.close()
        conn.close()

        return programacion_created
    

    def editar_Programacion(fecha_inicio, fecha_fin, duracion, horario, profesor,prog_id):
        conn = get_connection()
        cursor = conn.cursor(cursor_factory=extras.RealDictCursor)
        cursor.execute('UPDATE programacion SET prog_fecha_inicio=%s, prog_fecha_fin =%s, prog_duracion =%s, h_id =%s, prof_id =%s WHERE prog_id =%s RETURNING *' ,
                (fecha_inicio,fecha_fin, duracion, horario, profesor, prog_id))

        programacion_updated = cursor.fetchone()
        conn.commit()
        cursor.close()
        conn.close()

        return programacion_updated
    
    def eliminar_Programacion(prog_id):
        conn = get_connection()
        cursor = conn.cursor(cursor_factory=extras.RealDictCursor)
        cursor.execute('DELETE FROM programacion WHERE prog_id = %s RETURNING *',(prog_id,))

        programacion_deleted = cursor.fetchone()
    
        conn.commit()
        cursor.close()
        conn.close()

        return programacion_deleted
    
