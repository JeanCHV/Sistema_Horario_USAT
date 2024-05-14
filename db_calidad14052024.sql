/*
 Navicat Premium Data Transfer

 Source Server         : RAILWAY SistemaHorarioUsat
 Source Server Type    : MySQL
 Source Server Version : 80400 (8.4.0)
 Source Host           : monorail.proxy.rlwy.net:40341
 Source Schema         : db_calidad

 Target Server Type    : MySQL
 Target Server Version : 80400 (8.4.0)
 File Encoding         : 65001

 Date: 14/05/2024 08:56:20
*/

SET NAMES utf8mb4;
SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
-- Table structure for ambiente
-- ----------------------------
DROP TABLE IF EXISTS `ambiente`;
CREATE TABLE `ambiente`  (
  `idambiente` int NOT NULL AUTO_INCREMENT,
  `nombre` varchar(255) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NOT NULL,
  `aforo` int NOT NULL,
  `estado` varchar(50) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NOT NULL,
  `idedificio` int NOT NULL,
  `idambientetipo` int NOT NULL,
  PRIMARY KEY (`idambiente`) USING BTREE,
  INDEX `fk_ambiente_tipo_ambiente`(`idambientetipo` ASC) USING BTREE,
  INDEX `fk_edificio_ambiente`(`idedificio` ASC) USING BTREE,
  CONSTRAINT `fk_ambiente_tipo_ambiente` FOREIGN KEY (`idambientetipo`) REFERENCES `ambiente_tipo` (`idambientetipo`) ON DELETE RESTRICT ON UPDATE RESTRICT,
  CONSTRAINT `fk_edificio_ambiente` FOREIGN KEY (`idedificio`) REFERENCES `edificio` (`idedificio`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE = InnoDB AUTO_INCREMENT = 148 CHARACTER SET = utf8mb3 COLLATE = utf8mb3_general_ci ROW_FORMAT = DYNAMIC;

-- ----------------------------
-- Records of ambiente
-- ----------------------------
INSERT INTO `ambiente` VALUES (1, 'LABORATORIO-CLÍNICO 1 - CEFO', 28, 'Activo', 5, 2);
INSERT INTO `ambiente` VALUES (2, 'LABORATORIO-CLÍNICO 2 - CEFO', 28, 'Activo', 5, 2);
INSERT INTO `ambiente` VALUES (3, 'LABORATORIO-CLÍNICO 3 - CEFO', 28, 'Activo', 5, 2);
INSERT INTO `ambiente` VALUES (4, 'LABORATORIO-CLÍNICO 4 - CEFO', 28, 'Activo', 5, 2);
INSERT INTO `ambiente` VALUES (5, 'LABORATORIO-CLÍNICO 5 - CEFO', 28, 'Activo', 5, 2);
INSERT INTO `ambiente` VALUES (6, 'LABORATORIO-ODONTOLÓGICO 1', 21, 'Activo', 5, 2);
INSERT INTO `ambiente` VALUES (7, 'LABORATORIO-ODONTOLÓGICO 2', 21, 'Activo', 5, 2);
INSERT INTO `ambiente` VALUES (8, 'AULA-02', 39, 'Activo', 4, 1);
INSERT INTO `ambiente` VALUES (9, 'AULA-03', 40, 'Activo', 4, 1);
INSERT INTO `ambiente` VALUES (10, 'AULA-04', 19, 'Activo', 4, 1);
INSERT INTO `ambiente` VALUES (11, 'AULA-DE MÚSICA 1', 12, 'Activo', 4, 1);
INSERT INTO `ambiente` VALUES (12, 'LABORATORIO-DE FÍSICA', 38, 'Activo', 4, 2);
INSERT INTO `ambiente` VALUES (13, 'LABORATORIO-DE GEOTECNIA, CAMINOS Y ENSAYOS', 46, 'Activo', 4, 2);
INSERT INTO `ambiente` VALUES (14, 'LABORATORIO-DE HIDRÁULICA', 45, 'Activo', 4, 2);
INSERT INTO `ambiente` VALUES (15, 'LABORATORIO-DE INGENIERÍA SANITARIA Y AMBIENTAL', 25, 'Activo', 4, 2);
INSERT INTO `ambiente` VALUES (16, 'LABORATORIO-DE MATERIALES', 30, 'Activo', 4, 2);
INSERT INTO `ambiente` VALUES (17, 'LABORATORIO-DE MATERIALES 2 (EX DECANA 5)', 50, 'Activo', 4, 2);
INSERT INTO `ambiente` VALUES (18, 'LABORATORIO-DE MECÁNICA DE FLUIDOS E INGENIERÍA DE MATERIALES', 18, 'Activo', 4, 2);
INSERT INTO `ambiente` VALUES (19, 'LABORATORIO-DE MEDIOS AUDIOVISUALES', 27, 'Activo', 4, 2);
INSERT INTO `ambiente` VALUES (20, 'LABORATORIO-DE PRODUCCIÓN AUDIOVISUAL', 10, 'Activo', 4, 2);
INSERT INTO `ambiente` VALUES (21, 'LABORATORIO-DE PSICOLOGÍA', 12, 'Activo', 4, 2);
INSERT INTO `ambiente` VALUES (22, 'TALLER-AULA DE DISEÑO DE PINTURA Y ESCULTURA', 20, 'Activo', 4, 1);
INSERT INTO `ambiente` VALUES (23, 'TALLER-DE DANZAS', 39, 'Activo', 4, 1);
INSERT INTO `ambiente` VALUES (24, 'TALLER-DE GASTRONOMÍA', 32, 'Activo', 4, 1);
INSERT INTO `ambiente` VALUES (25, 'TALLER-SALA DE FOTOGRAFÍA', 40, 'Activo', 4, 1);
INSERT INTO `ambiente` VALUES (26, 'TALLER-SALA DE LITIGACIÓN', 48, 'Activo', 4, 1);
INSERT INTO `ambiente` VALUES (27, 'AULA-101', 56, 'Activo', 1, 1);
INSERT INTO `ambiente` VALUES (28, 'AULA-104', 56, 'Activo', 1, 1);
INSERT INTO `ambiente` VALUES (29, 'AULA-109-A', 14, 'Activo', 1, 1);
INSERT INTO `ambiente` VALUES (30, 'AULA-109-B', 14, 'Activo', 1, 1);
INSERT INTO `ambiente` VALUES (31, 'AULA-111', 40, 'Activo', 1, 1);
INSERT INTO `ambiente` VALUES (32, 'AULA-112-A', 14, 'Activo', 1, 1);
INSERT INTO `ambiente` VALUES (33, 'AULA-112-B', 14, 'Activo', 1, 1);
INSERT INTO `ambiente` VALUES (34, 'AULA-113-A', 14, 'Activo', 1, 1);
INSERT INTO `ambiente` VALUES (35, 'AULA-113-B', 14, 'Activo', 1, 1);
INSERT INTO `ambiente` VALUES (36, 'AULA-114-A', 14, 'Activo', 1, 1);
INSERT INTO `ambiente` VALUES (37, 'AULA-114-B', 14, 'Activo', 1, 1);
INSERT INTO `ambiente` VALUES (38, 'LABORATORIO-DE AUTOMATIZACIÓN Y CONTROL', 32, 'Activo', 1, 2);
INSERT INTO `ambiente` VALUES (39, 'LABORATORIO-DE PROCESOS INDUSTRIALES', 36, 'Activo', 1, 2);
INSERT INTO `ambiente` VALUES (40, 'LABORATORIO-DE REDES DE DATOS', 28, 'Activo', 1, 2);
INSERT INTO `ambiente` VALUES (41, 'AULA-201', 48, 'Activo', 1, 1);
INSERT INTO `ambiente` VALUES (42, 'AULA-202', 48, 'Activo', 1, 1);
INSERT INTO `ambiente` VALUES (43, 'AULA-203', 48, 'Activo', 1, 1);
INSERT INTO `ambiente` VALUES (44, 'AULA-205', 48, 'Activo', 1, 1);
INSERT INTO `ambiente` VALUES (45, 'AULA-206', 48, 'Activo', 1, 1);
INSERT INTO `ambiente` VALUES (46, 'AULA-207', 48, 'Activo', 1, 1);
INSERT INTO `ambiente` VALUES (47, 'AULA-208-A', 24, 'Activo', 1, 1);
INSERT INTO `ambiente` VALUES (48, 'AULA-208-B', 24, 'Activo', 1, 1);
INSERT INTO `ambiente` VALUES (49, 'AULA-209', 42, 'Activo', 1, 1);
INSERT INTO `ambiente` VALUES (50, 'AULA-210', 48, 'Activo', 1, 1);
INSERT INTO `ambiente` VALUES (51, 'AULA-211', 39, 'Activo', 1, 1);
INSERT INTO `ambiente` VALUES (52, 'AULA-212-A', 24, 'Activo', 1, 1);
INSERT INTO `ambiente` VALUES (53, 'AULA-212-B', 24, 'Activo', 1, 1);
INSERT INTO `ambiente` VALUES (54, 'AULA-213', 42, 'Activo', 1, 1);
INSERT INTO `ambiente` VALUES (55, 'AULA-214', 42, 'Activo', 1, 1);
INSERT INTO `ambiente` VALUES (56, 'AULA-301', 40, 'Activo', 1, 1);
INSERT INTO `ambiente` VALUES (57, 'AULA-302', 46, 'Activo', 1, 1);
INSERT INTO `ambiente` VALUES (58, 'AULA-303', 44, 'Activo', 1, 1);
INSERT INTO `ambiente` VALUES (59, 'AULA-304', 39, 'Activo', 1, 1);
INSERT INTO `ambiente` VALUES (60, 'AULA-305', 48, 'Activo', 1, 1);
INSERT INTO `ambiente` VALUES (61, 'AULA-306', 48, 'Activo', 1, 1);
INSERT INTO `ambiente` VALUES (62, 'AULA-307', 46, 'Activo', 1, 1);
INSERT INTO `ambiente` VALUES (63, 'AULA-308', 48, 'Activo', 1, 1);
INSERT INTO `ambiente` VALUES (64, 'AULA-309-A', 20, 'Activo', 1, 1);
INSERT INTO `ambiente` VALUES (65, 'AULA-309-B', 20, 'Activo', 1, 1);
INSERT INTO `ambiente` VALUES (66, 'AULA-310', 40, 'Activo', 1, 1);
INSERT INTO `ambiente` VALUES (67, 'AULA-311', 39, 'Activo', 1, 1);
INSERT INTO `ambiente` VALUES (68, 'AULA-312', 42, 'Activo', 1, 1);
INSERT INTO `ambiente` VALUES (69, 'AULA-313', 39, 'Activo', 1, 1);
INSERT INTO `ambiente` VALUES (70, 'AULA-314', 39, 'Activo', 1, 1);
INSERT INTO `ambiente` VALUES (71, 'AULA-401', 46, 'Activo', 1, 1);
INSERT INTO `ambiente` VALUES (72, 'AULA-402', 44, 'Activo', 1, 1);
INSERT INTO `ambiente` VALUES (73, 'AULA-403', 46, 'Activo', 1, 1);
INSERT INTO `ambiente` VALUES (74, 'AULA-404', 46, 'Activo', 1, 1);
INSERT INTO `ambiente` VALUES (75, 'AULA-405', 48, 'Activo', 1, 1);
INSERT INTO `ambiente` VALUES (76, 'AULA-406', 48, 'Activo', 1, 1);
INSERT INTO `ambiente` VALUES (77, 'AULA-407', 48, 'Activo', 1, 1);
INSERT INTO `ambiente` VALUES (78, 'AULA-408', 48, 'Activo', 1, 1);
INSERT INTO `ambiente` VALUES (79, 'AULA-409', 48, 'Activo', 1, 1);
INSERT INTO `ambiente` VALUES (80, 'AULA-410', 48, 'Activo', 1, 1);
INSERT INTO `ambiente` VALUES (81, 'AULA-411', 39, 'Activo', 1, 1);
INSERT INTO `ambiente` VALUES (82, 'AULA-412', 48, 'Activo', 1, 1);
INSERT INTO `ambiente` VALUES (83, 'AULA-413', 46, 'Activo', 1, 1);
INSERT INTO `ambiente` VALUES (84, 'AULA-414', 48, 'Activo', 1, 1);
INSERT INTO `ambiente` VALUES (85, 'LABORATORIO DE CÓMPUTO-105', 30, 'Activo', 1, 2);
INSERT INTO `ambiente` VALUES (86, 'LABORATORIO DE CÓMPUTO-106', 30, 'Activo', 1, 2);
INSERT INTO `ambiente` VALUES (87, 'LABORATORIO DE CÓMPUTO-107', 30, 'Activo', 1, 2);
INSERT INTO `ambiente` VALUES (88, 'LABORATORIO DE CÓMPUTO-108', 30, 'Activo', 1, 2);
INSERT INTO `ambiente` VALUES (89, 'LABORATORIO DE CÓMPUTO-204', 38, 'Activo', 1, 2);
INSERT INTO `ambiente` VALUES (90, 'LABORATORIO DE CÓMPUTO-416', 38, 'Activo', 1, 2);
INSERT INTO `ambiente` VALUES (91, 'LABORATORIO DE CÓMPUTO-417', 36, 'Activo', 1, 2);
INSERT INTO `ambiente` VALUES (92, 'LABORATORIO DE CÓMPUTO-419', 25, 'Activo', 1, 2);
INSERT INTO `ambiente` VALUES (93, 'LABORATORIO-DE INGENIERÍA DE SOFTWARE 1 (EX LAB 415)', 36, 'Activo', 1, 2);
INSERT INTO `ambiente` VALUES (94, 'LABORATORIO-DE INGENIERÍA DE SOFTWARE 2 (EX LAB 418)', 36, 'Activo', 1, 2);
INSERT INTO `ambiente` VALUES (95, 'AULA-201', 28, 'Activo', 3, 1);
INSERT INTO `ambiente` VALUES (96, 'AULA-202', 28, 'Activo', 3, 1);
INSERT INTO `ambiente` VALUES (97, 'AULA-203', 48, 'Activo', 3, 1);
INSERT INTO `ambiente` VALUES (98, 'AULA-301', 28, 'Activo', 3, 1);
INSERT INTO `ambiente` VALUES (99, 'AULA-302', 28, 'Activo', 3, 1);
INSERT INTO `ambiente` VALUES (100, 'AULA-303', 48, 'Activo', 3, 1);
INSERT INTO `ambiente` VALUES (101, 'LABORATORIO-CENTRO DE SIMULACIÓN', 49, 'Activo', 2, 2);
INSERT INTO `ambiente` VALUES (102, 'LABORATORIO-DE ANATOMÍA', 46, 'Activo', 2, 2);
INSERT INTO `ambiente` VALUES (103, 'LABORATORIO-DE HISTOLOGÍA, PATOLOGÍA Y EMBRIOLOGÍA', 39, 'Activo', 2, 2);
INSERT INTO `ambiente` VALUES (104, 'LABORATORIO-DE BIOFÍSICA, FARMACOLOGÍA Y FISIOLOGÍA', 38, 'Activo', 2, 2);
INSERT INTO `ambiente` VALUES (105, 'LABORATORIO-DE BIOLOGÍA, QUÍMICA Y BIOQUÍMICA', 38, 'Activo', 2, 2);
INSERT INTO `ambiente` VALUES (106, 'LABORATORIO-DE MICROBIOLOGÍA, PARASITOLOGÍA Y GENÉTICA', 38, 'Activo', 2, 2);
INSERT INTO `ambiente` VALUES (107, 'AULA-301', 39, 'Activo', 2, 1);
INSERT INTO `ambiente` VALUES (108, 'AULA-302 (COLB)', 36, 'Activo', 2, 1);
INSERT INTO `ambiente` VALUES (109, 'AULA-303', 39, 'Activo', 2, 1);
INSERT INTO `ambiente` VALUES (110, 'AULA-304', 39, 'Activo', 2, 1);
INSERT INTO `ambiente` VALUES (111, 'AULA-305 (COLB)', 36, 'Activo', 2, 1);
INSERT INTO `ambiente` VALUES (112, 'AULA-306', 39, 'Activo', 2, 1);
INSERT INTO `ambiente` VALUES (113, 'AULA-307', 48, 'Activo', 2, 1);
INSERT INTO `ambiente` VALUES (114, 'AULA-308', 39, 'Activo', 2, 1);
INSERT INTO `ambiente` VALUES (115, 'AULA-309', 50, 'Activo', 2, 1);
INSERT INTO `ambiente` VALUES (116, 'AULA-401', 39, 'Activo', 2, 1);
INSERT INTO `ambiente` VALUES (117, 'AULA-402 (COLB)', 36, 'Activo', 2, 1);
INSERT INTO `ambiente` VALUES (118, 'AULA-403', 39, 'Activo', 2, 1);
INSERT INTO `ambiente` VALUES (119, 'AULA-404', 39, 'Activo', 2, 1);
INSERT INTO `ambiente` VALUES (120, 'AULA-405 (COLB)', 36, 'Activo', 2, 1);
INSERT INTO `ambiente` VALUES (121, 'AULA-406', 39, 'Activo', 2, 1);
INSERT INTO `ambiente` VALUES (122, 'AULA-407', 48, 'Activo', 2, 1);
INSERT INTO `ambiente` VALUES (123, 'AULA-408', 39, 'Activo', 2, 1);
INSERT INTO `ambiente` VALUES (124, 'AULA-409', 50, 'Activo', 2, 1);
INSERT INTO `ambiente` VALUES (125, 'AULA-501', 39, 'Activo', 2, 1);
INSERT INTO `ambiente` VALUES (126, 'AULA-502 (COLB)', 36, 'Activo', 2, 1);
INSERT INTO `ambiente` VALUES (127, 'AULA-503', 39, 'Activo', 2, 1);
INSERT INTO `ambiente` VALUES (128, 'AULA-504', 39, 'Activo', 2, 1);
INSERT INTO `ambiente` VALUES (129, 'AULA-505 (COLB)', 36, 'Activo', 2, 1);
INSERT INTO `ambiente` VALUES (130, 'AULA-506', 39, 'Activo', 2, 1);
INSERT INTO `ambiente` VALUES (131, 'AULA-507', 48, 'Activo', 2, 1);
INSERT INTO `ambiente` VALUES (132, 'AULA-508', 39, 'Activo', 2, 1);
INSERT INTO `ambiente` VALUES (133, 'AULA-509', 50, 'Activo', 2, 1);
INSERT INTO `ambiente` VALUES (134, 'LABORATORIO-DE CREATIVIDAD E INNOVACIÓN', 25, 'Activo', 2, 2);
INSERT INTO `ambiente` VALUES (135, 'AULA-705', 39, 'Activo', 2, 1);
INSERT INTO `ambiente` VALUES (136, 'AULA-706', 39, 'Activo', 2, 1);
INSERT INTO `ambiente` VALUES (137, 'AULA-707', 39, 'Activo', 2, 1);
INSERT INTO `ambiente` VALUES (138, 'AULA-708', 39, 'Activo', 2, 1);
INSERT INTO `ambiente` VALUES (139, 'AULA-709', 39, 'Activo', 2, 1);
INSERT INTO `ambiente` VALUES (140, 'TALLER-AULA DE DISEÑO 701', 36, 'Activo', 2, 1);
INSERT INTO `ambiente` VALUES (141, 'TALLER-AULA DE DISEÑO 702', 36, 'Activo', 2, 1);
INSERT INTO `ambiente` VALUES (142, 'TALLER-AULA DE DISEÑO 703', 33, 'Activo', 2, 1);
INSERT INTO `ambiente` VALUES (143, 'TALLER-AULA DE DISEÑO 704', 37, 'Activo', 2, 1);
INSERT INTO `ambiente` VALUES (144, 'TALLER-AULA DE DISEÑO 1-A', 38, 'Activo', 2, 1);
INSERT INTO `ambiente` VALUES (145, 'TALLER-AULA DE DISEÑO 1-B', 38, 'Activo', 2, 1);
INSERT INTO `ambiente` VALUES (146, 'TALLER-AULA DE DISEÑO 2', 36, 'Activo', 2, 1);
INSERT INTO `ambiente` VALUES (147, 'AULA PARA CACHAR', 2, 'ACTIVO', 4, 2);

-- ----------------------------
-- Table structure for ambiente_tipo
-- ----------------------------
DROP TABLE IF EXISTS `ambiente_tipo`;
CREATE TABLE `ambiente_tipo`  (
  `idambientetipo` int NOT NULL AUTO_INCREMENT,
  `nombre` varchar(255) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NOT NULL,
  PRIMARY KEY (`idambientetipo`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 3 CHARACTER SET = utf8mb3 COLLATE = utf8mb3_general_ci ROW_FORMAT = DYNAMIC;

-- ----------------------------
-- Records of ambiente_tipo
-- ----------------------------
INSERT INTO `ambiente_tipo` VALUES (1, 'Aula');
INSERT INTO `ambiente_tipo` VALUES (2, 'Laboratorio');

-- ----------------------------
-- Table structure for curso
-- ----------------------------
DROP TABLE IF EXISTS `curso`;
CREATE TABLE `curso`  (
  `idcurso` int NOT NULL AUTO_INCREMENT,
  `nombre` varchar(255) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NOT NULL,
  `cod_curso` varchar(20) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NOT NULL,
  `creditos` int NOT NULL,
  `horas_teoria` int NOT NULL,
  `horas_practica` int NOT NULL,
  `ciclo` int NOT NULL,
  `tipo_curso` tinyint(1) NOT NULL,
  `estado` varchar(20) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NOT NULL,
  `id_plan_estudio` int NOT NULL,
  PRIMARY KEY (`idcurso`) USING BTREE,
  INDEX `fk_plan_estudio_curso`(`id_plan_estudio` ASC) USING BTREE,
  CONSTRAINT `fk_plan_estudio_curso` FOREIGN KEY (`id_plan_estudio`) REFERENCES `plan_estudio` (`id_plan_estudio`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE = InnoDB AUTO_INCREMENT = 69 CHARACTER SET = utf8mb3 COLLATE = utf8mb3_general_ci ROW_FORMAT = DYNAMIC;

-- ----------------------------
-- Records of curso
-- ----------------------------
INSERT INTO `curso` VALUES (1, 'COMPRENSIÓN DE TEXTOS Y REDACCIÓN BÁSICA', '0001502000HU', 3, 1, 4, 1, 0, 'Activo', 1);
INSERT INTO `curso` VALUES (3, 'DESARROLLO DE COMPETENCIAS DIGITALES', '0001502000IN', 2, 1, 2, 1, 1, 'Activo', 1);
INSERT INTO `curso` VALUES (4, 'ESTRATEGIAS PARA EL APRENDIZAJE AUTÓNOMO', '0001501000HU', 3, 1, 4, 1, 1, 'Activo', 1);
INSERT INTO `curso` VALUES (6, 'INTRODUCCIÓN A LA INGENIERÍA DE SISTEMAS Y COMPUTACIÓN', '1201601C20IN', 3, 1, 4, 1, 0, 'Activo', 1);
INSERT INTO `curso` VALUES (8, 'MATEMÁTICA BÁSICA', '0001501000IN', 3, 1, 4, 1, 0, 'Activo', 1);
INSERT INTO `curso` VALUES (9, 'MATEMÁTICA DISCRETA', '1201602000IN', 4, 3, 2, 1, 0, 'Activo', 1);
INSERT INTO `curso` VALUES (11, 'CÁLCULO DE UNA VARIABLE', '1202603000IN', 4, 2, 4, 2, 0, 'Activo', 1);
INSERT INTO `curso` VALUES (12, 'COMPRENSIÓN Y REDACCIÓN DE TEXTOS ACADÉMICOS', '0002501000HU', 3, 1, 4, 2, 0, 'Activo', 1);
INSERT INTO `curso` VALUES (13, 'ECOLOGÍA Y DESARROLLO SOSTENIBLE', '0002501000SA', 3, 2, 2, 2, 1, 'Activo', 1);
INSERT INTO `curso` VALUES (14, 'ECONOMÍA Y REALIDAD NACIONAL', '1202601000EM', 3, 2, 2, 2, 0, 'Activo', 1);
INSERT INTO `curso` VALUES (15, 'FUNDAMENTOS DE PROGRAMACIÓN', '1202602000IN', 3, 1, 4, 2, 0, 'Activo', 1);
INSERT INTO `curso` VALUES (16, 'TEORÍA Y PROCESOS ORGANIZACIONALES', '1202601000IN', 3, 1, 4, 2, 0, 'Activo', 1);
INSERT INTO `curso` VALUES (17, 'ANÁLISIS Y ESPECIFICACIÓN DE REQUISITOS', '1203701C10IN', 3, 1, 4, 3, 0, 'Activo', 1);
INSERT INTO `curso` VALUES (18, 'CÁLCULO DE VARIAS VARIABLES', '1203603000IN', 4, 2, 4, 3, 0, 'Activo', 1);
INSERT INTO `curso` VALUES (19, 'CONTABILIDAD Y FINANZAS', '1203601000EM', 3, 1, 4, 3, 0, 'Activo', 1);
INSERT INTO `curso` VALUES (20, 'FILOSOFÍA', '0003501000TE', 3, 3, 0, 3, 0, 'Activo', 1);
INSERT INTO `curso` VALUES (21, 'FÍSICA DE LOS CUERPOS RÍGIDOS', '1203602000IN', 4, 3, 2, 3, 0, 'Activo', 1);
INSERT INTO `curso` VALUES (22, 'METODOLOGÍAS DE PROGRAMACIÓN', '1203601000IN', 3, 1, 4, 3, 0, 'Activo', 1);
INSERT INTO `curso` VALUES (23, 'ANTROPOLOGÍA FILOSÓFICA', '0004501000TE', 3, 3, 0, 4, 0, 'Activo', 1);
INSERT INTO `curso` VALUES (24, 'BASE DE DATOS', '1204601C10IN', 4, 3, 2, 4, 0, 'Activo', 1);
INSERT INTO `curso` VALUES (25, 'DISEÑO DE SOFTWARE', '1204701C10IN', 3, 1, 4, 4, 0, 'Activo', 1);
INSERT INTO `curso` VALUES (26, 'ECUACIONES DIFERENCIALES Y MÉTODOS NUMÉRICOS', '1204603000IN', 4, 2, 4, 4, 0, 'Activo', 1);
INSERT INTO `curso` VALUES (27, 'ELECTRICIDAD Y MAGNETISMO', '1204602000IN', 4, 3, 2, 4, 0, 'Activo', 1);
INSERT INTO `curso` VALUES (28, 'ESTRUCTURA DE DATOS Y ALGORITMOS', '1204601000IN', 3, 1, 4, 4, 0, 'Activo', 1);
INSERT INTO `curso` VALUES (29, 'ADMINISTRACIÓN DE BASE DE DATOS', '1205701C20IN', 3, 1, 4, 5, 0, 'Activo', 1);
INSERT INTO `curso` VALUES (30, 'ARQUITECTURA Y ORGANIZACIÓN DE COMPUTADORAS', '1205601C20IN', 4, 3, 2, 5, 0, 'Activo', 1);
INSERT INTO `curso` VALUES (31, 'DISEÑO WEB', '1205701C10IN', 3, 1, 4, 5, 0, 'Activo', 1);
INSERT INTO `curso` VALUES (32, 'ESTADÍSTICA Y PROBABILIDADES', '1205601000IN', 3, 1, 4, 5, 0, 'Activo', 1);
INSERT INTO `curso` VALUES (33, 'ÉTICA', '0005501000TE', 3, 3, 0, 5, 0, 'Activo', 1);
INSERT INTO `curso` VALUES (34, 'INGENIERÍA DE PROCESOS', '1205602000IN', 3, 2, 2, 5, 0, 'Activo', 1);
INSERT INTO `curso` VALUES (35, 'TEORÍA GENERAL DE SISTEMAS', '1205603000IN', 2, 1, 2, 5, 0, 'Activo', 1);
INSERT INTO `curso` VALUES (36, 'DESARROLLO DE APLICACIONES DE ESCRITORIO', '1206702C10IN', 4, 2, 4, 6, 0, 'Activo', 1);
INSERT INTO `curso` VALUES (37, 'DESARROLLO DE APLICACIONES WEB', '1206701C10IN', 4, 2, 4, 6, 0, 'Activo', 1);
INSERT INTO `curso` VALUES (38, 'FE Y CULTURA', '0006501000TE', 3, 3, 0, 6, 0, 'Activo', 1);
INSERT INTO `curso` VALUES (39, 'INTELIGENCIA ARTIFICIAL', '1206602000IN', 4, 3, 2, 6, 0, 'Activo', 1);
INSERT INTO `curso` VALUES (40, 'INVESTIGACIÓN DE OPERACIONES', '1206601000IN', 3, 1, 4, 6, 0, 'Activo', 1);
INSERT INTO `curso` VALUES (41, 'SISTEMAS OPERATIVOS', '1206601C20IN', 3, 1, 4, 6, 0, 'Activo', 1);
INSERT INTO `curso` VALUES (42, 'DESARROLLO DE SISTEMAS INTELIGENTES', '1207701000IN', 2, 0, 4, 7, 0, 'Activo', 1);
INSERT INTO `curso` VALUES (43, 'FUNDAMENTOS Y DISEÑO DE REDES DE DATOS', '1207701C20IN', 3, 1, 4, 7, 0, 'Activo', 1);
INSERT INTO `curso` VALUES (44, 'INGENIERÍA Y CALIDAD DE SOFTWARE', '1207702C10IN', 4, 2, 4, 7, 0, 'Activo', 1);
INSERT INTO `curso` VALUES (45, 'INTELIGENCIA DE NEGOCIOS', '1207701C30IN', 3, 1, 4, 7, 0, 'Activo', 1);
INSERT INTO `curso` VALUES (46, 'INVESTIGACIÓN EN INGENIERÍA', '1207601000IN', 3, 1, 4, 7, 1, 'Activo', 1);
INSERT INTO `curso` VALUES (47, 'MORAL CATÓLICA', '0007501000TE', 3, 3, 0, 7, 0, 'Activo', 1);
INSERT INTO `curso` VALUES (48, 'SISTEMAS DISTRIBUIDOS', '1207701C10IN', 3, 1, 4, 7, 0, 'Activo', 1);
INSERT INTO `curso` VALUES (49, 'CONFIGURACIÓN Y ADMINISTRACIÓN DE REDES DE DATOS', '1208701C20IN', 4, 2, 2, 8, 0, 'Activo', 1);
INSERT INTO `curso` VALUES (50, 'DESARROLLO DE APLICACIONES MÓVILES', '1208701C10IN', 4, 2, 4, 8, 0, 'Activo', 1);
INSERT INTO `curso` VALUES (51, 'DOCTRINA SOCIAL DE LA IGLESIA', '0008501000TE', 3, 3, 0, 8, 0, 'Activo', 1);
INSERT INTO `curso` VALUES (52, 'GOBIERNO Y GESTIÓN DE TECNOLOGÍAS DE INFORMACIÓN', '1208701C30IN', 4, 3, 2, 8, 0, 'Activo', 1);
INSERT INTO `curso` VALUES (53, 'MINERÍA DE DATOS Y BIG DATA', '1208701000IN', 3, 1, 4, 8, 0, 'Activo', 1);
INSERT INTO `curso` VALUES (54, 'PROYECTO DE INVESTIGACIÓN', '1208601000IN', 3, 1, 4, 8, 1, 'Activo', 1);
INSERT INTO `curso` VALUES (55, 'CONFIGURACIÓN Y ADMINISTRACIÓN DE SERVIDORES', '1209701C20IN', 4, 3, 2, 9, 0, 'Activo', 1);
INSERT INTO `curso` VALUES (56, 'DEONTOLOGÍA Y LEGISLACIÓN LABORAL E INFORMÁTICA', '1209601000IN', 2, 1, 2, 9, 0, 'Activo', 1);
INSERT INTO `curso` VALUES (57, 'GESTIÓN DE RIESGOS Y SEGURIDAD DE LA INFORMACIÓN', '1209701C30IN', 4, 3, 2, 9, 0, 'Activo', 1);
INSERT INTO `curso` VALUES (58, 'GESTIÓN DE SERVICIOS DE TECNOLOGÍAS DE INFORMACIÓN', '1209702C30IN', 4, 3, 2, 9, 0, 'Activo', 1);
INSERT INTO `curso` VALUES (59, 'NEGOCIOS ELECTRÓNICOS Y MARKETING DIGITAL', '1209703C30IN', 4, 3, 2, 9, 0, 'Activo', 1);
INSERT INTO `curso` VALUES (60, 'SEMINARIO DE TESIS I', '1209602000IN', 3, 1, 4, 9, 1, 'Activo', 1);
INSERT INTO `curso` VALUES (61, 'AUDITORÍA DE SISTEMAS DE INFORMACIÓN', '1210701C30IN', 4, 3, 2, 10, 1, 'Activo', 1);
INSERT INTO `curso` VALUES (62, 'DESARROLLO DE VIDEO JUEGOS', '1210703000IN', 2, 0, 4, 10, 1, 'Activo', 1);
INSERT INTO `curso` VALUES (63, 'EMPRENDIMIENTO DE BASE TECNOLÓGICA', '1210601C30IN', 2, 0, 4, 10, 0, 'Activo', 1);
INSERT INTO `curso` VALUES (64, 'GESTIÓN DE PROYECTOS DE SISTEMAS DE INFORMACIÓN', '1210701000IN', 4, 2, 4, 10, 0, 'Activo', 1);
INSERT INTO `curso` VALUES (65, 'SEGURIDAD INFORMÁTICA', '1210701C20IN', 3, 1, 4, 10, 0, 'Activo', 1);
INSERT INTO `curso` VALUES (66, 'SEMINARIO DE TESIS II', '1210601000IN', 3, 1, 4, 10, 1, 'Activo', 1);
INSERT INTO `curso` VALUES (67, 'SISTEMAS ERP', '1210704000IN', 2, 0, 4, 10, 1, 'Activo', 1);
INSERT INTO `curso` VALUES (68, 'TÓPICOS AVANZADOS EN DESARROLLO DE SOFTWARE', '1210702000IN', 3, 0, 6, 10, 0, 'Activo', 1);

-- ----------------------------
-- Table structure for docente_disponibilidad
-- ----------------------------
DROP TABLE IF EXISTS `docente_disponibilidad`;
CREATE TABLE `docente_disponibilidad`  (
  `dia` varchar(255) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NOT NULL,
  `hora_inicio` time NOT NULL,
  `hora_fin` time NOT NULL,
  `idpersona` int NOT NULL,
  INDEX `fk_persona_docente_disponibilidad`(`idpersona` ASC) USING BTREE,
  CONSTRAINT `fk_persona_docente_disponibilidad` FOREIGN KEY (`idpersona`) REFERENCES `persona` (`idpersona`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE = InnoDB CHARACTER SET = utf8mb3 COLLATE = utf8mb3_general_ci ROW_FORMAT = DYNAMIC;

-- ----------------------------
-- Records of docente_disponibilidad
-- ----------------------------

-- ----------------------------
-- Table structure for edificio
-- ----------------------------
DROP TABLE IF EXISTS `edificio`;
CREATE TABLE `edificio`  (
  `idedificio` int NOT NULL AUTO_INCREMENT,
  `nombre` varchar(255) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NOT NULL,
  `estado` tinyint(1) NOT NULL,
  PRIMARY KEY (`idedificio`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 6 CHARACTER SET = utf8mb3 COLLATE = utf8mb3_general_ci ROW_FORMAT = DYNAMIC;

-- ----------------------------
-- Records of edificio
-- ----------------------------
INSERT INTO `edificio` VALUES (1, 'EDIFICIO ANTIGUO', 0);
INSERT INTO `edificio` VALUES (2, 'JUAN PABLO II', 0);
INSERT INTO `edificio` VALUES (3, 'IDIOMAS', 0);
INSERT INTO `edificio` VALUES (4, 'DECANAS', 0);
INSERT INTO `edificio` VALUES (5, 'CEFO', 0);

-- ----------------------------
-- Table structure for error_sql
-- ----------------------------
DROP TABLE IF EXISTS `error_sql`;
CREATE TABLE `error_sql`  (
  `idError` int NOT NULL AUTO_INCREMENT,
  `query` text CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NOT NULL,
  `error_message` text CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NOT NULL,
  `fecha` date NOT NULL,
  PRIMARY KEY (`idError`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 1 CHARACTER SET = utf8mb3 COLLATE = utf8mb3_general_ci ROW_FORMAT = DYNAMIC;

-- ----------------------------
-- Records of error_sql
-- ----------------------------

-- ----------------------------
-- Table structure for escuela
-- ----------------------------
DROP TABLE IF EXISTS `escuela`;
CREATE TABLE `escuela`  (
  `id_escuela` int NOT NULL AUTO_INCREMENT,
  `nombre` varchar(255) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NOT NULL,
  `descripcion` varchar(255) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL,
  `estado` varchar(20) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NOT NULL,
  `id_facultad` int NOT NULL,
  PRIMARY KEY (`id_escuela`) USING BTREE,
  INDEX `fk_facultad_escuela`(`id_facultad` ASC) USING BTREE,
  CONSTRAINT `fk_facultad_escuela` FOREIGN KEY (`id_facultad`) REFERENCES `facultad` (`id_facultad`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE = InnoDB AUTO_INCREMENT = 2 CHARACTER SET = utf8mb3 COLLATE = utf8mb3_general_ci ROW_FORMAT = DYNAMIC;

-- ----------------------------
-- Records of escuela
-- ----------------------------
INSERT INTO `escuela` VALUES (1, 'Ingenieria de Sistemas y Computación', 'Escuela de vagos', 'ACTIVO', 1);

-- ----------------------------
-- Table structure for facultad
-- ----------------------------
DROP TABLE IF EXISTS `facultad`;
CREATE TABLE `facultad`  (
  `id_facultad` int NOT NULL AUTO_INCREMENT,
  `nombre` varchar(255) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NOT NULL,
  `descripcion` varchar(255) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL,
  `estado` varchar(20) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NOT NULL,
  PRIMARY KEY (`id_facultad`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 2 CHARACTER SET = utf8mb3 COLLATE = utf8mb3_general_ci ROW_FORMAT = DYNAMIC;

-- ----------------------------
-- Records of facultad
-- ----------------------------
INSERT INTO `facultad` VALUES (1, 'Ingenieria', NULL, 'ACTIVO');

-- ----------------------------
-- Table structure for grupo
-- ----------------------------
DROP TABLE IF EXISTS `grupo`;
CREATE TABLE `grupo`  (
  `id_grupo` int NOT NULL AUTO_INCREMENT,
  `nombre` varchar(1) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NOT NULL,
  `vacantes` int NOT NULL,
  `idcurso` int NOT NULL,
  `idsemestre` int NOT NULL,
  PRIMARY KEY (`id_grupo`) USING BTREE,
  INDEX `fk_curso_grupo`(`idcurso` ASC) USING BTREE,
  INDEX `fk_semestre_academico_grupo`(`idsemestre` ASC) USING BTREE,
  CONSTRAINT `fk_curso_grupo` FOREIGN KEY (`idcurso`) REFERENCES `curso` (`idcurso`) ON DELETE RESTRICT ON UPDATE RESTRICT,
  CONSTRAINT `fk_semestre_academico_grupo` FOREIGN KEY (`idsemestre`) REFERENCES `semestre_academico` (`idsemestre`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE = InnoDB AUTO_INCREMENT = 1 CHARACTER SET = utf8mb3 COLLATE = utf8mb3_general_ci ROW_FORMAT = DYNAMIC;

-- ----------------------------
-- Records of grupo
-- ----------------------------

-- ----------------------------
-- Table structure for horario
-- ----------------------------
DROP TABLE IF EXISTS `horario`;
CREATE TABLE `horario`  (
  `idhorario` int NOT NULL AUTO_INCREMENT,
  `idambiente` int NOT NULL,
  `dia` varchar(255) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NOT NULL,
  `horainicio` time NOT NULL,
  `horafin` time NOT NULL,
  `h_virtual` tinyint(1) NOT NULL,
  `h_presencial` tinyint(1) NOT NULL,
  `idpersona` int NOT NULL,
  `id_grupo` int NOT NULL,
  PRIMARY KEY (`idhorario`) USING BTREE,
  INDEX `fk_ambiente_horario`(`idambiente` ASC) USING BTREE,
  INDEX `fk_grupo_horario`(`id_grupo` ASC) USING BTREE,
  INDEX `fk_persona_horario`(`idpersona` ASC) USING BTREE,
  CONSTRAINT `fk_ambiente_horario` FOREIGN KEY (`idambiente`) REFERENCES `ambiente` (`idambiente`) ON DELETE RESTRICT ON UPDATE RESTRICT,
  CONSTRAINT `fk_grupo_horario` FOREIGN KEY (`id_grupo`) REFERENCES `grupo` (`id_grupo`) ON DELETE RESTRICT ON UPDATE RESTRICT,
  CONSTRAINT `fk_persona_horario` FOREIGN KEY (`idpersona`) REFERENCES `persona` (`idpersona`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE = InnoDB AUTO_INCREMENT = 1 CHARACTER SET = utf8mb3 COLLATE = utf8mb3_general_ci ROW_FORMAT = DYNAMIC;

-- ----------------------------
-- Records of horario
-- ----------------------------

-- ----------------------------
-- Table structure for incidencia
-- ----------------------------
DROP TABLE IF EXISTS `incidencia`;
CREATE TABLE `incidencia`  (
  `idincidencia` int NOT NULL AUTO_INCREMENT,
  `descripcion` varchar(255) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NOT NULL,
  `estado` bit(1) NOT NULL,
  `idError` int NOT NULL,
  `idhorario` int NOT NULL,
  PRIMARY KEY (`idincidencia`) USING BTREE,
  INDEX `fk_horario_incidencia`(`idhorario` ASC) USING BTREE,
  INDEX `fk_incidencia_error_sql`(`idError` ASC) USING BTREE,
  CONSTRAINT `fk_horario_incidencia` FOREIGN KEY (`idhorario`) REFERENCES `horario` (`idhorario`) ON DELETE RESTRICT ON UPDATE RESTRICT,
  CONSTRAINT `fk_incidencia_error_sql` FOREIGN KEY (`idError`) REFERENCES `error_sql` (`idError`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE = InnoDB AUTO_INCREMENT = 1 CHARACTER SET = utf8mb3 COLLATE = utf8mb3_general_ci ROW_FORMAT = DYNAMIC;

-- ----------------------------
-- Records of incidencia
-- ----------------------------

-- ----------------------------
-- Table structure for modificacion_tablas
-- ----------------------------
DROP TABLE IF EXISTS `modificacion_tablas`;
CREATE TABLE `modificacion_tablas`  (
  `id_modificacion` int NOT NULL AUTO_INCREMENT,
  `descripcion` int NULL DEFAULT NULL,
  `tabla` int NOT NULL,
  `idusuario` int NOT NULL,
  PRIMARY KEY (`id_modificacion`) USING BTREE,
  INDEX `fk_usuario_modificacion`(`idusuario` ASC) USING BTREE,
  CONSTRAINT `fk_usuario_modificacion` FOREIGN KEY (`idusuario`) REFERENCES `usuario` (`idusuario`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE = InnoDB AUTO_INCREMENT = 1 CHARACTER SET = utf8mb3 COLLATE = utf8mb3_general_ci ROW_FORMAT = DYNAMIC;

-- ----------------------------
-- Records of modificacion_tablas
-- ----------------------------

-- ----------------------------
-- Table structure for persona
-- ----------------------------
DROP TABLE IF EXISTS `persona`;
CREATE TABLE `persona`  (
  `idpersona` int NOT NULL AUTO_INCREMENT,
  `nombres` varchar(255) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NOT NULL,
  `apellidos` varchar(255) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NOT NULL,
  `n_documento` varchar(11) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NOT NULL,
  `telefono` varchar(11) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NOT NULL,
  `correo` varchar(255) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NOT NULL,
  `tipopersona` char(1) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NOT NULL,
  `cantHoras` tinyint(1) NOT NULL,
  `tiempo_ref` tinyint(1) NOT NULL,
  `foto` varchar(255) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL,
  PRIMARY KEY (`idpersona`) USING BTREE,
  UNIQUE INDEX `n_documento`(`n_documento` ASC) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 6 CHARACTER SET = utf8mb3 COLLATE = utf8mb3_general_ci ROW_FORMAT = DYNAMIC;

-- ----------------------------
-- Records of persona
-- ----------------------------
INSERT INTO `persona` VALUES (1, 'Jeancarlos', 'Chafloque Velásquez', '71870269', '960920160', 'jc_26.10@hotmail.com', 'A', 0, 0, 'CHAFLOQUE_VELASQUEZ_JEANCARLOS.jpg');
INSERT INTO `persona` VALUES (2, 'Bruno Sebastian', 'Pisfil Falla', '75062773', '956213658', 'bunopisfil11@gmail.com', 'A', 0, 0, 'BRUNOPISFILFALLA.jpg');
INSERT INTO `persona` VALUES (3, 'Junior Alexis', 'Soplapuco Purisaca', '26378977', '989222878', 'jaspeach@gmail.com', 'D', 16, 4, NULL);
INSERT INTO `persona` VALUES (4, 'Ernesto Ludwin', 'Nicho Cordova', '19327600', '95874632', 'ncordova@usat.edu.pe', 'A', 0, 0, 'NICHO_CORDOVA_ERNESTO_LUDWIN.jpg');
INSERT INTO `persona` VALUES (5, 'Segundo Jose', 'Castillo Zumaran', '16761275', '987564823', 'scastillo@usat.edu.pe', 'D', 0, 0, 'CASTILLO ZUMARAN SEGUNDO JOSE.jpg');

-- ----------------------------
-- Table structure for plan_estudio
-- ----------------------------
DROP TABLE IF EXISTS `plan_estudio`;
CREATE TABLE `plan_estudio`  (
  `id_plan_estudio` int NOT NULL AUTO_INCREMENT,
  `nombre` varchar(7) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NOT NULL,
  `estado` varchar(20) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NOT NULL,
  `id_escuela` int NOT NULL,
  PRIMARY KEY (`id_plan_estudio`) USING BTREE,
  INDEX `fk_escuela_plan_estudio`(`id_escuela` ASC) USING BTREE,
  CONSTRAINT `fk_escuela_plan_estudio` FOREIGN KEY (`id_escuela`) REFERENCES `escuela` (`id_escuela`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE = InnoDB AUTO_INCREMENT = 2 CHARACTER SET = utf8mb3 COLLATE = utf8mb3_general_ci ROW_FORMAT = DYNAMIC;

-- ----------------------------
-- Records of plan_estudio
-- ----------------------------
INSERT INTO `plan_estudio` VALUES (1, '2017 V3', 'ACTIVO', 1);

-- ----------------------------
-- Table structure for semestre_academico
-- ----------------------------
DROP TABLE IF EXISTS `semestre_academico`;
CREATE TABLE `semestre_academico`  (
  `idsemestre` int NOT NULL AUTO_INCREMENT,
  `descripcion` varchar(10) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NOT NULL,
  `estado` tinyint(1) NOT NULL,
  PRIMARY KEY (`idsemestre`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 6 CHARACTER SET = utf8mb3 COLLATE = utf8mb3_general_ci ROW_FORMAT = DYNAMIC;

-- ----------------------------
-- Records of semestre_academico
-- ----------------------------
INSERT INTO `semestre_academico` VALUES (1, '2024-I', 0);
INSERT INTO `semestre_academico` VALUES (2, '2023-II', 0);
INSERT INTO `semestre_academico` VALUES (3, '2023-I', 0);
INSERT INTO `semestre_academico` VALUES (4, '2022-II', 0);
INSERT INTO `semestre_academico` VALUES (5, '2022-I', 0);

-- ----------------------------
-- Table structure for usuario
-- ----------------------------
DROP TABLE IF EXISTS `usuario`;
CREATE TABLE `usuario`  (
  `idusuario` int NOT NULL AUTO_INCREMENT,
  `username` varchar(255) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NOT NULL,
  `password` varchar(255) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NOT NULL,
  `estado` varchar(50) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NOT NULL,
  `idpersona` int NOT NULL,
  `token` varchar(255) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL,
  PRIMARY KEY (`idusuario`) USING BTREE,
  UNIQUE INDEX `username`(`username` ASC) USING BTREE,
  INDEX `fk_persona_usuario`(`idpersona` ASC) USING BTREE,
  CONSTRAINT `fk_persona_usuario` FOREIGN KEY (`idpersona`) REFERENCES `persona` (`idpersona`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE = InnoDB AUTO_INCREMENT = 4 CHARACTER SET = utf8mb3 COLLATE = utf8mb3_general_ci ROW_FORMAT = DYNAMIC;

-- ----------------------------
-- Records of usuario
-- ----------------------------
INSERT INTO `usuario` VALUES (1, 'admin', 'a665a45920422f9d417e4867efdc4fb8a04a1f3fff1fa07e998e86f7f7a27ae3', 'ACTIVO', 1, '7acc684a848a9b954959fdd22493f48cf44eed028275b6b9999c7cade8956fc7');
INSERT INTO `usuario` VALUES (2, 'bruno', 'a665a45920422f9d417e4867efdc4fb8a04a1f3fff1fa07e998e86f7f7a27ae3', 'ACTIVO', 2, 'cbf2f7864f1c988391a9ab199627a29bd60987da067748c2812b75785d7ec151');
INSERT INTO `usuario` VALUES (3, 'chuparan', 'a665a45920422f9d417e4867efdc4fb8a04a1f3fff1fa07e998e86f7f7a27ae3', 'ACTIVO', 5, '734d0759cdb4e0d0a35e4fd73749aee287e4fdcc8648b71a8d6ed591b7d4cb3f');

-- ----------------------------
-- Procedure structure for sp_Usuario_Gestion
-- ----------------------------
DROP PROCEDURE IF EXISTS `sp_Usuario_Gestion`;
delimiter ;;
CREATE PROCEDURE `sp_Usuario_Gestion`(IN _tipo INT,
    IN _idusuario INT,
    IN _username VARCHAR(255),
    IN _password VARCHAR(255),
    IN _estado VARCHAR(50),
    IN _idpersona INT,
    IN _token VARCHAR(255))
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
            SET v_query = CONCAT('UPDATE usuario SET estado = ''Baja'' WHERE idusuario = ', _idusuario);
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
END
;;
delimiter ;

SET FOREIGN_KEY_CHECKS = 1;
