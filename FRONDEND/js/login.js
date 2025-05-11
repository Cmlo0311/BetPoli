const form = document.getElementById('login-form');
const list = document.getElementById('usersList');

form.addEventListener('submit', async e => {
    e.preventDefault();
    list.innerHTML = ''; // limpiamos antes de cada submit

    const data = Object.fromEntries(new FormData(form).entries());

    try {
        const res = await fetch('http://192.168.2.6:5000/login', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify(data)
        });

        if (!res.ok) {
            throw new Error(`Error en el servidor: ${res.status}`);
        }

        const payload = await res.json();

        // Si viene un mensaje de éxito, lo mostramos en consola (o donde prefieras)
        console.log(payload.mensaje); // → "Login exitoso"

        // Extraemos el usuario
        const usuario = payload.usuario;
        if (!usuario) {
            throw new Error('Respuesta inesperada: falta la propiedad "usuario"');
        }

        // Envolvemos en array para usar forEach
        mostrarUsuarios([usuario]);

    } catch (err) {
        console.error('¡Houston, falló el POST!', err);
    }
});

function mostrarUsuarios(usuarios) {
    console.log(usuarios);
    usuarios.forEach(u => {
        const fecha = u.FechaNacimiento
            ? new Date(u.FechaNacimiento).toLocaleDateString('es-CO')
            : 'fecha desconocida';

        const li = document.createElement('li');
        li.innerHTML = `
      <p>${u.NombreUsuario}</p> 
      <p>${u.Nombre}</p>  
      <p>${u.Apellido}</p>  
    `;
        list.appendChild(li);
    });
}


fetch("../components/header.html")
    .then(res =>
        res.text())
    .then(data => {
        document.getElementById("mi-header").innerHTML = data;
    });

