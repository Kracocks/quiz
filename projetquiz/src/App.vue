<script>
import TodoItem from './components/TodoItem.vue';

let data = {
  todos: [
    { id:0, text: 'Faire les courses', checked: true },
    { id:1, text: 'Apprendre REST', checked: false }
  ],
  title: 'Mes tâches',
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
        this.todos.push({
          id: this.todos.length,
          text: text,
          checked: false
        });
        this.newItem = '';
      }
    },
    removeItem: function ($event) {

      for (let i = 0; i < this.todos.length; i++) {
        if ($event.id == this.todos[i].id) {
          this.todos.splice(i, 1);
          break;
        }
      }
    },
    updateItem: function($event){
      for (let i = 0; i < this.todos.length; i++) {
        if ($event.id == this.todos[i].id) {
          this.todos[i].text = $event.text;
          break;}
    }}
  },
  mounted() {
    fetch('http://127.0.0.1:5000/todo/api/v1.0/tasks')
      .then(response => response.json())
      .then(data => {
        this.todos = data.tasks;
      });
  },
  components: {
    TodoItem
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
      <TodoItem
      v-for="todo in todos"
      :todo="todo"
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
