console.log(location.search) // lee los argumentos pasados a este formulario
var id=location.search.substr(4)
console.log(id)
const { createApp } = Vue
createApp({
data() {
return {
id:0,
iddisco:0,
nombre:"",
videoclip:"",
url:'https://magalvan.pythonanywhere.com/videos/'+id,
}
},
methods: {
fetchData(url) {
fetch(url)
.then(response => response.json())
.then(data => {

console.log(data)
this.id=data.id,
this.iddisco=data.iddisco,
this.nombre=data.nombre,
this.videoclip=data.videoclip
})
.catch(err => {
console.error(err);
this.error=true
})
},
modificar() {
let video = {
id:this.id,
iddisco: this.iddisco,
nombre: this.nombre,
videoclip:this.videoclip
}
var options = {
body: JSON.stringify(video),
method: 'PUT',
headers: { 'Content-Type': 'application/json' },
redirect: 'follow'
}
fetch(this.url, options)
.then(function () {
alert("Registro modificado")
window.location.href = "../templates/videos.html?id="+video.iddisco;
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