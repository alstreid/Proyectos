CREATE TABLE admins(
a_cedula integer PRIMARY KEY NOT NULL,
a_nombres varchar(50), a_apellidos varchar(50), 
a_celular varchar(10),a_correo varchar(50), 
a_contraseña varchar(30));

CREATE TABLE participante(
p_cedula integer PRIMARY KEY NOT NULL,
p_nombres varchar(50), p_apellidos varchar(50), 
p_celular varchar(10),p_fecha_nacimiento date,
p_direccion varchar(100), p_genero boolean,
p_correo varchar(50), p_contraseña varchar(30));

CREATE TABLE profesor(
prof_id serial PRIMARY KEY NOT NULL,
prof_nombres varchar(50), prof_apellidos varchar(50), 
prof_celular varchar(10), prof_fecha_nacimiento date);

CREATE TABLE horario (
h_id serial PRIMARY KEY NOT NULL, 
h_dia varchar(15), h_hora_inicio varchar(8), hora_cierre varchar(8));

CREATE TABLE cursos(
c_id serial PRIMARY KEY NOT NULL,
c_nombre varchar(50),c_descripcion varchar(500),
c_estado boolean);

CREATE TABLE programacion(
prog_id serial PRIMARY KEY NOT NULL,
prog_fecha_inicio date, prog_fecha_fin date,
prog_duracion varchar(25), h_id integer,
prof_id integer, c_id integer,
CONSTRAINT fk_horario FOREIGN KEY (h_id)
REFERENCES horario(h_id),
CONSTRAINT fk_profesor FOREIGN KEY (prof_id)
REFERENCES profesor(prof_id),
CONSTRAINT fk_cursos FOREIGN KEY (c_id)
REFERENCES cursos(c_id));

CREATE TABLE estado_inscripcion(
ei_id serial PRIMARY KEY NOT NULL,
ei_descripcion varchar(50));

CREATE TABLE inscripcion(
i_id serial PRIMARY KEY NOT NULL,
i_fecha_inscripcion date, p_cedula integer,
ei_id integer, prog_id integer,
CONSTRAINT fk_p_cedula FOREIGN KEY (p_cedula)
REFERENCES participante(p_cedula),
CONSTRAINT fk_ei_id FOREIGN KEY (ei_id)
REFERENCES estado_inscripcion(ei_id),
CONSTRAINT fk_prog_id FOREIGN KEY (prog_id)
REFERENCES programacion(prog_id));