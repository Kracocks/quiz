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
        url = this.question.url;
        fetch(
            url,
            {
                headers: {
                    'Accept': 'application/json',
                    'Content-Type': 'application/json'
                },
                method: "DELETE"
            })
        .then(res => { console.log('Delete Success:' + res); } )
        .then(() => refreshQuestionnaireList())
        .catch( res => { console.log(res);  });
        this.$emit('remove', { id: this.todo.id });
    },
    valid: function () {
        fetch(
            uri, 
            {
                headers: {
                    'Accept': 'application/json',
                    'Content-Type': 'application/json'
                },
                method: "PUT",
                body: JSON.stringify({
                    "titre": titre,
                    "reponse": reponse
                })
            })
        .then(res => { console.log('Save Success') ;
            $("#result").text(res['contenu']) ;
            refreshQuestionList(event.data.id_qaire)
        })
        .catch( res => { console.log(res) });
        this.$emit('update', { id: this.todo.id, text: this.todo.text });
        this.isEditing = false;
    },
    modifType: function(new_type) {
        fetch(
            uri, 
            {
                headers: {
                    'Accept': 'application/json',
                    'Content-Type': 'application/json'
                },
                method: "PUT",
                body: JSON.stringify({
                    "type": new_type
                })
        })
        .then(res => { console.log('Save Success') ;
            $("#result").text(res['contenu']);
            refreshQuestionList(event.data.id_qaire)
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
  <li v-bind:class="{ 'alert alert-success': todo.checked }">
    <div class="checkbox">
      <label v-if="!isEditing">
        <input type="checkbox" v-model="todo.checked">
        {{ todo.text }}
      </label>
      <input v-if="isEditing" v-model="todo.text" class="form-control">
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
      class="btn btn-"
      value="Valider"
      @click="valid"
    >
  </li>
</template>