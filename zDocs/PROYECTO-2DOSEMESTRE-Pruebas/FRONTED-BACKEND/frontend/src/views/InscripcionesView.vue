<template>
    <div>
        <header class="header">
            <NavBar></NavBar>
            <div class="header-content container">
                <h1>INSCRIPCIONES</h1>
                <!-- <p>
          Ser creativo significa estar enamorado de la vida. 
          Puedes ser creativo solo si amas la vida lo suficiente como para querer realzar su belleza,
           quieres llevarle un poco más de música, un poquito más de poesía, un poco más de baile
        </p> -->
            </div>

        </header>
        <!-- <h4>Detalles de cursos {{ $route.params.id }}</h4> -->
        <div class="contenedor-info">
            <div class="contenedor-secundario-info">

                <div class="contenedor-imagen"></div>

                <div class="contenedor-curso">
                    <h1>{{ detalleCurso.c_nombre }}</h1>
                    <p class="descripcion">{{ detalleCurso.c_descripcion }}</p>
                    <p> Instructor: <span> {{ detalleCurso.prof_nombres }} {{ detalleCurso.prof_apellidos }} </span></p>
                    <div class="inicio-cierre">
                        <div class="fechas">
                            <p> Inicio: </p>
                            <span>{{ fechaFormateada1 }}</span>
                        </div>
                        <div class="fechas">
                            <p>Cierre: </p>
                            <span>{{ fechaFormateada2 }}</span>
                        </div>
                    </div>
                    <p> Horario: <span>{{ detalleCurso.h_dia }} </span> <span> Desde: {{ detalleCurso.h_hora_inicio }}
                        </span> <span> Hasta: {{ detalleCurso.h_hora_cierre }}</span></p>
                    <p> Duracion: <span>{{ detalleCurso.prog_duracion }}</span></p>

                </div>
            </div>

        </div>
        <Inscripcion :detalles="detalleCurso"></Inscripcion>

        <Footer></Footer>
    </div>
</template>

<script>
import axios from 'axios'
import Inscripcion from '../components/Inscripcion.vue'
import NavBar from '../components/NavBar.vue'
import Footer from '../components/Footer.vue'
import moment from 'moment'
export default {
    components: {
        Inscripcion,
        NavBar, Footer
    },
    data() {

        return {
            detalleCurso: [],
            // id: this.$route.params.id
            // fechaUno: ''
        }

    },
    methods: {
        getProgramacion() {
            const path = 'http://127.0.0.1:5000/api/programacion/' + this.$route.params.id
            axios.get(path)
                .then((res) => {
                    this.detalleCurso = res.data.datos
                    console.log(this.detalleCurso)
                    // this.fechaFormateada(this.detalleCurso.prog_fecha_inicio)

                })
        },
        postInscripcion(){
            const path = 'http://127.0.0.1:5000/api/programacion/'
            const payload = moment().format('YYYY-MM-DD');
            console.log(payload)
        }
    },
    computed: {
        fechaFormateada1() {

            return moment(this.detalleCurso.prog_fecha_inicio, 'ddd, DD MMM YYYY HH:mm:ss [GMT]').format('DD/MM/YYYY')
        },
        fechaFormateada2() {

            return moment(this.detalleCurso.prog_fecha_fin, 'ddd, DD MMM YYYY HH:mm:ss [GMT]').format('DD/MM/YYYY')
        }
    },
    created() {
        this.getProgramacion()
    }

}

</script>

<style scoped>
@import url('https://fonts.googleapis.com/css2?family=Inknut+Antiqua:wght@300;400;500;600;700;800&display=swap');

.header {
    background-image: linear-gradient(rgba(0, 0, 0, 0.7),
            rgba(0, 0, 0, 0.7)),
        url(../assets/img/hiphop.jpg);
    background-position: center bottom;
    background-repeat: no-repeat;
    background-size: cover;
    min-height: 100vh;
    display: flex;
    align-items: center;
}

.header-content {
    text-align: center;
}

.header-content h1 {
    font-size: 120px;
    line-height: 20px;
    color: #eaebed;
    position: relative;
    top: 50px;
    font-weight: 400;
    font-family: 'Inknut Antiqua', cursive;
    /* font-family: 'Poppins', cursive; */
    /* font-family: 'Great Vibes', cursive; */
}

.header-content p {
    font-size: 20px;
    color: #c5c5c5;
    padding: 0 250px;
    margin-bottom: 25px;
    text-align: center;
    position: relative;
    top: 120px;
}

.contenedor-secundario-info {
    margin: 0 auto;
    display: grid;
    grid-template-columns: 40% 60%;
    width: 80%;
    background: white;
    border-radius: 15px;
    padding: 10px 5px 10px 7px;
}

.contenedor-info {
    border: 2px solid green;
    /* text-align: center; */
    padding: 20px 50px;
    background: grey;
}

.contenedor-imagen {
    /* border: 5px solid brown; */
    width: 100%;
}

.contenedor-imagen {
    background-image: linear-gradient(rgba(0, 0, 0, 0.7),
            rgba(0, 0, 0, 0.7)),
        url(../assets/img/bailarina2.jpg);
    background-position: center bottom;
    background-repeat: no-repeat;
    background-size: cover;
    width: 100%;
    height: auto;
    /* border: 2px solid greenyellow; */
    border-radius: 10px;
    /* margin: 7px auto; */
}

.contenedor-curso {
    /* border: 2px solid blue; */
    grid-column-start: 2;
    width: 100%;
    text-align: left;
    padding-left: 20px;
}

.contenedor-curso p {
    font-size: 20px;
    font-weight: 500;
}

.contenedor-curso span {
    border: 2px solid rgb(3, 181, 3);
    background: greenyellow;
    color: black;
    font-weight: 700;
    border-radius: 10px;
    padding: 5px;
    font-size: 15px;

}

.inicio-cierre {
    /* text-align: center; */
    /* border:2px solid red ; */
    padding-bottom: 20px;

    display: grid;
    grid-template-columns: repeat(2, 1fr);
}

.descripcion {
    font-weight: 100;
    color: blue;
}
.fechas{
    display: flex;
    align-items: center;
}
.fechas span{
margin: 0px 0px 10px 20px;
}


</style>