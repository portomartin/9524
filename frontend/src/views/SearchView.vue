<script setup>
import { computed, ref } from 'vue'
import InputText from 'primevue/inputtext'
import Select from 'primevue/select'
import Button from 'primevue/button'
import Message from 'primevue/message'
import Paginator from 'primevue/paginator'
import PublicContentCard from '../components/PublicContentCard.vue'
import { usePlatformStore } from '../stores/platformStore'

const { state } = usePlatformStore()
const query = ref('')
const type = ref('all')
const category = ref(null)
const level = ref(null)
const modality = ref(null)
const first = ref(0)
const rows = 6

const allItems = computed(() => [
  ...state.offers.map((item) => ({ ...item, resultType: 'offer' })),
  ...state.learningNeeds.map((item) => ({ ...item, resultType: 'learning-need' })),
])
const options = (field) => [...new Set(allItems.value.map((item) => item[field]))]
const filtered = computed(() => allItems.value.filter((item) => {
  const term = query.value.trim().toLowerCase()
  return (!term || `${item.title} ${item.description} ${item.category}`.toLowerCase().includes(term))
    && (type.value === 'all' || item.resultType === type.value)
    && (!category.value || item.category === category.value)
    && (!level.value || item.level === level.value)
    && (!modality.value || item.modality === modality.value)
}))
const paged = computed(() => filtered.value.slice(first.value, first.value + rows))

function clearFilters() { query.value = ''; type.value = 'all'; category.value = null; level.value = null; modality.value = null; first.value = 0 }
</script>

<template>
  <section class="flex flex-column gap-4">
    <div><h1 class="mb-2">Buscar aprendizajes</h1><p class="text-color-secondary mt-0">Buscá propuestas y personas que quieren aprender algo que quizá vos podés enseñar.</p></div>
    <div class="surface-card border-round p-3 md:p-4 flex flex-column gap-3">
      <span class="p-input-icon-left w-full"><i class="pi pi-search" /><InputText v-model="query" placeholder="Tema, categoría o palabra clave" class="w-full" @input="first = 0" /></span>
      <div class="grid">
        <div class="col-12 md:col-3"><Select v-model="type" :options="[{label:'Todo',value:'all'},{label:'Propuestas',value:'offer'},{label:'Aprendizajes buscados',value:'learning-need'}]" option-label="label" option-value="value" class="w-full" @change="first = 0" /></div>
        <div class="col-12 md:col-3"><Select v-model="category" :options="options('category')" placeholder="Categoría" show-clear class="w-full" @change="first = 0" /></div>
        <div class="col-12 md:col-3"><Select v-model="level" :options="options('level')" placeholder="Nivel" show-clear class="w-full" @change="first = 0" /></div>
        <div class="col-12 md:col-3"><Select v-model="modality" :options="options('modality')" placeholder="Modalidad" show-clear class="w-full" @change="first = 0" /></div>
      </div>
      <Button label="Limpiar filtros" icon="pi pi-filter-slash" text class="align-self-start" @click="clearFilters" />
    </div>
    <Message v-if="filtered.length === 0" severity="secondary" :closable="false">No encontramos resultados con esos criterios. Probá limpiar algún filtro.</Message>
    <div v-else class="grid">
      <div v-for="item in paged" :key="`${item.resultType}-${item.id}`" class="col-12 md:col-6 lg:col-4"><PublicContentCard :item="item" :type="item.resultType" /></div>
    </div>
    <Paginator v-if="filtered.length > rows" v-model:first="first" :rows="rows" :total-records="filtered.length" />
  </section>
</template>
