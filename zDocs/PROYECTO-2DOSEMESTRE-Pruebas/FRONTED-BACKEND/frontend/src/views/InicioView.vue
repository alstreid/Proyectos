<script>
import Footer from '../components/Footer.vue'
import NavBar from '../components/NavBar.vue'
export default{
    components: {
        Footer, NavBar

}
}
</script>
<template>
    <div >
        <header class="header">
            <NavBar></NavBar>
            <div class="header-content container">
        <h1>Bailar es nuestra pasión</h1>
        <p>
          Ser creativo significa estar enamorado de la vida. 
          Puedes ser creativo solo si amas la vida lo suficiente como para querer realzar su belleza,
           quieres llevarle un poco más de música, un poquito más de poesía, un poco más de baile
        </p>
             </div>
    
        </header>

        <section class="coffee">
    <img class="coffee-img" src="../assets/img/bg2.png" alt="">

    <div class="coffee-content container">
      <h2>ESTILOS DE BAILE DISPONIBLES EN NUESTRA ESCUELA</h2>
      <p class="txt-p">
        Diferentes estilos forman a un bailarín completo.
        Con diferentes tipos de clase: coreografías,
        consejos, entrenamientos... Somos únicos en ofrecerte los estilos de 
        moda para que aprendas todo lo que te gusta.
      </p>
      <div class="coffee-group">

        <div class="coffee-1">
          <img src="../assets/img/bailarina2.jpg" alt="">
          <h3>HIP HOP</h3>
         

        </div>
        <div class="coffee-1">
          <img src="../assets/img/zumba.jpg" alt="">
          <h3>REGGAETON</h3>
          

        </div>
        <div class="coffee-1">
          <img src="../assets/img/contemporaneo.jpg" alt="">
          <h3>CONTEMPORÁNEO</h3>
          

        </div>
      </div>

    </div>
        </section>
        <section class="services">
            <div class="services-content container">
            <div class="services-group">

        <div class="services-1">
          <img src="../assets/img/yolanda.png" alt="">
          <h3>Inscripciones</h3>
        </div>
        <div class="services-1">
          <img src="../assets/img/cursos.jpg" alt="">
          <h3>Cursos</h3>
        </div>
        <div class="services-1">
          <img src="../assets/img/profesores.jpg" alt="">
          <h3>Profesores</h3>
        </div>
        </div>


      </div>
    </section>
<Footer></Footer>
    </div>

</template>

<style scoped>
@import url('https://fonts.googleapis.com/css2?family=Poppins:ital,wght@0,400;0,600;0,700;0,800;1,500&display=swap');
@import url('https://fonts.googleapis.com/css2?family=Dancing+Script:wght@700&family=Poppins:ital,wght@0,400;0,600;0,700;0,800;1,500&display=swap');
@import url('https://fonts.googleapis.com/css2?family=Dancing+Script:wght@700&family=Great+Vibes&display=swap');
*{
    margin: 0;
    padding: 0;
    box-sizing: border-box;
    text-decoration: none;
    list-style: none;
}

.contenedor-general{
    font-family: 'Poppins', sans-serif;
    background: rgba(18,36,38,255);
}
.container{
    max-width: 1200px;
    margin: 0 auto;
}

.header{
    background-image: linear-gradient(
        rgba(0,0,0,0.7),
        rgba(0,0,0,0.7)),
        url(../assets/img/bailarina1.jpg);
        background-position: center bottom;
        background-repeat: no-repeat;
        background-size: cover;
        min-height: 100vh;
        display: flex;
        align-items: center;
}
    

.header-content{
    text-align: center;
}

.header-content h1{
    font-size: 130px;
    line-height: 20px;
    color: #eaebed;
    
    position: relative;
    top: 50px;
    font-family: 'Dancing Script', cursive;
    font-family: 'Great Vibes', cursive;
}

.header-content p{
    font-size: 20px;
    color: #c5c5c5;
    padding: 0 250px;
    margin-bottom: 25px;
    text-align: center;
    position: relative;
    top: 120px;
}


.coffee{
    padding: 100px 0;
    background-color: #e1e2e6;
    position: relative;
}

.coffee-content{
    text-align: center;
}
.coffee-content h2{
    font-size:  55px;
    line-height: 70px;
    color: #323337;
    text-transform: uppercase;
    padding: 0 250px;
    margin-bottom: 15px;
}

.txt-p{
    font-size: 16px;
    color: #414247;
    padding: 0 250px;
    margin-bottom: 35px;
}

.coffee-group{
    display: flex;
    justify-content: space-between;
    margin-bottom: 50px;
}
.coffee-1{
    padding: 0 25px;
}

.coffee-1 img{
    width: 230px;
    height: 150px;
    border-radius: 8px;
    
}
.coffee-img{
    position: absolute;
    top: 0;
    right: 0;
}
.coffee-1 h3{
    color: #323337;
    font-size: 20px;
    margin-bottom: 15px;
}
.services{
    background-image: linear-gradient(
        rgba(0,0,0,0.7),
        rgba(0,0,0,0.7)),
        url(../assets/img/hiphop.jpg);
    background-position: center center;
    background-repeat: no-repeat;
    background-size: cover;
    background-attachment: fixed;
    padding: 100px 0;
}

.services-content{
    text-align: center;
}

.services-group{
    display: flex;
    justify-content: space-between;
    margin-bottom: 50px;
}
.services-1{
    padding: 0 100px;
}
.services-1 img{
    width: 190px;
    margin-bottom: 15px;
    border-radius: 100%;
    height: 180px;
}
.services-1 h3{
    color: #eaccb3;
    font-size: 18px;
}

h2{
    font-size: 55px;
    line-height: 70px;
    color: #323337;
    margin-bottom: 20px;
}
p{
    font-size: 16px;
    color: #414247;
    margin: 25px 0 45px 0;
}


</style>