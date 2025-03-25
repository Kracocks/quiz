<script>
export default {
  props: {
    todo: Object
  },
  data() {
    return {
      isEditing: false
    };
  },
  methods: {
    suppr: function () {
      this.$emit('remove', { id: this.todo.id });
    },
    valid: function () {
      this.$emit('update', { id: this.todo.id, text: this.todo.text });
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