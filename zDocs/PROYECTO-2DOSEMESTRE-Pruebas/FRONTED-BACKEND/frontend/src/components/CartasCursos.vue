<template>
    <div class = "contenedor-general">
        <div class="container px-4 text-center ">
            <div class="row gx-10 ">
                <div class="col">

                </div>
                <div class="contenedor-cursos">

                    <div class="col " v-for="(cursos, index) in listaCursos " :key="index">
                        <div class="contenedor-secundario-cartas">
                            <div class="contenedor-imagen"></div>
                            <p class="nombre-curso">{{ cursos.c_nombre }} </p>
                            <p>{{ cursos.c_descripcion }}</p>
                            <a v-bind:href="'/cursos/'+ cursos.prog_id"> <button type="button"
                                    class="btn btn-success">Ver más</button></a>

                        </div>
                    </div> 
                </div>
            </div>
        </div>

    </div>
</template>

<script>
import axios from 'axios';
export default {
    name: 'Cartas Cursos',
    data() {
        return {
            listaCursos: []
        }
    },
    methods: {
        getProgramaciones() {
            const path = 'http://localhost:5000/api/programacion';
            axios.get(path)
                .then((res) => {
                    this.listaCursos = res.data.datos
                    console.log(this.listaCursos)
                })
                .catch((error) => {
                    console.error(error);
                });
        }
    },
    created() {
        this.getProgramaciones()
    }
}

</script>

<style scoped>
.contenedor-general{
    background:rgba(224,225,228,255)
;
}
.contenedor-imagen {
    background-image: linear-gradient(
        rgba(0,0,0,0.7),
        rgba(0,0,0,0.7)),
        url(../assets/img/bailarina2.jpg);
        background-position: center bottom;
        background-repeat: no-repeat;
        background-size: cover;
    width: 93%;
    height: 175px;
    /* border: 2px solid greenyellow; */
    border-radius: 10px ;
    margin: 7px auto;
}
.contenedor-cursos {
    
    width: 100%;
    height: auto;
    /* border: 5px solid brown; */
    display: grid;
    grid-template-columns: repeat(3, 1fr);
}

.contenedor-secundario-cartas{
    background: white;
    padding-top: 3px;
    border-radius: 10px ;
    position: relative;
    margin: 20px auto;
    width: 75%;
    height: auto;
    /* border: 1px solid skyblue; */
    box-shadow: 18px 25px 29px -12px rgba(89,89,89,0.75);
    -webkit-box-shadow: 18px 25px 29px -12px rgba(89,89,89,0.75);
-moz-box-shadow: 18px 25px 29px -12px rgba(89,89,89,0.75);
}
.contenedor-secundario-cartas p{
    text-align: left;
    padding-left: 17px;
    /* padding-right: 15px; */
    font-weight: 700;
}

.btn{
    margin-bottom: 10px;
}
.contenedor-secundario-cartas .nombre-curso{
    position: absolute;
    top: 15px;
    /* left: 15px; */
    color: white;
    /* border: 2px solid white; */
    max-width: 90%;
    text-align: left;
    font-size: 17px ;
    font-weight: 600;
}
</style>