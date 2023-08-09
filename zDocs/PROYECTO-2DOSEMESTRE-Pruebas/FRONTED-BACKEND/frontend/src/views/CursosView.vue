<template>
    <div>
      <header class="header">
            <NavBar></NavBar>
            <div class="header-content container">
        <h1>CURSOS</h1>
        <p>
          Ser creativo significa estar enamorado de la vida. 
          Puedes ser creativo solo si amas la vida lo suficiente como para querer realzar su belleza,
           quieres llevarle un poco más de música, un poquito más de poesía, un poco más de baile
        </p>
             </div>
             
        </header>
      <CartasCursos></CartasCursos>
      <Footer></Footer>
    </div>
</template>

<script>
import NavBar from '../components/NavBar.vue'
import CartasCursos from '../components/CartasCursos.vue'
import Footer from '../components/Footer.vue'
export default{
    components:{
        CartasCursos,
        NavBar,
        Footer,
    }
  }

</script>

<style scoped>
@import url('https://fonts.googleapis.com/css2?family=Poppins:ital,wght@0,400;0,600;0,700;0,800;1,500&display=swap');
@import url('https://fonts.googleapis.com/css2?family=Dancing+Script:wght@700&family=Poppins:ital,wght@0,400;0,600;0,700;0,800;1,500&display=swap');
@import url('https://fonts.googleapis.com/css2?family=Dancing+Script:wght@700&family=Great+Vibes&display=swap');
@import url('https://fonts.googleapis.com/css2?family=Inknut+Antiqua:wght@300;400;500;600;700;800&display=swap');
*{
    margin: 0;
    padding: 0;
    box-sizing: border-box;
    text-decoration: none;
    list-style: none;
}

body{
    font-family: 'Poppins', sans-serif;
}
.container{
    max-width: 1200px;
    margin: 0 auto;
}

.header{
    background-image: linear-gradient(
        rgba(0,0,0,0.7),
        rgba(0,0,0,0.7)),
        url(../assets/img/bailarina2.jpg);
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
    font-weight: 400;
    font-family: 'Inknut Antiqua', cursive;
    /* font-family: 'Poppins', cursive; */
    /* font-family: 'Great Vibes', cursive; */
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
</style>
