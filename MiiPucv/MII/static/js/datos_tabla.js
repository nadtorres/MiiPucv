let table = $('#tablaAlumnos').DataTable({
        "ajax": {
            "url": "/api/alumnos/",
            "type": "GET"
        },
        "columns": [
            {"data": "id"},
            {"data": "nombre"},
            {"data": "apellido_pat"},
            {"data": "apellido_mat"},
            {"data": "rut"},
            {"data": "sexo"},
            {"data": "email"},
            {"data": "telefono"},
            {"data": "direccion"},
            {"data": "universidad_procedencia"},
            {"data": "posee"},
            {"data": "nivelacion"},
            {"data": "resultados_nivelacion"},
            {"data": "semestre_ingreso"},
            {"data": "anio_ingreso"},
            {"data": "estado_matricula"},
            {"data": "antecedentes_academicos"},
            {"data": "antecedentes_profesionales"},
            {"data": "carta_recomendacion"},
            {"data": "entrevista"},
            {"data": "puntaje"},
            {"data": "resultados_condicion"},
            {
                "data": null,
                "defaultContent": '<button type="button" class="btn btn-info">Edit</button>' + '&nbsp;&nbsp' +
                '<button type="button" class="btn btn-danger">Delete</button>'
            }
        ]
    });

let table = $('#tablaProfesores').DataTable({
        "ajax": {
            "url": "/api/profesores/",
            "type": "GET"
        },
        "columns": [
            {"data": "id"},
            {"data": "nombre"},
            {"data": "apellido_pat"},
            {"data": "apellido_mat"},
            {"data": "rut"},
            {"data": "sexo"},
            {"data": "email"},
            {"data": "telefono"},
            {"data": "direccion"},
            {"data": "profesion"},
            {"data": "cursos_impartados"},
            {
                "data": null,
                "defaultContent": '<button type="button" class="btn btn-info">Edit</button>' + '&nbsp;&nbsp' +
                '<button type="button" class="btn btn-danger">Delete</button>'
            }
        ]
    });

let table = $('#tablaUsuarios').DataTable({
        "ajax": {
            "url": "/api/users/",
            "type": "GET"
        },
        "columns": [
            {"data": "id"},
            {"data": "username"},
            {"data": "first_name"},
            {"data": "last_name"},
            {"data": "email"},
            {"data": "is_active"},
            {"data": "is_staff"},
            {
                "data": null,
                "defaultContent": '<button type="button" class="btn btn-info">Edit</button>' + '&nbsp;&nbsp' +
                '<button type="button" class="btn btn-danger">Delete</button>'
            }
        ]
    });

let table = $('#tablaPerfil').DataTable({
    "ajax": {
        "url": "/api/perfil/",
        "type": "GET"
    },
    "columns": [
            {"data": "imagen"},
            {"data": "edad"},
            {"data": "estado_civil"},
            {"data": "rut"},
            {"data": "email_inst"},
            {"data": "calle"},
            {"data": "ciudad"},
            {"data": "comuna"},
            {"data": "sexo"},
            {"data": "direccion"},
            {
                "data": null,
                "defaultContent": '<button type="button" class="btn btn-info">Edit</button' + '&nbsp;&nbsp' +
                '<button type="button" class=>"btn btn-danger">Delete</button>'
            }            
        ]
    });