<template>
    <div>
    <AdminNav></AdminNav>
    <Modal :modalCreate="abrirModal" :mensaje="Mensaje"></Modal>

        <div class="crear-curso">
            <h1> Profesores </h1>
            <button type="button" class="btn btn-success" @click="toggleCreateModal" >Agregar</button>
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
                        <th scope="col">Nombre</th>
                        <th scope="col">Apellido</th>
                        <th scope="col">Celular</th>
                        <th scope="col">Fecha Nacimiento</th>
                        <th></th>
                    </tr>
                </thead>
                <tbody>
                    <tr v-for="(profesor, index) in listaProfesores" :key="index">

                        <td>{{ profesor.prof_id }}</td>

                        <td>{{ profesor.prof_nombres }}</td>

                        <td>{{ profesor.prof_apellidos }}</td>
                        <td>{{ profesor.prof_celular }}</td>
                        <td> {{ profesor.prof_fecha_nacimiento }}</td>

                        <td> <button type="button" class="btn btn-warning btn-sm" @click="toggleEditProfeModal(profesor)">
                                <i class="bi bi-pencil-fill"></i>
                            </button>
                            <div class="btn-group" role="group">
                                <button type="button" class="btn btn-danger btn-sm" @click="eliminar(profesor.prof_id)"><i
                                        class="bi bi-trash3-fill"></i></button>
                            </div>
                        </td>
                    </tr>
                </tbody>
            </table>

        </div>

















        <div class="modal fade" :class="{ show: modalCreate, 'd-block': modalCreate }" tabindex="-1" role="dialog">
            <div class="modal-dialog" role="document">
                <div class="modal-content">
                    <div class="modal-header">
                        <h5 class="modal-title">Crear profesor </h5>
                        <button type="button" class="close" data-dismiss="modal" aria-label="Close"
                            @click="toggleCreateModal">
                            <span aria-hidden="true">&times;</span>
                        </button>
                    </div>
                    <!-- kjkññhñññk -->
                    <div class="modal-body">
                        <form>
                            <div class="mb-3">
                                <label class="form-label">Nombre:</label>
                                <input type="text" class="form-control" v-model="nombreP">
                            </div>
                            <div class="mb-3">
                                <label class="form-label">Apellido:</label>
                                <input type="text" class="form-control" v-model="apellidoP">
                            </div>
                            <div class="mb-3">
                                <label class="form-label">Celular:</label>
                                <input type="text" class="form-control" v-model="celularP">
                            </div>
                            <div class="mb-3">
                                <label class="form-label">Descripcion:</label>
                                <input type="date" class="form-control" v-model="fechaP">
                            </div>
                            <div class="btn-group" role="group">
                                <button type="button" class="btn btn-primary btn-sm" @click="crearProfesor">Crear</button>
                                <button type="button" class="btn btn-danger btn-sm" @click="handleCreateCancel ">
                                    Cancel
                                </button>
                            </div>
                        </form>
                    </div>
                </div>
            </div>
        </div>
        <div v-if="modalCreate" class="modal-backdrop fade show"></div>








        <div ref="editBookModal" class="modal fade" :class="{ show: activeEditProfeModal, 'd-block': activeEditProfeModal }"
            tabindex="-1" role="dialog">
            <div class="modal-dialog" role="document">
                <div class="modal-content">
                    <div class="modal-header">
                        <h5 class="modal-title">Actualizar ID: {{ editprofesorForm.prof_id }} </h5>
                        <button type="button" class="close" data-dismiss="modal" aria-label="Close"
                            @click="toggleEditProfeModal">
                            <span aria-hidden="true">&times;</span>
                        </button>
                    </div>
                    <div class="modal-body">
                        <form>
                            <div class="mb-3">
                                <label for="editBookTitle" class="form-label">Nombre:</label>
                                <input type="text" class="form-control" id="editBookTitle" v-model="editprofesorForm.prof_nombres"
                                    placeholder="">
                            </div>
                            <div class="mb-3">
                                <label for="editBookTitle" class="form-label">Apellido:</label>
                                <input type="text" class="form-control" id="editBookTitle" v-model="editprofesorForm.prof_apellidos"
                                    placeholder="">
                            </div>
                            <div class="mb-3">
                                <label for="editBookTitle" class="form-label">Celular:</label>
                                <input type="text" class="form-control" id="editBookTitle" v-model="editprofesorForm.prof_celular"
                                    placeholder="">
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
        <div v-if="activeEditProfeModal" class="modal-backdrop fade show"></div>






    </div>
</template>

<script>
import AdminNav from '../components/AdminNav.vue'   
import axios from 'axios'
import Modal from '../components/modal.vue'

export default {
    components:{
        AdminNav,
        Modal
    },
    data() {
        return {
            listaProfesores: [],
            EstadoEditar: true,
            modalCreate: false,
            activeEditProfeModal: false,
            editprofesorForm: {},
            nombreP: "",
            apellidoP: "",
            celularP: "",
            fechaP: '',

            abrirModal: false,
            Mensaje: ''
        }

    },
    methods: {
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
        crearProfesor() {
            const path = 'http://127.0.0.1:5000/api/profesores'
            const payload = {
                nombre: this.nombreP,
                apellido: this.apellidoP,
                celular: this.celularP,
                fecha: this.fechaP,
            }
            axios.post(path, payload)
                .then((res) => {
                    this.getProfesores()
                    console.log(res.data.mensaje)
                    console.log(res.data.datos)
                    this.Mensaje =res.data.mensaje
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
        },
        toggleCreateModal() {

            const body = document.querySelector('body');
            this.modalCreate = !this.modalCreate;
            if (this.modalCreate) {
                body.classList.add('modal-open');
            } else {
                body.classList.remove('modal-open');
            }
            // this.editprofesorForm.id = id
            // console.log(this.editprofesorForm)
        },
        toggleEditProfeModal(profesor) {
            if (profesor) {
                this.editprofesorForm = profesor;
            }
            const body = document.querySelector('body');
            this.activeEditProfeModal = !this.activeEditProfeModal;
            if (this.activeEditProfeModal) {
                body.classList.add('modal-open');
            } else {
                body.classList.remove('modal-open');
            }
            // this.editprofesorForm.id = id
            console.log(this.editprofesorForm)
        },
     
        actualizar() {
            const path = 'http://127.0.0.1:5000/api/profesores';
            const payload = {
                id: this.editprofesorForm.prof_id,
                nombres: this.editprofesorForm.prof_nombres,
                apellido: this.editprofesorForm.prof_apellidos,
                celular: this.editprofesorForm.prof_celular,
            }
            axios.put(path, payload)
                .then((res) => {
                    console.log(res.data.mensaje)
                    this.getProfesores()
                    this.Mensaje =res.data.mensaje
                    this.abrirModal= true
                    // this.message = res.data.mensaje;
                    // this.showMessage = true;
                    this.activeEditProfeModal = false
                })
                .catch(error => {
                    console.log(error)
                })
            console.log(payload)

        },
        eliminar(id) {
            const path = 'http://127.0.0.1:5000/api/profesores/' + id
            axios.delete(path).
                then((res) => {
                    console.log(res.data.mensaje)
                    this.Mensaje =res.data.mensaje
                    this.abrirModal= true
                    // this.message = res.data.mensaje;
                    // this.showMessage = true;
                    this.getProfesores()

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
            this.toggleEditProfeModal(null);
            // this.initForm();
            // this.getBooks(); // why?
        },


    },
    created() {
        this.getProfesores()
    }
}
</script>
<style scoped>
.container {
    /* border: 5px solid red; */
    /* background: red; */
}

.crear-curso{
    margin: 2px auto;
    width: 350px;
    /* border: 2px solid red; */
    display: flex;
        justify-content: space-between;
    align-items: center;
}


tbody {
    border: 3px solid green;

}

table {
    /* border: 2px solid blue; */
    border: 3px solid green;
    border-radius: 20px;

    width: 100%;
    height: 100%;
}


input{
    width: auto;
    
}

.input-nombre {
    width: auto;
    height: auto;
}

.input-descripcion {
    width: 550px;

}
</style>