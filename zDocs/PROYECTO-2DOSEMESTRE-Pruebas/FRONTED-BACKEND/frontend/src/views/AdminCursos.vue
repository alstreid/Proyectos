<template>
    <div>
        <AdminNav></AdminNav>
        <Modal :modalCreate="abrirModal" :mensaje="Mensaje"></Modal>
        <div class="crear-curso">
            <h1> Cursos</h1>
            <button type="button" class="btn btn-success" @click="toggleCreateModal" >Agregar</button>
        </div>
        

<div class="container">

    <table class="table table-hover glass-efect">
        <thead>
            <tr class="border border-success rounded-5">
                <th scope="col">ID</th>
                <th scope="col">Nombre del curso</th>
                <th scope="col">Descripcion</th>
                <th></th>
            </tr>
        </thead>
        <tbody>
            <tr v-for="(curso, index) in listaCursos" :key="index">

                <td>{{ curso.c_id }}</td>

                <td v-if="EstadoEditar">{{ curso.c_nombre }}</td>
                <td v-else><input type="text" :placeholder="curso.c_nombre" class="input-nombre"
                        v-model="nombreC">
                </td>

                <td v-if="EstadoEditar">{{ curso.c_descripcion }}</td>
                <td v-else><input type="text" :placeholder="curso.c_descripcion" class="input-descripcion"
                        v-model="nombreC"></td>


                <!-- <td v-if="curso.c_estado && EstadoEditar">Habilitado</td>
<td v-else>
<input type="radio">Habilitado                    
<input type="radio">Desabilitado          
</td>
<td v-if="!curso.c_estado && EstadoEditar">Desahibilitado</td> -->

                <td> <button type="button" class="btn btn-warning btn-sm"
                        @click="toggleEditBookModal(curso)">
                        <i class="bi bi-pencil-fill"></i>
                    </button>
                    <div class="btn-group" role="group">
                        <button type="button" class="btn btn-danger btn-sm" @click="eliminar(curso.c_id)"><i
                                class="bi bi-trash3-fill"></i></button>
                    </div>
                </td>
            </tr>
        </tbody>
    </table>

</div>

       

        <div>
            <div class="alert alert-success" role="alert" v-if="showMessage">{{ message }}</div>
            <br />
        </div>

















        <div class="modal fade" :class="{ show: modalCreate, 'd-block': modalCreate }" tabindex="-1" role="dialog">
            <div class="modal-dialog" role="document">
                <div class="modal-content">
                    <div class="modal-header">
                        <h5 class="modal-title">Crear curso </h5>
                        <button type="button" class="close" data-dismiss="modal" aria-label="Close"
                            @click="toggleCreateModal">
                            <span aria-hidden="true">&times;</span>
                        </button>
                    </div>
                    <div class="modal-body">
                        <form>
                            <div class="mb-3">
                                <label class="form-label">Nombre:</label>
                                <input type="text" class="form-control" v-model="nombreC">
                            </div>
                            <div class="mb-3">
                                <label class="form-label">Descripcion:</label>
                                <input type="text" class="form-control" v-model="descripcionC">
                            </div>
                            <div class="btn-group" role="group">
                                <button type="button" class="btn btn-primary btn-sm" @click="crearCurso">Crear</button>
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








        <div ref="editBookModal" class="modal fade" :class="{ show: activeEditBookModal, 'd-block': activeEditBookModal }"
            tabindex="-1" role="dialog">
            <div class="modal-dialog" role="document">
                <div class="modal-content">
                    <div class="modal-header">
                        <h5 class="modal-title">Actualizar ID: {{ editCursoForm.c_id }} </h5>
                        <button type="button" class="close" data-dismiss="modal" aria-label="Close"
                            @click="toggleEditBookModal">
                            <span aria-hidden="true">&times;</span>
                        </button>
                    </div>
                    <div class="modal-body">
                        <form>
                            <div class="mb-3">
                                <label for="editBookTitle" class="form-label">Nombre:</label>
                                <input type="text" class="form-control" id="editBookTitle" v-model="editCursoForm.c_nombre"
                                    placeholder="">
                            </div>
                            <div class="mb-3">
                                <label for="editBookAuthor" class="form-label">Descripcion:</label>
                                <input type="text" class="form-control" id="editBookAuthor"
                                    v-model="editCursoForm.c_descripcion" placeholder="Enter author">
                            </div>
                            <div class="mb-3 form-check">
                                <!-- <input type="checkbox" class="form-check-input" id="editBookRead"
                                            v-model="editBookForm.read"> -->
                                <!-- <label class="form-check-label" for="editBookRead">Read?</label> -->
                            </div>
                            <div class="btn-group" role="group">
                                <button type="button" class="btn btn-primary btn-sm" @click="actualizar">
                                    Submit
                                </button>
                                <button type="button" class="btn btn-danger btn-sm" @click="handleEditCancel">
                                    Cancel
                                </button>
                            </div>
                        </form>
                    </div>
                </div>
            </div>
        </div>
        <div v-if="activeEditBookModal" class="modal-backdrop fade show"></div>


        




    </div>
</template>

<script>
import AdminNav from '../components/AdminNav.vue'
import Modal from '../components/modal.vue'

import axios from 'axios'
export default {
    components: {
        AdminNav,
        Modal
    },
    data() {
        return {
            listaCursos: [],
            EstadoEditar: true,
            modalCreate: false,
            activeEditBookModal: false,
            editCursoForm: {},
            nombreC: "",
            descripcionC: '',
            Mensaje: '',
            abrirModal: false,
            message: '',
            showMessage: false,
        }

    },
    methods: {
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
        crearCurso() {
            const path = 'http://127.0.0.1:5000/api/cursos'
            const payload = {
                nombre: this.nombreC,
                descripcion: this.descripcionC
            }
            axios.post(path, payload)
                .then((res) => {
                    this.getCursos()
                    this.Mensaje = res.data.mensaje
                    this.abrirModal = true
                    console.log(res.data.mensaje)
                    console.log(res.data.datos)
                    this.modalCreate = false
                    this.nombreC = ''
                    this.descripcionC = ''
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
            // this.editCursoForm.id = id
            // console.log(this.editCursoForm)
        },
        toggleEditBookModal(curso) {
            if (curso) {
                this.editCursoForm = curso;
            }
            const body = document.querySelector('body');
            this.activeEditBookModal = !this.activeEditBookModal;
            if (this.activeEditBookModal) {
                body.classList.add('modal-open');
            } else {
                body.classList.remove('modal-open');
            }
            // this.editCursoForm.id = id
            console.log(this.editCursoForm)
        },
        // handleEditSubmit() {
        //     this.toggleEditBookModal(null);
        //     let read = false;
        //     if (this.editBookForm.read) read = true;
        //     const payload = {
        //         title: this.editBookForm.title,
        //         author: this.editBookForm.author,
        //         read,
        //     };
        //     this.updateBook(payload, this.editBookForm.id);
        // },
        actualizar() {
            const path = 'http://127.0.0.1:5000/api/cursos';
            const payload = {
                id: this.editCursoForm.c_id,
                nombre: this.editCursoForm.c_nombre,
                descripcion: this.editCursoForm.c_descripcion,
            }
            axios.put(path, payload)
                .then((res) => {
                    console.log(res.data.mensaje)
                    // if (res.data.mensaje == "Inscripcion creada"){
                    //   console.log("Inscrito")
                    // }} 
                    this.getCursos()
                    this.Mensaje = res.data.mensaje
                    this.abrirModal = true
                    // this.message = res.data.mensaje;
                    // this.showMessage = true;
                    this.activeEditBookModal = false
                })
                .catch(error => {
                    console.log(error)
                })
            console.log(payload)

        },
        eliminar(id) {
            const path = 'http://127.0.0.1:5000/api/cursos/' + id
            axios.delete(path).
                then((res) => {
                    console.log(res.data.mensaje)
                    this.message = res.data.mensaje;
                    this.Mensaje = res.data.mensaje
                    this.abrirModal = true
                    // this.showMessage = true;
                    this.getCursos()

                })
                .catch(error => {
                    console.log(error)
                })
        },
        handleCreateCancel() {
            this.toggleCreateModal(null);

            // this.initForm();
            // this.getBooks(); // why?
        },
        handleEditCancel() {
            this.toggleEditBookModal(null);

            // this.initForm();
            // this.getBooks(); // why?
        },


    },
    created() {
        this.getCursos()
    }
}
</script>
<style scoped>
.container {
    /* text-align: center; */
    /* border: 5px solid red; */
    /* border: 3px solid green; */

    /* background: red; */
}
h1{
    text-align: center;
}
.crear-curso{
    margin: 2px auto;
    width: 250px;
    /* border: 2px solid red; */
    display: flex;
        justify-content: space-between;
    align-items: center;
}
/* .crear-curso button{
    width: 60px;
    height: 25px;
    border: 2px solid blue;
    border-radius: 15px ;
    background: blue;
} */
/* .crear-curso button p {
    text-align: center;
    font-size: 20px;
    color:black;
} */

/* thead{
    border: 2px solid red;
} */

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

.glass-efect {
    background: #fafafa10;
    backdrop-filter: blur(0.4rem);
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

}




</style>