--CONSTRAINTS HECHAS POR POSTGRESQL PARA DETERMINAR CLAVES FORANEAS ENTRE MODELOS
--CONSTRAINTS DE ALUMNO
--ALUMNO

ALTER TABLE "Alumno_alumno"
   ADD CONSTRAINT fk_direccion 
   FOREIGN KEY (fk_direccion)
   REFERENCES "Direccion_direccion" (id_direccion); 

ALTER TABLE "Alumno_alumno"
   ADD CONSTRAINT fk_cursos_homologados 
   FOREIGN KEY (fk_cursos_homologados)
   REFERENCES "Alumno_cursos_homologados" (id_curso);

ALTER TABLE "Alumno_alumno"
   ADD CONSTRAINT fk_documento 
   FOREIGN KEY (fk_documento)
   REFERENCES "Documento_documento" (id_doc);

ALTER TABLE "Alumno_alumno"
   ADD CONSTRAINT fk_pagos 
   FOREIGN KEY (fk_pagos)
   REFERENCES "Pagos_pagos" (id_pago);

ALTER TABLE "Alumno_alumno"
   ADD CONSTRAINT fk_postulacion 
   FOREIGN KEY (fk_postulacion)
   REFERENCES "Postulacion_postulacion" (id_postulacion);

ALTER TABLE "Alumno_alumno"
   ADD CONSTRAINT fk_sede 
   FOREIGN KEY (fk_sede)
   REFERENCES "Sede_sede" (id_sede);


--CONSTRAINTS DE CURSOS
--DETALLE DE CURSO

ALTER TABLE "Cursos_detalle_curso"
   ADD CONSTRAINT fk_lista_alumnos 
   FOREIGN KEY (fk_lista_alumnos)
   REFERENCES "Cursos_lista_alumnos" (id_lista);

ALTER TABLE "Cursos_detalle_curso"
   ADD CONSTRAINT fk_profesor 
   FOREIGN KEY (fk_profesor)
   REFERENCES "Profesor_profesor" (id_profesor);


--LISTA DE ALUMNOS

ALTER TABLE "Cursos_lista_alumnos"
   ADD CONSTRAINT fk_alumno 
   FOREIGN KEY (fk_alumno)
   REFERENCES "Alumno_alumno" (id_alumno);


--CURSOS

ALTER TABLE "Cursos_cursos"
   ADD CONSTRAINT fk_alumno 
   FOREIGN KEY (fk_alumno)
   REFERENCES "Alumno_alumno" (id_alumno);

ALTER TABLE "Cursos_cursos"
   ADD CONSTRAINT fk_detalle_curso 
   FOREIGN KEY (fk_detalle_curso)
   REFERENCES "Cursos_detalle_curso" (id_detalle);

ALTER TABLE "Cursos_cursos"
   ADD CONSTRAINT fk_profesor 
   FOREIGN KEY (fk_profesor)
   REFERENCES "Profesor_profesor" (id_profesor);


--CONSTRAINT DE DIRECCION
--DIRECCION

ALTER TABLE "Direccion_direccion"
   ADD CONSTRAINT fk_alumno 
   FOREIGN KEY (fk_alumno)
   REFERENCES "Alumno_alumno" (id_alumno);

ALTER TABLE "Direccion_direccion"
   ADD CONSTRAINT fk_profesor 
   FOREIGN KEY (fk_profesor)
   REFERENCES "Profesor_profesor" (id_profesor);


