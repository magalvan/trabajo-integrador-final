console.log(location.search) // lee los argumentos pasados a este formulario
var id=location.search.substr(4)
console.log(id)
const { createApp } = Vue
createApp({
data() {
return {
videos:[],
url:'https://magalvan.pythonanywhere.com/videos',
// si el backend esta corriendo local usar localhost 5000(si no lo subieron a pythonanywhere)
//url:'http://promero.pythonanywhere.com/productos/', // si ya lo subieron a pythonanywhere
error:false,
cargando:true,
/*atributos para el guardar los valores del formulario */
id:0,
iddisco:id,
nombre:"",
videoclip:"",
}
},
methods: {
fetchData(url) {
fetch(url)
.then(response => response.json())
.then(data => {
this.videos = data.filter(video => video.iddisco == id);
this.cargando=false
})
.catch(err => {
console.error(err);
this.error=true
})
console.log(this.videos)
},
eliminar(video) {
const url = this.url+'/' + video;
var options = {
method: 'DELETE',
}
fetch(url, options)
.then(res => res.text()) // or res.json()
.then(res => {
location.reload();
})
},
grabar(){
let video = {
iddisco: this.iddisco,
nombre: this.nombre,
videoclip: this.videoclip,
}
var options = {
body:JSON.stringify(video),
method: 'POST',
headers: { 'Content-Type': 'application/json' },
redirect: 'follow'
}
fetch(this.url, options)
.then(function () {
alert("Registro grabado")
window.location.href = "../templates/videos.html?id="+video.iddisco;
})
.catch(err => {
console.error(err);
alert("Error al Grabarr")
})
}
},
created() {
this.fetchData(this.url)
},
}).mount('#app')