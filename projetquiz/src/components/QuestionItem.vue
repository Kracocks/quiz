<script>
export default {
  props: {
    question: Object
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
			this.$emit('remove', { return: res });
		} )
        .catch( res => { console.log(res);  });
    },
    valid: function () {
        fetch(
            this.question.uri, 
            {
                headers: {
                    'Accept': 'application/json',
                    'Content-Type': 'application/json'
                },
                method: "PUT",
                body: JSON.stringify({
                    "titre": this.question.titre,
					"proposition1": this.question.proposition1,
					"proposition2": this.question.proposition2,
                    "reponse": this.question.reponse
                })
            })
        .then(() => { console.log('Save Success') ;
            this.$emit('update', { return: res });
            this.isEditing = false;
        })
        .catch( res => { console.log(res) });
    },
    modif: function () {
        this.isEditing = true;
    }
  },
  emits: ['remove', 'update']
};
</script>

<template>
  <li>
    <div class="formModifierQuestion" v-if="isEditing">
		<label>
			<input type="text" v-model="question.titre">

		</label>
		<input type="radio" id="reponse1" name="reponse" :checked="question.reponse === question.proposition1" />
		<label for="reponse1">
			<input type="text" v-model="question.proposition1">
		</label>

		<input type="radio" id="reponse2" name="reponse" :checked="question.reponse === question.proposition2" />
		<label for="reponse2">
			<input type="text" v-model="question.proposition2">
		</label>
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