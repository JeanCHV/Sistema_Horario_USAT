/* 
function redireccionar(html) {
    var username = localStorage.getItem('username');
    var token = localStorage.getItem('token');

    if (!username || !token) {
        username = sessionStorage.getItem('username');
        token = sessionStorage.getItem('token');
    }

    if (!username || !token){
        window.location.href = '/login';
    }else{   
        fetch('/validar_login', {
            method: 'POST',
            headers: {
                'Content-type':'application/json'
            },
            body: JSON.stringify({
                username:username,
                token:token,
                html:html
            })
            })
            .then(response => response.json())
            .then(data =>{
                if (data.logeo){
                    window.location.href = '/'+html;
                }else{
                    window.location.href = '/login';
                }
            })
            .catch(error=>{
                window.location.href = '/login';
            });
    }     

    
} */


