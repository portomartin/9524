<script setup>
import { ref } from 'vue'

const count = ref(0)
</script>

<template>
  <main class="container">
    <h1>Hola, Vue</h1>
    <p>Tu aplicación mínima ya está funcionando.</p>
    <button type="button" @click="count++">
      Clics: {{ count }}
    </button>
  </main>
</template>

<style>
:root {
  font-family: Inter, system-ui, sans-serif;
  color: #213547;
  background: #f6f7fb;
}

body {
  margin: 0;
}

.container {
  display: grid;
  min-height: 100vh;
  place-content: center;
  gap: 0.75rem;
  text-align: center;
}

h1,
p {
  margin: 0;
}

button {
  margin-top: 0.75rem;
  padding: 0.65rem 1rem;
  border: 0;
  border-radius: 0.5rem;
  color: white;
  background: #42b883;
  cursor: pointer;
  font: inherit;
}

button:hover {
  background: #369b6d;
}
</style>
