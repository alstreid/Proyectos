<template>
    <div class="contenedor-general">
        <Modal :modalCreate="abrirModal" :mensaje="Mensaje"></Modal>
        <div class="fondo"></div>
    <div class="container">
        <div class="content">
            <a href="/"><h2 class="logo"><i class='bx bxl-firebase' ></i>Academia de baile</h2> </a>
            <div class="texto">
                <h2>Bienvenido! <br> <span>A nuestro sitio web.</span></h2>
                <p>Hay atajos para la felicidad, y el baile es uno de ellos</p>
                     <div class="iconos">
                        <a href=""><i class='bx bxl-linkedin'></i></a>
                        <a href=""><i class='bx bxl-facebook-circle' ></i></a>
                        <a href=""><i class='bx bxl-instagram' ></i></a>
                        <a href=""><i class='bx bxl-twitter'></i></a>
                     </div>
            </div>
        </div>
        <div class="logreg-box"  :class= "{'active' : activoRegistro}">
            <div class="form-box login">
                <form  v-on:submit.prevent="login">
                    <h2>Iniciar Sesion</h2>

                    <div class="input-box">
                        <span class="icono"><i class='bx bxl-gmail'  ></i></span>
                        <input type="email" required v-model="usuario">
                        <label>Usuario</label>
                    </div>

                    <div class="input-box">
                        <span class="icono"><i class='bx bx-lock-alt' ></i></span>
                        <input type="password" required v-model="password">
                        <label>Contraseña</label>
                    </div>
                    <div class="olvidar">
                        <!-- <label><input type="checkbox">Ver Contraseña</label> -->
                        <!-- <a href="">Olvidaste la contraseña?</a> -->
                    </div>
                    <button type="submit" class="boton">Iniciar</button>
                    <div class="login-register">
                        <p>No tengo cuenta <a href="#" @click= "activoRegistro = true" class="register-link">Registrarse</a></p>
                    </div>
                </form>
            </div>


            <div class="form-box register">
                <form action="#" >
                    <h2>Registrarse</h2>

                    <div class="input-box nombre">
                        <span class="icono"><i class='bx bxs-user' ></i></span>
                        <input type="text" required>
                        <label>Nombre</label>
                    </div>
                    <div class="input-box apellido">
                        <span class="icono"><i class='bx bxs-user' ></i></span>
                        <input type="text" required>
                        <label>Apellido</label>
                    </div>

                    <div class="input-box correo">
                        <span class="icono"><i class='bx bxl-gmail' ></i></span>
                        <input type="email" required>
                        <label>Correo</label>
                    </div>

                    <div class="input-box contraseña">
                        <span class="icono"><i class='bx bx-lock-alt' ></i></span>
                        <input type="text" required>
                        <label>Contraseña</label>
                    </div>
                    <div class="input-box direccion">
                        <span class="icono"><i class='bx bx-lock-alt' ></i></span>
                        <input type="text" required>
                        <label>Direccion</label>
                    </div>
                    <div class="input-box genero">
                        <!-- <span class="icono"><i class='bx bx-lock-alt' ></i></span> -->
                        <section>
                            <option value=""></option>
                        </section>
                        <!-- <input type="select" required> -->
                        <label>Genero</label>
                    </div>
                    <div class="input-box fecha">
                        <span class="icono"><i class='bx bx-lock-alt' ></i></span>
                        <input type="text" required>
                        <label>Fecha Nacimiento</label>
                    </div>

                    <div class="olvidar">
                        <!-- <label><input type="checkbox">Estoy de acuerdo con los términos y condiciones</label> -->
                
                    </div>
                    <button type="submit" class="boton">Registrarse</button>
                    <div class="login-register">
                        <p>Ya tengo cuenta <a href="#" class="login" @click= "activoRegistro = false">Iniciar Sesion</a></p>
                    </div>
                </form>
            </div>
        </div>
    </div>

    </div>
</template>


<script>
import Modal from '../components/modal.vue'

import axios from 'axios';
export default {
    components:{
        Modal
    },
    data (){
        return{
            usuario: "",
            password: "",
            error: false,
            error_msg: "",
            activoRegistro: false,
            Mensaje: '',
            abrirModal: false,
        }
    },
    methods:{
        login(){
               let json  ={
                    "usuario": this.usuario,
                    "password": this.password
               } 
            //    console.log(json)
                const path = 'http://127.0.0.1:5000/login'
                axios.post(path,json)
                .then((res) =>{
                    if (res.data.mensaje == 'Usuario Encontrado'){

                        sessionStorage.setItem("session",JSON.stringify(res.data.credenciales))
                        this.dbusuario = res.data.credenciales
                        // console.log(res.data.mensaje) 
                        // this.alert
                        console.log(this.dbusuario.p_cedula)
                        this.$router.push('/')
                    }else{
                        this.Mensaje = 'Usuario o contraseña incorrectos'
                        this.abrirModal = true
                    }
                    
                }).catch((error) =>{
                    console.error(error)
                })
            },
            registrarse(){
                const logregBox = document.querySelector('.logreg-box');
                logregBox.classList.add('active');
            }
    }
    // , 
    //     mounted() {
    //         getUser()
    //     }
}
</script>



<style scoped>
@import url('https://fonts.googleapis.com/css2?family=Dancing+Script:wght@700&family=Poppins:ital,wght@0,100;0,400;0,600;0,700;0,800;1,500&display=swap');

* {
    margin: 0;
    padding: 0;
    box-sizing: border-box;
    font-family: 'Poppins', sans-serif;
    text-decoration: none;
    outline: none;
}
.contenedor-general{
    background: #020202;
}
.content a{
    color:#e4e4e4
}
.fondo{
    width: 100%;
    height: 100vh;
    background: none;
    background-size: cover;
    background-position: center;
    filter:blur(10px)
}
.container{ 
    position: absolute;
    top: 45%;
    left: 50%;
    transform: translate(-50%, -50%);
    width: 75%;
    height: 500px;
    background: url(../assets/img/Captura.png)no-repeat;
    background-size: cover;
    background-position: center;
    border-radius: 10px;
    margin-top: 20px;
    border: 2px solid #c4103d;
    box-shadow: 10px 10px 103px 17px rgba(196,16,61,0.72);
    -webkit-box-shadow: 10px 10px 103px 17px rgba(196,16,61,0.72);
    -moz-box-shadow: 10px 10px 103px 17px rgba(196,16,61,0.72);
}
.container .content{
    position: absolute;
    top: 0;
    left: 0;
    width: 58%;
    height: 100%;
    background: transparent;
    padding: 80px;
    color: #e4e4e4;
    display: flex;
    justify-content: space-between;
    flex-direction: column;
}
.content .logo{
    font-size: 30px;
}
.texto h2{
    font-size: 40px;
    line-height: 1;
}
.texto h2 span{
    font-size: 25px;
}
.texto p{
    font-size: 16px;
    margin: 20px 0;
}
.iconos a i{
    font-size: 22px;
    color: #e4e4e4;
    margin-right: 10px;
    transition: .5s ease;
}
.iconos a:hover i{
    transform: scale(1.2);
}
.container .logreg-box{
    position: absolute;
    /* width: calc(100% - 58%); */
    width: 100%;
    right: 0;
    top: 0;
    height: 100%;
    overflow: hidden;
}
.logreg-box .form-box{
    position: absolute;
    display: flex;
    justify-content: center;
    align-items: center;
    width: 100%;
    height: 100%;
    background: transparent;
    backdrop-filter: blur(20px);
    border-top-right-radius: 10px;
    border-bottom-right-radius: 10px;
    color: #e4e4e4;
}
.logreg-box .form-box.login{
    width: 450px;
    transform: translateX(590px);
    transition: transform .6s ease;
    transition-delay: .7s;
}
.logreg-box.active .form-box.login{
    transform: translateX(1030px);
    transition-delay: 0s;
}

.logreg-box .form-box.register{
    transform: translateX(1030px);
    transition: transform .6s ease;
    transition-delay: 0s;
}
.logreg-box.active .form-box.register{
    transform: translateX(0);
    transition-delay: .7s;
}
.form-box{
    border: 2px solid yellow;
}
.form-box h2{
    font-size: 32px;
    text-align: center;
}

.form-box .input-box{
    position: relative;
    width: 340px;
    height: 50px;
    border-bottom: 2px solid #e4e4e4;
    margin: 30px 0;
    left: 10px;
}

.input-box input{
    width: 90%;
    height: 100%;
    background: transparent;
    border: none;
    outline: none;
    font-size: 16px;
    color: #e4e4e4;
    font-weight: 500;
    padding-right: 28px;
}
.input-box label{
    position: absolute;
    top: 50%;
    left: 0;
    transform: translateY(-50%);
    font-size: 16px;
    font-weight: 500;
    pointer-events: none;
    transition: .5s ease;
}
.input-box input:focus~label,
.input-box input:valid~label{
    top: -5px;
}
.input-box .icono{
    position: absolute;
    top: 13px;
    right: 0;
    font-size: 19px;
}
.form-box .olvidar{
    font-size: 14.5px;
    font-weight: 500;
    margin: -15px o 15px;
    display: flex;
    justify-content: space-between;
}

.olvidar label input{
    accent-color: #e4e4e4;
    margin-right: 3px;
}
.olvidar a{
    color: #e4e4e4;
    text-decoration: none;
}
.olvidar a:hover{
    text-decoration: underline;
}
.boton{
    width: 100%;
    height: 45px;
    background: #c4103d;
    border: none;
    outline: none;
    border-radius: 4px;
    cursor: pointer;
    font-size: 16px;
    color: #e4e4e4;
    font-weight: 500;
    box-shadow: 0 0 10px rgba(0, 0, 0, 0.5);
}
.form-box .login-register{
    font-size: 14.5px;
    font-weight: 500;
    text-align: center;
    margin-top: 25px;
}
.login-register p a{
    color: #e4e4e4;
    font-weight: 600;
    text-decoration: none;
}
.login-register p a:hover{
    text-decoration: underline;
}
.nombre{
        position: relative;
        /* top: 50px */
        transform: translate(-270px, 120px);
        /* transform: translateY(70px); */
        width: 120px;
        /* left: 0px; */
        border: 2px solid yellow;
}
.apellido{
        position: relative;
        /* top: 50px */
        /* transform: translatex(250px);
        transform: translateY(60%); */
        transform: translate(-270px, 120px);


        left: 250px;
        border: 2px solid yellow;
}
.correo{
        position: relative;
        /* top: 50px */
        /* transform: translatex(-90%);
        transform: translateY(60%); */
        transform: translate(-270px, 120px);


        left: 250px;
        border: 2px solid yellow;
}
.contraseña{
        position: relative;
        /* top: 50px */
        /* transform: translatex(-90%); */
        transform: translate(-270px, 120px);

        left: 250px;
        border: 2px solid yellow;
}
.direccion{
        position: relative;
        /* top: 50px */
        /* transform: translatex(90%);
        transform: translateY(-200%); */
        transform: translate(270px, -200px);

        left: 250px;
        border: 2px solid blue;
}
.genero{
        position: relative;
        /* top: 50px */
        /* transform: translatex(90%);
        transform: translateY(-200%); */
        transform: translate(270px, -200px);

        left: 250px;
        border: 2px solid blue;
}
.fecha{
    position: relative;
        /* top: 50px */
        /* transform: translatex(90%);
        transform: translateY(-200%); */
        transform: translate(270px, -200px);

        left: 250px;
        border: 2px solid blue;
}


</style>