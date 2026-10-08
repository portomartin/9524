<script setup>
import { onMounted, ref } from 'vue'
import { useRouter } from 'vue-router'
import { RefreshCw, Search, Sparkles, Star } from '@lucide/vue'
import PublicContentCard from '../components/PublicContentCard.vue'
import UiBadge from '../components/ui/Badge.vue'
import UiButton from '../components/ui/Button.vue'
import UiCard from '../components/ui/Card.vue'
import { usePublicCatalog } from '../composables/usePublicCatalog'

const { offers, learningNeeds, isLoading, error, loadCatalog } = usePublicCatalog()
const router = useRouter()
const activeTab = ref('offers')
onMounted(loadCatalog)
</script>

<template>
  <section class="space-y-8">
    <div class="relative isolate overflow-hidden rounded-3xl border bg-card px-6 py-16 text-center shadow-sm sm:px-12 lg:py-24">
      <div class="pointer-events-none absolute inset-x-0 top-0 -z-10 h-64 bg-gradient-to-b from-primary/15 to-transparent" />
      <div class="pointer-events-none absolute -left-20 top-20 -z-10 size-72 rounded-full bg-primary/10 blur-3xl" />
      <div class="pointer-events-none absolute -right-20 bottom-0 -z-10 size-72 rounded-full bg-violet-300/20 blur-3xl" />
      <UiBadge variant="secondary" class="gap-1.5 px-3 py-1"><Sparkles :size="14" />Aprender también puede ser un intercambio</UiBadge>
      <h1 class="mx-auto mt-6 max-w-4xl text-4xl font-black tracking-tight sm:text-6xl lg:text-7xl">Descubrí lo que otras personas saben</h1>
      <p class="mx-auto mt-6 max-w-3xl text-lg leading-8 text-muted-foreground sm:text-xl">Explorá propuestas para aprender o encontrá personas que buscan un conocimiento que vos podés compartir. No necesitás registrarte para mirar.</p>
      <div class="mt-8 flex flex-col justify-center gap-3 sm:flex-row">
        <UiButton size="lg" @click="router.push({ name: 'search' })"><Search :size="19" />Buscar un aprendizaje</UiButton>
        <UiButton variant="outline" size="lg" @click="router.push({ name: 'trust' })"><Star :size="19" />Ver cómo funciona</UiButton>
      </div>
    </div>

    <div v-if="error" class="flex flex-col items-start justify-between gap-3 rounded-xl border border-destructive/30 bg-destructive/5 p-4 text-sm sm:flex-row sm:items-center">
      <span>{{ error.message }}</span><UiButton size="sm" variant="outline" @click="loadCatalog"><RefreshCw :size="15" />Reintentar</UiButton>
    </div>

    <div v-else-if="isLoading" class="grid gap-5 md:grid-cols-2 lg:grid-cols-3" aria-live="polite" aria-label="Cargando contenido público">
      <div v-for="position in 6" :key="position" class="h-80 animate-pulse rounded-xl border bg-muted" />
    </div>

    <UiCard v-else class="overflow-hidden">
      <div class="flex gap-1 border-b bg-muted/40 p-2" role="tablist" aria-label="Contenido público">
        <UiButton :variant="activeTab === 'offers' ? 'default' : 'ghost'" role="tab" :aria-selected="activeTab === 'offers'" @click="activeTab = 'offers'">Propuestas para aprender <span class="rounded-full bg-background/20 px-2 py-0.5 text-xs">{{ offers.length }}</span></UiButton>
        <UiButton :variant="activeTab === 'learning-needs' ? 'default' : 'ghost'" role="tab" :aria-selected="activeTab === 'learning-needs'" @click="activeTab = 'learning-needs'">Aprendizajes buscados <span class="rounded-full bg-background/20 px-2 py-0.5 text-xs">{{ learningNeeds.length }}</span></UiButton>
      </div>

      <div class="p-4 sm:p-6">
        <template v-if="activeTab === 'offers'">
          <div v-if="offers.length" class="grid gap-5 md:grid-cols-2 lg:grid-cols-3"><PublicContentCard v-for="offer in offers" :key="offer.id" :item="offer" type="offer" /></div>
          <div v-else class="rounded-xl border border-dashed p-10 text-center text-muted-foreground">Todavía no hay propuestas públicas. Volvé pronto para descubrir nuevas oportunidades.</div>
        </template>
        <template v-else>
          <div v-if="learningNeeds.length" class="grid gap-5 md:grid-cols-2 lg:grid-cols-3"><PublicContentCard v-for="item in learningNeeds" :key="item.id" :item="item" type="learning-need" /></div>
          <div v-else class="rounded-xl border border-dashed p-10 text-center text-muted-foreground">Todavía no hay aprendizajes buscados públicos.</div>
        </template>
      </div>
    </UiCard>
  </section>
</template>
