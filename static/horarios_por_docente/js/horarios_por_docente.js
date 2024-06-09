const espacio_tabla = document.querySelector("#espacio_tabla");
const columna_horas=[];
for (let i = 7; i < 23; i++) {
        columna_horas.push(`${i.toString().padStart(2, '0')}:00 - ${(i+1).toString().padStart(2, '0')}:00`);
    }

const columna_dias=['Lunes','Martes','Miércoles','Jueves','Viernes','Sábado'];
let bmos_lista_datos = [];

    function mostrarAlerta(icon, title, text) {
        Swal.fire({
            icon: icon,
            title: title,
            text: text
        });
    }

    function mostrarFoto(nombre_foto) {
        nombre_foto = nombre_foto.toUpperCase().replace(/ /g, "_");
        nombre_formateado = nombre_foto.normalize("NFD").replace(/[\u0300-\u036f]/g, "");

        var img = new Image();
        img.src = "/static/img/" + nombre_formateado + ".jpg";

        img.onload = function() {
            document.getElementById("foto_perfil").src = img.src;
        };
        
        img.onerror = function() {
            document.getElementById("foto_perfil").src = "/static/img/USUARIO.jpg";
        };
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

$(document).ready(function(){
    obtener_docentes();
    $('#collapseOne').collapse('show');
});



/*INICIO SCRIPT BUSCADOR*/

const bmos_contenedor = document.querySelector("#buscador-multiopcion-sugerencias");
const bmos_barra_busqueda = document.querySelector("#bmos-barra-busqueda");
const bmos_etiquetas_busqueda = bmos_barra_busqueda.querySelectorAll(".bmos-etiqueta");
const bmos_input = bmos_barra_busqueda.querySelector("p");
const bmos_lista_sugerencias = document.querySelector("#bmos-lista-sugerencias");


bmos_input.onkeyup = (event) => {
    let datos_entrada = bmos_input.textContent;
    let datos_salida = [];

    if(datos_entrada.length){
        bmos_contenedor.classList.add("active");
        datos_salida = bmos_generar_sugerencias(datos_entrada);
        datos_filtrados = bmos_filtrar_sugerencias(datos_salida);
        bmos_mostrar_sugerencias(datos_filtrados);

    }else{
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


function bmos_mostrar_sugerencias(lista){
    bmos_lista_sugerencias.innerHTML = "";
    lista.forEach(element => {
        bmos_lista_sugerencias.innerHTML += 
        `<li class="bmos-sugerencia" onclick="bmos_insertar_etiqueta(this);"
            id="${element[0]}">${element[1]}</li>`;
    });
}

function bmos_insertar_etiqueta(element){
    if(element.id != -1){
        bmos_input.textContent = "";
        bmos_contenedor.classList.remove("active");
        var nuevoSpan = document.createElement("span");
        nuevoSpan.className = "bmos-etiqueta";
        nuevoSpan.setAttribute("contenteditable", "false");
        nuevoSpan.setAttribute("id",`${element.id}`);
        nuevoSpan.innerHTML = `${element.textContent}<button data-etiqueta="${element.id}" onclick="bmos_eliminarEtiqueta(this);">X</button>`;       
        bmos_barra_busqueda.appendChild(nuevoSpan);
        bmos_input.focus();
        let horarios = obtenerHorariosDocente(element.id, document.querySelector("#combo_semestre").value)
            .then(horarios => {
                crearTablaHorario(element.id,element.textContent,horarios);
            })
            .catch(error => {
                console.error('Error al obtener horarios:', error);
            });
    }
}

function bmos_eliminarEtiqueta(element){
    var id_docente = element.getAttribute("data-etiqueta");
    document.querySelector(`#horario_${id_docente}`).remove();
    element.parentNode.remove();
}

function bmos_filtrar_sugerencias(lista_sugerencias) {
    let sugerencias_filtadas = lista_sugerencias.slice();
    if (sugerencias_filtadas.length > 0) {
        let nombres_sugerencias = sugerencias_filtadas.map(element => element[1].toLowerCase().trim());

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

bmos_barra_busqueda.addEventListener("click",()=>{
    bmos_input.focus();
});


bmos_barra_busqueda.addEventListener("keydown",function(event){
    if(event.key === "Enter"){
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

/*INICIO SCRIPT MOSTRAR TABLAS*/

function obtenerHorariosDocente(id_docente,semestre){
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

function crearTablaHorario(id_docente,nombre_docente,horarios_docente){
    var tabla_existente = document.querySelector(`#horario_${id_docente}`);
    if(tabla_existente !== null){
        tabla_existente.remove();
    }
    espacio_tabla.innerHTML += `<table id="horario_${id_docente}"><thead><tr><th colspan="8">${nombre_docente}</th></tr>
        <tr><th>Horas</th></tr></thead><tbody></tbody></table>`;
    var thead_tabla = document.querySelector(`#horario_${id_docente} thead tr:nth-child(2)`);
    var tbody_tabla = document.querySelector(`#horario_${id_docente} tbody`);
    thead_tabla.innerHTML += columna_dias.map(dia => `<th>${dia}</th>`).join('');

    if(!horarios_docente.length){
        tbody_tabla.innerHTML +=`<tr><td colspan="8">No hay horarios registrados</td></tr>`;
    }else{
        for(let i=0; i<columna_horas.length; i++){
            var fila = `<tr><td>${columna_horas[i]}</td>`;
            var h_inicio_tabla = parseInt(columna_horas[i].substring(0,2));
            var h_fin_tabla = h_inicio_tabla+1;
            for(let j=0; j<columna_dias.length; j++){
                fila += "<td>";
                var dia_tabla = columna_dias[j].normalize("NFD").replace(/[\u0300-\u036f]/g, "").trim().toUpperCase();
                for(let k=0; k<horarios_docente.length; k++){
                    var dia_horario = horarios_docente[k][3].normalize("NFD").replace(/[\u0300-\u036f]/g, "").trim().toUpperCase();
                    var h_inicio_horario = parseInt(horarios_docente[k][4].substring(0,2)); 
                    var h_fin_horario = parseInt(horarios_docente[k][5].substring(0,2));
                    if (dia_horario===dia_tabla && h_inicio_tabla>=h_inicio_horario && h_fin_tabla<=h_fin_horario){
                        var curso = horarios_docente[k][2];
                        var ciclo = horarios_docente[k][10];
                        var carrera = horarios_docente[k][11];
                        var grupo = horarios_docente[k][9];
                        var tipo = horarios_docente[k][8];
                        var ambiente = horarios_docente[k][1];
                        fila+= `<span>${curso}</span>`;
                        fila+= `<span>(${ciclo} ciclo - Grupo ${grupo})</span>`;
                        fila+= `<span>${carrera}</span>`;
                        fila+=`<span data-tipo="${tipo}">${tipo}</span>`;
                        fila+=`<span>${ambiente}</span>`;
                    }   
                }
                fila+="</td>";
            }
            tbody_tabla.innerHTML+= fila;
        }
    }
}

/*FIN SCRIPT MOSTRAR TABLAS*/