<template>
<div>
    <header class="header">
        <section class="section">
        <h1 class="titulo">CERTIFICADO</h1>
        <h3 class="subtitulo">DE APROBACIÓN</h3>
        <p class="name">{{ this.aprobado.p_nombres }} {{ this.aprobado.p_apellidos }}</p>
        <p class="descripcion">con número de cédula {{ this.aprobado.p_cedula }}, por elevar <br> los estudios artísticos y por su gran participacion
            en la Academia de baile.</p>
        <h2 class="h2-left">Fecha</h2>
        <h2 class="h2-right">Firma</h2>
    </section>
        </header>
</div>
</template>


<script>
import axios from 'axios'

export default {
    data(){
        return{
            aprobado: []

        }
    },
    methods:{
            getCertificado(){
            const path = 'http://127.0.0.1:5000/api/certificado/'+ this.$route.params.id+'/'+this.$route.params.p_cedula
            axios.get(path)
            .then((res) => {
                this.aprobado = res.data.datos
                console.log(this.aprobado)
            })
            .catch(error => {
                    console.log(error)
                })
            // /<p_cedula';
                
            }
    },
    created(){
        this.getCertificado()
    }
}
</script>

<style scoped>
    /* .header{
        background-image: url(../assets/img/certificado.jpeg);  
        background-position: center top ;
        background-repeat: no-repeat;
        background-size: cover;
        width: 1260px;
        height: 700px;

      
} */
.header{
    background-image: 
        url(../assets/img/certificado1.jpeg);
        background-position: center top;
        background-repeat: no-repeat;
        background-size: 90%;
        width: 1390px;
        height: 650px;
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
.section {
            text-align: center;
            color: goldenrod;
            font-family: "Bodoni MT  / Bodoni 72";
        
        }
        
        .titulo {
            position: absolute;
            
            font-size: 56px;
            font-weight: bold;
            top: 100px;
            left: 500px;            
        }
        
        .subtitulo {
            position: absolute;
            font-size: 24px;
            margin-top: 1px;
            top: 170px;
            left: 600px;
        }
        .name {
            position: absolute;
            font-style: italic;
            font-size: 100px;
            margin-top: 1px;
            top: 170px;
            text-shadow: 1px 1px 1px rgb(255, 254, 254);
            left: 29%;
        }
        .descripcion {
            font-size: 22px;
            margin: 20px 50px 0px 400px;
        }
        
        .h2-left {
            position: absolute;
            bottom: 10px;
            left: 140px;
            font-size: 24px;
            top: 87%;
        }
        
        .h2-right {
            position: absolute;
            bottom: 10px;
            right: 175px;
            font-size: 24px;
            top: 87%;
        }
</style>