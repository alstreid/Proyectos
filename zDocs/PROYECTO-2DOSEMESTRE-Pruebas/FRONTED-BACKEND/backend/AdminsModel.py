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


class Admin:
    def __init__(self, cedula, nombre, apellido, celular,email, password,):
        self.cedula = cedula
        self.nombre = nombre
        self.apellido = apellido
        self.celular = celular
        self.email = email
        self.password = password

    def obtener_Admins():

        conn = get_connection()
        cursor = conn.cursor(cursor_factory=extras.RealDictCursor)
        cursor.execute('SELECT * FROM admins')
        admin_list = cursor.fetchall()
        cursor.close()
        conn.close()

        return admin_list
    
    def guardar_Admin(self):
        conn = get_connection()
        cursor = conn.cursor(cursor_factory=extras.RealDictCursor)
        cursor.execute('INSERT INTO admins(a_cedula, a_nombres, a_apellidos, a_celular, a_correo, a_contraseña) VALUES (%s, %s, %s, %s, %s, %s) RETURNING *' ,
                (self.cedula, self.nombre, self.apellido, self.celular, self.email,self.password))
        
        admin_created = cursor.fetchone()
        conn.commit()
        cursor = conn.close()
        conn.close()

        return admin_created 
    


    
