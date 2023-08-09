<template>
    <div>
        <div class="modal fade" :class="{ show: modalCreate, 'd-block': modalCreate }" tabindex="-1" role="dialog">
            <div class="modal-dialog modal-dialog-centered modal-sm " role="document">
                <div class="modal-content">
                    <div class="modal-body">
                        <h3>{{ mensaje }}</h3>
                        <div class="btn-group" role="group">
                            <button type="button" class="btn btn-danger btn-sm" @click="modalCreate =! modalCreate">
                                OK
                            </button>
                        </div>
                    </div>
                </div>
            </div>
        </div>
        <div v-if="modalCreate" class="modal-backdrop fade show"></div>
    </div>
</template>
<script>
export default {
    props:[
    'modalCreate','mensaje'
    ],
    data() {
        
        return {
            // modalCreate: true

        }
    },
    methods: {
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
        }
    }
}
</script>
<style scoped></style>
