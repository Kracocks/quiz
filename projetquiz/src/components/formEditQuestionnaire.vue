<script>
import QuestionItem from './QuestionItem.vue';

export default {
  props: {
    questionnaire: {
      type: Object,
      default: () => ({
        name: '',
        questions: []
      })
    }
  },
  data() {
    return {
      isEditQuestion: false,
      newQuestions: '',
      isAddingQuestion: false,
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
          body: JSON.stringify({ "name": this.questionnaire.name, "questions": this.questionnaire.question })
        }
      )
        .then(res => {
          console.log('Save Success');
          this.$emit('refresh');
        })
        .catch(res => { console.log(res) });
    },
    saveChanges() {
      this.$emit('update', { id: this.questionnaire.id, name: this.questionnaire.name, uri: this.questionnaire.uri, questions: this.questionnaire.question });
    },
    addQuestions: function () {
      let nameQ = this.newQuestions.trim();
      if (nameQ) {
        this.questionnaire.questions.push({
          title: this.nameQ,
          type: "simple_question"
        });
        this.newQuestions = '';
        this.isAddingQuestion = false;
        this.refreshQuestion();
      }
    },
    ajouteQuestion: function () {
      this.isAddingQuestion = true;
    },
    refreshQuestion: function () {
      let requete = "http://127.0.0.1:5000/quiz/api/v1.0/questionnaires/" + this.questionnaire.id + "/questions";
      fetch(requete)
        .then(response => response.json())
        .then(data => this.questionnaires = data)
        .catch(error => console.log("Erreur : ", error));
    }
  },
  emits: ['refresh', 'update'],
  components: {
    QuestionItem
  }
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
    <div id="questions">
      <h2>Les questions</h2>
      <ol>
        <QuestionItem
          v-for="question in questionnaire.questions"
          :question="question"
        />
      </ol>
      <div
        v-if="isAddingQuestion"
        id="ajoute-question"
      >
        <input
          v-model="newQuestions"
          @keyup.enter="addQuestions"
          placeholder="Ajouter une question"
          class="btn btn-alert"
          type="text"
        >
      </div>
      <button
        @click="ajouteQuestion"
      >
        Ajouter une question
      </button>
    </div>

    <div class="pt-1 row">
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
