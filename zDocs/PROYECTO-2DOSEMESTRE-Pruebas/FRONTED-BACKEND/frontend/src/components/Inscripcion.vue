<template>
  <div>
    <Modal :modalCreate="abrirModal" :mensaje="Mensaje"></Modal>

    <section class="services">

      <section id="cursos" class="glass-efect">
        <h1>INSCRIPCION</h1>

        <form>
          <div class="info-personal">
            <h3>Datos personales</h3>
            <label>Cedula: </label>
            <div class="datos">{{ participante.p_cedula }}</div>
            <label>Nombres:</label>
            <div class="datos">{{ participante.p_nombres }} {{ participante.p_apellidos }}</div>
            <label>Celular: </label>
            <div class="datos">{{ participante.p_celular }}</div>

          </div>

          <div class="info-curso">

            <h3>Datos cursos</h3>
            <label>Curso:</label>
            <div class="datos">{{ detalles.c_nombre }}</div>
            <label>Horario:</label>
            <div class="datos">Desde: {{ detalles.h_hora_inicio }} a {{ detalles.h_hora_cierre }}</div>
            <label>Instructor:</label>
            <div class="datos">{{ detalles.prof_nombres }} {{ detalles.prof_apellidos }} </div>
          </div>
        </form>
        <button v-if="sesionIniciada" @click="postInscripcion"> Inscribirse</button>
        <a href="/login" v-else><button >Iniciar sesion para inscribirse.</button></a>
      </section>

    </section>

  </div>
</template>
<script>
import Modal from '../components/modal.vue'
import moment from 'moment'
import axios from 'axios'

export default {
  components:{
    Modal,
    
  },
  props: ['detalles'],
  data() {
    return {
      participante: [],
      sesionIniciada : false,
      mensaje: "",
      Mensaje: '',
      abrirModal: false,
  }

  },
  methods: {
    postInscripcion() {
      const path = 'http://127.0.0.1:5000/api/inscripciones'

      const payload = {
        fecha_inscripcion: moment().format('YYYY-MM-DD'),
        cedula: this.participante.p_cedula,
        estado_inscripcion: 1,
        prog_id: this.detalles.prog_id
      }
      axios.post(path, payload)
        .then((res) => {
          console.log(res.data.mensaje)
          this.Mensaje = res.data.mensaje
          this.abrirModal = true
          // if (res.data.mensaje == "Inscripcion creada"){
          //   console.log("Inscrito")
          // }
        })
        .catch(error => {
          console.log(error)
        })

      // console.log(payload)
    },
    validacionInscripcion() {
      const sesion = JSON.parse(sessionStorage.getItem('session'))
      console.log(sesion)
      if (sesion == null) {
        this.participante = {
          p_cedula :"Inicia sesion",
          p_nombres: "para ",
          p_apellidos: "poder",
          p_celular : "inscribirte",
          }
        } else {
          this.participante = JSON.parse(sessionStorage.getItem('session'))
          this.sesionIniciada = true
      }
    }

  },
  created() {
    this.validacionInscripcion()
    // this.participante = JSON.parse(sessionStorage.getItem('session'))
    // console.log(this.participante)
    // console.log(this.detalles)
  }
}
</script>
<style scoped>
h1 {
  color: White;
  text-align: center;
  /* border: 2px solid red; */
}

section {
  padding: 50px;
  align-self: auto;
}


.datos {
  /* width: 125px; */
  max-width: 270px;
  width: auto;
  padding: 2px 0px 2px 10px;
  /* margin-bottom: 10px; */
  height: 32px;
  margin: 7px 0px 5px 5px;
  /* border: 2px solid gray; */
  border: 2px solid greenyellow;

  border-radius: 7px;
  background: transparent;
  color: white;

}

form {
  display: grid;
  grid-template-columns: repeat(2, 1fr);
  /* width: 100%; */
  padding: 5px;
  margin-bottom: 10px;
  /* border: 2px solid blue; */
  grid-gap: 25px;
  color: white;
}

button {
  margin: 1px auto;
  background-color: transparent;
  color: white;
  padding: 10px 20px;
  width: auto;
  border: 2px solid greenyellow;
  border-radius: 15px;

  cursor: pointer;
  grid-column: span 2;
}

button:hover {
  background: greenyellow;
  color: black;
  font-weight: 700;
}

h3 {
  color: greenyellow;
}

.info-personal {
  border: 2px solid yellowgreen;
  border-radius: 15px;

  padding: 20px 0px 20px 20px;

  grid-column-start: 1;
  display: flex;
  flex-direction: column;
}

.info-curso {
  border: 2px solid yellowgreen;
  border-radius: 15px;
  grid-column-start: 2;
  padding: 20px 0px 20px 20px;

  display: flex;
  flex-direction: column;
}

#cursos {
  border: 2px solid black;
  width: 70%;
  margin: 2px auto;
  border: 2px solid greenyellow;

  border-radius: 30px;
  /* filter: blur(7px); */
}

.glass-efect {
  background: #fafafa10;
  backdrop-filter: blur(0.4rem);
}

label {
  color: white;
  font-weight: 600;
  font-size: 18px;
}

.services {
  background-image: linear-gradient(rgba(0, 0, 0, 0.7),
      rgba(0, 0, 0, 0.7)),
    url(../assets/img/hiphop.jpg);
  /* background: gray; */
  background-position: center center;
  background-repeat: no-repeat;
  background-size: cover;
  background-attachment: fixed;
  padding: 100px 0;
}</style>