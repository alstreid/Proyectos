from flask import Flask, jsonify, request,render_template
from flask_cors import CORS
from psycopg2 import connect,extras
from AdminsModel import Admin
from UsuariosModel import Usuario
from ProfesoresModel import Profesor
from ProgramacionModel import Programacion 
from CursosModel import Cursos 
from HorarioModel import Horarios 
from InscripcionesModel import Inscripciones

app = Flask(__name__)
app.config.from_object(__name__)
CORS(app, resources={r'/': {'origins': '*'}})


host = 'localhost'
port = 5432
dbname = 'ProyectoAcademia'
user = 'postgres'
password = '1234'

def get_connection():
    conn = connect(host=host, port=port, dbname = dbname, user=user, password=password )
    return conn 

# @app.route('/')
# def home():
#     return "Wenas Wenas"

@app.route('/api', methods= ['GET'])
def home():
    return jsonify('Hola desde flask con vue')




# USUARIOS ADMINS

@app.route('/api/admins', methods= ['GET'])
def mostrar_admins():
    admins_list = Admin.obtener_Admins()
    
    return jsonify({'mensaje':'Lista de admins',
                    'datos': admins_list})


@app.get('/api/admins/<cedula>')
def get_admin(cedula):

    conn = get_connection()
    cur = conn.cursor(cursor_factory=extras.RealDictCursor)
    cur.execute('SELECT * FROM admins WHERE a_cedula = %s',(cedula,))
    # print(cur.execute)
    admin_new = cur.fetchone()

    return jsonify({'mensaje':'Usuario',
                    'data':admin_new})


@app.route('/api/admins', methods=['POST'])
def post_admin():
    new_data = request.get_json()
    cedula = new_data['cedula']
    nombre = new_data['nombre']
    apellido = new_data['apellido']
    celular = new_data['celular']
    correo = new_data['correo']
    contraseña = new_data['contraseña']

    admin_created = Admin(cedula, nombre, apellido, celular, correo, contraseña)
    admin_created.guardar_Admin()

    return jsonify({'mensaje':'Admin Creado',
                    'data':admin_created})




@app.put('/api/admins/<a_cedula>')
def put_admin(a_cedula):

    new_data = request.get_json()
    cedula = new_data['a_cedula']
    nombres = new_data['a_nombres']
    apellidos = new_data['a_apellidos']
    celular = new_data['a_celular']
    correo = new_data['a_correo']
    contraseña = new_data['a_contraseña']

    conn = get_connection()
    cur = conn.cursor(cursor_factory=extras.RealDictCursor)

    cur.execute('UPDATE admins SET a_cedula =%s, a_nombres=%s, a_apellidos=%s, a_celular=%s, a_correo=%s, a_contraseña=%s WHERE a_cedula = %s RETURNING *',
                (cedula, nombres,apellidos,celular,correo,contraseña, a_cedula,))
    
    admin_uptated = cur.fetchone()

    conn.commit()
    cur.close()
    conn.close()

    return jsonify({'mensaje':'Admin actualizado',
                    'data':admin_uptated})



@app.delete('/api/admins/<a_cedula>')
def delete_admin(a_cedula):

    conn = get_connection()
    cur = conn.cursor(cursor_factory=extras.RealDictCursor)
    cur.execute('DELETE FROM admins WHERE a_cedula = %s RETURNING *',(a_cedula,))

    admin_deleted = cur.fetchone()
    
    conn.commit()
    cur.close()
    conn.close()

    return jsonify({'mensaje':'Usuario Eliminado',
                    'data':admin_deleted})






# PARTICIPANTES

@app.route('/api/participantes', methods=['GET'])
def mostrar_participantes():   
    usurios_list = Usuario.obtener_Usuarios()
    
    return jsonify({'mensaje':'Lista de participantes',
                    'datos': usurios_list})
    

@app.route('/login', methods = ['POST'])
def login_participante():

    try:
        post_data = request.get_json()
        email = post_data['usuario']
        password = post_data['password']

        login_usuario = Usuario.login_Usuario(email,password)
        print (login_usuario)
        if login_usuario:
            return jsonify({'mensaje': 'Usuario Encontrado',
                            'credenciales': login_usuario })
        else:
            return jsonify({'mensaje': 'Credenciales invalidas'})
    except KeyError as e:
        return (jsonify({'mensaje': KeyError}))
 
    

@app.route('/api/participantes', methods=['POST'])
def post_participantes():
    new_data = request.get_json()
    cedula = new_data['p_cedula']
    nombres = new_data['p_nombres']
    apellidos = new_data['p_apellidos']
    celular = new_data['p_celular']
    fecha_nacimiento = new_data['p_fecha_nacimiento']
    direccion = new_data['p_direccion']
    genero = new_data['p_genero']
    correo = new_data['p_correo']
    contraseña = new_data['p_contraseña']


    participante_created = Usuario(cedula, nombres,apellidos, celular, fecha_nacimiento, direccion, genero, correo,contraseña)
    participante_created.crear_Usuario()


    return jsonify({'mensaje':'Participante Creado',
                    'datos':participante_created})

@app.put('/api/participantes/<p_cedula>')
def actualizar_participantes(p_cedula):

    new_data = request.get_json()
    cedula = new_data['p_cedula']
    nombres = new_data['p_nombres']
    apellidos = new_data['p_apellidos']
    celular = new_data['p_celular']
    fecha_nacimiento = new_data['p_fecha_nacimiento']
    direccion = new_data['p_direccion']
    genero = new_data['p_genero']
    correo = new_data['p_correo']
    contraseña = new_data['p_contraseña']

    participante_updated = Usuario(cedula, nombres ,apellidos, celular, fecha_nacimiento, direccion, genero, correo,contraseña)
    participante_updated.editar_Usuario

    return jsonify({'mensaje':'Participante actualizado',
                    'datos':participante_updated})


@app.delete('/api/participantes/<p_cedula>')
def delete_participante(p_cedula):
    participante_deleted = Usuario(p_cedula)
    participante_deleted.eliminar_Usuario()
    
    return jsonify({'mensaje':'Participante Eliminado',
                    'data':participante_deleted})








# PROFESORES

@app.get('/api/profesores')
def get_profesores():

    profesores_list = Profesor.obtener_Profesores()
    

    return jsonify({'mensaje':'Lista de profesores',
                    'datos':profesores_list})

# @app.get('/api/profesores/<prof_id>')
# def get_profesor(prof_id):


#     one_profesor = cur.fetchone()

#     return jsonify({'mensaje':'Un profesor',
#                     'data':one_profesor})


@app.post('/api/profesores')
def post_profesores():

    new_data = request.get_json()
    nombres = new_data['nombre']
    apellidos = new_data['apellido']
    celular = new_data['celular']
    fecha_nacimiento = new_data['fecha']

    profesor_created = Profesor.crear_Profesor(nombres,apellidos,celular,fecha_nacimiento)
    

    return jsonify({'mensaje':'Profesor Creado',
                    'data':profesor_created})

@app.put('/api/profesores')
def editar_profesores():

    new_data = request.get_json()
    prof_id = new_data['id']
    nombres = new_data['nombres']
    apellidos = new_data['apellido']
    celular = new_data['celular']

    
    profesor_updated = Profesor.editar_Profesor(nombres,apellidos,celular,prof_id)


    return jsonify({'mensaje':'Profesor actualizado',
                    'datos':profesor_updated})

@app.delete('/api/profesores/<prof_id>')
def delete_profesor(prof_id):

    profesor_deleted = Profesor.eliminar_Profesor(prof_id)

    return jsonify({'mensaje':'Profesoer Eliminado',
                    'data':profesor_deleted})










# CURSOS
@app.route('/api/cursos', methods = ['GET'])
def get_cursos():

    cursos_list = Cursos.obtener_Cursos()

    return jsonify({'mensaje':'Lista de cursos',
                    'datos':cursos_list})


@app.get('/api/cursos/<c_id>')
def get_curso(c_id):

    conn = get_connection()
    cur = conn.cursor(cursor_factory=extras.RealDictCursor)
    cur.execute('SELECT * FROM cursos WHERE  c_id = %s', (c_id,))

    one_curso = cur.fetchone()

    return jsonify({'mensaje':'Un curso',
                    'data':one_curso})

@app.post('/api/cursos')
def post_cursos():

    new_data = request.get_json()
    nombre = new_data['nombre']
    descripcion = new_data['descripcion']
    # estado = new_data['c_estado']
    
    curso_created = Cursos.crear_Curso(nombre, descripcion)

    return jsonify({'mensaje':'Curso creado',
                    'datos':curso_created})


@app.put('/api/cursos')
def put_cursos():

    new_data = request.get_json()
    c_id = new_data['id']
    nombre = new_data['nombre']
    descripcion = new_data['descripcion']
    # estado = new_data['c_estado']
    
    curso_updated = Cursos.editar_Curso( nombre, descripcion, c_id)

    return jsonify({'mensaje':'Curso actualizado',
                    'data':curso_updated})

@app.delete('/api/cursos/<c_id>')
def delete_cursos(c_id):

    curso_deleted = Cursos.eliminar_Curso(c_id,)

    return jsonify({'mensaje':'Curso eliminado'})










# PROGRAMACION
@app.get('/api/programacion')
def lista_programaciones():

    programacion_list = Programacion.obtener_Programaciones()

    return jsonify({'mensaje':'Lista de programaciones',
                    'datos':programacion_list})

@app.get('/api/programacion/<prog_id>')
def detalle_programacion(prog_id):

    programacion_detalle = Programacion.obtener_Programacion_Detalle(prog_id)

    return jsonify({'mensaje':'Lista de programaciones',
                    'datos':programacion_detalle})


@app.post('/api/programacion')
def crear_programacion():

    new_data = request.get_json()
    fecha_inicio = new_data['fecha_inicio']
    fecha_fin = new_data['fecha_fin']
    duracion = new_data['duracion']
    horario = new_data['horario']
    profesor = new_data['profesor']
    curso = new_data['curso']
    # curso = new_data['c_id']

    programacion_created = Programacion.crear_Programacion(fecha_inicio, fecha_fin, duracion, horario, profesor,curso)

    return jsonify({'mensaje':'Programacion creada',
                    'datos':programacion_created})




@app.put('/api/programacion')
def put_programacion():

    new_data = request.get_json()
    fecha_inicio = new_data['fecha_inicio']
    fecha_fin = new_data['fecha_fin']
    duracion = new_data['duracion']
    horario = new_data['horario']
    profesor = new_data['profesor']
    prog_id = new_data['id']

    
    programacion_updated = Programacion.editar_Programacion(fecha_inicio, fecha_fin, duracion, horario, profesor,prog_id)


    return jsonify({'mensaje':'Programacion actualizada',
                    'datos':programacion_updated})


@app.delete('/api/programacion/<prog_id>')
def delete_programacion(prog_id):
    
    programacion_deleted = Programacion.eliminar_Programacion(prog_id)

    return jsonify({'mensaje':'Curso eliminado',
                    'data':programacion_deleted})









# HORARIOS
@app.get('/api/horarios')
def get_horarios():

    horario_list = Horarios.obtener_Horarios()
   

    print(horario_list)
   

    return jsonify({'mensaje':'Horarios listados',
                    'datos': horario_list})



# @app.get('/api/horarios/<h_id>')
# def get_horario(h_id):
   
#     horario_list = Horarios()
#     horario_list.obtener_Horarios()
   
   

#     print(horario_list)

#     return jsonify({'mensaje':'Horarios en la terminal'})



@app.post('/api/admins/horarios')
def post_horarios():
    new_data = request.get_json()
    dia = new_data['h_dia']
    inicio = new_data['h_hora_inicio']
    cierre = new_data['h_hora_cierre']

    horario_created =  Horarios(dia, inicio,cierre)
    horario_created.crear_Horarios()

    return (jsonify({'mensaje': 'Horario creado',
                     'data': horario_created}))


@app.put('/api/horarios/<h_id>')
def put_horarios(h_id):
    new_data = request.get_json()
    dia = new_data['h_dia']
    inicio = new_data['h_hora_inicio']
    cierre = new_data['h_hora_cierre']
    
    horario_updated =  Horarios(h_id,dia, inicio,cierre)
    horario_updated.editar_Horario()
    return (jsonify({'mensaje': 'Horario creado',
                     'data': horario_updated}))


@app.delete('/api/horarios/<h_id>')
def delete_horarios(h_id):

    horario_deleted = Horarios(h_id)
    horario_deleted.eliminar_Horario()

    return jsonify({'mensaje':'Horario eliminado',
                    'data':horario_deleted})










# INSCRIPCION

@app.get('/api/inscripciones')
def get_inscripciones():

    inscripciones_list =  Inscripciones.obtener_Inscripciones()

    return jsonify({'mensaje':'Lista de de inscripciones de un curso',
                    'datos': inscripciones_list})

@app.get('/api/inscripciones/<prog_id>')
def curso_inscripcion(prog_id):

    inscripcion_programacion =  Inscripciones.inscripcion_programacion(prog_id)
    

    return jsonify({'mensaje':'Lista de de inscripciones de un curso',
                    'datos': inscripcion_programacion})


@app.post('/api/inscripciones')
def post_inscripciones():
    new_data = request.get_json()
    fecha_inscripcion = new_data['fecha_inscripcion']
    cedula_participante = new_data['cedula']
    estado_inscripcion = new_data['estado_inscripcion']
    programacion = new_data['prog_id']

    inscripciones_crated = Inscripciones.crear_Inscripcion(cedula_participante,fecha_inscripcion,programacion,estado_inscripcion)

    

    return jsonify({'mensaje':'Inscripción realizada',
                    'data': inscripciones_crated})


@app.put('/api/inscripciones/')
def put_inscripciones():
    new_data = request.get_json()
    ei_id = new_data['ei_id']
    i_id = new_data['id']

    inscripciones_updated = Inscripciones.editar_Inscripcion(ei_id, i_id)
  

    return jsonify({'mensaje':'Inscripción actualizada',
                    'datos': inscripciones_updated})


@app.delete('/api/inscripciones/<i_id>')
def delete_inscripciones(i_id):


    inscripciones_deleted = Inscripciones(i_id)
    inscripciones_deleted.eliminar_Inscripcion()


    return jsonify({'mensaje':'Inscripcion eliminada',
                    'data': inscripciones_deleted})






#ESTADOS INSCRIPCION

@app.get('/api/estados')
def get_estados():
    conn = get_connection()
    cursor = conn.cursor(cursor_factory=extras.RealDictCursor)
    cursor.execute('SELECT * FROM estado_inscripcion')
    estados_list =  cursor.fetchall()

    return jsonify({'mensaje':'Lista de estados',
                    'datos': estados_list})


@app.get('/api/certificado/<i_id>/<p_cedula>')
def get_certificados(i_id,p_cedula):
    conn = get_connection()
    cursor = conn.cursor(cursor_factory=extras.RealDictCursor)
    cursor.execute("""SELECT i.p_cedula, p_nombres,p_apellidos FROM inscripcion as i, participante WHERE i.p_cedula = participante.p_cedula 
                        AND prog_id = %s AND i.p_cedula = %s """,(i_id,p_cedula,))
    certificado_list =  cursor.fetchone()

    return jsonify({'mensaje':'Certificado Listado',
                    'datos': certificado_list})
    
if __name__ == '__main__':
    app.run(debug=True)