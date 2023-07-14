console.log(location.search) // lee los argumentos pasados a este formulario
var id=location.search.substr(4)
console.log(id)
const { createApp } = Vue
createApp({
data() {
return {
id:0,
nombre:"",
imagen:"",
afecha:0,
artista:"",
url:'https://magalvan.pythonanywhere.com/discos/'+id,
}
},
methods: {
fetchData(url) {
fetch(url)
.then(response => response.json())
.then(data => {

console.log(data)
this.id=data.id,
this.nombre = data.nombre,
this.artista=data.artista,
this.afecha=data.afecha,
this.imagen=data.imagen
})
.catch(err => {
console.error(err);
this.error=true
})
},
modificar() {
let disco = {
nombre:this.nombre,
artista: this.artista,
afecha: this.afecha,
imagen:this.imagen
}
var options = {
body: JSON.stringify(disco),
method: 'PUT',
headers: { 'Content-Type': 'application/json' },
redirect: 'follow'
}
fetch(this.url, options)
.then(function () {
alert("Registro modificado")
window.location.href = "../templates/discos.html";
})
.catch(err => {
console.error(err);
alert("Error al Modificar")
})
}
},
created() {
this.fetchData(this.url)
},
}).mount('#app')