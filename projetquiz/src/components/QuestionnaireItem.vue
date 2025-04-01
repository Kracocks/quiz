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
      this.$emit('remove', { id: this.questionnaire.id, uri: this.questionnaire.uri });
    },
    modif: function () {
      this.$emit('edit', this.questionnaire);
      this.isEditing = true;
    }
  },
  emits: ['remove', 'edit']
};
</script>

<template>
  <li>
    <div class="questionnaire">
      <label>
        {{ questionnaire.name }}
      </label>
      
    </div>

    <input
      type="button"
      class="btn btn-danger"
      value="Supprimer"
      @click="suppr"
    >
    <input
      type="button"
      class="btn btn-"
      value="Modifier"
      @click="modif"
    >
  </li>
</template>