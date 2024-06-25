document.addEventListener('DOMContentLoaded', function () {
    const div_loading = document.querySelector('#loading');
    const espacio_tabla = document.querySelector("#espacio_tabla");
    const combo_semestre = document.querySelector("#combo_semestre");
    const combo_edificio = document.querySelector("#combo_edificio");
    const combo_ambiente = document.querySelector("#combo_ambiente");
    const panel_ambientes = document.querySelector("#panel_ambientes");

    const columna_horas = [];
    for (let i = 7; i < 23; i++) {
        columna_horas.push(`${i.toString().padStart(2, '0')}:00 - ${(i + 1).toString().padStart(2, '0')}:00`);
    }

    const columna_dias = ['Lunes', 'Martes', 'Miércoles', 'Jueves', 'Viernes', 'Sábado'];
    combo_edificio.disabled = true;

    combo_edificio.addEventListener('change', fetchAmbientes);
    combo_ambiente.addEventListener('change', fetchHorarios);

    combo_semestre.addEventListener('change', function() {
        // Habilitar el combo de edificio solo si se ha seleccionado un semestre válido
        if (combo_semestre.value !== "-1") {
            combo_edificio.disabled = false;
        } else {
            combo_edificio.disabled = true;
        }
        fetchHorarios();
    });

    combo_edificio.addEventListener('change', function() {
        // Habilitar el combo de ambiente solo si se ha seleccionado un edificio válido
        if (combo_edificio.value !== "-1") {
            combo_ambiente.disabled = false;
        } else {
            combo_ambiente.disabled = true;
        }
        fetchHorarios();    
    });

    let ambientesMap = {};

    function fetchAmbientes() {
        const edificioId = combo_edificio.value;
        console.log("ID de Edificio Seleccionado:", edificioId);

        fetch('/ambientes_por_edificio/' + encodeURIComponent(edificioId))
            .then(response => response.json())
            .then(data => {
                console.log("Datos recibidos:", data);
                combo_ambiente.innerHTML = '<option value="-1" selected>[-- SELECCIONE --]</option>';
                ambientesMap = {};
                if (data.length > 0) {
                    data.forEach(ambiente => {
                        combo_ambiente.innerHTML += `<option value="${ambiente.idambiente}">${ambiente.nombre}</option>`;
                        ambientesMap[ambiente.idambiente] = ambiente.nombre;
                    });
                } else {
                    combo_ambiente.innerHTML += '<option>No hay ambientes disponibles</option>';
                }
            })
            .catch(error => {
                console.error("Error:", error);
                Swal.fire({
                    title: 'Error',
                    text: 'No se pudieron obtener los ambientes. Por favor, intente nuevamente.',
                    icon: 'error',
                    confirmButtonText: 'OK'
                });
            });
    }

    function fetchHorarios() {
        const semestre = combo_semestre.value;
        const ambiente = combo_ambiente.value;
        const nombreAmbiente = ambientesMap[ambiente];

        if (semestre !== "-1" && ambiente !== "-1") {
            div_loading.style.display = "block";

            obtenerHorariosxAmbiente(ambiente, semestre)
                .then(horarios => {
                    div_loading.style.display = "none";
                    agregarAmbientePanel(ambiente,nombreAmbiente,semestre, horarios);
                    resetCombos();
                })
                .catch(error => {
                    div_loading.style.display = "none";
                    console.error('Error al obtener horarios:', error);
                });
        }
    }

    function obtenerHorariosxAmbiente(ambiente, semestre) {
        return fetch('/obtener_horarios_por_ambiente', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({
                idambiente: ambiente,
                semestre: semestre
                
            })
        })
        .then(response => response.json())
        .catch(error => {
            console.error('Error al obtener horarios:', error);
        });
    }

    function agregarAmbientePanel(ambiente,nombreAmbiente, semestre, horarios) {
        const ambienteId = `${ambiente.replace(/\s+/g, '_')}_${semestre.replace(/\s+/g, '_')}`;
        const existente = document.querySelector(`#ambiente_${ambienteId}`);
        
        if (existente) {
            return;
        }
        
        const ambienteTab = document.createElement("div");
        ambienteTab.className = "ambientes-tab";
        ambienteTab.id = `ambiente_${ambienteId}`;
        ambienteTab.innerHTML = `${nombreAmbiente} - Semestre: ${semestre} <button class="eliminar-btn">&times;</button>`;
        ambienteTab.onclick = () => {
            document.querySelectorAll('.ambientes-tab').forEach(t => t.classList.remove('active'));
            ambienteTab.classList.add('active');
            crearTablaHorario(horarios, nombreAmbiente, semestre);
        };

        const eliminarBtn = ambienteTab.querySelector('.eliminar-btn');
        eliminarBtn.addEventListener('click', (e) => {
            e.stopPropagation(); // Evitar que se dispare el evento onclick del cicloTab
            eliminarAmbientePanel(ambienteId);
        });

        panel_ambientes.appendChild(ambienteTab);
        ambienteTab.click(); // Simulate a click to make it active initially
    }

    function eliminarAmbientePanel(ambienteId) {
        const ambienteTab = document.querySelector(`#ambiente_${ambienteId}`);
        if (ambienteTab) {
            ambienteTab.remove();
            espacio_tabla.innerHTML = ""; // Limpia el horario cuando se elimina un ambiente
        }
    }

    function resetCombos() {
        combo_ambiente.value = '-1';
        combo_semestre.value = '-1';
        combo_edificio.value = '-1';
    }

    function crearTablaHorario(horarios_ambiente, nombreAmbiente, semestre) {
        espacio_tabla.innerHTML = ''; // Limpiar la tabla existente

        if (horarios_ambiente.length === 0) {
            espacio_tabla.innerHTML = `<p>No hay horarios registrados</p>`;
            return;
        }

        const tabla = document.createElement('table');
        tabla.className = 'table';

        const thead = document.createElement('thead');
        const tbody = document.createElement('tbody');
        tabla.appendChild(thead);
        tabla.appendChild(tbody);

        const fila_ambiente = document.createElement('tr');
        fila_ambiente.innerHTML = `<th data-horario="nombre_docente" colspan="8">${nombreAmbiente} - Semestre: ${semestre}</th>`;
        thead.appendChild(fila_ambiente);

        // Crear encabezado de la tabla
        const fila_encabezado = document.createElement('tr');
        fila_encabezado.innerHTML = '<th>Horas</th>' + columna_dias.map(dia => `<th>${dia}</th>`).join('');
        thead.appendChild(fila_encabezado);

        // Crear cuerpo de la tabla
        columna_horas.forEach(hora => {
            const fila = document.createElement('tr');
            fila.innerHTML = `<td>${hora}</td>`;

            columna_dias.forEach(dia => {
                const celda = document.createElement('td');
                const horario = horarios_ambiente.find(h => 
                    h.dia.normalize("NFD").replace(/[\u0300-\u036f]/g, "").trim().toUpperCase() === dia.normalize("NFD").replace(/[\u0300-\u036f]/g, "").trim().toUpperCase() &&
                    parseInt(h.horainicio.substring(0, 2)) <= parseInt(hora.substring(0, 2)) &&
                    parseInt(h.horafin.substring(0, 2)) > parseInt(hora.substring(0, 2))
                );

                if (horario) {
                    celda.innerHTML = `
                    <span>${horario.curso} </span>
                    <span> (${horario.ciclo} Ciclo - Grupo ${horario.grupo})</span>
                    <span>${horario.escuela}</span>
                    <span data-tipo="${horario.tipoCurso}">${horario.tipoCurso}</span>
                    <span>${horario.docente}</span> 
                `;
                }

                fila.appendChild(celda);
            });

            tbody.appendChild(fila);
        });

        espacio_tabla.appendChild(tabla);
    }
});
