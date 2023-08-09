<template>
<div>
    <footer class="footer">
  <div class="footer-content container"> 
    <div class="link">
      <h3>Contactos</h3>
      <ul>
        <li>Quito</li>
        <li><a href="https://www.whatsapp.com/">PBX:(593)0999878385</a></li>
        <li>Guayaquil</li>
        <li><a href="https://www.whatsapp.com/">PBX:(593)0999878385</a></li>
        <li>Horario de atención</li>
        <li>8h:30 a 17h15</li>
      </ul>


    </div>
    <div class="link">
      <h3>Siguenos en:</h3>
      <ul>
        <li><img src="../assets/img/insta.png" alt=""><img src="../assets/img/face.png" alt=""> <img src="../assets/img/twitter.png" alt=""></li>
      </ul>


    </div>
    <div class="link">
      <h3>Contact Center</h3>
      <ul>
        <li><a href="#">1800 1234567</a></li>
        <li>Tambien puedes comunicarte <br>
           a nuestro convencional </li>
          
          <li><a href="#">(02)12345648</a></li>
        
      </ul>


    </div>

  </div>
</footer>
</div>    
</template>
<script>
    export default{
        name: 'Footer'
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
.footer{
    padding: 20px 0;
    background-color: #c5c5c58b;
}
.footer-content{
    display: flex;
    justify-content: space-between;
}
.link h3{
    font-size: 18px;
    color: rgba(60, 220, 126, 0.667);
    margin-bottom: 15px;
}
.link a{
    font-size: 16px;
    color: #000000;
    display: block;
    margin-bottom: 15px;
}
.general{
    display: flex;
}
.general-1{
    width: 100%;
    padding: 100px;
    background-color: #ffffff5e;
}
</style>