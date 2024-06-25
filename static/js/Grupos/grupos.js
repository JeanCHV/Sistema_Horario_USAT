$(document).ready(function () {
    function cargarCursos() {
        return $.ajax({
            url: '/obtener_cursos',
            type: 'GET',
            contentType: 'application/json',
            success: function (response) {
                $('#filtro_cursos, #cursoGrupo').empty();
                $('#filtro_cursos').append($('<option>', { value: '', text: 'Todos los cursos' }));
                $('#cursoGrupo').append($('<option>', { value: '', text: 'Seleccionar curso' }));
                response.forEach(function (curso) {
                    $('#filtro_cursos, #cursoGrupo').append($('<option>', {
                        value: curso.nombre, // Asegúrate de que el valor sea el nombre del curso
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
                $('#semestreGrupo').empty();
                $('#semestreGrupo').append($('<option>', { value: '', text: 'Seleccionar semestre' }));
                response.forEach(function (semestre) {
                    $('#semestreGrupo').append($('<option>', {
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

    function cargarSelects() {
        return $.when(cargarCursos(), cargarSemestres());
    }

    cargarCursos();
    cargarSemestres();

    // Supongamos que tienes una función para editar grupo
    window.cargarDatosEnModal = function (grupo) {
        console.log(grupo);
        cargarSelects().done(function() {
            $('#grupoId').val(grupo.id_grupo);
            $('#nombreGrupo').val(grupo.nombre);
            $('#vacantesGrupo').val(grupo.vacantes);
            $('#semestreGrupo').val(grupo.idsemestre).change();

            // Buscar y seleccionar el curso por su nombre
            $('#cursoGrupo option').each(function() {
                if ($(this).text() === grupo.curso) {
                    $(this).prop('selected', true);
                }
            });

            $('#modalGrupoLabel').text('Modificar Grupo');
            $('#modalGrupo').modal('show');
        });
    };

    $('#formGrupo').on('submit', function (event) {
        event.preventDefault();
        const idGrupo = $('#grupoId').val();
        const formData = {
            id: idGrupo,
            nombre: $('#nombreGrupo').val(),
            vacantes: $('#vacantesGrupo').val(),
            idcurso: $('#cursoGrupo').val(),
            idsemestre: $('#semestreGrupo').val()
        };
        const url = idGrupo ? '/modificar_grupo' : '/agregar_grupo';
        const mensajeConfirmacion = idGrupo ? 'modificar' : 'agregar';

        Swal.fire({
            title: `¿Estás seguro de ${mensajeConfirmacion} este grupo?`,
            icon: 'warning',
            showCancelButton: true,
            confirmButtonColor: '#3085d6',
            cancelButtonColor: '#d33',
            confirmButtonText: `Sí, ${mensajeConfirmacion}`,
            cancelButtonText: 'Cancelar'
        }).then((result) => {
            if (result.isConfirmed) {
                $.ajax({
                    url: url,
                    type: 'POST',
                    contentType: 'application/json',
                    data: JSON.stringify(formData),
                    success: function (response) {
                        Swal.fire(
                            '¡Éxito!',
                            `El grupo ha sido ${mensajeConfirmacion}do exitosamente.`,
                            'success'
                        );
                        $('#modalGrupo').modal('hide');
                        $('#tabla-grupo').DataTable().ajax.reload();
                    },
                    error: function (xhr, status, error) {
                        Swal.fire(
                            '¡Error!',
                            `Hubo un problema al ${mensajeConfirmacion} el grupo. Inténtalo nuevamente.`,
                            'error'
                        );
                    }
                });
            }
        });
    });

    var table = $('#tabla-grupo').DataTable({
        ajax: {
            url: "/get_grupos",
            dataSrc: ""
        },
        paging: false,
        info: false,
        responsive: true,
        autoWidth: true,
        searching: true,
        scrollY: "600px",
        dom: 'Bfrtip',
        buttons: [
            {
                extend: 'collection',
                text: '<i class="fas fa-file-export"></i> Exportar/Imprimir',
                className: 'btn btn-secondary',
                buttons: [
                    {
                        extend: 'copy',
                        text: '<i class="fas fa-copy"></i> Copiar',
                        className: 'dropdown-item',
                        exportOptions: {
                            columns: ':not(:last-child)'
                        }
                    },
                    {
                        extend: 'csv',
                        text: '<i class="fas fa-file-csv"></i> CSV',
                        className: 'dropdown-item',
                        exportOptions: {
                            columns: ':not(:last-child)'
                        }
                    },
                    {
                        extend: 'excel',
                        text: '<i class="fas fa-file-excel"></i> Excel',
                        className: 'dropdown-item',
                        exportOptions: {
                            columns: ':not(:last-child)'
                        }
                    },
                    {
                        extend: 'pdf',
                        text: '<i class="fas fa-file-pdf"></i> PDF',
                        className: 'dropdown-item',
                        exportOptions: {
                            columns: ':not(:last-child)'
                        }
                    },
                    {
                        extend: 'print',
                        text: '<i class="fas fa-print"></i> Imprimir',
                        className: 'dropdown-item',
                        exportOptions: {
                            columns: ':not(:last-child)'
                        }
                    }
                ]
            },
            {
                text: '<i class="fas fa-plus"></i> Agregar Nuevo Grupo',
                className: 'btn_agregar_grupo',
                action: function (e) {
                    e.preventDefault();
                    $('#formGrupo')[0].reset();
                    $('#grupoId').val(''); // Limpiar el valor de grupoId
                    cargarSelects().done(function() {
                        $('#modalGrupoLabel').text('Agregar Grupo');
                        $('#modalGrupo').modal('show');
                    });
                }
            }
        ],
        columns: [
            { data: "nombre", "className": "dt-center" },
            { data: "vacantes", "className": "" },
            { data: "curso", "className": "dt-left" },
            { data: "descripcion", "className": "dt-center" },
            {
                data: null,
                defaultContent: "<button class='btn btn-warning' title='Modificar'><i class='fas fa-pencil-alt'></i></button> <button class='btn btn-danger' title='Eliminar'><i class='fas fa-times'></i></button>"
            },
        ],
        // columnDefs: [
        //     { "className": "dt-center", "targets": "_all" }
        // ],
        language: {
            url: "https://cdn.datatables.net/plug-ins/1.13.7/i18n/es-ES.json"
        }
    });

    $('#filtro_cursos').on('change', function () {
        var filtro = $(this).val();
        table.column(2).search(filtro).draw();
    });

    $('#tabla-grupo tbody').on('click', 'button', function () {
        var data = table.row($(this).parents('tr')).data();
        if ($(this).hasClass('btn-warning')) {
            cargarDatosEnModal(data);
        } else if ($(this).hasClass('btn-danger')) {
            Swal.fire({
                title: '¿Estás seguro de eliminar este grupo?',
                text: `El grupo ${data.nombre} será eliminado permanentemente.`,
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
                        data: JSON.stringify({ id_grupo: data.id_grupo }),
                        success: function (response) {
                            Swal.fire(
                                '¡Eliminado!',
                                'El grupo ha sido eliminado exitosamente.',
                                'success'
                            );
                            table.ajax.reload();
                        },
                        error: function (xhr, status, error) {
                            Swal.fire(
                                '¡Error!',
                                'Hubo un problema al eliminar el grupo. Inténtalo nuevamente.',
                                'error'
                            );
                        }
                    });
                }
            });
        }
    });
});
