CREATE TABLE ambiente (
  idambiente     int(10) NOT NULL AUTO_INCREMENT, 
  nombre         varchar(255) NOT NULL, 
  aforo          int(10) NOT NULL, 
  estado         char(1) NOT NULL, 
  idedificio     int(10) NOT NULL, 
  idambientetipo int(10) NOT NULL, 
  PRIMARY KEY (idambiente));
CREATE TABLE ambiente_tipo (
  idambientetipo int(10) NOT NULL AUTO_INCREMENT, 
  nombre         varchar(255) NOT NULL, 
  PRIMARY KEY (idambientetipo));
CREATE TABLE curso (
  idcurso         int(10) NOT NULL AUTO_INCREMENT, 
  nombre          varchar(255) NOT NULL, 
  cod_curso       varchar(20) NOT NULL, 
  creditos        int(10) NOT NULL, 
  horas_teoria    int(10) NOT NULL, 
  horas_practica  int(10) NOT NULL, 
  ciclo           int(10) NOT NULL, 
  tipo_curso      tinyint(1) NOT NULL, 
  estado          char(1) NOT NULL, 
  id_plan_estudio int(10) NOT NULL, 
  PRIMARY KEY (idcurso));
CREATE TABLE docente_disponibilidad (
  dia         varchar(255) NOT NULL, 
  hora_inicio time NOT NULL, 
  hora_fin    time NOT NULL, 
  idpersona   int(10) NOT NULL);
CREATE TABLE edificio (
  idedificio int(10) NOT NULL AUTO_INCREMENT, 
  nombre     varchar(255) NOT NULL, 
  estado     char(1) NOT NULL, 
  PRIMARY KEY (idedificio));
CREATE TABLE escuela (
  id_escuela  int(10) NOT NULL AUTO_INCREMENT, 
  nombre      varchar(255) NOT NULL, 
  descripcion varchar(255), 
  estado      char(1) NOT NULL, 
  id_facultad int(10) NOT NULL, 
  PRIMARY KEY (id_escuela));
CREATE TABLE facultad (
  id_facultad int(10) NOT NULL AUTO_INCREMENT, 
  nombre      varchar(255) NOT NULL, 
  descripcion varchar(255), 
  estado      char(1) NOT NULL, 
  PRIMARY KEY (id_facultad));
CREATE TABLE grupo (
  id_grupo int(10) NOT NULL AUTO_INCREMENT, 
  nombre   char(1) NOT NULL, 
  vacantes int(10) NOT NULL, 
  idcurso  int(10) NOT NULL, 
  PRIMARY KEY (id_grupo));
CREATE TABLE horario (
  idhorario    int(10) NOT NULL AUTO_INCREMENT, 
  idambiente   int(10) NOT NULL, 
  dia          varchar(255) NOT NULL, 
  horainicio   time NOT NULL, 
  horafin      time NOT NULL, 
  h_virtual    tinyint(1) NOT NULL, 
  h_presencial tinyint(1) NOT NULL, 
  idsemestre   int(10) NOT NULL, 
  idpersona    int(10) NOT NULL, 
  id_grupo     int(10) NOT NULL, 
  PRIMARY KEY (idhorario));
CREATE TABLE persona (
  idpersona   int(10) NOT NULL AUTO_INCREMENT, 
  nombres     varchar(255) NOT NULL, 
  apellidos   varchar(255) NOT NULL, 
  n_documento varchar(11) NOT NULL UNIQUE, 
  telefono    varchar(11) NOT NULL, 
  correo      varchar(255) NOT NULL, 
  tipopersona char(1) NOT NULL, 
  cantHoras   tinyint(1) NOT NULL, 
  tiempo_ref  tinyint(1) NOT NULL, 
  PRIMARY KEY (idpersona));
CREATE TABLE plan_estudio (
  id_plan_estudio int(10) NOT NULL AUTO_INCREMENT, 
  nombre          varchar(7) NOT NULL, 
  estado          varchar(20) NOT NULL, 
  id_escuela      int(10) NOT NULL, 
  PRIMARY KEY (id_plan_estudio));
CREATE TABLE semestre_academico (
  idsemestre  int(10) NOT NULL AUTO_INCREMENT, 
  descripcion varchar(10) NOT NULL, 
  estado      tinyint(1) NOT NULL, 
  PRIMARY KEY (idsemestre));
CREATE TABLE usuario (
  idusuario int(10) NOT NULL AUTO_INCREMENT, 
  username  varchar(255) NOT NULL UNIQUE, 
  password  varchar(255) NOT NULL, 
  estado    varchar(50) NOT NULL, 
  idpersona int(10) NOT NULL, 
  PRIMARY KEY (idusuario));
ALTER TABLE curso ADD CONSTRAINT FKcurso558317 FOREIGN KEY (id_plan_estudio) REFERENCES plan_estudio (id_plan_estudio);
ALTER TABLE ambiente ADD CONSTRAINT FKambiente610600 FOREIGN KEY (idambientetipo) REFERENCES ambiente_tipo (idambientetipo);
ALTER TABLE horario ADD CONSTRAINT fk_ambiente_horario FOREIGN KEY (idambiente) REFERENCES ambiente (idambiente);
ALTER TABLE grupo ADD CONSTRAINT fk_curso_grupo FOREIGN KEY (idcurso) REFERENCES curso (idcurso);
ALTER TABLE ambiente ADD CONSTRAINT fk_edificio_ambiente FOREIGN KEY (idedificio) REFERENCES edificio (idedificio);
ALTER TABLE plan_estudio ADD CONSTRAINT fk_escuela_plan_estudio FOREIGN KEY (id_escuela) REFERENCES escuela (id_escuela);
ALTER TABLE escuela ADD CONSTRAINT fk_facultad_escuela FOREIGN KEY (id_facultad) REFERENCES facultad (id_facultad);
ALTER TABLE horario ADD CONSTRAINT fk_grupo_horario FOREIGN KEY (id_grupo) REFERENCES grupo (id_grupo);
ALTER TABLE docente_disponibilidad ADD CONSTRAINT fk_persona_docente_disponibilidad FOREIGN KEY (idpersona) REFERENCES persona (idpersona);
ALTER TABLE horario ADD CONSTRAINT fk_persona_horario FOREIGN KEY (idpersona) REFERENCES persona (idpersona);
ALTER TABLE usuario ADD CONSTRAINT fk_persona_usuario FOREIGN KEY (idpersona) REFERENCES persona (idpersona);
ALTER TABLE horario ADD CONSTRAINT fk_semestre_academico_horario FOREIGN KEY (idsemestre) REFERENCES semestre_academico (idsemestre);
