<template>
  <div>
    <div class="menu container">
      <a href="#" class="logo"><img src="../assets/img/logozapatilla.png.png" alt=""></a>
      <input type="checkbox" id="menu">
      <label for="menu">
        <img src="../assets/img/menu.png" class="menu-icono" alt="">
      </label>
      <nav class="navbar">
        <ul>
          <li><a href="/admin">INICIO</a></li>
          <li><a href="/admin/cursos">CURSOS</a></li>
          <li><a href="/admin/programaciones">PROGRAMACIONES</a></li>
          <li><a href="/admin/profesores">PROFESORES</a></li>
          

        </ul>
      </nav>
        </div>
  </div>  
</template>
<script>
export default {
    components:{
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
    max-width: 1390px;
    margin: 0 auto;
}
.menu{
    /* position: absolute;
    top: 0;
    left: 0;
    right: 0; */
    display: flex;
    align-items: center;
    justify-content: space-between;
    background: #01c0e2;
    /* background: transparent; */
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
    padding: 20px 0px 20px 20px;
    color: white;
    display: block;
    font-weight: 600;
}
.menu .navbar ul li a:hover{
    color: skyblue;
}

#menu{
    display: none;
}

.menu-icono{
    width: 100px;
}

.menu label{
    cursor: pointer;
    display: none;
}

</style>
