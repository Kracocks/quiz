<script>
export default {
  data() {
    return {
        isAddingQuestion: false,
        name: ''
    };
  },
   methods: {
    add: function () {
      this.$emit('add', { name: this.name });
    }
  },
  emits: ['add']
};
</script>

<template>
  <div class="input-group">
    <h2>Le questionnaire</h2>
      <span class="input-group-btn">
        <div class="formQuestionnaire">
          <input
            type="text"
            v-model="this.name"
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