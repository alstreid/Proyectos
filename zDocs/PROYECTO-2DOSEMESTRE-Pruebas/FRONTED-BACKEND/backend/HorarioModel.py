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


class Horarios:
    def __init__(self, h_id, dia, inicio, cierre,):
        self.h_id = h_id
        self.dia = dia
        self.inicio = inicio
        self.cierre = cierre

    def obtener_Horarios():

        conn = get_connection()
        cursor = conn.cursor(cursor_factory=extras.RealDictCursor)
        cursor.execute('SELECT * FROM horario')
        horario_list = cursor.fetchall()
        cursor.close()
        conn.close()

        return horario_list
    
    def crear_Horarios(self):
        conn = get_connection()
        cursor = conn.cursor(cursor_factory=extras.RealDictCursor)
        cursor.execute('INSERT INTO horario(h_dia, h_hora_inicio, h_hora_cierre) VALUES(%s, %s, %s) RETURNING h_dia',
                (self.dia,self.inicio,self.cierre))

        horario_created = cursor.fetchone()
        conn.commit()
        cursor.close()
        conn.close()

        return horario_created
    

    # def editar_Horario(self):
    #     conn = get_connection()
    #     cursor = conn.cursor(cursor_factory=extras.RealDictCursor)
    #     cursor.execute('UPDATE horario SET h_dia=%s, h_hora_inicio=%s, h_hora_cierre=%s WHERE h_id =%s RETURNING h_dia',
    #             (self.dia,self.inicio,self.cierre,self.h_id))

    #     horario_updated = cursor.fetchone()
    #     conn.commit()
    #     cursor.close()
    #     conn.close()

    #     return horario_updated
    
    def eliminar_Horario(self):
        conn = get_connection()
        cursor = conn.cursor(cursor_factory=extras.RealDictCursor)
        cursor.execute('DELETE FROM horario  WHERE h_id=%s RETURNING *' ,
                    (self.h_id))

        horario_deleted = cursor.fetchone()
        conn.commit()
        cursor.close()
        conn.close()

        return horario_deleted
    