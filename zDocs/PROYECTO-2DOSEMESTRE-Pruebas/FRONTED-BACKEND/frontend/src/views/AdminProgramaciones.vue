<template>
    <div>
        <AdminNav></AdminNav>
        <Modal :modalCreate="abrirModal" :mensaje="Mensaje"></Modal>

        <div class="crear-curso">
            <h1> Programaciones</h1>
            <button type="button" class="btn btn-success" @click="toggleCreateModal">Agregar</button>
        </div>
        <div>
            <div class="alert alert-success" role="alert" v-if="showMessage">{{ message }}</div>
            <br />
        </div>
        <div class="container">

            <table class="table table-hover">
                <thead>
                    <tr>
                        <th scope="col">ID</th>
                        <th scope="col">Nombre curso</th>
                        <th scope="col">Descripción</th>
                        <th scope="col">Fecha inicio</th>
                        <th scope="col">Fecha final</th>
                        <th scope="col">Horario</th>
                        <th scope="col">Profesor</th>
                        <th scope="col">Duración</th>
                        <th></th>
                    </tr>
                </thead>
                <tbody>
                    <tr v-for="(programacion, index) in listaProgramacion" :key="index">

                        <td>{{ programacion.prog_id }}</td>

                        <td>{{ programacion.c_nombre }}</td>

                        <td>{{ programacion.c_descripcion }}</td>
                        <td>{{ fechaFormateada1(programacion.prog_fecha_inicio) }}</td>
                        <td>{{ fechaFormateada2(programacion.prog_fecha_fin) }}</td>
                        <td> {{ programacion.h_dia }} de {{ programacion.h_hora_inicio }} hasta {{
                            programacion.h_hora_cierre }}</td>
                        <td> {{ programacion.prof_nombres }} {{ programacion.prof_apellidos }}</td>
                        <td> {{ programacion.prog_duracion }} </td>

                        <td> <button type="button" class="btn btn-warning btn-sm"
                                @click="toggleEditPrograModal(programacion)">
                                <i class="bi bi-pencil-fill"></i>
                            </button>
                            <!-- <div class="btn-group" role="group"> -->
                            <button type="button" class="btn btn-danger btn-sm" @click="eliminar(programacion.prog_id)"><i
                                    class="bi bi-trash3-fill"></i></button>
                            <!-- </div> -->
                            <!-- <div class="btn-group" role="group"> -->

                            <a v-bind:href="'/admin/programaciones/'+programacion.prog_id"><button type="button" class="btn btn-success btn-sm"><i
                                    class="bi bi-person-square"></i></button></a>
                            <!-- </div> -->
                        </td>
                    </tr>
                </tbody>
            </table>

        </div>

















        <div class="modal fade" :class="{ show: modalCreate, 'd-block': modalCreate }" tabindex="-1" role="dialog">
            <div class="modal-dialog" role="document">
                <div class="modal-content">
                    <div class="modal-header">
                        <h5 class="modal-title">Crear programacion </h5>
                        <button type="button" class="close" data-dismiss="modal" aria-label="Close"
                            @click="toggleCreateModal">
                            <span aria-hidden="true">&times;</span>
                        </button>
                    </div>
                    <div class="modal-body">
                        <form>
                            <div class="mb-3">
                                <label for="editBookTitle" class="form-label">Curso:</label>
                                <select name="" id="" v-model="nuevaProgramacion.c_id">
                                    <option v-for="curso in listaCursos" :key="curso.c_id" :value="curso.c_id">
                                        {{ curso.c_nombre }}</option>
                                </select>

                            </div>
                            <div class="mb-3">
                                <label for="editBookTitle" class="form-label">Fecha de inicio:</label>
                                <input type="date" class="form-control" id="editBookTitle"
                                    v-model="nuevaProgramacion.fecha_inicio" placeholder="">
                            </div>
                            <div class="mb-3">
                                <label for="editBookTitle" class="form-label">Fecha de finalización:</label>
                                <input type="date" class="form-control" id="editBookTitle"
                                    v-model="nuevaProgramacion.fecha_fin" placeholder="">
                            </div>
                            <div class="mb-3">
                                <label class="form-label">Duracion:</label>
                                <input type="text" class="form-control" v-model="nuevaProgramacion.duracion">
                            </div>
                            <div class="mb-3">
                                <label for="editBookTitle" class="form-label">Profesor:</label>
                                <select name="" id="" v-model="nuevaProgramacion.prof_id">
                                    <option v-for="profesor in listaProfesores" :key="profesor.prof_id"
                                        :value="profesor.prof_id">
                                        {{ profesor.prof_nombres }} {{ profesor.prof_apellidos }}</option>
                                </select>
                            </div>
                            <div class="mb-3">
                                <label for="editBookTitle" class="form-label">Horario:</label>
                                <select name="" id="" v-model="nuevaProgramacion.h_id">
                                    <option v-for="horario in listaHorarios" :key="horario.h_id" :value="horario.h_id">
                                        {{ horario.h_dia }} de {{ horario.h_hora_inicio }} a {{ horario.h_hora_cierre
                                        }}----{{ horario.h_id }}</option>
                                </select>


                                <!-- <div class="mb-3">
                                <label for="editBookTitle" class="form-label">Horario:</label>
                                <select name="" id="" v-model="editPrograForm.h_id">
                                    <option v-for="horario in listaHorarios" :key="horario.h_id" >
                                        {{ horario.h_dia }} de {{ horario.h_hora_inicio }} a {{ horario.h_hora_cierre }}</option>
                                </select> -->

                                <!-- </div> -->
                            </div>

                            <div class="btn-group" role="group">
                                <button type="button" class="btn btn-primary btn-sm"
                                    @click="crearProgramacion">Crear</button>
                                <button type="button" class="btn btn-danger btn-sm" @click="handleCreateCancel">
                                    Cancel
                                </button>
                            </div>
                        </form>
                    </div>
                </div>
            </div>
        </div>
        <div v-if="modalCreate" class="modal-backdrop fade show"></div>








        <div ref="editBookModal" class="modal fade"
            :class="{ show: activeEditPrograModal, 'd-block': activeEditPrograModal }" tabindex="-1" role="dialog">
            <div class="modal-dialog" role="document">
                <div class="modal-content">
                    <div class="modal-header">
                        <h5 class="modal-title">Actualizar ID: {{ editPrograForm.prof_id }} </h5>
                        <button type="button" class="close" data-dismiss="modal" aria-label="Close"
                            @click="toggleEditPrograModal">
                            <span aria-hidden="true">&times;</span>
                        </button>
                    </div>
                    <div class="modal-body">
                        <form>
                            <div class="mb-3">
                                <label for="editBookTitle" class="form-label">Fecha de inicio:</label>
                                <input type="date" class="form-control" id="editBookTitle"
                                    v-model="editPrograForm.prof_celular" placeholder="">
                            </div>
                            <div class="mb-3">
                                <label for="editBookTitle" class="form-label">Fecha de finalización:</label>
                                <input type="date" class="form-control" id="editBookTitle"
                                    v-model="editPrograForm.prof_celular" placeholder="">
                            </div>
                            <div class="mb-3">
                                <label for="editBookTitle" class="form-label">Duración:</label>
                                <input type="text" class="form-control" id="editBookTitle"
                                    v-model="editPrograForm.prog_duracion" placeholder="">
                            </div>
                            <div class="mb-3">
                                <label for="editBookTitle" class="form-label">Horario:</label>
                                <select name="" id="" v-model="editPrograForm.h_id">
                                    <option v-for="horario in listaHorarios" :key="horario.h_id" :value=horario.h_id>
                                        {{ horario.h_dia }} de {{ horario.h_hora_inicio }} a {{ horario.h_hora_cierre }}
                                    </option>
                                </select>

                            </div>
                            <div class="mb-3">
                                <label for="editBookTitle" class="form-label">Profesor:</label>
                                <select name="" id="" v-model="editPrograForm.prof_id">
                                    <option v-for="profesor in listaProfesores" :key="profesor.prof_id"
                                        :value="profesor.prof_id">
                                        {{ profesor.prof_nombres }} {{ profesor.prof_apellidos }}</option>
                                </select>
                            </div>


                            <div class="btn-group" role="group">
                                <button type="button" class="btn btn-primary btn-sm" @click="actualizar">
                                    Editar
                                </button>
                                <button type="button" class="btn btn-danger btn-sm" @click="handleEditCancel">
                                    Cancelar
                                </button>
                            </div>
                        </form>
                    </div>
                </div>
            </div>
        </div>
        <div v-if="activeEditPrograModal" class="modal-backdrop fade show"></div>






    </div>
</template>

<script>
import AdminNav from '../components/AdminNav.vue'
import Modal from '../components/modal.vue'

import moment from 'moment'
import axios from 'axios'
export default {
    components: {
        AdminNav,Modal
    },
    data() {
        return {
            listaProgramacion: [],
            listaHorarios: [],
            listaProfesores: [],
            listaCursos: [],
            EstadoEditar: true,
            modalCreate: false,
            activeEditPrograModal: false,
            editPrograForm: {},
            nuevaProgramacion: {
                fecha_inicio: "",
                fecha_fin: "",
                duracion: "",
                prof_id: '',
                h_id: "",
                c_id: "",

            },
            itemProfe: {
                prof_id: ''
            },
            abrirModal: false,
            Mensaje: 'Hola'
            
        }

    },
    methods: {
        getprogramaciones() {
            const path = 'http://127.0.0.1:5000/api/programacion'
            axios.get(path)
                .then((res) => {
                    this.listaProgramacion = res.data.datos

                    console.log(this.listaProgramacion)
                })
                .catch((error) => {
                    console.log(error);
                })
        },
        getHorarios() {
            const path = 'http://127.0.0.1:5000/api/horarios'
            axios.get(path)
                .then((res) => {
                    this.listaHorarios = res.data.datos
                    console.log(this.listaHorarios)
                })
                .catch((error) => {
                    console.log(error);
                })
        },
        getProfesores() {
            const path = 'http://127.0.0.1:5000/api/profesores'
            axios.get(path)
                .then((res) => {
                    this.listaProfesores = res.data.datos
                    console.log(this.listaProfesores)
                })
                .catch((error) => {
                    console.log(error);
                })
        },
        getCursos() {
            const path = 'http://127.0.0.1:5000/api/cursos'
            axios.get(path)
                .then((res) => {
                    this.listaCursos = res.data.datos
                    console.log(this.listaCursos)
                })
                .catch((error) => {
                    console.log(error);
                })
        },
        crearProgramacion() {
            const path = 'http://127.0.0.1:5000/api/programacion'
            const payload = {
                fecha_inicio: this.nuevaProgramacion.fecha_inicio,
                fecha_fin: this.nuevaProgramacion.fecha_fin,
                duracion: this.nuevaProgramacion.duracion,
                horario: this.nuevaProgramacion.h_id,
                profesor: this.nuevaProgramacion.prof_id,
                curso: this.nuevaProgramacion.c_id,

            }
            axios.post(path, payload)
                .then((res) => {
                    this.getprogramaciones()
                    console.log(res.data.mensaje)
                    console.log(res.data.datos)
                    this.Mensaje = res.data.mensaje
                    this.abrirModal = true
                    this.modalCreate = false
                    this.nombreP = ''
                    this.apellidoP = ''
                    this.celularP = ''
                    this.fechaP = ''
                })
                .catch((error) => {
                    console.log(error)
                })
            // console.log(payload)
        },
        toggleCreateModal() {

            const body = document.querySelector('body');
            this.modalCreate = !this.modalCreate;
            if (this.modalCreate) {
                body.classList.add('modal-open');
            } else {
                body.classList.remove('modal-open');
            }
            // this.editPrograForm.id = id
            // console.log(this.editPrograForm)
        },
        toggleEditPrograModal(programacion) {
            if (programacion) {
                this.editPrograForm = programacion;
            }
            const body = document.querySelector('body');
            this.activeEditPrograModal = !this.activeEditPrograModal;
            if (this.activeEditPrograModal) {
                body.classList.add('modal-open');
            } else {
                body.classList.remove('modal-open');
            }
            // this.editPrograForm.id = id
            console.log(this.editPrograForm)
        },

        actualizar() {
            const path = 'http://127.0.0.1:5000/api/programacion';
            const payload = {
                id: this.editPrograForm.prog_id,
                fecha_inicio: this.editPrograForm.prog_fecha_inicio,
                fecha_fin: this.editPrograForm.prog_fecha_fin,
                duracion: this.editPrograForm.prog_duracion,
                horario: this.editPrograForm.h_id,
                profesor: this.editPrograForm.prof_id,
            }
            axios.put(path, payload)
                .then((res) => {
                    console.log(res.data.mensaje)
                    // if (res.data.mensaje == "Inscripcion creada"){
                    //   console.log("Inscrito")
                    // }} 
                    this.getprogramaciones()
                    this.Mensaje = res.data.mensaje
                    this.abrirModal = true
                    this.activeEditPrograModal = false
                })
                .catch(error => {
                    console.log(error)
                })
            console.log(payload)

        },
        eliminar(id) {
            const path = 'http://127.0.0.1:5000/api/programacion/' + id
            axios.delete(path).
                then((res) => {
                    console.log(res.data.mensaje)
                    this.Mensaje = res.data.mensaje
                    this.abrirModal = true
                   
                    this.getprogramaciones()

                })
                .catch(error => {
                    console.log(error)
                })
        },
        handleCreateCancel() {
            this.toggleCreateModal(null);
            this.nombreP = ''
            this.apellidoP = ''
            this.celularP = ''
            this.fechaP = ''
            // this.initForm();
            // this.getBooks(); // why?
        },
        handleEditCancel() {
            this.toggleEditPrograModal(null);
            // this.initForm();
            // this.getBooks(); // why?
        },
        fechaFormateada1(x) {

            return moment(x, 'ddd, DD MMM YYYY HH:mm:ss [GMT]').format('DD/MM/YYYY')
        },
        fechaFormateada2(y) {

            return moment(y, 'ddd, DD MMM YYYY HH:mm:ss [GMT]').format('DD/MM/YYYY')
        }

    },
    created() {
        this.getprogramaciones()
        this.getHorarios()
        this.getProfesores()
        this.getCursos()

    }
}
</script>
<style scoped>
.container {
    /* border: 5px solid red; */
    /* background: red; */
}

.crear-curso {
    margin: 2px auto;
    width: 420px;
    /* border: 2px solid red; */
    display: flex;
    justify-content: space-between;
    align-items: center;
}

tbody {
    border: 3px solid green;
    font-weight: 600;

}

table {
    /* border: 2px solid blue; */
    border: 3px solid green;
    border-radius: 20px;

    width: 100%;
    height: 100%;
}

/* input{
    width: auto;
    
} */

.input-nombre {
    width: auto;
    height: auto;
}

.input-descripcion {
    width: 550px;

}</style>