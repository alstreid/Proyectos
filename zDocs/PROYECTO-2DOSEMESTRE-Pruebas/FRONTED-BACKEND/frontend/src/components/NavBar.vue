<template>
  <div>
    <div class="menu container">
      <a href="/" class="logo"><img src="../assets/img/logozapatilla.png.png" alt=""></a>

        <h4>{{ this.usuario.mensaje }} {{ this.usuario.nombre }}</h4>

      <input type="checkbox" id="menu">
      <label for="menu">
        <img src="../assets/img/menu.png" class="menu-icono" alt="">
      </label>
      <nav class="navbar">
        <ul>
          <li><a href="/">INICIO</a></li>
          <li><a href="/cursos">CURSOS</a></li>
          <li><a href="/nosotros">NOSOTROS</a></li>
          <li v-if="sesionIniciada"><a href="/login">INICIAR SESION</a></li>
        </ul>
      </nav>
        </div>
    
  </div>  
</template>

<script>
export default {

  data(){
    return{
      usuario:{
        mensaje: '',
        nombre:''
      },
      sesionIniciada: false

    }
  },
  methods:{
      validacionSesion(){
        const sesion = JSON.parse(sessionStorage.getItem('session'))
        if (sesion != null) {
          this.usuario.mensaje = 'Bienvenido'
        this.usuario.nombre = sesion.p_nombres
        this.sesionIniciada = false
      } else {
        // this.participante = JSON.parse(sessionStorage.getItem('session'))
        this.sesionIniciada = true
      }
      }
  },
  created(){
    this.validacionSesion()
  }
}
</script>
<style scoped>
*{
    margin: 0;
    padding: 0;
    box-sizing: border-box;
    text-decoration: none;
    list-style: none;
} 

 .container{
    max-width: 1200px;
    margin: 0 auto;
}
.menu{
    position: absolute;
    top: 0;
    left: 0;
    right: 0;
    display: flex;
    align-items: center;
    justify-content: space-between;

}
h4{
  color: white;
}

.logo{
    color: #FFFDFC;
    font-size: 25px;
    font-weight: 800;
}

.menu .navbar ul li{
    position: relative;
    float: left;
}

.menu .navbar ul li a{
    font-size: 18px;
    padding: 20px;
    color: #FFFDFC;
    display: block;
    font-weight: 600;
}
.menu .navbar ul li a:hover{
    color: #CE967B;
}

#menu{
    display: none;
}

.menu-icono{
    width: 25px;
}

.menu label{
    cursor: pointer;
    display: none;
}

</style>