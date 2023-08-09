<template>
    <div class="contenedor-general">
        <AdminNav></AdminNav>

        <div class="container px-4 text-center ">
            <div class="row gx-10 ">
                <div class="col">

                </div>
                <div class="contenedor-cursos">

                    <div class="col ">
                        <div class="contenedor-secundario-cartas">
                            <i class="bi bi-person-square"></i>
                            <p>Cursos</p>
                            <a v-bind:href="'/admin/cursos'"> <button type="button" class="btn btn-success">Ver
                                    más</button></a>

                        </div>
                    </div>
                    <div class="col ">
                        <div class="contenedor-secundario-cartas">
                            <i class="bi bi-person-square"></i>
                            <p>Programaciones</p>
                            <a v-bind:href="'/admin/programaciones'"> <button type="button" class="btn btn-success">Ver más</button></a>

                        </div>
                    </div>
                    <div class="col ">
                        <div class="contenedor-secundario-cartas">
                            <i class="bi bi-person-square"></i>
                            <p>Profesores</p>
                            <a v-bind:href="'/admin/profesores'"> <button type="button" class="btn btn-success">Ver más</button></a>

                        </div>
                    </div>
                </div>
            </div>
        </div>
        <!-- <button @click="abrirModal =! abrirModal">Abrir Modal</button> -->




    </div>
</template>
<script>
// import Modal from '../components/modal.vue'

import AdminNav from '../components/AdminNav.vue'
export default {
    components:{
        AdminNav, 
        // Modal
    },
    name: 'Cartas Cursos',
    data() {
        return {
            listaCursos: [],
            abrirModal: false,
            Mensaje: 'Hola'
        }
    },
    methods: {
       
    },

}

</script>

<style scoped>
 /* .contenedor-general{
    background:skyblue;
}   */
.contenedor-general{
    /* background: rgba(18,36,38,255); */
    height: 667px;
}
i {
    color: black;
    font-size: 70px;
}

p {
    text-align: center;
}

.contenedor-cursos {

    width: 100%;
    height: auto;
    /* border: 5px solid brown; */
    display: grid;
    grid-template-columns: repeat(3, 1fr);
}

.contenedor-secundario-cartas {
    /* background: #444d3b85; */
    padding-top: 3px;
    border-radius: 10px;
    position: relative;
    margin: 20px auto;
    width: 75%;
    height: auto;
    border: 3px solid #01c0e2;
    box-shadow: 18px 25px 29px -12px rgba(91, 91, 91, 0.75);
    -webkit-box-shadow: 18px 25px 29px -12px rgba(87, 87, 87, 0.75);
    -moz-box-shadow: 18px 25px 29px -12px rgba(94, 93, 93, 0.75);
}

.contenedor-secundario-cartas p {
    text-align: left;
    /* padding-left: 17px; */
    /* padding-right: 15px; */
    font-weight: 700;
    text-align: center;
    /* border: 2px solid red */
}

.btn {
    margin-bottom: 10px;
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
        width: 800px;
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


</style>