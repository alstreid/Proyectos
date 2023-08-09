<template>
    <div>
        <p>{{ mensaje }}</p>
        <div class="container">
            <button type="button" class="btn btn-primary">{{ mensaje }}</button>
         </div>
    </div>
</template>

<script>
import axios from 'axios';
export default {
name: 'Api',
data(){
    return {
        mensaje: '',
    }
},
methods: {
    getMensaje(){
        const path = 'http://127.0.0.1:5000/api'
        axios.get(path) 
            .then((res) => {
                this.mensaje = res.data 
            }) 
            .catch((error) => {
                console.error(error)
            })
    },
},
    created (){
        this.getMensaje()
    }
}

</script>