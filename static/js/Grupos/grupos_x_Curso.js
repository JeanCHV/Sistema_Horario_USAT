$(document).ready(function () {
    var table = $('#tabla-cursos').DataTable({
        paging: false,
        info: false,
        responsive: true,
        autoWidth: true,
        searching: true,
        scrollY: "400px",

        columns: [
            { data: "idcurso", className: "text-center id" },
            { data: "nombre" },
            { data: "ciclo", className: "text-center" },
            {
                data: "total_grupos",
                render: function (data, type, row) {
                    return `<input type="number" value="${data}" class="numeric-input form-control bg-white text-black mx-auto text-center grupos" style="width:80px">`;
                },
                className: "text-center"
            },
            {
                data: null,
                render: function (data, type, row) {
                    return `<input type="checkbox" class="form-check-input me-3 border border-dark che">`;
                },
                className: "text-center",
                "orderable": false
            }
        ],
        language: {
            "url": "https://cdn.datatables.net/plug-ins/1.13.7/i18n/es-ES.json"
        }
    });

    // Eliminamos el atributo "step" de los campos numéricos al inicializar la tabla
    table.on('draw.dt', function () {
        // Asignar evento 'click' a los inputs de tipo número con clase 'numeric-input'
        $('.numeric-input').off('input').on('input', function () {
            valida(this);
        });
    });

    function valida(element) {
        var padre = element.parentNode.parentNode;
        var checkbox = padre.querySelector('.che');
        var valor = parseInt(element.value, 10);
        if (valor > 0 && valor < 28) {
            checkbox.checked = true;
            checkbox.disabled = false;
        } else {
            checkbox.checked = false;
            checkbox.disabled = true;
        }
    }

    window.rellenarTabla = function (escuela, semestre) {
        fetch(`/rellenar_tabla/${escuela}/${semestre}`)
            .then(response => response.json())
            .then(data => {
                table.clear();
                table.rows.add(data);
                table.draw();
            })
            .catch(error => {
                console.error('Error al obtener los datos de la tablas:', error);
            });
    };

    function grupos(datos) {
        return fetch('/mantenimiento_grupos', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(datos)
        })
            .then(response => response.json());
    }

    window.seleccionar_toda = function () {
        var checkbox = document.getElementById('est');
        var isChecked = checkbox.checked;
        var input_check = document.querySelectorAll('input[type="checkbox"]');
        for (var i = 0; i < input_check.length; i++) {
            input_check[i].checked = isChecked;
        }
    };

    window.dato_selecciondo = function () {
        var input_check = document.querySelectorAll('td input[type="checkbox"]');
        var semestre = document.getElementById('semestre').value;
        var escuela = document.getElementById('escuela').value;
        var datos = {
            "escuela": escuela,
            "semestre": semestre,
            "valores": []
        };
        for (var i = 0; i < input_check.length; i++) {
            if (input_check[i].checked) {
                var padre = input_check[i].parentElement.parentElement;
                var valor = padre.querySelector('.grupos').value;
                var id_v = padre.querySelector('.id').textContent;
                datos.valores.push({
                    "id": id_v,
                    "valor": valor
                });
            }
        }

        if (datos.valores.length === 0) {
            // Mostrar un mensaje si no se ha seleccionado ningún checkbox
            Swal.fire({
                title: 'Error',
                text: 'Debe seleccionar al menos un grupo para modificar.',
                icon: 'error',
                confirmButtonText: 'Ok'
            });
            return;
        }

        Swal.fire({
            title: '¿Seguro de querer modificar grupos?',
            text: "No podrás revertir esta acción.",
            icon: 'warning',
            showCancelButton: true,
            buttonsStyling: false,
            confirmButtonText: 'Sí, modificar',
            cancelButtonText: 'Cancelar',
            customClass: {
                confirmButton: 'btn btn-primary me-2',
                cancelButton: 'btn btn-danger'
            },
            showLoaderOnConfirm: true,
            preConfirm: () => {
                return grupos(datos).then(data => {
                    if (data) {
                        return data;
                    } else {
                        throw new Error(data.message);
                    }
                }).catch(error => {
                    Swal.showValidationMessage(
                        `Request failed: ${error}`
                    );
                });
            },
            allowOutsideClick: () => !Swal.isLoading()
        }).then((result) => {
            if (result.isConfirmed) {
                Swal.fire({
                    title: 'Éxito',
                    text: 'Grupos modificados correctamente',
                    icon: 'success',
                    confirmButtonText: 'OK'
                }).then(() => {
                    // Desmarcar todos los checkboxes después de cerrar el cuadro de éxito
                    var input_check = document.querySelectorAll('td input[type="checkbox"]');
                    input_check.forEach(function (checkbox) {
                        checkbox.checked = false;
                    });
                });
                rellenarTabla(escuela, semestre);
            }
        });
    };

    window.validar = function () {
        var semestre = document.getElementById('semestre');
        var escuela = document.getElementById('escuela');
        if (semestre.selectedIndex > 0 && escuela.selectedIndex > 0) {
            rellenarTabla(escuela.value, semestre.value);
        }
    };
});
