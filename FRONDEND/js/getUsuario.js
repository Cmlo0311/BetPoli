fetch("http://192.168.2.6:5000/getUsuario")
    .then(res => {
        if (!res.ok) throw new Error(`Error ${res.status}`);
        return res.json();
    })
    .then(usuarios => mostrarUsuarios(usuarios))

    .catch(err => console.error('¡Houston, tenemos un problema!', err));

function mostrarUsuarios(usuarios) {
    const list = document.getElementById('usersList');
    usuarios.forEach(u => {
        const li = document.createElement('li');
        const fecha = new Date(u.FechaNacimiento).toLocaleDateString('es-CO');
        li.innerHTML = `<strong>${u.NombreUsuario}</strong> — ${u.Nombre} ${u.Apellido} (nacido: ${fecha})`;
        list.appendChild(li);
    });
}

fetch("../components/header.html")
    .then(res =>
        res.text())
    .then(data => {
        document.getElementById("mi-header").innerHTML = data;
    });