<script>
export default {
  props: {
    question: Object,
  },
  data() {
    return {
      	isEditing: false
    };
  },
  methods: {
    refresh: function () {
        
    },
    suppr: function () {
        fetch(
            this.question.uri,
            {
                headers: {
                    'Accept': 'application/json',
                    'Content-Type': 'application/json'
                },
                method: "DELETE"
            })
        .then(res => { 
			console.log('Delete Success:' + res); 
			this.$emit('refresh', { return: res });
		} )
        .catch( res => { console.log(res);  });
    },
    valid: function () {
      	console.log(this.question)
        fetch(
            this.question.uri, 
            {
                headers: {
                    'Accept': 'application/json',
                    'Content-Type': 'application/json'
                },
                method: "PUT",
                body: JSON.stringify({
                    "titre": this.question.title ? this.question.title : "",
                    "proposition1": this.question.proposition1,
                    "proposition2": this.question.proposition2,
                    "reponse": this.question.reponse
                })
            })
        .then(res => { console.log('Save Success') ;
            this.$emit('refresh', { return: res });
            this.isEditing = false;
        })
        .catch( res => { console.log(res) });
    },
    modif: function () {
        this.isEditing = true;
    }
  },
  emits: ['refresh']
};
</script>

<template>
  <li>
    <div class="formModifierQuestion" v-if="isEditing">
      <label>
        <input type="text" v-model="question.title" placeholder="Nouveau nom de la question">
      </label>

      <input type="radio" id="reponse1" name="reponse" :value="true" v-model="question.reponse" />
      <label for="reponse1">
        <input type="text" v-model="question.proposition1">
      </label>

      <input type="radio" id="reponse2" name="reponse" :value="false" v-model="question.reponse" />
      <label for="reponse2">
        <input type="text" v-model="question.proposition2">
      </label>
    </div>

	<div class="afficheQuestion" v-if="!isEditing">
		<p>{{ question.title }}</p>
		<p>{{ question.proposition1 }}</p>
		<p v-if="question.reponse">Bonne Réponse</p>
		<p>{{ question.proposition2 }}</p>
		<p v-if="!question.reponse">Bonne Réponse</p>
	</div>

    <input
      type="button"
      class="btn btn-danger"
      value="Supprimer"
      @click="suppr"
    >
    <input
      v-if="!isEditing"
      type="button"
      class="btn btn-"
      value="Modifier"
      @click="modif"
    >
    <input
      v-if="isEditing"
      type="button"
      class="btn btn-valid"
      value="Valider"
      @click="valid"
    >
  </li>
</template>