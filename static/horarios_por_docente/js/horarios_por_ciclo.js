document.addEventListener('DOMContentLoaded', function () {
    const div_loading = document.querySelector('#loading');
    const espacio_tabla = document.querySelector("#espacio_tabla");
    const combo_semestre = document.querySelector("#combo_semestre");
    const combo_ciclo = document.querySelector("#combo_ciclo");

    const columna_horas = [];
    for (let i = 7; i < 23; i++) {
        columna_horas.push(`${i.toString().padStart(2, '0')}:00 - ${(i+1).toString().padStart(2, '0')}:00`);
    }

    const columna_dias = ['Lunes', 'Martes', 'Miércoles', 'Jueves', 'Viernes', 'Sábado'];

    combo_semestre.addEventListener('change', fetchHorarios);
    combo_ciclo.addEventListener('change', fetchHorarios);

    function fetchHorarios() {
        const semestre = combo_semestre.value;
        const ciclo = combo_ciclo.value;

        if (semestre !== "-1" && ciclo !== "-1") {
            div_loading.style.display = "block";

            obtenerHorariosxCiclo(ciclo, semestre)
                .then(horarios => {
                    div_loading.style.display = "none";
                    console.log('Horarios obtenidos:', horarios);
                    crearTablaHorario(horarios,ciclo,semestre);
                })
                .catch(error => {
                    div_loading.style.display = "none";
                    console.error('Error al obtener horarios:', error);
                });
        }
    }

    function obtenerHorariosxCiclo(ciclo, semestre) {
        return fetch('/obtener_horarios_semestre_ciclo', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({
                ciclo: ciclo,
                semestre: semestre
            })
        })
        .then(response => response.json())
        .catch(error => {
            console.error('Error al obtener horarios:', error);
        });
    }

    function crearTablaHorario(horarios_ciclo,ciclo,semestre) {
        espacio_tabla.innerHTML = ''; // Limpiar la tabla existente

        if (horarios_ciclo.length === 0) {
            espacio_tabla.innerHTML = `<p>No hay horarios registrados</p>`;
            return;
        }

        const tabla = document.createElement('table');
        tabla.className = 'table';

        const thead = document.createElement('thead');
        const tbody = document.createElement('tbody');
        tabla.appendChild(thead);
        tabla.appendChild(tbody);

        const fila_ciclo = document.createElement('tr');
        fila_ciclo.innerHTML = `<th data-horario="nombre_docente" colspan="8">Ciclo Académico ${ciclo} -  Semestre: ${semestre}</th>`;
        thead.appendChild(fila_ciclo);

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
                const horario = horarios_ciclo.find(h => 
                    h.dia.normalize("NFD").replace(/[\u0300-\u036f]/g, "").trim().toUpperCase() === dia.normalize("NFD").replace(/[\u0300-\u036f]/g, "").trim().toUpperCase() &&
                    parseInt(h.horainicio.substring(0, 2)) <= parseInt(hora.substring(0, 2)) &&
                    parseInt(h.horafin.substring(0, 2)) > parseInt(hora.substring(0, 2))
                );

                if (horario) {
                    celda.innerHTML = `
                    <span>${horario.curso} <br> <span class="docente-nombre">${horario.docente}</span> </span>
                    <span> Grupo ${horario.grupo}</span>
                    <span>${horario.escuela}</span>
                    <span data-tipo="${horario.tipoCurso}">${horario.tipoCurso}</span>
                    <span>${horario.ambiente}</span>
                `;
                }

                fila.appendChild(celda);
            });

            tbody.appendChild(fila);
        });

        espacio_tabla.appendChild(tabla);
    }
});
