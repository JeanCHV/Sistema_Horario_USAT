CREATE TABLE ambiente (
  idambiente     int(10) NOT NULL AUTO_INCREMENT comment 'Identificador auto incremental de ambiente', 
  nombre         varchar(255) NOT NULL comment 'Nombre del ambiente', 
  aforo          int(10) NOT NULL comment 'Aforo por cada ambiente', 
  estado         char(1) NOT NULL comment 'Estado de ambiente(Activo o Inactivo)', 
  idedificio     int(10) NOT NULL comment 'Identificador de referencia de la tabla edificio', 
  idambientetipo int(10) NOT NULL comment 'Identificador de referencia de la tabla ambiente_tipo', 
  PRIMARY KEY (idambiente)) AUTO_INCREMENT=164;
CREATE TABLE ambiente_tipo (
  idambientetipo int(10) NOT NULL AUTO_INCREMENT comment 'Identificador auto incremental de la tabla ambiente_tipo', 
  nombre         varchar(255) NOT NULL comment 'Nombre de la tabla ambiente_tipo
', 
  PRIMARY KEY (idambientetipo)) AUTO_INCREMENT=3;
CREATE TABLE curso (
  idcurso         int(10) NOT NULL AUTO_INCREMENT comment 'Identificador auto incremental de la tabla curso', 
  nombre          varchar(255) NOT NULL comment 'nombre para la tabla curso', 
  cod_curso       varchar(20) NOT NULL comment 'Identificador Propio de la universidad de tabla curso
', 
  creditos        int(10) NOT NULL comment 'Créditos asignados para cada curso', 
  horas_teoria    int(10) NOT NULL comment 'Horas teoricas que por semana tiene cada curso', 
  horas_practica  int(10) NOT NULL comment 'Horas Pracicas que por semana tiene cada curso', 
  ciclo           int(10) NOT NULL comment 'Ciclo en el que se lleva la asignatura', 
  tipo_curso      tinyint(1) NOT NULL comment 'Tipo de cada curso (Virtual o Presencial)', 
  estado          char(1) NOT NULL comment 'El estado de cada curso( Activo= 0  o Inactivo=1)', 
  id_plan_estudio int(10) NOT NULL comment 'Identificador que se referencia de la tabla plan_estudio', 
  PRIMARY KEY (idcurso)) AUTO_INCREMENT=86;
CREATE TABLE curso_ambiente (
  idcurso    int(10) NOT NULL comment 'Identificador que referencia de la tabla curso', 
  idambiente int(10) NOT NULL comment 'Identificador que refernecia de la tabla ambiente', 
  PRIMARY KEY (idcurso, 
  idambiente));
CREATE TABLE curso_docente (
  idcurso   int(10) NOT NULL, 
  idpersona int(10) NOT NULL, 
  PRIMARY KEY (idcurso, 
  idpersona));
CREATE TABLE docente_disponibilidad (
  dia         varchar(255) NOT NULL comment 'Identificador de día por semana', 
  hora_inicio time(8) NOT NULL comment 'Hora de inicio donde tiene disponibilidad', 
  hora_fin    time(8) NOT NULL comment 'Hora de fin donde termina sus disponibilidad', 
  idpersona   int(10) NOT NULL comment 'Identificador que se referencia de la tabla persona  '),
  id_disponibilidad_docente int(10) NOT NULL AUTO_INCREMENT PRIMARY KEY
CREATE TABLE edificio (
  idedificio  int(10) NOT NULL AUTO_INCREMENT comment 'Identificador auto incremental de la tabla edificio', 
  nombre      varchar(255) NOT NULL comment 'Nombre del Edificio', 
  estado      char(1) NOT NULL comment 'Estado (Activo o Inactivo)', 
  abreviatura varchar(20) NOT NULL comment 'Abreviatura del Nombre del Edificio', 
  PRIMARY KEY (idedificio)) AUTO_INCREMENT=6;
CREATE TABLE error_sql (
  idError       int(10) NOT NULL AUTO_INCREMENT comment 'Identificador autoincremental de la tabla error', 
  query         text, 
  error_message text NOT NULL comment 'Mensaje del error', 
  fecha         date NOT NULL comment 'Fecha en que se presentó el error', 
  PRIMARY KEY (idError)) AUTO_INCREMENT=61;
CREATE TABLE escuela (
  id_escuela  int(10) NOT NULL AUTO_INCREMENT comment 'Identificador autoincremental de escuela', 
  nombre      varchar(255) NOT NULL comment 'Nombre de la tabla escuela', 
  descripcion varchar(255) comment 'Descripción de cada escuela presente', 
  estado      char(1) NOT NULL comment 'Estado de escuela (Activo o Inactivo)', 
  id_facultad int(10) NOT NULL comment 'Identificador que referencia de la tabla facultad', 
  abreviatura varchar(10) NOT NULL, 
  PRIMARY KEY (id_escuela)) AUTO_INCREMENT=19;
CREATE TABLE facultad (
  id_facultad int(10) NOT NULL AUTO_INCREMENT comment 'Identificador autoincremental de la tabla facultad', 
  nombre      varchar(255) NOT NULL comment 'Nombre de la tabla facultad', 
  descripcion varchar(255) comment 'Descripción por cada facultad', 
  estado      char(1) NOT NULL comment 'Estado de la tabla facultad (Activo o Inactivo)', 
  PRIMARY KEY (id_facultad)) AUTO_INCREMENT=6;
CREATE TABLE grupo (
  id_grupo   int(10) NOT NULL AUTO_INCREMENT comment 'Identificador autoincremental de la tabla grupo', 
  nombre     char(1) NOT NULL comment 'Nombre del Grupo', 
  vacantes   int(10) DEFAULT 15 NOT NULL comment 'Vacantes Disponibles en dicho grupo', 
  idcurso    int(10) NOT NULL comment 'Identificador que se referencia de curso', 
  idsemestre int(10) NOT NULL comment 'Identificador que se referencia de semestre', 
  PRIMARY KEY (id_grupo)) AUTO_INCREMENT=289;
CREATE TABLE horario (
  idhorario    int(10) NOT NULL AUTO_INCREMENT, 
  idambiente   int(10) NOT NULL, 
  dia          varchar(255) NOT NULL, 
  horainicio   time(8) NOT NULL, 
  horafin      time(8) NOT NULL, 
  h_virtual    tinyint(1) NOT NULL, 
  h_presencial tinyint(1) NOT NULL, 
  idpersona    int(10) NOT NULL, 
  id_grupo     int(10) NOT NULL, 
  PRIMARY KEY (idhorario)) AUTO_INCREMENT=30;
CREATE TABLE incidencia (
  idincidencia int(10) NOT NULL AUTO_INCREMENT, 
  descripcion  varchar(255) NOT NULL, 
  estado       bit(1) NOT NULL, 
  idError      int(10) NOT NULL, 
  idhorario    int(10) NOT NULL, 
  PRIMARY KEY (idincidencia));
CREATE TABLE bitacora (
    id INT AUTO_INCREMENT PRIMARY KEY,
    usuario VARCHAR(50),
    accion VARCHAR(100),
    tabla_afectada VARCHAR(50),
    registro_afectado_id INT,
    fecha TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    detalles TEXT
);
CREATE TABLE persona (
  idpersona   int(10) NOT NULL AUTO_INCREMENT comment 'Identicador autoincremental de persona', 
  nombres     varchar(255) NOT NULL comment 'Nombre de persona', 
  apellidos   varchar(255) NOT NULL comment 'Apellidos de Persona', 
  n_documento varchar(11) comment 'número de documento de identidad de la persona', 
  telefono    varchar(11) comment 'número de teléfono de persona', 
  correo      varchar(255) comment 'correo electrónico de persona', 
  tipopersona char(1) NOT NULL comment 'tipo de persona (A:Admin,D:Docente)', 
  cantHoras   tinyint(1) comment 'Horas', 
  tiempo_ref  tinyint(1), 
  foto        varchar(255) comment 'Foto de la persona', 
  estado      tinyint(1) NOT NULL comment 'Estado de la persona (Activo o Inactivo)', 
  PRIMARY KEY (idpersona), 
  UNIQUE INDEX (n_documento)) AUTO_INCREMENT=47;
CREATE TABLE plan_estudio (
  id_plan_estudio int(10) NOT NULL AUTO_INCREMENT comment 'Identificar autoincremental de plan de estudio', 
  nombre          varchar(7) NOT NULL comment 'Nombre de semestre académico', 
  estado          char(1) NOT NULL comment 'Estado de tabla plan de estudio (Actvo o Inactivo)', 
  id_escuela      int(10) NOT NULL comment 'Identificador que referencia a la escuela', 
  PRIMARY KEY (id_plan_estudio)) AUTO_INCREMENT=3;
CREATE TABLE semestre_academico (
  idsemestre  int(10) NOT NULL AUTO_INCREMENT comment 'Identificador autoincremental de la tabla semestre', 
  descripcion varchar(10) NOT NULL comment 'Descripción del semestre académico', 
  estado      tinyint(1) NOT NULL comment 'El estado de cada semestre (Activo o Inactivo)', 
  PRIMARY KEY (idsemestre)) AUTO_INCREMENT=6;
CREATE TABLE usuario (
  idusuario int(10) NOT NULL AUTO_INCREMENT comment 'Identificador autoincremental de tabla usuario', 
  username  varchar(255) NOT NULL comment 'Nombre de login de usuario', 
  password  varchar(255) NOT NULL comment 'Contraseña de usuario', 
  estado    char(1) NOT NULL comment 'Estado de usuario (Activo o Inactivo)', 
  idpersona int(10) NOT NULL comment 'Identificador autoincremental que referencia a la tabla persona', 
  token     varchar(255) comment 'Se genera por seguridad', 
  PRIMARY KEY (idusuario), 
  UNIQUE INDEX (username)) AUTO_INCREMENT=6;
CREATE UNIQUE INDEX unique_abreviatura_curso 
  ON escuela (abreviatura);
ALTER TABLE horario ADD CONSTRAINT fk_ambiente_horario FOREIGN KEY (idambiente) REFERENCES ambiente (idambiente) ON UPDATE Restrict ON DELETE Restrict;
ALTER TABLE ambiente ADD CONSTRAINT fk_ambiente_tipo_ambiente FOREIGN KEY (idambientetipo) REFERENCES ambiente_tipo (idambientetipo) ON UPDATE Restrict ON DELETE Restrict;
ALTER TABLE grupo ADD CONSTRAINT fk_curso_grupo FOREIGN KEY (idcurso) REFERENCES curso (idcurso) ON UPDATE Restrict ON DELETE Restrict;
ALTER TABLE ambiente ADD CONSTRAINT fk_edificio_ambiente FOREIGN KEY (idedificio) REFERENCES edificio (idedificio) ON UPDATE Restrict ON DELETE Restrict;
ALTER TABLE plan_estudio ADD CONSTRAINT fk_escuela_plan_estudio FOREIGN KEY (id_escuela) REFERENCES escuela (id_escuela) ON UPDATE Restrict ON DELETE Restrict;
ALTER TABLE escuela ADD CONSTRAINT fk_facultad_escuela FOREIGN KEY (id_facultad) REFERENCES facultad (id_facultad) ON UPDATE Restrict ON DELETE Restrict;
ALTER TABLE horario ADD CONSTRAINT fk_grupo_horario FOREIGN KEY (id_grupo) REFERENCES grupo (id_grupo) ON UPDATE Restrict ON DELETE Restrict;
ALTER TABLE incidencia ADD CONSTRAINT fk_horario_incidencia FOREIGN KEY (idhorario) REFERENCES horario (idhorario) ON UPDATE Restrict ON DELETE Restrict;
ALTER TABLE incidencia ADD CONSTRAINT fk_incidencia_error_sql FOREIGN KEY (idError) REFERENCES error_sql (idError) ON UPDATE Restrict ON DELETE Restrict;
ALTER TABLE docente_disponibilidad ADD CONSTRAINT fk_persona_docente_disponibilidad FOREIGN KEY (idpersona) REFERENCES persona (idpersona) ON UPDATE Restrict ON DELETE Restrict;
ALTER TABLE horario ADD CONSTRAINT fk_persona_horario FOREIGN KEY (idpersona) REFERENCES persona (idpersona) ON UPDATE Restrict ON DELETE Restrict;
ALTER TABLE usuario ADD CONSTRAINT fk_persona_usuario FOREIGN KEY (idpersona) REFERENCES persona (idpersona) ON UPDATE Restrict ON DELETE Restrict;
ALTER TABLE curso ADD CONSTRAINT fk_plan_estudio_curso FOREIGN KEY (id_plan_estudio) REFERENCES plan_estudio (id_plan_estudio) ON UPDATE Restrict ON DELETE Restrict;
ALTER TABLE grupo ADD CONSTRAINT fk_semestre_academico_grupo FOREIGN KEY (idsemestre) REFERENCES semestre_academico (idsemestre) ON UPDATE Restrict ON DELETE Restrict;
ALTER TABLE modificacion_tablas ADD CONSTRAINT fk_usuario_modificacion FOREIGN KEY (idusuario) REFERENCES usuario (idusuario) ON UPDATE Restrict ON DELETE Restrict;
ALTER TABLE curso_ambiente ADD CONSTRAINT idambiente FOREIGN KEY (idambiente) REFERENCES ambiente (idambiente) ON UPDATE Restrict ON DELETE Restrict;
ALTER TABLE curso_ambiente ADD CONSTRAINT idcurso FOREIGN KEY (idcurso) REFERENCES curso (idcurso) ON UPDATE Restrict ON DELETE Restrict;
