<script>
import QuestionnaireItem from './components/QuestionnaireItem.vue';
import FormQuestionnaire from './components/formQuestionnaire.vue';
import formEditQuestionnaire from './components/formEditQuestionnaire.vue';

let data = {
  questionnaires: {},
  title: 'Mes questionnaires',
  newItem: '',
  isAffiche: false,
  isEdit: false,
  selectedQuestionnaire: null
};

export default {
  data() {
    return data;
  },
  methods: {
    ajouteQuestionnairer: function (newQuestionnaire) {
      fetch("http://127.0.0.1:5000/quiz/api/v1.0/questionnaires", {
        headers: {
          'Accept': 'application/json',
          'Content-Type': 'application/json'
        },
        method: "POST",
        body: JSON.stringify({ nom: newQuestionnaire.name, questions: newQuestionnaire.questions })
      })
        .then(response => {
          if (!response.ok) {
            throw new Error("Erreur lors de l'ajout du questionnaire");
          }
          console.log('Add Success:', response);
        })
        .then(() => this.refreshItem())
        .catch(error => {
          console.log('Add Error:', error);
        });
    },
    removeQuestionnaire: function ($event) {
      fetch($event.uri, {
        headers: {
          'Accept': 'application/json',
          'Content-Type': 'application/json'
        },
        method: "DELETE"
      })
        .then(response => {
          console.log('Delete Success:' + response);
        })
        .then(() => this.refreshItem())
        .catch(response => {
          console.log(response);
        });
    },
    updateQuestionnaire: function ($event) {
      fetch($event.uri, {
        headers: {
          'Accept': 'application/json',
          'Content-Type': 'application/json'
        },
        method: "PUT",
        body: JSON.stringify({ nom: $event.name})
      })
        .then(response => {
          console.log('Update Success:', response);
        })
        .then(() => this.refreshItem())
        .catch(response => {
          console.log('Update Error:', response);
        });
    },
    refreshItem: function () {
      this.isAffiche = false;
      this.isEdit = false;
      let requete = "http://127.0.0.1:5000/quiz/api/v1.0/questionnaires";
      fetch(requete)
        .then(response => response.json())
        .then(data => this.questionnaires = data)
        .catch(error => console.log("Erreur : ", error));
    },
    addQuestionnaire: function () {
      this.isEdit = false;
      this.isAffiche = true;
    },
    editQuestionnaire: function ($event) {
      this.isAffiche = false;
      this.selectedQuestionnaire = $event;
      this.isEdit = true;
    },
  },
  mounted() {
    this.refreshItem();
  },
  components: {
    QuestionnaireItem,
    FormQuestionnaire,
    formEditQuestionnaire
  }
};
</script>

<template>
  <link
    rel="stylesheet"
    href="https://cdn.jsdelivr.net/npm/bootstrap@5.2.3/dist/css/bootstrap.min.css"
    integrity="sha384-rbsA2VBKQhggwzxH7pPCaAqO46MgnOM80zW1RWuH61DGLwZJEdK2Kadq2F9CUG65"
    crossorigin="anonymous"
  >
  <div class="container-fluid w-100 vh-100 border border-dark">
    <div class="row h-100">
      <div id="gauche" class="col-6 text-white p-5 border-end border-dark" style="background-color: #60a7db;">
        <h2>{{ title }}</h2>
        <ol>
          <QuestionnaireItem
            v-for="questionnaire in questionnaires"
            :questionnaire="questionnaire"
            @remove="removeQuestionnaire"
            @update="updateQuestionnaire"
            @edit="editQuestionnaire"
          />
        </ol>
        <button
          @click="addQuestionnaire"
          class="btn btn-default"
          type="button">
          Ajouter un questionnaire
        </button>
      </div>

      <div id="droite" class="col-6 text-white p-5 border-start border-dark" style="background-color: #9ce477;">
        <FormQuestionnaire
          v-if="isAffiche"
          @add="ajouteQuestionnairer"
        />

        <formEditQuestionnaire
          v-if="isEdit"
          :questionnaire="selectedQuestionnaire"
          @refresh="refreshItem"
          @update="updateQuestionnaire"
        />
      </div>
    </div>
  </div>
</template>
