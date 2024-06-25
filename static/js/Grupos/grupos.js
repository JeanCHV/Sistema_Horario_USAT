$(document).ready(function () {
    var grupos = [];
    var cursos = [];
    var semestres = [];
    var table = $('#tabla-grupo').DataTable({
        paging: false,
        info: true,
        responsive: true,
        autoWidth: true,
        stateSave: true,
        scrollY: "510px",
        columns: [
            { data: "nombre", className: 'dt-body-center' },
            { data: "vacantes", className: 'dt-body-center' },
            {
                data: "curso",
                render: function (data, type, row) {
                    return cursos[data] || data;
                }
            },
            { data: "descripcion", className: 'dt-body-center' },
            {
                data: null, className: 'dt-body-center',
                render: function (data, type, row) {
                    return `
                        <button class="btn btn-warning btn-sm btnModificar" data-id_grupo="${row.id_grupo}" title="Modificar"><i class="fas fa-pencil-alt"></i></button>
                        <button class="btn btn-danger btn-sm btnEliminar" data-id_grupo="${row.id_grupo}" title="Eliminar"><i class="fas fa-times"></i></button>
                    `;
                }
            }
        ],
        "language": {
            "url": "https://cdn.datatables.net/plug-ins/1.13.7/i18n/es-ES.json"
        }
    });

    function cargarGrupos() {
        $.ajax({
            url: '/get_grupos',
            type: 'GET',
            contentType: 'application/json',
            success: function (response) {
                grupos = response;
                table.clear().rows.add(grupos).draw();
                $('#filtro_cursos').val('').change();
            },
            error: function (xhr, status, error) {
                console.log(error);
            }
        });
    }
    cargarGrupos();

    $('#collapseOne').collapse('show');

    function cargarCursosEnFiltro() {
        $.ajax({
            url: '/obtener_cursos',
            type: 'GET',
            contentType: 'application/json',
            success: function (response) {
                var select = $('#filtro_cursos');
                select.empty();
                select.append($('<option>', { value: '', text: 'Todos los cursos' }));
                response.forEach(function (curso) {
                    select.append($('<option>', {
                        value: curso.idcurso,
                        text: curso.nombre
                    }));
                    cursos[curso.idcurso] = curso.nombre;
                });
            },
            error: function (xhr, status, error) {
                console.log('Error al cargar los cursos:', error);
            }
        });
    }
    cargarCursosEnFiltro();

    $('#filtro_cursos').on('change', function () {
        var filtro = $(this).val();
        if (filtro) {
            table.column(2).search(cursos[filtro]).draw();
        } else {
            table.column(2).search('').draw();
        }
    });

    function cargarCursos() {
        return $.ajax({
            url: '/obtener_cursos',
            type: 'GET',
            contentType: 'application/json',
            success: function (response) {
                cursos = response;
                var select = $('#agregarCurso, #modificarCurso');
                select.empty();
                response.forEach(function (curso) {
                    select.append($('<option>', {
                        value: curso.idcurso,
                        text: curso.nombre
                    }));
                });
            },
            error: function (xhr, status, error) {
                console.log('Error al cargar los cursos:', error);
            }
        });
    }

    function cargarSemestres() {
        return $.ajax({
            url: '/obtener_semestres',
            type: 'GET',
            contentType: 'application/json',
            success: function (response) {
                semestres = response;
                var select = $('#agregarSemestre, #modificarSemestre');
                select.empty();
                response.forEach(function (semestre) {
                    select.append($('<option>', {
                        value: semestre.idsemestre,
                        text: semestre.descripcion
                    }));
                });
            },
            error: function (xhr, status, error) {
                console.log('Error al cargar los semestres:', error);
            }
        });
    }

    $('#btn_agregar_grupo').click(function (e) {
        e.preventDefault();
        $('#modalAgregarGrupo').modal('show');
        $('#formAgregarGrupo')[0].reset();
        $.when(cargarCursos(), cargarSemestres()).done(function () {
            $('#agregarCurso').val('');
            $('#agregarSemestre').val('');
        });
    });

    $('#formAgregarGrupo').submit(function (e) {
        e.preventDefault();
        var data = {
            nombre: $('#agregarGrupo').val(),
            vacantes: $('#agregarVacante').val(),
            idcurso: $('#agregarCurso').val(),
            idsemestre: $('#agregarSemestre').val()
        };

        $.ajax({
            url: '/agregar_grupo',
            type: 'POST',
            contentType: 'application/json',
            data: JSON.stringify(data),
            success: function (response) {
                console.log(response);
                $('#mensajeResultado').removeClass().empty();
                if (response.error) {
                    $('#mensajeResultado').addClass('alert alert-danger').text('Error: ' + response.error);
                } else {
                    $('#mensajeResultado').addClass('alert alert-success').text('Grupo agregado correctamente');
                    $('#modalAgregarGrupo').modal('hide');
                    cargarGrupos();
                }
                $('#mensajeResultado').show();
            },
            error: function (xhr, status, error) {
                console.log(error);
            }
        });
    });

    $('#formModificarGrupo').submit(function (e) { // Cambié aquí de 'formModificarGrupos' a 'formModificarGrupo'
        e.preventDefault();
        var data = {
            id_grupo: $('#modificarIdGrupo').val(),
            nombre: $('#modificarNombre').val(),
            vacantes: $('#modificarVacantes').val(),
            idcurso: $('#modificarCurso').val(),
            idsemestre: $('#modificarSemestre').val(),
        };

        $.ajax({
            url: '/modificar_grupo',
            type: 'POST',
            contentType: 'application/json',
            data: JSON.stringify(data),
            success: function (response) {
                if (response.error) {
                    Swal.fire('Error', response.error, 'error');
                } else {
                    Swal.fire('Éxito', 'Grupo modificado correctamente', 'success');
                    cargarGrupos(); // Cambié de 'table.ajax.reload();' a 'cargarGrupos();'
                    $('#modalModificarGrupo').modal('hide');
                }
            },
            error: function (xhr, status, error) {
                Swal.fire('Error', 'Hubo un error al modificar el grupo', 'error');
                console.log(error);
            }
        });
    });

    $('#tabla-grupo tbody').on('click', '.btnModificar', function () {
        var id = $(this).data('id_grupo');
        $.ajax({
            url: '/obtener_grupo_por_id/' + id,
            type: 'GET',
            contentType: 'application/json',
            success: function (response) {
                if (response.error) {
                    console.log(response.error);
                    return;
                }

                var grupo = response;
                $('#modificarIdGrupo').val(grupo.id_grupo);
                $('#modificarNombre').val(grupo.nombre);
                $('#modificarVacantes').val(grupo.vacantes);

                // Cargar cursos y semestres antes de mostrar el modal
                $.when(cargarCursos(), cargarSemestres()).done(function () {
                    $('#modificarCurso').val(grupo.idcurso);
                    $('#modificarSemestre').val(grupo.idsemestre);
                    $('#modalModificarGrupo').modal('show');
                });
            },
            error: function (xhr, status, error) {
                console.log(error);
            }
        });
    });

    $('#tabla-grupo tbody').on('click', '.btnEliminar', function () {
        var id = $(this).data('id_grupo');
        Swal.fire({
            title: '¿Estás seguro de que deseas eliminar este grupo?',
            text: "Esta acción no se puede deshacer.",
            icon: 'warning',
            showCancelButton: true,
            confirmButtonColor: '#3085d6',
            cancelButtonColor: '#d33',
            confirmButtonText: 'Sí, eliminar',
            cancelButtonText: 'Cancelar'
        }).then((result) => {
            if (result.isConfirmed) {
                $.ajax({
                    url: '/eliminar_grupo',
                    type: 'POST',
                    contentType: 'application/json',
                    data: JSON.stringify({ id_grupo: id }),
                    success: function (response) {
                        console.log(response);
                        $('#mensajeResultado').removeClass().empty();
                        if (response.error) {
                            $('#mensajeResultado').addClass('alert alert-danger').text('Error: ' + response.error);
                        } else {
                            $('#mensajeResultado').addClass('alert alert-success').text('Grupo eliminado correctamente');
                            cargarGrupos();
                        }
                        $('#mensajeResultado').show();
                    },
                    error: function (xhr, status, error) {
                        console.log(error);
                    }
                });
            }
        });
    });
});
