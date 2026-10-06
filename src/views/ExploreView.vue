<script setup>
import { onMounted } from 'vue'
import { useRouter } from 'vue-router'
import Tabs from 'primevue/tabs'
import TabList from 'primevue/tablist'
import Tab from 'primevue/tab'
import TabPanels from 'primevue/tabpanels'
import TabPanel from 'primevue/tabpanel'
import Message from 'primevue/message'
import Button from 'primevue/button'
import Skeleton from 'primevue/skeleton'
import Tag from 'primevue/tag'
import PublicContentCard from '../components/PublicContentCard.vue'
import { usePublicCatalog } from '../composables/usePublicCatalog'

const { offers, learningNeeds, isLoading, error, loadCatalog } = usePublicCatalog()
const router = useRouter()
onMounted(loadCatalog)
</script>

<template>
  <section class="flex flex-column gap-4">
    <div class="surface-card border-1 surface-border border-round-3xl shadow-2 text-center px-3 py-6 md:px-6 md:py-8 overflow-hidden">
      <Tag value="Aprender también puede ser un intercambio" icon="pi pi-sparkles" severity="info" />
      <h1 class="text-4xl md:text-6xl line-height-1 mt-4 mb-3">Descubrí lo que otras personas saben</h1>
      <p class="text-lg md:text-xl text-color-secondary line-height-3 mb-4 mx-auto">
        Explorá propuestas para aprender o encontrá personas que buscan un conocimiento que vos podés compartir. No necesitás registrarte para mirar.
      </p>
      <div class="flex flex-column sm:flex-row justify-content-center gap-2">
        <Button label="Buscar un aprendizaje" icon="pi pi-search" size="large" @click="router.push({ name: 'search' })" />
        <Button label="Ver cómo funciona" icon="pi pi-star" severity="secondary" outlined size="large" @click="router.push({ name: 'trust' })" />
      </div>
    </div>

    <Message v-if="error" severity="error" :closable="false">
      <div class="flex flex-column md:flex-row md:align-items-center gap-3">
        <span>{{ error.message }}</span>
        <Button label="Reintentar" icon="pi pi-refresh" size="small" @click="loadCatalog" />
      </div>
    </Message>

    <div v-else-if="isLoading" aria-live="polite" aria-label="Cargando contenido público">
      <div class="grid">
        <div v-for="position in 6" :key="position" class="col-12 md:col-6 lg:col-4">
          <Skeleton height="18rem" border-radius="12px" />
        </div>
      </div>
    </div>

    <Tabs v-else value="offers" class="surface-card border-1 surface-border border-round-xl shadow-1 overflow-hidden">
      <TabList>
        <Tab value="offers">Propuestas para aprender ({{ offers.length }})</Tab>
        <Tab value="learning-needs">Aprendizajes buscados ({{ learningNeeds.length }})</Tab>
      </TabList>
      <TabPanels>
        <TabPanel value="offers">
          <Message v-if="offers.length === 0" severity="secondary" :closable="false">
            Todavía no hay propuestas públicas. Volvé pronto para descubrir nuevas oportunidades.
          </Message>
          <div v-else class="grid">
            <div v-for="offer in offers" :key="offer.id" class="col-12 md:col-6 lg:col-4">
              <PublicContentCard :item="offer" type="offer" />
            </div>
          </div>
        </TabPanel>
        <TabPanel value="learning-needs">
          <Message v-if="learningNeeds.length === 0" severity="secondary" :closable="false">
            Todavía no hay aprendizajes buscados públicos.
          </Message>
          <div v-else class="grid">
            <div v-for="learningNeed in learningNeeds" :key="learningNeed.id" class="col-12 md:col-6 lg:col-4">
              <PublicContentCard :item="learningNeed" type="learning-need" />
            </div>
          </div>
        </TabPanel>
      </TabPanels>
    </Tabs>
  </section>
</template>
