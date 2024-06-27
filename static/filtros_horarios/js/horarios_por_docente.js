const span_mensaje_error = document.querySelector("span[data-mensaje-error]");
const div_loading = document.querySelector('#loading');
const espacio_tabla = document.querySelector("#espacio_tabla");
const panel_docentes = document.querySelector("#panel_docentes");
const etiquetas_docentes_seleccionados = document.querySelector("#etiquetas_docentes_seleccionados");
const columna_horas = [];
for (let i = 7; i < 23; i++) {
    columna_horas.push(`${i.toString().padStart(2, '0')}:00 - ${(i + 1).toString().padStart(2, '0')}:00`);
}

const columna_dias = ['Lunes', 'Martes', 'Miércoles', 'Jueves', 'Viernes', 'Sábado', 'Domingo'];
let bmos_lista_datos = [];

function mostrarAlerta(icon, title, text) {
    Swal.fire({
        icon: icon,
        title: title,
        text: text
    });
}

function mostrarFotoDocente(idpersona) {
    fetch(`/obtener_docente_por_id/${idpersona}`)
        .then(response => {
            if (!response.ok) {
                throw new Error(`HTTP error! status: ${response.status}`);
            }
            return response.json();
        })
        .then(data => {
            if (data.foto === null) {
                document.getElementById("foto_perfil").src = "/static/img/USUARIO.jpg";
            } else {
                var img = new Image();
                img.src = "/static/img/" + data.foto;
                img.onload = function() {
                    document.getElementById("foto_perfil").src = img.src;
                }
                img.onerror = function() {
                    document.getElementById("foto_perfil").src = "/static/img/USUARIO.jpg";
                }
            }         
        })
        .catch(error => {
            console.error('Error al obtener la foto del docente:', error);
            document.getElementById("foto_perfil").src = "/static/img/USUARIO.jpg";
        });
}



function obtener_docentes() {
    fetch('/get_personas_docentes_activas', {
        headers: {
            'Content-Type': 'application/json'
        },
    })
        .then(response => response.json())
        .then(data => {
            bmos_lista_datos = data;
        })
        .catch(error => {
            mostrarAlerta("error", "No se pudo obtener los horarios", error.responseText);
        });
}

$(document).ready(function () {
    obtener_docentes();
    $('#collapseOne').collapse('show');
    combo_semestre.focus();
});

/*INICIO SCRIPT BUSCADOR*/

const bmos_contenedor = document.querySelector("#buscador-multiopcion-sugerencias");
const bmos_barra_busqueda = document.querySelector("#bmos-barra-busqueda");
const bmos_input = bmos_barra_busqueda.querySelector("p");
var bmos_lista_sugerencias = document.querySelector("#bmos-lista-sugerencias");
var combo_semestre = document.querySelector("#combo_semestre");
let index = -1;

combo_semestre.addEventListener('change', () => {
    index = -1;
    if (combo_semestre.value === "-1") {
        bmos_input.contentEditable = false;
        span_mensaje_error.textContent = "Debe seleccionar un semestre para escribir";
    } else {
        bmos_input.contentEditable = true;
        span_mensaje_error.textContent = "";

        var tabs = document.querySelectorAll('div.docente-tab');
        if (tabs.length > 0) {
            div_loading.style.display = "block";
            tabs.forEach(tab => {
                var id_docente = tab.id.substring(4);
                var nombre_docente = tab.textContent.slice(0, -1);
                var semestre = combo_semestre.value;
                let horarios = obtenerHorariosDocente(id_docente, semestre)
                    .then(horarios => {
                        mostrarHorario(id_docente, nombre_docente, horarios, semestre); 
                        if(tab.classList.contains('activo')){
                            tab.click();
                        }
                        div_loading.style.display = "none";
                    })
                    .catch(error => {
                        console.error('Error al obtener horarios:', error);
                        if(tab.classList.contains('activo')){
                            tab.click();
                        }
                        div_loading.style.display = "none";
                    });
            });
        }
        bmos_input.focus();
    }
});

bmos_input.onkeyup = (event) => {
    let datos_entrada = bmos_input.textContent;
    let datos_salida = [];

    if (datos_entrada.length) {
        bmos_contenedor.classList.add("active");
        datos_salida = bmos_generar_sugerencias(datos_entrada);
        datos_filtrados = bmos_filtrar_sugerencias(datos_salida);
        bmos_mostrar_sugerencias(datos_filtrados);

    } else {
        bmos_contenedor.classList.remove("active");
    }
};

function bmos_generar_sugerencias(dato) {
    let datos_salida = [];
    bmos_lista_datos.forEach(element => {
        var nombre = element[2] + " " + element[1];
        var id = element[0];

        if (nombre.toLowerCase().trim().includes(dato.toLowerCase().trim())) {
            datos_salida.push([id, nombre]);
        }
    });
    return datos_salida;
}

function bmos_mostrar_sugerencias(lista) {
    bmos_lista_sugerencias.innerHTML = "";
    lista.forEach(element => {
        bmos_lista_sugerencias.innerHTML +=
            `<li class="bmos-sugerencia" onclick="bmos_insertar_etiqueta(this);"
            id="${element[0]}">${element[1]}</li>`;
    });
}

function bmos_insertar_etiqueta(element) {
    if (element.id != -1) {
        bmos_input.textContent = "";
        bmos_contenedor.classList.remove("active");

        var nuevoSpan = document.createElement("span");
        nuevoSpan.className = "bmos-etiqueta-seleccionada";
        nuevoSpan.setAttribute("contenteditable", "false");
        nuevoSpan.setAttribute("id", `${element.id}`);
        nuevoSpan.innerHTML = `${element.textContent}<button data-etiqueta="${element.id}" onclick="bmos_eliminarEtiqueta(this);">X</button>`;

        var combo_semestre = document.querySelector("#combo_semestre");
        div_loading.style.display = "block";
        let horarios = obtenerHorariosDocente(element.id, combo_semestre.value)
            .then(horarios => {
                agregarDocentePanel(element.id, element.textContent, horarios, combo_semestre.value);
                etiquetas_docentes_seleccionados.appendChild(nuevoSpan);
                bmos_input.focus();
                mostrarFoto(element.textContent);
                div_loading.style.display = "none";
            })
            .catch(error => {
                console.error('Error al obtener horarios:', error);
                div_loading.style.display = "none";
            });
    }
}

function bmos_eliminarEtiqueta(element) {
    div_loading.style.display = "block";
    var id_docente = element.getAttribute("data-etiqueta");
    var tab_docente = document.querySelector(`#tab_${id_docente}`);
    if (tab_docente !== null) {
        tab_docente.remove();
    }
    element.parentNode.remove();
    espacio_tabla.innerHTML = "";
    mostrarFoto("");
    div_loading.style.display = "none";
}

function bmos_filtrar_sugerencias(lista_sugerencias) {
    let sugerencias_filtadas = lista_sugerencias.slice();
    if (sugerencias_filtadas.length > 0) {
        let nombres_seleccionados = [];
        bmos_barra_busqueda.querySelectorAll('.bmos-etiqueta').forEach(etiqueta => {
            let nombre = etiqueta.textContent.trim().slice(0, -1).toLowerCase();
            nombres_seleccionados.push(nombre);
        });

        sugerencias_filtadas = sugerencias_filtadas.filter(sugerencia => {
            let nombre_sugerencia = sugerencia[1].toLowerCase().trim();
            return !nombres_seleccionados.includes(nombre_sugerencia);
        });
    } else {
        sugerencias_filtadas.push([-1, "No hay resultados"]);
    }
    return sugerencias_filtadas;
}

bmos_barra_busqueda.addEventListener("click", () => {
    bmos_input.focus();
});

bmos_barra_busqueda.addEventListener("keydown", function (event) {
    if (event.key === "Enter") {
        event.preventDefault();
    }
});

document.addEventListener("click", (event) => {
    const buscadorMultiopcion = document.querySelector("#buscador-multiopcion-sugerencias");
    if (!buscadorMultiopcion.contains(event.target)) {
        buscadorMultiopcion.classList.remove("active");
    }
});

/*FIN SCRIPT BUSCADOR*/

/*INICIO SCRIPT MOSTRAR MENUS*/

function obtenerHorariosDocente(id_docente, semestre) {
    return fetch('/get_horarios_docentesId_semestre', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({
            id_docente: id_docente,
            semestre: semestre
        })
    })
        .then(response => response.json())
        .catch(error => {
            console.error('Error al obtener horarios:', error);
        });
}

function agregarDocentePanel(idpersona, nombre_docente, horarios_docente, semestre) {
    var tabExistente = document.querySelector(`#tab_${idpersona}`);
    if (tabExistente !== null) {
        tabExistente.remove();
    }

    let tab = document.createElement("div");
    tab.className = "docente-tab";
    tab.classList.add('activo');
    tab.id = `tab_${idpersona}`;

    // Crear el contenido del div con el nombre del docente y el botón de eliminación
    tab.innerHTML = `${nombre_docente} <span class="eliminar-docente">X</span>`;
    
    // Añadir evento de click para eliminar el docente seleccionado
    tab.querySelector(".eliminar-docente").addEventListener("click", (event) => {
        event.stopPropagation(); // Evitar que el click en la "X" dispare el evento del tab
        tab.remove();
        // Limpiar la tabla de horarios si es la del docente eliminado
        var tabla_existente = document.querySelector(`#horario_${idpersona}`);
        if (tabla_existente !== null) {
            tabla_existente.remove();
        }
        espacio_tabla.innerHTML = "";
        document.getElementById("foto_perfil").src = "/static/img/USUARIO.jpg"; // Restablecer la foto de perfil por defecto
    });

    tab.onclick = () => {
        desmarcarTabsTodos();
        tab.classList.add('activo');
        div_loading.style.display = "block";
        let horariosX = obtenerHorariosDocente(idpersona, combo_semestre.value)
            .then(horariosX => {
                mostrarHorario(idpersona, nombre_docente, horariosX, combo_semestre.value);
                mostrarFotoDocente(idpersona); // Mostrar la foto del docente seleccionado
                bmos_input.focus();
                div_loading.style.display = "none";
            })
            .catch(error => {
                mostrarHorario(idpersona, nombre_docente, horariosX, combo_semestre.value);
                mostrarFotoDocente(idpersona); // Mostrar la foto del docente seleccionado
                bmos_input.focus();
                console.error('Error al obtener horarios:', error);
                div_loading.style.display = "none";
            });
    };

    desmarcarTabsTodos();
    panel_docentes.appendChild(tab);
    mostrarHorario(idpersona, nombre_docente, horarios_docente, semestre);
    mostrarFotoDocente(idpersona); // Mostrar la foto del docente seleccionado al agregar el panel
}


function desmarcarTabsTodos(){
    var tabs = document.querySelectorAll('div.docente-tab');
        tabs.forEach(tab=>{
            if(tab.classList.contains('activo')){
                tab.classList.remove('activo');
            }
        })
}



function mostrarHorario(id_docente, nombre_docente, horarios_docente, semestre) {
    var tabla_existente = document.querySelector(`#horario_${id_docente}`);
    if (tabla_existente !== null) {
        tabla_existente.remove();
    }
    espacio_tabla.innerHTML = `<table id="horario_${id_docente}"><thead><tr><th data-horario="nombre_docente" colspan="8">${nombre_docente} - Semestre ${semestre}</th></tr>
    </thead><tbody></tbody></table>`;
    var thead_tabla = document.querySelector(`#horario_${id_docente} thead`);
    var tbody_tabla = document.querySelector(`#horario_${id_docente} tbody`);

    if (!horarios_docente.length) {
        tbody_tabla.innerHTML += `<tr><td colspan="8" data-horario="Sin horarios">No hay horarios registrados</td></tr>`;
    } else {
        var columna_hora_dia = '<tr><th>Horas</th>';
        columna_hora_dia += columna_dias.map(dia => `<th>${dia}</th>`).join('');
        columna_hora_dia += '</tr>';
        thead_tabla.innerHTML += columna_hora_dia;
        for (let i = 0; i < columna_horas.length; i++) {
            var fila = `<tr><td>${columna_horas[i]}</td>`;
            var h_inicio_tabla = parseInt(columna_horas[i].substring(0, 2));
            var h_fin_tabla = h_inicio_tabla + 1;
            for (let j = 0; j < columna_dias.length; j++) {
                fila += "<td>";
                var dia_tabla = columna_dias[j].normalize("NFD").replace(/[\u0300-\u036f]/g, "").trim().toUpperCase();
                for (let k = 0; k < horarios_docente.length; k++) {
                    var dia_horario = horarios_docente[k][3].normalize("NFD").replace(/[\u0300-\u036f]/g, "").trim().toUpperCase();
                    var h_inicio_horario = parseInt(horarios_docente[k][4].substring(0, 2));
                    var h_fin_horario = parseInt(horarios_docente[k][5].substring(0, 2));
                    if (dia_horario === dia_tabla && h_inicio_tabla >= h_inicio_horario && h_fin_tabla <= h_fin_horario) {
                        var curso = horarios_docente[k][2];
                        var ciclo = horarios_docente[k][10];
                        var carrera = horarios_docente[k][11];
                        var grupo = horarios_docente[k][9];
                        var tipo = horarios_docente[k][8];
                        var ambiente = horarios_docente[k][1];
                        fila += `<span>${curso}</span>`;
                        fila += `<span>(${ciclo} ciclo - Grupo ${grupo})</span>`;
                        fila += `<span>${carrera}</span>`;
                        fila += `<span data-tipo="${tipo}">${tipo}</span>`;
                        fila += `<span>${ambiente}</span>`;
                    }
                }
                fila += "</td>";
            }
            tbody_tabla.innerHTML += fila;
        }
    }
}

/*FIN SCRIPT MOSTRAR MENUS*/

bmos_input.addEventListener('keyup', (event) => {
    if (bmos_input.textContent.length > 0) {
        bmos_input.focus();
        if (document.activeElement === bmos_input && event.key === 'ArrowDown') {
            let sugerencias = document.querySelectorAll('#bmos-lista-sugerencias .bmos-sugerencia');
            event.preventDefault();
            index = Math.min(index + 1, sugerencias.length - 1);
            sugerencias[index].classList.add('seleccionado');
            sugerencias[index].focus();
            if (index > 0) {
                sugerencias[index - 1].classList.remove('seleccionado');
            }
        } else if (document.activeElement === bmos_input && event.key === "ArrowUp") {
            let sugerencias = document.querySelectorAll('#bmos-lista-sugerencias .bmos-sugerencia');
            event.preventDefault();
            index = Math.max(index - 1, 0);
            sugerencias[index].focus();
            sugerencias[index].classList.add('seleccionado');
            if (index < sugerencias.length - 1) {
                sugerencias[index + 1].classList.remove('seleccionado');
            }
        }

        if (document.activeElement === bmos_input && event.key === 'Enter' && index !== -1) {
            let sugerencias = document.querySelectorAll('#bmos-lista-sugerencias .bmos-sugerencia');
            event.preventDefault();
            sugerencias[index].click();
            index = -1;
        }
    }
});
