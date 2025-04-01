<script>
export default {
    props: {
  questionnaire: {
    type: Object,
    default: () => ({ name: '' })
  }
},
  data() {
    return {
        isEditQuestion: false,
    };
  },
  methods: {
    add: function () {
        fetch(
            "http://127.0.0.1:5000/quiz/api/v1.0/questionnaires",
            {
                headers: {
                    'Accept': 'application/json',
                    'Content-Type': 'application/json'
                },
                method: "POST",
                body: JSON.stringify({"name": this.questionnaire.name})
            }
        )
        .then(res => { 
            console.log('Save Success') ;
            this.$emit('refresh');
        })
        .catch( res => { console.log(res) });
    },
        saveChanges() {
      this.$emit('update', { id: this.questionnaire.id, name: this.questionnaire.name, uri: this.questionnaire.uri });
    }
  },
  emits: ['refresh', 'update']
};
</script>

<template>
  <div class="container mt-4">
    <div class="row">
      <div class="col-12">
        <h2 class="text-center mb-4">Modifier le questionnaire</h2>
      </div>
    </div>
    <div class="row">
      <div class="col-12">
        <div class="mb-3">
          <label for="questionnaireName" class="form-label">Nom du questionnaire</label>
          <input
            id="questionnaireName"
            type="text"
            v-model="questionnaire.name"
            class="form-control"
            placeholder="Entrez le nom du questionnaire"
          />
        </div>
      </div>
    </div>
    <div class="row">
      <div class="col-12 text-center">
        <button
          @click="saveChanges"
          class="btn btn-primary"
        >
          Enregistrer
        </button>
      </div>
    </div>
  </div>
</template>