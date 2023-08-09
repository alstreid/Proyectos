<template>
    <div class="container">
      <div class="row">
        <div class="col-sm-12">
          <h1>Books</h1>
          <hr><br><br>
          <button
          type="button"
          class="btn btn-success btn-sm"
          @click="toggleAddBookModal">
          Add Book
        </button>
          <br><br>
          <table class="table table-hover">
            <thead>
              <tr>
                <th scope="col">Cedula</th>
                <th scope="col">Nombres</th>
                <th scope="col">Apellidos</th>
                <th scope="col">Celular</th>
                <th scope="col">Fecha de nacimiento</th>
                <th scope="col">Dirección</th>
                <th scope="col">Genero</th>
                <th scope="col">Correo</th>
                <th scope="col">Contraseña</th>
                <th></th>
              </tr>
            </thead>
            <tbody>
              <tr v-for="(admin,index) in administradores" :key="index">
                <td>{{ index }}</td>
                <td>{{ admin.a_cedula }}</td>
                <td>{{ admin.a_nombres }}</td>
                <td>{{ admin.a_apellidos }}</td>
                <td>{{ admin.a_celular }}</td>
                <td>{{ admin.a_correo }}</td>
                <td>{{ admin.a_contraseña }}</td>
                <!-- <td>
                    <span v-if="participante.p_genero">Hombre</span>
                    <span v-else>Mujer</span>
                </td> -->
                <!-- <td>{{ participante.p_correo }}</td> -->
                <td>hola</td>
                <!-- <td>{{ participante.p_contraseña }}</td> -->
                <td>siii</td>
                <td>
                  <div class="btn-group" role="group">
                    <button type="button" class="btn btn-warning btn-sm">Update</button>
                    <button type="button" class="btn btn-danger btn-sm">Delete</button>
                  </div>
                </td>
              </tr>
            </tbody>
          </table>
        </div>
      </div>
      <div
      ref="addBookModal"
      class="modal fade"
      :class="{ show: activeAddAdminModal, 'd-block': activeAddAdminModal }"
      tabindex="-1"
      role="dialog">
      <div class="modal-dialog" role="document">
        <div class="modal-content">
          <div class="modal-header">
            <h5 class="modal-title">Add a new book</h5>
            <button
              type="button"
              class="close"
              data-dismiss="modal"
              aria-label="Close"
              @click="toggleAddAdminModal">
              <span aria-hidden="true">&times;</span>
            </button>
          </div>
          <div class="modal-body">
            <form>
              <div class="mb-3">
                <label for="addAdminCedula" class="form-label">Cedula</label>
                <input
                  type="text"
                  class="form-control"
                  id="addAdminCedula"
                  v-model="addAdminForm.cedula"
                  placeholder="Enter title">
              </div>
              <div class="mb-3">
                <label for="addAdminNombre" class="form-label">Nombre</label>
                <input
                  type="text"
                  class="form-control"
                  id="addAdminNombre"
                  v-model="addAdminForm.nombre"
                  placeholder="Enter title">
              </div>
              <div class="mb-3">
                <label for="addAdminApellido" class="form-label">Apellido</label>
                <input
                  type="text"
                  class="form-control"
                  id="addAdminApellido"
                  v-model="addAdminForm.apellido"
                  placeholder="Enter author">
              </div>
              <div class="mb-3 ">
                <label class="form-check-label" for="addBookRead">Celular</label>
                <input
                type="text"
                class="form-control"
                id="addBookRead"
                v-model="addAdminForm.celular">
              </div>
              <div class="mb-3">
                <label for="addAdminCorreo" class="form-label">Correo</label>
                <input
                  type="text"
                  class="form-control"
                  id="addAdminCorreo"
                  v-model="addAdminForm.correo"
                  placeholder="Enter author">
              </div>
              <div class="mb-3">
                <label for="addAdminContraseña" class="form-label">Contraseña</label>
                <input
                  type="text"
                  class="form-control"
                  id="addAdminContraseña"
                  v-model="addAdminForm.contraseña"
                  placeholder="Enter author">
              </div>
              <div class="btn-group" role="group">
                <button
                  type="button"
                  class="btn btn-primary btn-sm"
                  @click="handleAddSubmit">
                  Submit
                </button>
                <button
                  type="button"
                  class="btn btn-danger btn-sm"
                  @click="handleAddReset">
                  Reset
                </button>
              </div>
            </form>
          </div>
        </div>
      </div>
    </div>
    <div v-if="activeAddAdminModal" class="modal-backdrop fade show"></div>
  </div>
   



    
  </template>


<script>
import axios from 'axios';

export default {
  data() {
    return {
      activeAddAdminModal: false,
      addAdminForm: {
        cedula: '',
        nombre: '',
        apellido: '',
        celular: '',
        correo:'',
        contraseña:''
      },
      administradores: [],
    };
  },
  methods: {
    getParticipantes() {
      const path = 'http://localhost:5000/api/admins';
      axios.get(path)
        .then((res) => {
          this.administradores = res.data.datos
        })
        .catch((error) => {
          console.error(error);
        });
    },postAdmins(payload){
      const path = 'http://localhost:5000/api/admins';
      axios.post(path,payload)
        .then(() => {
          this.getParticipantes()
        })
        .catch((error)=>{
          console.log(error)
          this.getParticipantes()
        })
        
    },
    imprimir(){
      console.log(this.addAdminForm)
    },
    handleAddReset() {
      this.initForm();
    },
    handleAddSubmit() {
      // this.toggleAddAdminModal();
      const payload = {
        cedula: this.addAdminForm.cedula,
        nombre: this.addAdminForm.nombre,
        apellido: this.addAdminForm.apellido,
        celular: this.addAdminForm.celular,
        correo: this.addAdminForm.correo,
        contraseña: this.addAdminForm.contraseña,
      };
      this.postAdmins(payload);
      // this.initForm();
    },
    initForm() {
      this.addAdminForm.cedula = '';
      this.addAdminForm.nombre = '';
      this.addAdminForm.apellido = '';
      this.addAdminForm.celular = '';
      this.addAdminForm.correo = '';
      this.addAdminForm.contraseña = '';
    },
    toggleAddBookModal() {
      const body = document.querySelector('body');
      this.activeAddAdminModal = !this.activeAddAdminModal;
      if (this.activeAddAdminModal) {
        body.classList.add('modal-open');
      } else {
        body.classList.remove('modal-open');
      }
    },
  },
  created() {
    this.getParticipantes();
  },
};
</script>