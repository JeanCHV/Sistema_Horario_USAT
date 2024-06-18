let logoutTimer;
let warningTimer;

function resetLogoutTimer() {
    clearTimeout(logoutTimer);
    clearTimeout(warningTimer);

    warningTimer = setTimeout(showWarning, 50000); // Mostrar advertencia después de 50 segundos
    logoutTimer = setTimeout(logoutUser, 60000); // Cerrar sesión después de 60 segundos
}

function showWarning() {
    Swal.fire({
        icon: 'warning',
        title: 'Inactividad Detectada',
        text: 'Su sesión se cerrará en 10 segundos si no hay actividad.',
        timer: 10000,
        timerProgressBar: true,
        onClose: () => {
            if (document.hidden) {
                logoutUser();
            } else {
                resetLogoutTimer();
            }
        }
    });
}

function logoutUser() {
    Swal.fire({
        icon: 'info',
        title: 'Sesión Cerrada',
        text: 'Su sesión ha sido cerrada por inactividad.',
        timer: 2000,
        onClose: () => {
            window.location.href = '/logout';
        }
    });
}

document.addEventListener('mousemove', resetLogoutTimer);
document.addEventListener('keypress', resetLogoutTimer);
document.addEventListener('click', resetLogoutTimer);
document.addEventListener('scroll', resetLogoutTimer);

// Iniciar el temporizador la primera vez
resetLogoutTimer();
