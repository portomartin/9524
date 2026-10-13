<script setup>
import { ref, computed } from 'vue'
import { useRouter } from 'vue-router'
import {
  Compass,
  BookOpen,
  Search,
  Filter,
  ArrowRight,
  Clock,
  Inbox,
  AlertTriangle,
  RotateCw
} from 'lucide-vue-next'
import { usePlatformStore } from '../stores/platformStore'
import Button from '../components/ui/Button.vue'
import Badge from '../components/ui/Badge.vue'
import Card from '../components/ui/Card.vue'

const router = useRouter()
const platformStore = usePlatformStore()

const activeTab = ref('offers') // 'offers' | 'needs'
const isLoading = ref(false)
const errorMessage = ref(null)

const offersList = computed(() => platformStore.offers)
const needsList = computed(() => platformStore.needs)

function handleRetry() {
  isLoading.value = true
  errorMessage.value = null
  setTimeout(() => {
    platformStore.refreshAll()
    isLoading.value = false
  }, 350)
}
</script>

<template>
  <div class="max-w-7xl mx-auto flex flex-col gap-8">
    <!-- Header -->
    <div class="rounded-3xl border border-border bg-card p-6 md:p-10 shadow-xs">
      <Badge variant="outline" class="mb-3 text-primary border-primary/20 bg-primary/5">
        <Compass class="h-3 w-3 mr-1" />
        Exploración Pública Libre
      </Badge>
      <h1 class="text-3xl md:text-4xl font-black tracking-tight text-foreground mb-2">
        Explorar Oportunidades de Aprendizaje
      </h1>
      <p class="text-sm text-muted-foreground max-w-2xl leading-relaxed">
        Descubre lo que los miembros de la comunidad ofrecen para enseñar o encuentra personas que buscan lo que tú sabes compartir.
        No necesitas registrarte para mirar.
      </p>
    </div>

    <!-- Navigation & Switcher -->
    <div class="flex flex-wrap items-center justify-between gap-4">
      <div class="flex items-center gap-1 rounded-xl bg-muted p-1 border border-border">
        <button
          class="flex items-center gap-2 rounded-lg px-4 py-2 text-xs font-semibold transition-all cursor-pointer border-none"
          :class="activeTab === 'offers' ? 'bg-card text-foreground shadow-xs' : 'text-muted-foreground hover:text-foreground bg-transparent'"
          @click="activeTab = 'offers'"
        >
          <BookOpen class="h-3.5 w-3.5" />
          <span>Propuestas para Aprender</span>
          <span class="rounded-full bg-muted-foreground/15 px-2 py-0.5 text-[10px]">{{ offersList.length }}</span>
        </button>

        <button
          class="flex items-center gap-2 rounded-lg px-4 py-2 text-xs font-semibold transition-all cursor-pointer border-none"
          :class="activeTab === 'needs' ? 'bg-card text-foreground shadow-xs' : 'text-muted-foreground hover:text-foreground bg-transparent'"
          @click="activeTab = 'needs'"
        >
          <Search class="h-3.5 w-3.5" />
          <span>Aprendizajes Buscados</span>
          <span class="rounded-full bg-muted-foreground/15 px-2 py-0.5 text-[10px]">{{ needsList.length }}</span>
        </button>
      </div>

      <Button variant="outline" size="sm" @click="router.push({ name: 'search' })">
        <Filter class="h-3.5 w-3.5 mr-1" />
        Buscador Avanzado
      </Button>
    </div>

    <!-- Error State -->
    <div v-if="errorMessage" class="rounded-xl border border-destructive/20 bg-destructive/5 p-4 flex items-center justify-between text-sm">
      <div class="flex items-center gap-2 text-destructive">
        <AlertTriangle class="h-4 w-4" />
        <span>{{ errorMessage }}</span>
      </div>
      <Button variant="outline" size="sm" @click="handleRetry">
        <RotateCw class="h-3.5 w-3.5 mr-1" />
        Reintentar
      </Button>
    </div>

    <!-- Loading Skeleton -->
    <div v-else-if="isLoading" class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-5">
      <div v-for="i in 6" :key="i" class="h-64 rounded-xl border border-border bg-muted/40 animate-pulse"></div>
    </div>

    <!-- Offers List -->
    <div v-else-if="activeTab === 'offers'">
      <div v-if="offersList.length > 0" class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-5">
        <Card
          v-for="offer in offersList"
          :key="offer.id"
          class="p-5 flex flex-col justify-between hover:border-primary/40 hover:shadow-md transition-all"
        >
          <div>
            <div class="flex items-center justify-between mb-3">
              <Badge variant="info">{{ offer.category }}</Badge>
              <span class="text-xs text-muted-foreground">{{ offer.durationMinutes }} min · {{ offer.modality }}</span>
            </div>
            <h3 class="text-base font-bold text-foreground mb-2 leading-snug">{{ offer.title }}</h3>
            <p class="text-xs text-muted-foreground line-clamp-3 mb-4 leading-relaxed">{{ offer.description }}</p>
            <div class="flex items-center gap-2 mb-4">
              <span class="text-[11px] font-semibold text-muted-foreground bg-muted px-2 py-0.5 rounded-md">
                Nivel: {{ offer.level }}
              </span>
            </div>
          </div>

          <div class="pt-4 border-t border-border flex items-center justify-between">
            <div>
              <span class="text-[10px] text-muted-foreground block uppercase font-bold tracking-wider">Enseña</span>
              <span class="text-xs font-bold text-foreground">{{ offer.userName }}</span>
            </div>
            <Button
              size="sm"
              @click="router.push({ name: 'offer-detail', params: { id: offer.id } })"
            >
              Ver Detalle
              <ArrowRight class="h-3.5 w-3.5 ml-1" />
            </Button>
          </div>
        </Card>
      </div>

      <!-- Empty State -->
      <div v-else class="rounded-2xl border border-dashed border-border p-12 text-center text-muted-foreground">
        <Inbox class="h-8 w-8 mx-auto mb-3 opacity-40" />
        <h3 class="text-base font-bold text-foreground">No hay propuestas públicas disponibles</h3>
        <p class="text-xs mt-1">Pronto se sumarán nuevos temas. Vuelve a consultar más tarde.</p>
      </div>
    </div>

    <!-- Needs List -->
    <div v-else-if="activeTab === 'needs'">
      <div v-if="needsList.length > 0" class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-5">
        <Card
          v-for="need in needsList"
          :key="need.id"
          class="p-5 flex flex-col justify-between hover:border-amber-400/40 hover:shadow-md transition-all"
        >
          <div>
            <div class="flex items-center justify-between mb-3">
              <Badge variant="warning">{{ need.category }}</Badge>
              <span class="text-xs text-muted-foreground">{{ need.modality }}</span>
            </div>
            <h3 class="text-base font-bold text-foreground mb-2 leading-snug">{{ need.title }}</h3>
            <div class="rounded-lg bg-muted/60 p-3 text-xs text-foreground mb-4">
              <span class="text-[10px] font-bold text-muted-foreground block uppercase tracking-wider mb-1">
                Objetivo de aprendizaje:
              </span>
              {{ need.goal }}
            </div>
            <span class="text-[11px] font-semibold text-muted-foreground bg-muted px-2 py-0.5 rounded-md">
              Nivel deseado: {{ need.level }}
            </span>
          </div>

          <div class="pt-4 border-t border-border flex items-center justify-between mt-4">
            <div>
              <span class="text-[10px] text-muted-foreground block uppercase font-bold tracking-wider">Busca aprender</span>
              <span class="text-xs font-bold text-foreground">{{ need.userName }}</span>
            </div>
            <Button
              variant="outline"
              size="sm"
              @click="router.push({ name: 'need-detail', params: { id: need.id } })"
            >
              Ver Detalle
              <ArrowRight class="h-3.5 w-3.5 ml-1" />
            </Button>
          </div>
        </Card>
      </div>

      <!-- Empty State -->
      <div v-else class="rounded-2xl border border-dashed border-border p-12 text-center text-muted-foreground">
        <Inbox class="h-8 w-8 mx-auto mb-3 opacity-40" />
        <h3 class="text-base font-bold text-foreground">No hay pedidos de aprendizaje activos</h3>
        <p class="text-xs mt-1">Los miembros no han publicado pedidos en este momento.</p>
      </div>
    </div>
  </div>
</template>
