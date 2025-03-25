<script>
import QuestionnaireItem from './components/QuestionnaireItem.vue';

let data = {
  questionnaires: [],
  title: 'Mes questionnaires',
  newItem: ''
};

export default {
  data() {
    return data;
  },
  methods: {
    addItem: function () {
      let text = this.newItem.trim();
      if (text) {
        this.questionnaires.push({
          id: this.questionnaires.length,
          text: text,
          checked: false
        });
        this.newItem = '';
      }
    },
    removeItem: function ($event) {

      for (let i = 0; i < this.questionnaires.length; i++) {
        if ($event.id == this.questionnaires[i].id) {
          this.questionnaires.splice(i, 1);
          break;
        }
      }
    },
    updateItem: function($event){
      for (let i = 0; i < this.questionnaires.length; i++) {
        if ($event.id == this.questionnaires[i].id) {
          this.questionnaires[i].text = $event.text;
          break;}
    }}
  },
  mounted() {
    fetch('http://127.0.0.1:5000/quiz/api/v1.0/questionnaires')
      .then(response => response.json())
      .then(data => {
        this.questionnaires = data;
      });
  },
  components: {
    QuestionnaireItem
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
  <div class="container">
    <h2>{{ title }}</h2>
    <ol>
      <QuestionnaireItem
      v-for="questionnaire in questionnaires"
      :questionnaire="questionnaire"
      @remove="removeItem"
      @update="updateItem"
      />
    </ol>
    <div class="input-group">
      <input
        v-model="newItem"
        @keyup.enter="addItem"
        placeholder="Ajouter une tache à la liste"
        type="text"
        class="form-control"
      >
      <span class="input-group-btn">
        <button
          @click="addItem"
          class="btn btn-default"
          type="button"
        >
          Ajouter
        </button>
      </span>
    </div>
  </div>
</template>
