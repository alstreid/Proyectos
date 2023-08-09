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


class Usuario:
    def __init__(self, cedula, nombre, apellido, celular, fecha_nacimiento ,direccion,genero,email, password,):
        self.cedula = cedula
        self.nombre = nombre
        self.apellido = apellido
        self.celular = celular
        self.fecha_nacimiento = fecha_nacimiento
        self.direccion = direccion
        self.genero = genero
        self.email = email
        self.password = password

    def obtener_Usuarios():

        conn = get_connection()
        cursor = conn.cursor(cursor_factory=extras.RealDictCursor)
        cursor.execute('SELECT * FROM participante')
        participantes_list = cursor.fetchall()
        cursor.close()

        return participantes_list
    
    def crear_Usuario(self):
        conn = get_connection()
        cursor = conn.cursor(cursor_factory=extras.RealDictCursor)
        cursor.execute('INSERT INTO participante(p_cedula, p_nombres, p_apellidos, p_celular, p_fecha_nacimiento, p_direccion,p_genero,p_correo,p_contraseña) VALUES (%s, %s, %s, %s, %s, %s,%s,%s,%s) RETURNING *' ,
                (self.cedula,self.nombre, self.apellido, self.celular, self.fecha_nacimiento, self.direccion, self.genero, self.email, self.password ))

        participante_created = cursor.fetchone()
        conn.commit()
        cursor.close()
        conn.close()

        return participante_created
    

    def editar_Usuario(self):
        conn = get_connection()
        cursor = conn.cursor(cursor_factory=extras.RealDictCursor)
        cursor.execute('UPDATE participante SET p_cedula= %s, p_nombres=%s, p_apellidos=%s, p_celular=%s, p_fecha_nacimiento=%s, p_direccion=%s, p_genero=%s, p_correo=%s, p_contraseña=%s WHERE p_cedula = %s RETURNING *',
                    (self.cedula,self.nombre, self.apellido, self.celular, self.fecha_nacimiento, self.direccion, self.genero, self.email, self.password ))

        participante_updated = cursor.fetchone()
        conn.commit()
        cursor.close()
        conn.close()

        return participante_updated
    
    def eliminar_Usuario(self):
        conn = get_connection()
        cursor = conn.cursor(cursor_factory=extras.RealDictCursor)
        cursor.execute('DELETE FROM participante WHERE p_cedula = %s RETURNING *',(self.cedula,))

        participante_deleted = cursor.fetchone()
    
        conn.commit()
        cursor.close()
        conn.close()

        return participante_deleted
    
    def login_Usuario(email, password):
        conn = get_connection()
        cur = conn.cursor(cursor_factory=extras.RealDictCursor)
        print(email, password)

        cur.execute('SELECT * FROM participante WHERE p_correo = %s and p_contraseña =%s ',(email, password,))
        login_participante = cur.fetchone()
        conn.close()
        cur.close()
        
        return login_participante

