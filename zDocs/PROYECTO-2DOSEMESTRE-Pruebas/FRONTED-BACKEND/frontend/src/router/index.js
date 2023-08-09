import { createRouter, createWebHistory } from 'vue-router'
import Api from '../components/Api.vue'
import Inicio from '../views/InicioView.vue'
import Login from '../views/LoginView.vue'
import Nosotros from '../views/NosotrosView.vue'
import Select from '../components/Select.vue'
import Cursos from '../views/CursosView.vue'
import Inscripciones from '../views/InscripcionesView.vue'
import InicioAdmin from '../views/InicioAdmin.vue'
import AdminCursos from '../views/AdminCursos.vue'
import AdminProgramaciones from '../views/AdminProgramaciones.vue'
import AdminProfesores from '../views/AdminProfesores.vue'
import AdminInscripciones from '../views/AdminInscripciones.vue'
import Certificado from '../views/AdminCertificado.vue'
// import Registro from '../views/RegistrarView.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path:'/',
      name: 'inicio',
      component: Inicio
    },
    {
      path: '/api',
      name: 'api',
      component: Api
    },
    {
      path: '/nosotros',
      name: 'nosotros',
      component: Nosotros
    },
    {
      path: '/select',
      name: 'select',
      component: Select
    },
    {
      path: '/login',
      name: 'login',
      component: Login
    },
    {
      path: '/cursos',
      name: 'cursos',
      component: Cursos
    },
    {
      path: '/cursos/:id',
      name: 'inscripciones',
      component: Inscripciones
    },
    {
      path: '/admin/',
      name: 'inicioAdmin',
      component: InicioAdmin
    },
    {
      path: '/admin/cursos',
      name: 'cursosAdmin',
      component: AdminCursos
    },
    {
      path: '/admin/programaciones',
      name: 'adminProgramaciones',
      component: AdminProgramaciones
    },
    {
      path: '/admin/profesores',
      name: 'AdminProfesores',
      component: AdminProfesores
    },
    {
      path: '/admin/programaciones/:id',
      name: 'AdminInscripciones',
      component: AdminInscripciones
    },
    {
      path: '/admin/programaciones/:id/:p_cedula/certificado',
      name: 'Certificado',
      component: Certificado
    },
    // {
    //   path: '/registrarse',
    //   name: 'registro',
    //   component: Registro
    // },
  ]

})

export default router
