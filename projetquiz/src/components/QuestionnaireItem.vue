<script>
export default {
  props: {
    questionnaire: Object
  },
  data() {
    return {
      isEditing: false
    };
  },
  methods: {
    suppr: function () {
      this.$emit('remove', { id: this.questionnaire.id });
    },
    valid: function () {
      this.$emit('update', { id: this.questionnaire.id, name: this.questionnaire.name });
      this.isEditing = false;
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
    <div class="questionnaire">
      <label v-if="!isEditing">
        {{ questionnaire.name }}
      </label>
      <input v-if="isEditing" v-model="questionnaire.name" class="form-control">
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