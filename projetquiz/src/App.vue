<script>
import QuestionnaireItem from './components/QuestionnaireItem.vue';
import FormQuestionnaire from './components/formQuestionnaire.vue';

let data = {
  questionnaires: {},
  title: 'Mes questionnaires',
  newItem: '',
};

export default {
  data() {
    return data;
  },
  methods: {
    addItem: function () {
      this.refreshItem();
    },
    removeQuestionnaire: function ($event) {
      fetch(
        $event.uri,
        {
          headers: {
            'Accept': 'application/json',
            'Content-Type': 'application/json'
          },
          method: "DELETE"
        })
      .then(response => { console.log('Delete Success:' + response); } )
      .then(() => this.refreshItem())
      .catch( response => { console.log(response);  });
    },
    updateQuestionnaire: function($event){
      fetch(
        $event.uri,
        {
          headers: {
            'Accept': 'application/json',
            'Content-Type': 'application/json'
          },
          method: "PUT",
          body: JSON.stringify({nom: $event.name})
        })
      .then(response => { console.log('Update Success:' + response); } )
      .then(() => this.refreshItem())
      .catch( response => { console.log(response);  });
    },
    refreshItem: function() {
      let requete = "http://127.0.0.1:5000/quiz/api/v1.0/questionnaires";
      fetch(requete)
      .then(response => response.json())
      .then( data => this.questionnaires = data)
      .catch(error => console.log("Erreur : ", error));
    }
  },
  mounted() {
    this.refreshItem();
  },
  components: {
    QuestionnaireItem,
    FormQuestionnaire
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
      @remove="removeQuestionnaire"
      @update="updateQuestionnaire"/>
    </ol>
    <FormQuestionnaire
    @refresh="refreshItem"/>
  </div>
</template>
