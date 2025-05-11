fetch("../components/header.html")
    .then(res =>
        res.text())
    .then(data => {
        document.getElementById("mi-header").innerHTML = data;
    });