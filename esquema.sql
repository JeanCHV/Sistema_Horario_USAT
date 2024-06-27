CREATE TABLE ambiente (
  idambiente     int(10) NOT NULL AUTO_INCREMENT comment 'Identificador auto incremental de ambiente', 
  nombre         varchar(255) NOT NULL comment 'Nombre del ambiente', 
  aforo          int(10) NOT NULL comment 'Aforo por cada ambiente', 
  estado         char(1) NOT NULL comment 'Estado de ambiente(Activo o Inactivo)', 
  idedificio     int(10) NOT NULL comment 'Identificador de referencia de la tabla edificio', 
  idambientetipo int(10) NOT NULL comment 'Identificador de referencia de la tabla ambiente_tipo', 
  PRIMARY KEY (idambiente)) comment='Contiene información sobre los diferentes ambientes disponibles en la institución, incluyendo su capacidad y estado' AUTO_INCREMENT=166;
CREATE TABLE ambiente_tipo (
  idambientetipo int(10) NOT NULL AUTO_INCREMENT comment 'Identificador auto incremental de la tabla ambiente_tipo', 
  nombre         varchar(255) NOT NULL comment 'Nombre de la tabla ambiente_tipo', 
  PRIMARY KEY (idambientetipo)) comment='Define los diferentes tipos de ambientes, como aulas y laboratorios.' AUTO_INCREMENT=3;
CREATE TABLE bitacora (
  id                   int(10) NOT NULL AUTO_INCREMENT, 
  usuario              varchar(50), 
  accion               varchar(100), 
  tabla_afectada       varchar(50), 
  registro_afectado_id int(10), 
  fecha                timestamp(19) DEFAULT CURRENT_TIMESTAMP NULL, 
  detalles             text, 
  PRIMARY KEY (id)) AUTO_INCREMENT=651;
CREATE TABLE curso (
  idcurso         int(10) NOT NULL AUTO_INCREMENT comment 'Identificador auto incremental de la tabla curso', 
  nombre          varchar(255) NOT NULL comment 'Nombre del curso', 
  cod_curso       varchar(20) NOT NULL comment 'Identificador propio de la universidad del curso', 
  creditos        int(10) NOT NULL comment 'Créditos asignados para cada curso', 
  horas_teoria    int(10) NOT NULL comment 'Horas teóricas por semana para cada curso', 
  horas_practica  int(10) NOT NULL comment 'Horas prácticas por semana para cada curso', 
  ciclo           int(10) NOT NULL comment 'Ciclo en el que se lleva la asignatura', 
  tipo_curso      tinyint(1) NOT NULL comment 'Tipo de curso (Virtual o Presencial)', 
  estado          char(1) NOT NULL comment 'Estado del curso (Activo o Inactivo)', 
  id_plan_estudio int(10) NOT NULL comment 'Identificador de referencia de la tabla plan_estudio', 
  PRIMARY KEY (idcurso)) comment='Registra los cursos ofrecidos por la institución, detallando sus características como nombre, código, créditos y horas' AUTO_INCREMENT=143;
CREATE TABLE curso_ambiente (
  idcurso    int(10) NOT NULL comment 'Identificador de referencia de la tabla curso', 
  idambiente int(10) NOT NULL comment 'Identificador de referencia de la tabla ambiente', 
  PRIMARY KEY (idcurso, 
  idambiente)) comment='Establece la relación entre los cursos y los ambientes donde se imparten';
CREATE TABLE docente_disponibilidad (
  dia                       varchar(255) NOT NULL comment 'Día de la semana', 
  hora_inicio               time(6) NOT NULL comment 'Hora de inicio de disponibilidad', 
  hora_fin                  time(6) NOT NULL comment 'Hora de fin de disponibilidad', 
  idpersona                 int(10) NOT NULL comment 'Identificador de referencia de la tabla persona', 
  id_disponibilidad_docente int(10) NOT NULL AUTO_INCREMENT, 
  PRIMARY KEY (id_disponibilidad_docente)) comment='Almacena la disponibilidad horaria de los docentes para planificar las clases' AUTO_INCREMENT=227;
CREATE TABLE edificio (
  idedificio  int(10) NOT NULL AUTO_INCREMENT comment 'Identificador auto incremental de la tabla edificio', 
  nombre      varchar(255) NOT NULL comment 'Nombre del edificio', 
  estado      char(1) NOT NULL comment 'Estado del edificio (Activo o Inactivo)', 
  abreviatura varchar(20) NOT NULL comment 'Abreviatura del nombre del edificio', 
  PRIMARY KEY (idedificio)) comment='Contiene información sobre los edificios de la institución, incluyendo su nombre, estado y abreviatura' AUTO_INCREMENT=6;
CREATE TABLE error_sql (
  idError       int(10) NOT NULL AUTO_INCREMENT comment 'Identificador auto incremental de la tabla error_sql', 
  query         text comment 'Consulta que generó el error', 
  error_message text NOT NULL comment 'Mensaje de error', 
  fecha         date NOT NULL comment 'Fecha en que se presentó el error', 
  PRIMARY KEY (idError)) comment='Registra los errores SQL ocurridos, incluyendo el mensaje de error y la fecha en que ocurrió' AUTO_INCREMENT=107;
CREATE TABLE escuela (
  id_escuela  int(10) NOT NULL AUTO_INCREMENT comment 'Identificador auto incremental de la tabla escuela', 
  nombre      varchar(255) NOT NULL comment 'Nombre de la escuela', 
  descripcion varchar(255) comment 'Descripción de la escuela', 
  estado      char(1) NOT NULL comment 'Estado de la escuela (Activo o Inactivo)', 
  id_facultad int(10) NOT NULL comment 'Identificador de referencia de la tabla facultad', 
  abreviatura varchar(10) NOT NULL comment 'Abreviatura de la escuela', 
  PRIMARY KEY (id_escuela)) comment='Registra las diferentes escuelas dentro de la institución, junto con su descripción y estado' AUTO_INCREMENT=19;
CREATE TABLE facultad (
  id_facultad int(10) NOT NULL AUTO_INCREMENT comment 'Identificador auto incremental de la tabla facultad', 
  nombre      varchar(255) NOT NULL comment 'Nombre de la facultad', 
  descripcion varchar(255) comment 'Descripción de la facultad', 
  estado      char(1) NOT NULL comment 'Estado de la facultad (Activo o Inactivo)', 
  PRIMARY KEY (id_facultad)) comment='Almacena información sobre las facultades, describiendo cada una y su estado' AUTO_INCREMENT=6;
CREATE TABLE grupo (
  id_grupo   int(10) NOT NULL AUTO_INCREMENT comment 'Identificador auto incremental de la tabla grupo', 
  nombre     char(1) NOT NULL comment 'Nombre del grupo', 
  vacantes   int(10) NOT NULL comment 'Vacantes disponibles en el grupo', 
  idcurso    int(10) NOT NULL comment 'Identificador de referencia de la tabla curso', 
  idsemestre int(10) NOT NULL comment 'Identificador de referencia de la tabla semestre_academico', 
  PRIMARY KEY (id_grupo)) comment='Registra los grupos de estudio, incluyendo su nombre, vacantes disponibles y curso asociado' AUTO_INCREMENT=298;
CREATE TABLE grupo_docente (
  idgrupo   int(10) NOT NULL, 
  idpersona int(10) NOT NULL, 
  PRIMARY KEY (idgrupo, 
  idpersona)) comment='Asocia a los docentes con los grupos que enseñan, permitiendo gestionar quién enseña qué curso y grupo';
CREATE TABLE horario (
  idhorario    int(10) NOT NULL AUTO_INCREMENT comment 'Identificador auto incremental de la tabla horario', 
  idambiente   int(10) NOT NULL comment 'Identificador de referencia de la tabla ambiente', 
  dia          varchar(255) NOT NULL comment 'Día de la semana', 
  horainicio   time(6) NOT NULL comment 'Hora de inicio del horario', 
  horafin      time(6) NOT NULL comment 'Hora de fin del horario', 
  h_virtual    tinyint(1) NOT NULL comment 'Horas virtuales del horario', 
  h_presencial tinyint(1) NOT NULL comment 'Horas presenciales del horario', 
  idpersona    int(10) NOT NULL comment 'Identificador de referencia de la tabla persona', 
  id_grupo     int(10) NOT NULL comment 'Identificador de referencia de la tabla grupo', 
  PRIMARY KEY (idhorario)) comment='Registra los horarios de los cursos, detallando el día, hora, ambiente y grupo asignado' AUTO_INCREMENT=29;
CREATE TABLE incidencia (
  idincidencia int(10) NOT NULL AUTO_INCREMENT comment 'Identificador auto incremental de la tabla incidencia', 
  descripcion  varchar(255) NOT NULL comment 'Descripción de la incidencia', 
  estado       bit(1) NOT NULL comment 'Estado de la incidencia', 
  idError      int(10) NOT NULL comment 'Identificador de referencia de la tabla error_sql', 
  idhorario    int(10) NOT NULL comment 'Identificador de referencia de la tabla horario', 
  PRIMARY KEY (idincidencia)) comment='Registra las incidencias reportadas en el sistema, incluyendo una descripción y el estado';
CREATE TABLE persona (
  idpersona   int(10) NOT NULL AUTO_INCREMENT comment 'Identificador auto incremental de la tabla persona', 
  nombres     varchar(255) NOT NULL comment 'Nombres de la persona', 
  apellidos   varchar(255) NOT NULL comment 'Apellidos de la persona', 
  n_documento varchar(11) comment 'Número de documento de identidad de la persona', 
  telefono    varchar(11) comment 'Número de teléfono de la persona', 
  correo      varchar(255) comment 'Correo electrónico de la persona', 
  tipopersona char(1) NOT NULL comment 'Tipo de persona (A: Administrador, D: Docente)', 
  cantHoras   tinyint(1) comment 'Cantidad de horas asignadas a la persona', 
  tiempo_ref  tinyint(1) comment 'Referencia de tiempo', 
  foto        varchar(255) comment 'Foto de la persona', 
  estado      tinyint(1) NOT NULL comment 'Estado de la persona (Activo o Inactivo)', 
  PRIMARY KEY (idpersona), 
  UNIQUE INDEX (n_documento)) comment='Almacena la información personal de todos los usuarios del sistema, incluyendo nombres, apellidos y contacto' AUTO_INCREMENT=59;
CREATE TABLE plan_estudio (
  id_plan_estudio int(10) NOT NULL AUTO_INCREMENT comment 'Identificador auto incremental de la tabla plan_estudio', 
  nombre          varchar(7) NOT NULL comment 'Nombre del plan de estudio', 
  estado          char(1) NOT NULL comment 'Estado del plan de estudio (Activo o Inactivo)', 
  id_escuela      int(10) NOT NULL comment 'Identificador de referencia de la tabla escuela', 
  PRIMARY KEY (id_plan_estudio)) comment='Registra los planes de estudio ofrecidos por las escuelas, detallando su nombre y estado' AUTO_INCREMENT=3;
CREATE TABLE semestre_academico (
  idsemestre  int(10) NOT NULL AUTO_INCREMENT comment 'Identificador auto incremental de la tabla semestre_academico', 
  descripcion varchar(10) NOT NULL comment 'Descripción del semestre académico', 
  estado      tinyint(1) NOT NULL comment 'Estado del semestre (Activo o Inactivo)', 
  PRIMARY KEY (idsemestre)) comment='Registra los semestres académicos, detallando su descripción y estado' AUTO_INCREMENT=6;
CREATE TABLE usuario (
  idusuario int(10) NOT NULL AUTO_INCREMENT comment 'Identificador auto incremental de la tabla usuario', 
  username  varchar(255) NOT NULL comment 'Nombre de usuario', 
  password  varchar(255) NOT NULL comment 'Contraseña de usuario', 
  estado    char(1) NOT NULL comment 'Estado del usuario (Activo o Inactivo)', 
  idpersona int(10) NOT NULL comment 'Identificador de referencia de la tabla persona', 
  token     varchar(255) comment 'Token de seguridad', 
  PRIMARY KEY (idusuario), 
  UNIQUE INDEX (username)) comment='Almacena la información de los usuarios que tienen acceso al sistema, incluyendo sus credenciales y estado' AUTO_INCREMENT=7;
create view view_docentes_activos as select `db_calidad`.`persona`.`idpersona` AS `idpersona`,`db_calidad`.`persona`.`nombres` AS `nombres`,`db_calidad`.`persona`.`apellidos` AS `apellidos`,`db_calidad`.`persona`.`n_documento` AS `n_documento`,`db_calidad`.`persona`.`telefono` AS `telefono`,`db_calidad`.`persona`.`correo` AS `correo`,`db_calidad`.`persona`.`tipopersona` AS `tipopersona`,`db_calidad`.`persona`.`cantHoras` AS `cantHoras`,`db_calidad`.`persona`.`tiempo_ref` AS `tiempo_ref`,`db_calidad`.`persona`.`foto` AS `foto`,`db_calidad`.`persona`.`estado` AS `estado` from `db_calidad`.`persona` where ((`db_calidad`.`persona`.`tipopersona` = 'D') and (`db_calidad`.`persona`.`estado` = 1));
create view vista_usuarios as select `db_calidad`.`usuario`.`idusuario` AS `idusuario`,`db_calidad`.`usuario`.`username` AS `username`,`db_calidad`.`usuario`.`estado` AS `estado`,`db_calidad`.`usuario`.`idpersona` AS `idpersona`,`db_calidad`.`usuario`.`token` AS `token` from `db_calidad`.`usuario`;
CREATE UNIQUE INDEX unique_abreviatura_curso 
  ON escuela (abreviatura);
CREATE INDEX idgrupo 
  ON grupo_docente (idgrupo);
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
ALTER TABLE curso_ambiente ADD CONSTRAINT idambiente FOREIGN KEY (idambiente) REFERENCES ambiente (idambiente) ON UPDATE Restrict ON DELETE Restrict;
ALTER TABLE curso_ambiente ADD CONSTRAINT idcurso FOREIGN KEY (idcurso) REFERENCES curso (idcurso) ON UPDATE Restrict ON DELETE Restrict;
DROP PROCEDURE IF EXISTS actualizar_grupos;
create procedure actualizar_grupos(out id_curso int, out n_grupos int, semestre_desc varchar)
BEGIN
    DECLARE i INT DEFAULT 1;
    DECLARE nombre_grupo CHAR(1);
    DECLARE grupo_existe INT;
    DECLARE id_semestre INT;

    SELECT idsemestre INTO id_semestre
    FROM semestre_academico
    WHERE descripcion = semestre_desc;

    IF id_semestre IS NULL THEN
        SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'Semestre no encontrado';
    END IF;

    WHILE i <= n_grupos DO
        SET nombre_grupo = CHAR(64 + i);
        
        SELECT COUNT(*) INTO grupo_existe
        FROM grupos
        WHERE id_curso = id_curso AND nombre_grupo = nombre_grupo AND idsemestre = id_semestre;
        
        IF grupo_existe > 0 THEN
            -- No hay acciones necesarias si el grupo ya existe.
            -- Agrega un comentario para cumplir con la sintaxis de MySQL.
            -- Puedes eliminar este comentario si lo deseas.
            SELECT 'Grupo ya existe';
        ELSE
            INSERT INTO grupos (id_curso, nombre_grupo, idsemestre) 
            VALUES (id_curso, nombre_grupo, id_semestre);
        END IF;
        
        SET i = i + 1;
    END WHILE;

    DELETE FROM grupos
    WHERE id_curso = id_curso AND idsemestre = id_semestre AND CHAR(64 + n_grupos) < nombre_grupo;

END;
DROP PROCEDURE IF EXISTS InsertarHorario;
create procedure InsertarHorario(p_aula varchar, p_curso varchar, p_dia varchar, p_docente varchar, p_grupo varchar, p_hora_fin time, p_hora_inicio time, p_tipo_curso varchar)
BEGIN
    -- Declarar variables
    DECLARE v_idambiente INT;
    DECLARE v_idpersona INT;
    DECLARE v_idgrupo INT;

    DECLARE EXIT HANDLER FOR SQLEXCEPTION
    BEGIN
        -- Manejar error: Rollback
        ROLLBACK;

        -- Insertar el error en la tabla error_sql
        INSERT INTO error_sql (query, error_message, fecha) 
        VALUES (
            CONCAT('INSERT INTO horario (idambiente, dia, horainicio, horafin, h_virtual, h_presencial, idpersona, id_grupo) VALUES (', 
                    IFNULL(v_idambiente, 'NULL'), ', ', 
                    p_dia, ', ', 
                    p_hora_inicio, ', ', 
                    p_hora_fin, ', ', 
                    IF(p_tipo_curso = 'Virtual', TIMESTAMPDIFF(MINUTE, p_hora_inicio, p_hora_fin)/60, 0), ', ', 
                    IF(p_tipo_curso = 'Presencial', TIMESTAMPDIFF(MINUTE, p_hora_inicio, p_hora_fin)/60, 0), ', ', 
                    IFNULL(v_idpersona, 'NULL'), ', ', 
                    IFNULL(v_idgrupo, 'NULL'), ')'
            ), 
            'Error inserting data into horario table', 
            CURDATE()
        );

        -- Insertar la incidencia en la tabla incidencia
        INSERT INTO incidencia (descripcion, estado, idError) 
        VALUES (
            'Error al insertar datos en la tabla horario', 
            1, 
            (SELECT MAX(idError) FROM error_sql)
        );

        -- Retornar mensaje de error
        SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'Error inserting data into horario table';
    END;

    -- Empezar la transacción
    START TRANSACTION;

    -- Obtener el idambiente
    BEGIN
        DECLARE CONTINUE HANDLER FOR NOT FOUND 
        BEGIN
            INSERT INTO error_sql (query, error_message, fecha)
            VALUES (
                CONCAT('SELECT idambiente FROM ambiente WHERE nombre = ', p_aula), 
                'No se encontró el ambiente especificado', 
                CURDATE()
            );
            ROLLBACK;
            SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'No se encontró el ambiente especificado';
        END;
        SELECT idambiente INTO v_idambiente FROM ambiente WHERE nombre = p_aula LIMIT 1;
    END;

    -- Obtener el idpersona (docente)
    BEGIN
        DECLARE CONTINUE HANDLER FOR NOT FOUND 
        BEGIN
            INSERT INTO error_sql (query, error_message, fecha)
            VALUES (
                CONCAT('SELECT idpersona FROM persona WHERE CONCAT(nombres, apellidos) = ', p_docente), 
                'No se encontró el docente especificado', 
                CURDATE()
            );
            ROLLBACK;
            SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'No se encontró el docente especificado';
        END;
        SELECT idpersona INTO v_idpersona FROM persona WHERE CONCAT(nombres, ' ', apellidos) = p_docente LIMIT 1;
    END;

    -- Obtener el id_grupo
    BEGIN
        DECLARE CONTINUE HANDLER FOR NOT FOUND 
        BEGIN
            INSERT INTO error_sql (query, error_message, fecha)
            VALUES (
                CONCAT('SELECT grupo.id_grupo FROM grupo INNER JOIN curso ON grupo.idcurso=curso.idcurso INNER JOIN grupo_docente ON grupo.id_grupo=grupo_docente.idgrupo INNER JOIN persona ON grupo_docente.idpersona=persona.idpersona WHERE curso.nombre = ', p_curso, ' AND persona.idpersona = ', v_idpersona), 
                'No se encontró el grupo especificado', 
                CURDATE()
            );
            ROLLBACK;
            SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'No se encontró el grupo especificado';
        END;
        SELECT grupo.id_grupo INTO v_idgrupo 
        FROM grupo 
        INNER JOIN curso ON grupo.idcurso = curso.idcurso 
        INNER JOIN grupo_docente ON grupo.id_grupo = grupo_docente.idgrupo 
        INNER JOIN persona ON grupo_docente.idpersona = persona.idpersona 
        WHERE curso.nombre = p_curso AND persona.idpersona = v_idpersona
        LIMIT 1;
    END;

    -- Insertar datos en horario
    INSERT INTO horario (idambiente, dia, horainicio, horafin, h_virtual, h_presencial, idpersona, id_grupo)
    VALUES (
        v_idambiente,
        p_dia,
        p_hora_inicio,
        p_hora_fin,
        IF(p_tipo_curso = 'Virtual', TIMESTAMPDIFF(MINUTE, p_hora_inicio, p_hora_fin)/60, 0),
        IF(p_tipo_curso = 'Presencial', TIMESTAMPDIFF(MINUTE, p_hora_inicio, p_hora_fin)/60, 0),
        v_idpersona,
        v_idgrupo
    );

    -- Commit la transacción
    COMMIT;
END;
DROP PROCEDURE IF EXISTS sp_AmbienteTipo_Gestion;
create procedure sp_AmbienteTipo_Gestion(out _tipo int, out _idambientetipo int, _nombre varchar)
BEGIN
    DECLARE v_query TEXT;
    DECLARE affected_rows INT;

    DECLARE EXIT HANDLER FOR SQLEXCEPTION
    BEGIN
        GET DIAGNOSTICS CONDITION 1
        @errno = MYSQL_ERRNO, @text = MESSAGE_TEXT;
        INSERT INTO error_sql (query, error_message, fecha) VALUES (v_query, @text, CURDATE());
        RESIGNAL;
    END;

    CASE _tipo
        WHEN 0 THEN
            SET v_query = 'SELECT * FROM ambiente_tipo';
            SELECT * FROM ambiente_tipo;
        WHEN 1 THEN
            SET v_query = CONCAT('INSERT INTO ambiente_tipo(nombre) VALUES (', QUOTE(_nombre), ')');
            INSERT INTO ambiente_tipo(nombre)
            VALUES (_nombre);
        WHEN 2 THEN
            SET v_query = CONCAT('UPDATE ambiente_tipo SET nombre = ', QUOTE(_nombre), ' WHERE idambientetipo = ', _idambientetipo);
            UPDATE ambiente_tipo SET
                nombre = _nombre
            WHERE idambientetipo = _idambientetipo;
            SET affected_rows = ROW_COUNT();
            IF affected_rows = 0 THEN
                SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'No se encontró el tipo de ambiente para modificar';
            END IF;
        WHEN 3 THEN
            SET v_query = CONCAT('DELETE FROM ambiente_tipo WHERE idambientetipo = ', _idambientetipo);
            DELETE FROM ambiente_tipo WHERE idambientetipo = _idambientetipo;
            SET affected_rows = ROW_COUNT();
            IF affected_rows = 0 THEN
                SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'No se encontró el tipo de ambiente para eliminar';
            END IF;
        ELSE
            SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'Tipo de operación no válido';
    END CASE;
END;
DROP PROCEDURE IF EXISTS sp_Ambiente_Gestion;
create procedure sp_Ambiente_Gestion(out _tipo int, out _idambiente int, _nombre varchar, out _aforo int, in _estado char, out _idedificio int, out _idambientetipo int)
BEGIN
    DECLARE v_query TEXT;
    DECLARE affected_rows INT;

    DECLARE EXIT HANDLER FOR SQLEXCEPTION
    BEGIN
        GET DIAGNOSTICS CONDITION 1
        @errno = MYSQL_ERRNO, @text = MESSAGE_TEXT;
        IF v_query IS NULL THEN
            SET v_query = 'Query not set before exception';
        END IF;
        INSERT INTO error_sql (query, error_message, fecha) VALUES (v_query, @text, CURDATE());
        RESIGNAL;
    END;

    CASE _tipo
        WHEN 0 THEN
            SET v_query = 'SELECT * FROM ambiente';
            SELECT * FROM ambiente;
        WHEN 1 THEN
            SET v_query = CONCAT('INSERT INTO ambiente(nombre, aforo, estado, idedificio, idambientetipo) VALUES (', QUOTE(TRIM(_nombre)), ', ', _aforo, ', ', QUOTE(TRIM(_estado)), ', ', _idedificio, ', ', _idambientetipo, ')');
            INSERT INTO ambiente(nombre, aforo, estado, idedificio, idambientetipo) 
            VALUES (TRIM(_nombre), _aforo, TRIM(_estado), _idedificio, _idambientetipo);
        WHEN 2 THEN
            IF EXISTS (SELECT 1 FROM ambiente 
                       WHERE idambiente = _idambiente AND 
                             (nombre != TRIM(_nombre) OR 
                              aforo != _aforo OR 
                              estado != TRIM(_estado) OR 
                              idedificio != _idedificio OR 
                              idambientetipo != _idambientetipo)) THEN
                SET v_query = CONCAT('UPDATE ambiente SET nombre = ', QUOTE(TRIM(_nombre)), ', aforo = ', _aforo, ', estado = ', QUOTE(TRIM(_estado)), ', idedificio = ', _idedificio, ', idambientetipo = ', _idambientetipo, ' WHERE idambiente = ', _idambiente);
                UPDATE ambiente SET
                    nombre = TRIM(_nombre),
                    aforo = _aforo,
                    estado = TRIM(_estado),
                    idedificio = _idedificio,
                    idambientetipo = _idambientetipo
                WHERE idambiente = _idambiente;
                SET affected_rows = ROW_COUNT();
                IF affected_rows = 0 THEN
                    SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'No se encontró el ambiente para modificar';
                END IF;
            ELSE
                SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'Los datos proporcionados son iguales a los existentes. No se realizó ninguna modificación';
            END IF;
        WHEN 3 THEN
            SET v_query = CONCAT('UPDATE ambiente SET estado = 'I' WHERE idambiente = ', _idambiente);
            UPDATE ambiente SET
                estado = 'Baja'
            WHERE idambiente = _idambiente;
            SET affected_rows = ROW_COUNT();
            IF affected_rows = 0 THEN
                SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'No se encontró el ambiente para dar de baja';
            END IF;
        WHEN 4 THEN
            -- Eliminar registros relacionados en 'horario'
            SET v_query = CONCAT('DELETE FROM horario WHERE idambiente = ', _idambiente);
            DELETE FROM horario WHERE idambiente = _idambiente;
            
            -- Eliminar el ambiente
            SET v_query = CONCAT('DELETE FROM ambiente WHERE idambiente = ', _idambiente);
            DELETE FROM ambiente WHERE idambiente = _idambiente;
            SET affected_rows = ROW_COUNT();
            IF affected_rows = 0 THEN
                SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'No se encontró el ambiente para eliminar';
            END IF;
        ELSE
            SET v_query = 'Tipo de operación no válido';
            SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'Tipo de operación no válido';
    END CASE;
END;
DROP PROCEDURE IF EXISTS sp_CursosAmbiente_Gestion;
create procedure sp_CursosAmbiente_Gestion(out _tipo int, out _idcurso int, out _idambiente int)
BEGIN
    DECLARE v_query TEXT;
    DECLARE affected_rows INT;

    DECLARE EXIT HANDLER FOR SQLEXCEPTION
    BEGIN
        GET DIAGNOSTICS CONDITION 1
        @errno = MYSQL_ERRNO, @text = MESSAGE_TEXT;
        INSERT INTO error_sql (query, error_message, fecha) VALUES (v_query, @text, CURDATE());
        RESIGNAL;
    END;

    CASE _tipo
        WHEN 0 THEN
            SET v_query = 'SELECT * FROM curso_ambiente';
            SELECT * FROM curso_ambiente;
        WHEN 1 THEN
            SET v_query = CONCAT('INSERT INTO curso_ambiente(idcurso, idambiente) VALUES (', _idcurso, ', ', _idambiente, ')');
            INSERT INTO curso_ambiente(idcurso, idambiente) VALUES (_idcurso, _idambiente);
        WHEN 2 THEN
            SET v_query = CONCAT('UPDATE curso_ambiente SET idcurso = ', _idcurso, ', idambiente = ', _idambiente, ' WHERE idcurso = ', _idcurso, ' AND idambiente = ', _idambiente);
            UPDATE curso_ambiente SET idcurso = _idcurso, idambiente = _idambiente WHERE idcurso = _idcurso AND idambiente = _idambiente;
            SET affected_rows = ROW_COUNT();
            IF affected_rows = 0 THEN
                SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'No se encontró la relación curso-ambiente para modificar';
            END IF;
        WHEN 3 THEN
            SET v_query = CONCAT('DELETE FROM curso_ambiente WHERE idcurso = ', _idcurso, ' AND idambiente = ', _idambiente);
            DELETE FROM curso_ambiente WHERE idcurso = _idcurso AND idambiente = _idambiente;
            SET affected_rows = ROW_COUNT();
            IF affected_rows = 0 THEN
                SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'No se encontró la relación curso-ambiente para eliminar';
            END IF;
        ELSE
            SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'Tipo de operación no válido';
    END CASE;
END;
DROP PROCEDURE IF EXISTS sp_CursosDocente_Gestion;
create procedure sp_CursosDocente_Gestion(out _tipo int, out _idcurso int, out _idpersona int)
BEGIN
    DECLARE v_query TEXT;
    DECLARE affected_rows INT;

    DECLARE EXIT HANDLER FOR SQLEXCEPTION
    BEGIN
        GET DIAGNOSTICS CONDITION 1
        @errno = MYSQL_ERRNO, @text = MESSAGE_TEXT;
        INSERT INTO error_sql (query, error_message, fecha) VALUES (v_query, @text, CURDATE());
        RESIGNAL;
    END;

    CASE _tipo
        WHEN 0 THEN
            SET v_query = 'SELECT * FROM curso_docente';
            SELECT * FROM curso_docente;
        WHEN 1 THEN
            SET v_query = CONCAT('INSERT INTO curso_docente(idcurso, idpersona) VALUES (', _idcurso, ', ', _idpersona, ')');
            INSERT INTO curso_docente(idcurso, idpersona) VALUES (_idcurso, _idpersona);
        WHEN 2 THEN
            SET v_query = CONCAT('UPDATE curso_docente SET idpersona = ', _idpersona, ' WHERE idcurso = ', _idcurso);
            UPDATE curso_docente SET idpersona = _idpersona WHERE idcurso = _idcurso;
            SET affected_rows = ROW_COUNT();
            IF affected_rows = 0 THEN
                SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'No se encontró la relación curso-docente para modificar';
            END IF;
        WHEN 3 THEN
            SET v_query = CONCAT('DELETE FROM curso_docente WHERE idcurso = ', _idcurso, ' AND idpersona = ', _idpersona);
            DELETE FROM curso_docente WHERE idcurso = _idcurso AND idpersona = _idpersona;
            SET affected_rows = ROW_COUNT();
            IF affected_rows = 0 THEN
                SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'No se encontró la relación curso-docente para eliminar';
            END IF;
        ELSE
            SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'Tipo de operación no válido';
    END CASE;
END;
DROP PROCEDURE IF EXISTS sp_Curso_Gestion;
create procedure sp_Curso_Gestion(out _tipo int, out _idcurso int, _nombre varchar, _cod_curso varchar, out _creditos int, out _horas_teoria int, out _horas_practica int, out _ciclo int, _tipo_curso tinyint, in _estado char, out _id_plan_estudio int)
BEGIN
    DECLARE v_query TEXT;
    DECLARE affected_rows INT;

    DECLARE EXIT HANDLER FOR SQLEXCEPTION
    BEGIN
        GET DIAGNOSTICS CONDITION 1
        @errno = MYSQL_ERRNO, @text = MESSAGE_TEXT;
        INSERT INTO error_sql (query, error_message, fecha) VALUES (v_query, @text, CURDATE());
        RESIGNAL;
    END;

    CASE _tipo
        WHEN 0 THEN
            SET v_query = 'SELECT * FROM curso';
            SELECT * FROM curso;
        WHEN 1 THEN
            SET v_query = CONCAT('INSERT INTO curso(nombre, cod_curso, creditos, horas_teoria, horas_practica, ciclo, tipo_curso, estado, id_plan_estudio) VALUES (', QUOTE(_nombre), ', ', QUOTE(_cod_curso), ', ', _creditos, ', ', _horas_teoria, ', ', _horas_practica, ', ', _ciclo, ', ', _tipo_curso, ', ', QUOTE(_estado), ', ', _id_plan_estudio, ')');
            INSERT INTO curso(nombre, cod_curso, creditos, horas_teoria, horas_practica, ciclo, tipo_curso, estado, id_plan_estudio)
            VALUES (_nombre, _cod_curso, _creditos, _horas_teoria, _horas_practica, _ciclo, _tipo_curso, _estado, _id_plan_estudio);
        WHEN 2 THEN
            SET v_query = CONCAT('UPDATE curso SET nombre = ', QUOTE(_nombre), ', cod_curso = ', QUOTE(_cod_curso), ', creditos = ', _creditos, ', horas_teoria = ', _horas_teoria, ', horas_practica = ', _horas_practica, ', ciclo = ', _ciclo, ', tipo_curso = ', _tipo_curso, ', estado = ', QUOTE(_estado), ', id_plan_estudio = ', _id_plan_estudio, ' WHERE idcurso = ', _idcurso);
            UPDATE curso SET
                nombre = _nombre,
                cod_curso = _cod_curso,
                creditos = _creditos,
                horas_teoria = _horas_teoria,
                horas_practica = _horas_practica,
                ciclo = _ciclo,
                tipo_curso = _tipo_curso,
                estado = _estado,
                id_plan_estudio = _id_plan_estudio
            WHERE idcurso = _idcurso;
            SET affected_rows = ROW_COUNT();
            IF affected_rows = 0 THEN
                SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'No se encontró el curso para modificar';
            END IF;
        WHEN 3 THEN
            SET v_query = CONCAT('UPDATE curso SET estado = 'Baja' WHERE idcurso = ', _idcurso);
            UPDATE curso SET
                estado = 'Baja'
            WHERE idcurso = _idcurso;
            SET affected_rows = ROW_COUNT();
            IF affected_rows = 0 THEN
                SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'No se encontró el curso para dar de baja';
            END IF;
        WHEN 4 THEN
            SET v_query = CONCAT('DELETE FROM curso WHERE idcurso = ', _idcurso);
            DELETE FROM curso WHERE idcurso = _idcurso;
            SET affected_rows = ROW_COUNT();
            IF affected_rows = 0 THEN
                SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'No se encontró el curso para eliminar';
            END IF;
        ELSE
            SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'Tipo de operación no válido';
    END CASE;
END;
DROP PROCEDURE IF EXISTS sp_DocenteDisponibilidad_Gestion;
create procedure sp_DocenteDisponibilidad_Gestion(out _tipo int, _dia varchar, _hora_inicio time, _hora_fin time, out _idpersona int)
BEGIN
    DECLARE v_query TEXT;
    DECLARE affected_rows INT;

    DECLARE EXIT HANDLER FOR SQLEXCEPTION
    BEGIN
        GET DIAGNOSTICS CONDITION 1
        @errno = MYSQL_ERRNO, @text = MESSAGE_TEXT;
        IF v_query IS NULL THEN
            SET v_query = 'Query not set before exception';
        END IF;
        INSERT INTO error_sql (query, error_message, fecha) VALUES (v_query, @text, CURDATE());
        RESIGNAL;
    END;

    CASE _tipo
        WHEN 0 THEN
            SET v_query = 'SELECT * FROM docente_disponibilidad';
            SELECT * FROM docente_disponibilidad;
        WHEN 1 THEN
            SET v_query = CONCAT(
                'INSERT INTO docente_disponibilidad(dia, hora_inicio, hora_fin, idpersona) VALUES (', 
                QUOTE(_dia), ', ', 
                QUOTE(_hora_inicio), ', ', 
                QUOTE(_hora_fin), ', ', 
                _idpersona, ')'
            );
            INSERT INTO docente_disponibilidad(dia, hora_inicio, hora_fin, idpersona) 
            VALUES (_dia, _hora_inicio, _hora_fin, _idpersona);
        WHEN 2 THEN
            SET v_query = CONCAT(
                'UPDATE docente_disponibilidad SET hora_inicio = ', QUOTE(_hora_inicio), 
                ', hora_fin = ', QUOTE(_hora_fin), 
                ' WHERE dia = ', QUOTE(_dia), 
                ' AND idpersona = ', _idpersona
            );
            UPDATE docente_disponibilidad SET
                hora_inicio = _hora_inicio,
                hora_fin = _hora_fin
            WHERE dia = _dia
              AND idpersona = _idpersona;
            SET affected_rows = ROW_COUNT();
            IF affected_rows = 0 THEN
                SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'No se encontró la disponibilidad para modificar';
            END IF;
        WHEN 3 THEN
            SET v_query = CONCAT(
                'DELETE FROM docente_disponibilidad WHERE dia = ', QUOTE(_dia), 
                ' AND hora_inicio = ', QUOTE(_hora_inicio), 
                ' AND hora_fin = ', QUOTE(_hora_fin), 
                ' AND idpersona = ', _idpersona
            );
            DELETE FROM docente_disponibilidad 
            WHERE dia = _dia 
              AND hora_inicio = _hora_inicio 
              AND hora_fin = _hora_fin 
              AND idpersona = _idpersona;
            SET affected_rows = ROW_COUNT();
            IF affected_rows = 0 THEN
                SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'No se encontró la disponibilidad para eliminar';
            END IF;
        ELSE
            SET v_query = 'Tipo de operación no válido';
            SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'Tipo de operación no válido';
    END CASE;
END;
DROP PROCEDURE IF EXISTS sp_Edificio_Gestion;
create procedure sp_Edificio_Gestion(out _tipo int, out _idedificio int, _nombre varchar, in _estado char)
BEGIN
    DECLARE v_query TEXT;
    DECLARE affected_rows INT;

    DECLARE EXIT HANDLER FOR SQLEXCEPTION
    BEGIN
        GET DIAGNOSTICS CONDITION 1
        @errno = MYSQL_ERRNO, @text = MESSAGE_TEXT;
        INSERT INTO error_sql (query, error_message, fecha) VALUES (v_query, @text, CURDATE());
        RESIGNAL;
    END;

    CASE _tipo
        WHEN 0 THEN
            SET v_query = 'SELECT * FROM edificio';
            SELECT * FROM edificio;
        WHEN 1 THEN
            SET v_query = CONCAT('INSERT INTO edificio(nombre, estado) VALUES (', QUOTE(_nombre), ', ', _estado, ')');
            INSERT INTO edificio(nombre, estado)
            VALUES (_nombre, _estado);
        WHEN 2 THEN
            SET v_query = CONCAT('UPDATE edificio SET nombre = ', QUOTE(_nombre), ', estado = ', _estado, ' WHERE idedificio = ', _idedificio);
            UPDATE edificio SET
                nombre = _descripcion,
                estado = _estado
            WHERE idedificio= _idedificio;
            SET affected_rows = ROW_COUNT();
            IF affected_rows = 0 THEN
                SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'No se encontró el edificio para modificar';
            END IF;
        WHEN 3 THEN
            SET v_query = CONCAT('DELETE FROM edificio WHERE idedificio = ', _idedificio);
            DELETE FROM edificio WHERE idedificio = _idedificio;
            SET affected_rows = ROW_COUNT();
            IF affected_rows = 0 THEN
                SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'No se encontró el edificio para eliminar';
            END IF;
        ELSE
            SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'Tipo de operación no válido';
    END CASE;
END;
DROP PROCEDURE IF EXISTS sp_Escuela_Gestion;
create procedure sp_Escuela_Gestion(out _tipo int, out _id_escuela int, _nombre varchar, _descripcion varchar, in _estado char, out _id_facultad int)
BEGIN
    DECLARE v_query TEXT;
    DECLARE affected_rows INT;

    DECLARE EXIT HANDLER FOR SQLEXCEPTION
    BEGIN
        GET DIAGNOSTICS CONDITION 1
        @errno = MYSQL_ERRNO, @text = MESSAGE_TEXT;
        INSERT INTO error_sql (query, error_message, fecha) VALUES (v_query, @text, CURDATE());
        RESIGNAL;
    END;

    CASE _tipo
        WHEN 0 THEN
            SET v_query = 'SELECT * FROM escuela';
            SELECT * FROM escuela;
        WHEN 1 THEN
            SET v_query = CONCAT('INSERT INTO escuela(nombre, descripcion, estado, id_facultad) VALUES (', QUOTE(_nombre), ', ', QUOTE(_descripcion), ', ', QUOTE(_estado), ', ', _id_facultad, ')');
            INSERT INTO escuela(nombre, descripcion, estado, id_facultad)
            VALUES (_nombre, _descripcion, _estado, _id_facultad);
        WHEN 2 THEN
            SET v_query = CONCAT('UPDATE escuela SET nombre = ', QUOTE(_nombre), ', descripcion = ', QUOTE(_descripcion), ', estado = ', QUOTE(_estado), ', id_facultad = ', _id_facultad, ' WHERE id_escuela = ', _id_escuela);
            UPDATE escuela SET
                nombre = _nombre,
                descripcion = _descripcion,
                estado = _estado,
                id_facultad = _id_facultad
            WHERE id_escuela = _id_escuela;
            SET affected_rows = ROW_COUNT();
            IF affected_rows = 0 THEN
                SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'No se encontró la escuela para modificar';
            END IF;
        WHEN 3 THEN
            SET v_query = CONCAT('DELETE FROM escuela WHERE id_escuela = ', _id_escuela);
            DELETE FROM escuela WHERE id_escuela = _id_escuela;
            SET affected_rows = ROW_COUNT();
            IF affected_rows = 0 THEN
                SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'No se encontró la escuela para eliminar';
            END IF;
        ELSE
            SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'Tipo de operación no válido';
    END CASE;
END;
DROP PROCEDURE IF EXISTS sp_Facultad_Gestion;
create procedure sp_Facultad_Gestion(out _tipo int, out _id_facultad int, _nombre varchar, _descripcion varchar, in _estado char)
BEGIN
    DECLARE v_query TEXT;
    DECLARE affected_rows INT;

    DECLARE EXIT HANDLER FOR SQLEXCEPTION
    BEGIN
        GET DIAGNOSTICS CONDITION 1
        @errno = MYSQL_ERRNO, @text = MESSAGE_TEXT;
        INSERT INTO error_sql (query, error_message, fecha) VALUES (v_query, @text, CURDATE());
        RESIGNAL;
    END;

    CASE _tipo
        WHEN 0 THEN
            SET v_query = 'SELECT * FROM facultad';
            SELECT * FROM facultad;
        WHEN 1 THEN
            SET v_query = CONCAT('INSERT INTO facultad(nombre, descripcion, estado) VALUES (', QUOTE(_nombre), ', ', QUOTE(_descripcion), ', ', QUOTE(_estado), ')');
            INSERT INTO facultad(nombre, descripcion, estado)
            VALUES (_nombre, _descripcion, _estado);
        WHEN 2 THEN
            SET v_query = CONCAT('UPDATE facultad SET nombre = ', QUOTE(_nombre), ', descripcion = ', QUOTE(_descripcion), ', estado = ', QUOTE(_estado), ' WHERE id_facultad = ', _id_facultad);
            UPDATE facultad SET
                nombre = _nombre,
                descripcion = _descripcion,
                estado = _estado
            WHERE id_facultad = _id_facultad;
            SET affected_rows = ROW_COUNT();
            IF affected_rows = 0 THEN
                SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'No se encontró la facultad para modificar';
            END IF;
        WHEN 3 THEN
            SET v_query = CONCAT('DELETE FROM facultad WHERE id_facultad = ', _id_facultad);
            DELETE FROM facultad WHERE id_facultad = _id_facultad;
            SET affected_rows = ROW_COUNT();
            IF affected_rows = 0 THEN
                SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'No se encontró la facultad para eliminar';
            END IF;
        ELSE
            SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'Tipo de operación no válido';
    END CASE;
END;
DROP PROCEDURE IF EXISTS sp_Grupo_Gestion;
create procedure sp_Grupo_Gestion(out _tipo int, out _id_grupo int, in _nombre char, out _vacantes int, out _idcurso int, out _idsemestre int)
BEGIN
    DECLARE v_query TEXT;
    DECLARE affected_rows INT;

    DECLARE EXIT HANDLER FOR SQLEXCEPTION
    BEGIN
        GET DIAGNOSTICS CONDITION 1
        @errno = MYSQL_ERRNO, @text = MESSAGE_TEXT;
        IF v_query IS NULL THEN
            SET v_query = 'Query not set before exception';
        END IF;
        INSERT INTO error_sql (query, error_message, fecha) VALUES (v_query, @text, CURDATE());
        RESIGNAL;
    END;

    CASE _tipo
        WHEN 0 THEN
            SET v_query = 'SELECT * FROM grupo';
            SELECT * FROM grupo;
        WHEN 1 THEN
            SET v_query = CONCAT('INSERT INTO grupo(nombre, vacantes, idcurso, idsemestre) VALUES (', QUOTE(_nombre), ', ', _vacantes, ', ', _idcurso, ', ', _idsemestre, ')');
            INSERT INTO grupo(nombre, vacantes, idcurso, idsemestre) 
            VALUES (_nombre, _vacantes, _idcurso, _idsemestre);
        WHEN 2 THEN
            SET v_query = CONCAT('UPDATE grupo SET nombre = ', QUOTE(_nombre), ', vacantes = ', _vacantes, ', idcurso = ', _idcurso, ', idsemestre = ', _idsemestre, ' WHERE id_grupo = ', _id_grupo);
            UPDATE grupo SET
                nombre = _nombre,
                vacantes = _vacantes,
                idcurso = _idcurso,
                idsemestre = _idsemestre
            WHERE id_grupo = _id_grupo;
            SET affected_rows = ROW_COUNT();
            IF affected_rows = 0 THEN
                SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'No se encontró el grupo para modificar';
            END IF;
        WHEN 3 THEN
            SET v_query = CONCAT('UPDATE grupo SET vacantes = 0 WHERE id_grupo = ', _id_grupo);
            UPDATE grupo SET
                vacantes = 0
            WHERE id_grupo = _id_grupo;
            SET affected_rows = ROW_COUNT();
            IF affected_rows = 0 THEN
                SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'No se encontró el grupo para dar de baja';
            END IF;
        WHEN 4 THEN
            SET v_query = CONCAT('DELETE FROM grupo WHERE id_grupo = ', _id_grupo);
            DELETE FROM grupo WHERE id_grupo = _id_grupo;
            SET affected_rows = ROW_COUNT();
            IF affected_rows = 0 THEN
                SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'No se encontró el grupo para eliminar';
            END IF;
        ELSE
            SET v_query = 'Tipo de operación no válido';
            SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'Tipo de operación no válido';
    END CASE;
END;
DROP PROCEDURE IF EXISTS sp_Persona_Gestion;
create procedure sp_Persona_Gestion(out _tipo int, out _idpersona int, _nombres varchar, _apellidos varchar, _n_documento varchar, _telefono varchar, _correo varchar, in _tipopersona char, _cantHoras tinyint, _tiempo_ref tinyint, _estado tinyint)
BEGIN
    DECLARE v_query TEXT;
    DECLARE affected_rows INT;

    DECLARE EXIT HANDLER FOR SQLEXCEPTION
    BEGIN
        GET DIAGNOSTICS CONDITION 1
        @errno = MYSQL_ERRNO, @text = MESSAGE_TEXT;
        INSERT INTO error_sql (query, error_message, fecha) VALUES (v_query, @text, CURDATE());
        RESIGNAL;
    END;

    CASE _tipo
        WHEN 0 THEN
            SET v_query = 'SELECT * FROM persona';
            SELECT * FROM persona;
        WHEN 1 THEN
            SET v_query = CONCAT('INSERT INTO persona(nombres, apellidos, n_documento, telefono, correo, tipopersona, cantHoras, tiempo_ref, estado) VALUES (', 
                                 QUOTE(_nombres), ', ', QUOTE(_apellidos), ', ', QUOTE(_n_documento), ', ', QUOTE(_telefono), ', ', 
                                 QUOTE(_correo), ', ', QUOTE(_tipopersona), ', ', _cantHoras, ', ', _tiempo_ref, ', ', _estado, ')');
            INSERT INTO persona(nombres, apellidos, n_documento, telefono, correo, tipopersona, cantHoras, tiempo_ref, estado)
            VALUES (_nombres, _apellidos, _n_documento, _telefono, _correo, _tipopersona, _cantHoras, _tiempo_ref, _estado);
        WHEN 2 THEN
            SET v_query = CONCAT('UPDATE persona SET nombres = ', QUOTE(_nombres), ', apellidos = ', QUOTE(_apellidos), ', n_documento = ', 
                                 QUOTE(_n_documento), ', telefono = ', QUOTE(_telefono), ', correo = ', QUOTE(_correo), ', tipopersona = ', 
                                 QUOTE(_tipopersona), ', cantHoras = ', _cantHoras, ', tiempo_ref = ', _tiempo_ref, ', estado = ', _estado, 
                                 ' WHERE idpersona = ', _idpersona);
            UPDATE persona SET
                nombres = _nombres,
                apellidos = _apellidos,
                n_documento = _n_documento,
                telefono = _telefono,
                correo = _correo,
                tipopersona = _tipopersona,
                cantHoras = _cantHoras,
                tiempo_ref = _tiempo_ref,
                estado = _estado
            WHERE idpersona = _idpersona;
            SET affected_rows = ROW_COUNT();
            IF affected_rows = 0 THEN
                SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'No se encontró la persona para modificar';
            END IF;
        WHEN 3 THEN
            SET v_query = CONCAT('DELETE FROM persona WHERE idpersona = ', _idpersona);
            DELETE FROM persona WHERE idpersona = _idpersona;
            SET affected_rows = ROW_COUNT();
            IF affected_rows = 0 THEN
                SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'No se encontró la persona para eliminar';
            END IF;
        ELSE
            SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'Tipo de operación no válido';
    END CASE;
END;
DROP PROCEDURE IF EXISTS sp_PlanEstudio_Gestion;
create procedure sp_PlanEstudio_Gestion(out _tipo int, out _id_plan_estudio int, _nombre varchar, in _estado char, out _id_escuela int)
BEGIN
    DECLARE v_query TEXT;
    DECLARE affected_rows INT;

    DECLARE EXIT HANDLER FOR SQLEXCEPTION
    BEGIN
        GET DIAGNOSTICS CONDITION 1
        @errno = MYSQL_ERRNO, @text = MESSAGE_TEXT;
        INSERT INTO error_sql (query, error_message, fecha) VALUES (v_query, @text, CURDATE());
        RESIGNAL;
    END;

    CASE _tipo
        WHEN 0 THEN
            SET v_query = 'SELECT * FROM plan_estudio';
            SELECT * FROM plan_estudio;
        WHEN 1 THEN
            SET v_query = CONCAT('INSERT INTO plan_estudio(nombre, estado, id_escuela) VALUES (', QUOTE(_nombre), ', ', QUOTE(_estado), ', ', _id_escuela, ')');
            INSERT INTO plan_estudio(nombre, estado, id_escuela)
            VALUES (_nombre, _estado, _id_escuela);
        WHEN 2 THEN
            SET v_query = CONCAT('UPDATE plan_estudio SET nombre = ', QUOTE(_nombre), ', estado = ', QUOTE(_estado), ', id_escuela = ', _id_escuela, ' WHERE id_plan_estudio = ', _id_plan_estudio);
            UPDATE plan_estudio SET
                nombre = _nombre,
                estado = _estado,
                id_escuela = _id_escuela
            WHERE id_plan_estudio = _id_plan_estudio;
            SET affected_rows = ROW_COUNT();
            IF affected_rows = 0 THEN
                SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'No se encontró el plan de estudio para modificar';
            END IF;
        WHEN 3 THEN
            SET v_query = CONCAT('DELETE FROM plan_estudio WHERE id_plan_estudio = ', _id_plan_estudio);
            DELETE FROM plan_estudio WHERE id_plan_estudio = _id_plan_estudio;
            SET affected_rows = ROW_COUNT();
            IF affected_rows = 0 THEN
                SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'No se encontró el plan de estudio para eliminar';
            END IF;
        ELSE
            SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'Tipo de operación no válido';
    END CASE;
END;
DROP PROCEDURE IF EXISTS sp_SemestreAcademico_Gestion;
create procedure sp_SemestreAcademico_Gestion(out _tipo int, out _idsemestre int, _descripcion varchar, _estado tinyint)
BEGIN
    DECLARE v_query TEXT;
    DECLARE affected_rows INT;

    DECLARE EXIT HANDLER FOR SQLEXCEPTION
    BEGIN
        GET DIAGNOSTICS CONDITION 1
        @errno = MYSQL_ERRNO, @text = MESSAGE_TEXT;
        INSERT INTO error_sql (query, error_message, fecha) VALUES (v_query, @text, CURDATE());
        RESIGNAL;
    END;

    CASE _tipo
        WHEN 0 THEN
            SET v_query = 'SELECT * FROM semestre_academico';
            SELECT * FROM semestre_academico;
        WHEN 1 THEN
            SET v_query = CONCAT('INSERT INTO semestre_academico(descripcion, estado) VALUES (', QUOTE(_descripcion), ', ', _estado, ')');
            INSERT INTO semestre_academico(descripcion, estado)
            VALUES (_descripcion, _estado);
        WHEN 2 THEN
            SET v_query = CONCAT('UPDATE semestre_academico SET descripcion = ', QUOTE(_descripcion), ', estado = ', _estado, ' WHERE idsemestre = ', _idsemestre);
            UPDATE semestre_academico SET
                descripcion = _descripcion,
                estado = _estado
            WHERE idsemestre = _idsemestre;
            SET affected_rows = ROW_COUNT();
            IF affected_rows = 0 THEN
                SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'No se encontró el semestre académico para modificar';
            END IF;
        WHEN 3 THEN
            SET v_query = CONCAT('DELETE FROM semestre_academico WHERE idsemestre = ', _idsemestre);
            DELETE FROM semestre_academico WHERE idsemestre = _idsemestre;
            SET affected_rows = ROW_COUNT();
            IF affected_rows = 0 THEN
                SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'No se encontró el semestre académico para eliminar';
            END IF;
        ELSE
            SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'Tipo de operación no válido';
    END CASE;
END;
DROP PROCEDURE IF EXISTS sp_Usuario_Gestion;
create procedure sp_Usuario_Gestion(out _tipo int, out _idusuario int, _username varchar, _password varchar, in _estado char, out _idpersona int, _token varchar)
BEGIN
    DECLARE v_query TEXT;
    DECLARE affected_rows INT;

    DECLARE EXIT HANDLER FOR SQLEXCEPTION
    BEGIN
        GET DIAGNOSTICS CONDITION 1
        @errno = MYSQL_ERRNO, @text = MESSAGE_TEXT;
        INSERT INTO error_sql (query, error_message, fecha) VALUES (v_query, @text, CURDATE());
        RESIGNAL;
    END;

    CASE _tipo
        WHEN 0 THEN
            SET v_query = 'SELECT * FROM usuario';
            SELECT * FROM usuario;
        WHEN 1 THEN
            SET v_query = CONCAT('INSERT INTO usuario(username, password, estado, idpersona, token) VALUES (', QUOTE(_username), ', ', QUOTE(SHA2(_password, 256)), ', ', QUOTE(_estado), ', ', _idpersona, ', ', QUOTE(_token), ')');
            INSERT INTO usuario(username, password, estado, idpersona, token) 
            VALUES (_username, SHA2(_password, 256), _estado, _idpersona, _token);
        WHEN 2 THEN
            SET v_query = CONCAT('UPDATE usuario SET username = ', QUOTE(_username), ', password = ', QUOTE(SHA2(_password, 256)), ', estado = ', QUOTE(_estado), ', idpersona = ', _idpersona, ', token = ', QUOTE(_token), ' WHERE idusuario = ', _idusuario);
            UPDATE usuario SET
                username = _username,
                password = SHA2(_password, 256),
                estado = _estado,
                idpersona = _idpersona,
                token = _token
            WHERE idusuario = _idusuario;
            SET affected_rows = ROW_COUNT();
            IF affected_rows = 0 THEN
                SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'No se encontró el usuario para modificar';
            END IF;
        WHEN 3 THEN
            SET v_query = CONCAT('UPDATE usuario SET estado = 'Baja' WHERE idusuario = ', _idusuario);
            UPDATE usuario SET
                estado = 'Baja'
            WHERE idusuario = _idusuario;
            SET affected_rows = ROW_COUNT();
            IF affected_rows = 0 THEN
                SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'No se encontró el usuario para dar de baja';
            END IF;
        WHEN 4 THEN
            SET v_query = CONCAT('DELETE FROM usuario WHERE idusuario = ', _idusuario);
            DELETE FROM usuario WHERE idusuario = _idusuario;
            SET affected_rows = ROW_COUNT();
            IF affected_rows = 0 THEN
                SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'No se encontró el usuario para eliminar';
            END IF;
        ELSE
            SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'Tipo de operación no válido';
    END CASE;
END;
DROP TRIGGER IF EXISTS tr_curso_insert;
CREATE TRIGGER tr_curso_insert AFTER INSERT ON curso
FOR EACH ROW
BEGIN
    INSERT INTO bitacora (usuario, accion, tabla_afectada, registro_afectado_id, detalles)
    VALUES (SESSION_USER(), 'INSERT', 'curso', NEW.idcurso, 'Se ha insertado un nuevo curso');
END;
DROP TRIGGER IF EXISTS tr_curso_update;
CREATE TRIGGER tr_curso_update AFTER UPDATE ON curso
FOR EACH ROW
BEGIN
    INSERT INTO bitacora (usuario, accion, tabla_afectada, registro_afectado_id, detalles)
    VALUES (SESSION_USER(), 'UPDATE', 'curso', NEW.idcurso, 'Se ha actualizado un curso');
END;
DROP TRIGGER IF EXISTS after_estado_update;
CREATE TRIGGER after_estado_update AFTER UPDATE ON curso
FOR EACH ROW
BEGIN
    -- Comprueba si la columna 'estado' ha cambiado
    IF NEW.estado <> OLD.estado THEN
        -- Añade la lógica para registrar el cambio en la tabla 'bitacora'
        IF NEW.estado = 'A' THEN
            INSERT INTO bitacora (usuario, accion, tabla_afectada, registro_afectado_id, fecha, detalles)
            VALUES (SESSION_USER(), 'Estado cambiado a Activo', 'curso', NEW.idcurso, NOW(), 
                    CONCAT('Estado cambiado de ', OLD.estado, ' a ', NEW.estado));
        ELSEIF NEW.estado = 'I' THEN
            INSERT INTO bitacora (usuario, accion, tabla_afectada, registro_afectado_id, fecha, detalles)
            VALUES (SESSION_USER(), 'Estado cambiado a Inactivo', 'curso', NEW.idcurso, NOW(), 
                    CONCAT('Estado cambiado de ', OLD.estado, ' a ', NEW.estado));
        END IF;
    END IF;
END;
DROP TRIGGER IF EXISTS tr_curso_delete;
CREATE TRIGGER tr_curso_delete AFTER DELETE ON curso
FOR EACH ROW
BEGIN
    INSERT INTO bitacora (usuario, accion, tabla_afectada, registro_afectado_id, detalles)
    VALUES (SESSION_USER(), 'DELETE', 'curso', OLD.idcurso, 'Se ha eliminado un curso');
END;
DROP TRIGGER IF EXISTS tr_grupo_insert;
CREATE TRIGGER tr_grupo_insert AFTER INSERT ON grupo
FOR EACH ROW
BEGIN
    INSERT INTO bitacora (usuario, accion, tabla_afectada, registro_afectado_id, detalles)
    VALUES (SESSION_USER(), 'INSERT', 'grupo', NEW.id_grupo, CONCAT('Se ha insertado un nuevo grupo. Nombre: ', NEW.nombre));
END;
DROP TRIGGER IF EXISTS tr_grupo_update;
CREATE TRIGGER tr_grupo_update AFTER UPDATE ON grupo
FOR EACH ROW
BEGIN
    INSERT INTO bitacora (usuario, accion, tabla_afectada, registro_afectado_id, detalles)
    VALUES (SESSION_USER(), 'UPDATE', 'grupo', NEW.id_grupo, CONCAT('Se ha actualizado el grupo. Nombre: ', NEW.nombre));
END;
DROP TRIGGER IF EXISTS tr_grupo_delete;
CREATE TRIGGER tr_grupo_delete AFTER DELETE ON grupo
FOR EACH ROW
BEGIN
    INSERT INTO bitacora (usuario, accion, tabla_afectada, registro_afectado_id, detalles)
    VALUES (SESSION_USER(), 'DELETE', 'grupo', OLD.id_grupo, CONCAT('Se ha eliminado el grupo. Nombre: ', OLD.nombre));
END;
DROP TRIGGER IF EXISTS tr_persona_insert;
CREATE TRIGGER tr_persona_insert AFTER INSERT ON persona
FOR EACH ROW
BEGIN
    INSERT INTO bitacora (usuario, accion, tabla_afectada, registro_afectado_id, detalles)
    VALUES (SESSION_USER(), 'INSERT', 'persona', NEW.idpersona, CONCAT('Se ha insertado una nueva persona. Nombre: ', NEW.nombres, ' ', NEW.apellidos));
END;
DROP TRIGGER IF EXISTS tr_persona_update;
CREATE TRIGGER tr_persona_update AFTER UPDATE ON persona
FOR EACH ROW
BEGIN
    INSERT INTO bitacora (usuario, accion, tabla_afectada, registro_afectado_id, detalles)
    VALUES (SESSION_USER(), 'UPDATE', 'persona', NEW.idpersona, CONCAT('Se ha actualizado la persona. Nombre: ', NEW.nombres, ' ', NEW.apellidos));
END;
DROP TRIGGER IF EXISTS tr_persona_delete;
CREATE TRIGGER tr_persona_delete AFTER DELETE ON persona
FOR EACH ROW
BEGIN
    INSERT INTO bitacora (usuario, accion, tabla_afectada, registro_afectado_id, detalles)
    VALUES (SESSION_USER(), 'DELETE', 'persona', OLD.idpersona, CONCAT('Se ha eliminado la persona. Nombre: ', OLD.nombres, ' ', OLD.apellidos));
END;
DROP TRIGGER IF EXISTS tr_ambiente_insert;
CREATE TRIGGER tr_ambiente_insert AFTER INSERT ON ambiente
FOR EACH ROW
BEGIN
    INSERT INTO bitacora (usuario, accion, tabla_afectada, registro_afectado_id, detalles)
    VALUES (SESSION_USER(), 'INSERT', 'ambiente', NEW.idambiente, CONCAT('Se ha insertado un nuevo ambiente. Nombre: ', NEW.nombre, ', Aforo: ', NEW.aforo));
END;
DROP TRIGGER IF EXISTS tr_ambiente_update;
CREATE TRIGGER tr_ambiente_update AFTER UPDATE ON ambiente
FOR EACH ROW
BEGIN
    INSERT INTO bitacora (usuario, accion, tabla_afectada, registro_afectado_id, detalles)
    VALUES (SESSION_USER(), 'UPDATE', 'ambiente', NEW.idambiente, CONCAT('Se ha actualizado el ambiente. Nombre: ', NEW.nombre, ', Aforo: ', NEW.aforo));
END;
DROP TRIGGER IF EXISTS tr_ambiente_delete;
CREATE TRIGGER tr_ambiente_delete AFTER DELETE ON ambiente
FOR EACH ROW
BEGIN
    INSERT INTO bitacora (usuario, accion, tabla_afectada, registro_afectado_id, detalles)
    VALUES (SESSION_USER(), 'DELETE', 'ambiente', OLD.idambiente, CONCAT('Se ha eliminado el ambiente. Nombre: ', OLD.nombre, ', Aforo: ', OLD.aforo));
END;
DROP TRIGGER IF EXISTS tr_docente_disponibilidad_insert;
CREATE TRIGGER tr_docente_disponibilidad_insert AFTER INSERT ON docente_disponibilidad
FOR EACH ROW
BEGIN
    INSERT INTO bitacora (usuario, accion, tabla_afectada, registro_afectado_id, detalles)
    VALUES (SESSION_USER(), 'INSERT', 'docente_disponibilidad', NEW.idpersona, CONCAT('Se ha insertado una nueva disponibilidad. Día: ', NEW.dia, ', Hora de inicio: ', NEW.hora_inicio, ', Hora de fin: ', NEW.hora_fin));
END;
DROP TRIGGER IF EXISTS tr_docente_disponibilidad_update;
CREATE TRIGGER tr_docente_disponibilidad_update AFTER UPDATE ON docente_disponibilidad
FOR EACH ROW
BEGIN
    INSERT INTO bitacora (usuario, accion, tabla_afectada, registro_afectado_id, detalles)
    VALUES (SESSION_USER(), 'UPDATE', 'docente_disponibilidad', NEW.idpersona, CONCAT('Se ha actualizado la disponibilidad. Día: ', NEW.dia, ', Hora de inicio: ', NEW.hora_inicio, ', Hora de fin: ', NEW.hora_fin));
END;
DROP TRIGGER IF EXISTS tr_docente_disponibilidad_delete;
CREATE TRIGGER tr_docente_disponibilidad_delete AFTER DELETE ON docente_disponibilidad
FOR EACH ROW
BEGIN
    INSERT INTO bitacora (usuario, accion, tabla_afectada, registro_afectado_id, detalles)
    VALUES (SESSION_USER(), 'DELETE', 'docente_disponibilidad', OLD.idpersona, CONCAT('Se ha eliminado la disponibilidad. Día: ', OLD.dia, ', Hora de inicio: ', OLD.hora_inicio, ', Hora de fin: ', OLD.hora_fin));
END;
