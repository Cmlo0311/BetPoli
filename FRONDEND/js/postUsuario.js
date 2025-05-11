const form = document.getElementById('userForm');
form.addEventListener('submit', e => {
    e.preventDefault();
    const data = {};
    new FormData(form).forEach((v, k) => data[k] = v);

    fetch("http://192.168.2.6:5000/postUsuario", {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(data)
    }
    )
        .then(res => {
            if (res.status === 201)
                return res.json();
            throw new Error(`Error al crear: ${res.status}`);
        })
        .then(data => {
            console.log('Usuario creado:', data);
        })
        .catch(err => {
            console.error('¡Houston, falló el POST!', err);
        });
});


fetch("../components/header.html")
    .then(res =>
        res.text())
    .then(data => {
        document.getElementById("mi-header").innerHTML = data;
    });