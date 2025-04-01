<script>
export default {
  data() {
    return {
        isAdding: false,
        isAddingQuestion: false,
        questionnaire: {nom: "", questions: []},
    };
  },
  methods: {
    addingQuestionnaire: function () {
        this.isAdding = true;
    },
    add: function () {
        fetch(
            "http://127.0.0.1:5000/quiz/api/v1.0/questionnaires",
            {
                headers: {
                    'Accept': 'application/json',
                    'Content-Type': 'application/json'
                },
                method: "POST",
                body: JSON.stringify({"nom": this.questionnaire.nom})
            }
        )
        .then(res => { 
            console.log('Save Success') ;
            this.isAdding = false;
            this.$emit('refresh');
        })
        .catch( res => { console.log(res) });
    },
  },
  emits: ['refresh']
};
</script>

<template>
  <div class="input-group">
      <span class="input-group-btn">

        <button
          v-if="!isAdding"
          @click="addingQuestionnaire"
          class="btn btn-default"
          type="button">
          Ajouter un questionnaire
        </button>

        <div v-if="isAdding" class="formQuestionnaire">
          <input
            type="text"
            v-model="questionnaire.nom"
            class="form-control"
            placeholder="Nom du nouveau questionnaire">
          <input
            type="button"
            class="btn btn-alert"
            value="Ajouter une question">



          <button
            @click="add"
            class="btn btn-default"
            type="button">
            Ajouter le questionnaire
          </button>
        </div>

      </span>
    </div>
</template>