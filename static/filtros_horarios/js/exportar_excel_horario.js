document.addEventListener('DOMContentLoaded', function() {
    const btn_exportar_excel = document.querySelector("#btn-exportar-excel");

    if (btn_exportar_excel) {
        btn_exportar_excel.addEventListener("click", function() {
            const tabla = document.querySelector("#espacio_tabla table");
            if (tabla) {
                const wb = XLSX.utils.table_to_book(tabla, { sheet: "Horario" });
                const idpersona = tabla.id.replace("horario_", "");
                const nombreArchivo = `Horario_${idpersona}.xlsx`;
                XLSX.writeFile(wb, nombreArchivo);
            } else {
                alert("No hay horario para exportar o no seleccionó un docente.");
            }
        });
    }
});

