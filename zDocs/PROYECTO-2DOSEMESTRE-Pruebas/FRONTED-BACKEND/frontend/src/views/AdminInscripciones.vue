<template>
    <div>
        <AdminNav></AdminNav>
        <Modal :modalCreate="abrirModal" :mensaje="Mensaje"></Modal>

        <div class="container">
            <div class="crear-curso">
                <h1>Inscripciones</h1>
                <button type="button" class="btn btn-success" @click="toggleCreateModal">Agregar</button>
            </div>
            <table class="table table-hover">
                <thead>
                    <tr>
                        <th scope="col">ID</th>
                        <th scope="col">Cedula</th>
                        <th scope="col">Nombre del participante</th>
                        <th scope="col">Fecha de inscripcion</th>
                        <th scope="col">Estado participante</th>
                        <th></th>
                    </tr>
                </thead>
                <tbody>
                    <tr v-for="inscripcion in  listaInscripciones " :key="inscripcion.i_id">

                        <td>{{ inscripcion.i_id }}</td>
                        <td>{{ inscripcion.p_cedula }}</td>

                        <td>{{ inscripcion.p_nombres }} {{ inscripcion.p_apellidos }}</td>
                        <td>{{ fechaFormateada1(inscripcion.i_fecha_inscripcion) }}</td>

                        <td>{{ inscripcion.ei_descripcion }}</td>

                        <td> <button type="button" class="btn btn-warning btn-sm"
                                @click="toggleEditInscripcionesModal(inscripcion)">
                                <i class="bi bi-pencil-fill"></i>
                            </button>
                            <button type="button" class="btn btn-danger btn-sm" @click="eliminar(inscripciones.prog_id)"><i
                                    class="bi bi-trash3-fill"></i></button>
                 <button type="button" class="btn btn-success btn-sm" v-if="inscripcion.ei_id == 3" @click="certificado(inscripcion.p_cedula)"><i class="bi bi-save2"></i></button>
                        </td>
                    </tr>
                </tbody>
            </table>

        </div>






        <div ref="editBookModal" class="modal fade"
            :class="{ show: activeEditInscripcionModal, 'd-block': activeEditInscripcionModal }" tabindex="-1" role="dialog">
            <div class="modal-dialog" role="document">
                <div class="modal-content">
                    <div class="modal-header">
                        <h5 class="modal-title">Actualizar ID: {{ editInscripcionForm.i_id }}</h5>
                        <button type="button" class="close" data-dismiss="modal" aria-label="Close"
                            @click="toggleEditInscripcionesModal">
                            <span aria-hidden="true">&times;</span>
                        </button>
                    </div>
                    <div class="modal-body">
                        <form>
                            <div class="mb-3">
                                <label for="editBookTitle" class="form-label">Estado participante:</label>
                                <select name="" id="" v-model="editInscripcionForm.ei_id">
                                    <option v-for="estado in listaEstadosIns" :key="estado.ei_id" :value=estado.ei_id>
                                        {{ estado.ei_id }}--{{ estado.ei_descripcion }}
                                    </option>
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
        <div v-if="activeEditInscripcionModal" class="modal-backdrop fade show"></div>











    </div>
</template>

<script>
import AdminNav from '../components/AdminNav.vue'
import axios from 'axios'
import moment from 'moment'
import Modal from '../components/modal.vue'

export default {
    components: {
        AdminNav,
        Modal
    },
    data() {
        return {
            listaInscripciones: [],
            editInscripcionForm:{},
            activeEditInscripcionModal: false,
            listaEstadosIns : []
        }
    },
    methods: {
        getInscripciones() {
            const path = 'http://127.0.0.1:5000/api/inscripciones/' + this.$route.params.id
            axios.get(path)
                .then((res) => {
                    this.listaInscripciones = res.data.datos
                    console.log(this.listaInscripciones)
                })
                .catch(error => {
                    console.log(error)
                })
        },
        getEstadosInscripcion(){
            const path = 'http://127.0.0.1:5000/api/estados' 
            axios.get(path)
                .then((res) => {
                    this.listaEstadosIns = res.data.datos
                    console.log(this.listaEstadosIns)
                })
                .catch(error => {
                    console.log(error)
                })
        },
        actualizar() {
            const path = 'http://127.0.0.1:5000/api/inscripciones';
            const payload = {
                id: this.editInscripcionForm.i_id,
                ei_id: this.editInscripcionForm.ei_id,
            }
            axios.put(path, payload)
                .then((res) => {
                    console.log(res.data.mensaje)
                     this.getInscripciones()
                     this.activeEditInscripcionModal = false
                    
                    this.Mensaje = res.data.mensaje
                    this.abrirModal = true
                })
                .catch(error => {
                    console.log(error)
                })
            console.log(payload)

        },
        fechaFormateada1(x) {
            return moment(x, 'ddd, DD MMM YYYY HH:mm:ss [GMT]').format('DD/MM/YYYY')
        },
        toggleEditInscripcionesModal(inscripcion) {
            if (inscripcion) {
                this.editInscripcionForm = inscripcion;
            }
            const body = document.querySelector('body');
            this.activeEditInscripcionModal = !this.activeEditInscripcionModal;
            if (this.activeEditInscripcionModal) {
                body.classList.add('modal-open');
            } else {
                body.classList.remove('modal-open');
            }
            // this.editInscripcionForm.id = id
            console.log(this.editInscripcionForm)
        },
        certificado(x){
            this.$router.push(this.$route.params.id+"/"+x+"/certificado")
        }
    },
    created() {
        this.getInscripciones()
        this.getEstadosInscripcion()
    }
}
</script>

<style scoped>
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
</style>