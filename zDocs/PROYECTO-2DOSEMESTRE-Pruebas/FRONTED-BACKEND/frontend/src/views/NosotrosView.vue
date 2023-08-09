<script>
import Footer from '../components/Footer.vue'
import NavBar from '../components/NavBar.vue'
export default{
    components:{
        Footer, NavBar
    }
}
</script>
<template>
    <div>
        <header class="header1">
            <NavBar></NavBar>           
            <div class="header1-content container">
                <h1>nuestra visión</h1>
                <p class="parrafo">
                    Nuestro objetivo es convertirnos <br>en una academia para la <br> preservación de las bellas artes 
                </p>
            </div>
    
        </header>
        <section class="header1-content">
        <div class="general-1">
          <h2>nuestra misión</h2>
          <p class="parrafo1">
              
              Fomentar la pasión por el baile y proporcionar <br> a nuestros estudiantes 
          un ambiente estimulante <br>y acogedor donde puedan desarrollar sus habilidades<br> artísticas. 
          Nos comprometemos a ofrecer una <br>enseñanza de alta calidad, dirigida por profesionales <br>
          experimentados y apasionados por el baile.
        </p>
        
    </div>
    
    
</section>
<Footer></Footer>
    </div>
</template>
<!-- <link rel="stylesheet" href="../assets/styles/estilo.css"> -->
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
    overflow-x: hidden ;


}

body{
    font-family: 'Poppins', sans-serif;
}
.container{
    max-width: 1200px;
    margin: 0 auto;
}

.header1{
    background-image: linear-gradient(
        rgba(61, 59, 59, 0.7),
        rgba(170, 166, 166, 0.7)),
        url(../assets/img/bailarina.jpg);
        background-position: center bottom;
        background-repeat: no-repeat;
        background-size: cover;
        min-height: 100vh;
        display: flex;
        align-items: center;


}

.header1-content h1{
    
    font-family: 'Dancing Script', cursive;
    font-size: 100px;
    color: rgb(23, 23, 23);
    text-align: justify;
    position:relative;
    left: 280px;
    top: 80px;

}
.header1-content h1::first-letter{
    font-size: 350px;
    color: rgba(192, 199, 195, 0.724);
}
.header1-content h2{
    font-family: 'Dancing Script', cursive;
    font-size: 100px;
    color: rgb(23, 23, 23);
    /* text-align: center; */
    padding-left:10px ;
    height: 170px;
    align-items: center;
    overflow-y: hidden ;
    
}
.header1-content h2::first-letter{
    /* display: flex;
    align-items: center; */
    font-size: 320px;
    color: rgba(80, 80, 80, 0.724);
    overflow-x: hidden ;

}

.parrafo{
        color: #FFFDFC;
        font-size: 35px; 
        font-family: Georgia, 'Times New Roman', Times, serif;
        position: relative;
        left: 340px;
}
.parrafo1{
        color: #8a8a86;
        font-size: 35px; 
        font-family: Georgia, 'Times New Roman', Times, serif;
        position: relative;
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

.general-1{
    width: 90%;
    padding: 100px;
    background-color: #ffffff5e;
    overflow-y: hidden ;
}






</style>