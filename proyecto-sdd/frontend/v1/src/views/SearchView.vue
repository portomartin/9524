<script setup>
import { ref, computed } from 'vue'
import { useRouter } from 'vue-router'
import {
  Search,
  FilterX,
  ArrowRight,
  Sparkles,
  Inbox
} from '@lucide/vue'
import { usePlatformStore } from '../stores/platformStore'
import Button from '../components/ui/Button.vue'
import Badge from '../components/ui/Badge.vue'
import Card from '../components/ui/Card.vue'
import Input from '../components/ui/Input.vue'

const router = useRouter()
const platformStore = usePlatformStore()

const query = ref('')
const selectedType = ref('ALL') // 'ALL' | 'OFFERS' | 'NEEDS'
const selectedCategory = ref('ALL')
const selectedLevel = ref('ALL')
const selectedModality = ref('ALL')

const categories = ['ALL', 'Programación', 'Idiomas', 'Diseño', 'DevOps', 'Música', 'Negocios']
const levels = ['ALL', 'PRINCIPIANTE', 'INTERMEDIO', 'AVANZADO', 'TODOS']
const modalities = ['ALL', 'VIRTUAL', 'PRESENCIAL', 'HIBRIDA']

function clearFilters() {
  query.value = ''
  selectedType.value = 'ALL'
  selectedCategory.value = 'ALL'
  selectedLevel.value = 'ALL'
  selectedModality.value = 'ALL'
}

const filteredResults = computed(() => {
  const q = query.value.trim().toLowerCase()
  const results = []

  // Ofertas
  if (selectedType.value === 'ALL' || selectedType.value === 'OFFERS') {
    platformStore.offers.forEach(offer => {
      if (selectedCategory.value !== 'ALL' && offer.category !== selectedCategory.value) return
      if (selectedLevel.value !== 'ALL' && offer.level !== selectedLevel.value && offer.level !== 'TODOS') return
      if (selectedModality.value !== 'ALL' && offer.modality !== selectedModality.value) return

      if (q) {
        const matchesTitle = offer.title.toLowerCase().includes(q)
        const matchesDesc = offer.description.toLowerCase().includes(q)
        const matchesCat = offer.category.toLowerCase().includes(q)
        const matchesAuthor = offer.userName.toLowerCase().includes(q)
        if (!matchesTitle && !matchesDesc && !matchesCat && !matchesAuthor) return
      }

      results.push({
        ...offer,
        resultType: 'OFFER'
      })
    })
  }

  // Necesidades
  if (selectedType.value === 'ALL' || selectedType.value === 'NEEDS') {
    platformStore.needs.forEach(need => {
      if (selectedCategory.value !== 'ALL' && need.category !== selectedCategory.value) return
      if (selectedLevel.value !== 'ALL' && need.level !== selectedLevel.value) return
      if (selectedModality.value !== 'ALL' && need.modality !== selectedModality.value) return

      if (q) {
        const matchesTitle = need.title.toLowerCase().includes(q)
        const matchesGoal = need.goal.toLowerCase().includes(q)
        const matchesCat = need.category.toLowerCase().includes(q)
        const matchesAuthor = need.userName.toLowerCase().includes(q)
        if (!matchesTitle && !matchesGoal && !matchesCat && !matchesAuthor) return
      }

      results.push({
        ...need,
        resultType: 'NEED'
      })
    })
  }

  return results
})
</script>

<template>
  <div class="max-w-7xl mx-auto flex flex-col gap-8">
    <!-- Header & Search Bar -->
    <div class="rounded-3xl border border-border bg-card p-6 md:p-10 shadow-xs">
      <Badge variant="outline" class="mb-3 text-primary border-primary/20 bg-primary/5">
        <Sparkles class="h-3 w-3 mr-1" />
        Buscador Facetado
      </Badge>
      <h1 class="text-3xl md:text-4xl font-black tracking-tight text-foreground mb-2">
        Buscador y Filtros Combinables
      </h1>
      <p class="text-sm text-muted-foreground max-w-2xl leading-relaxed mb-6">
        Encuentra exactamente los conocimientos que te interesan filtrando por categoría, nivel y modalidad.
      </p>

      <!-- Main Input -->
      <div class="flex gap-2">
        <div class="relative flex-1">
          <Input
            v-model="query"
            placeholder="Buscar por tema, palabra clave o persona (ej. Vue, Inglés, Docker...)"
            class="h-11 px-4 text-base"
          />
        </div>
        <Button
          v-if="query || selectedType !== 'ALL' || selectedCategory !== 'ALL' || selectedLevel !== 'ALL' || selectedModality !== 'ALL'"
          variant="outline"
          class="h-11"
          @click="clearFilters"
        >
          <FilterX class="h-4 w-4 mr-1.5" />
          Limpiar
        </Button>
      </div>

      <!-- Filters row -->
      <div class="grid grid-cols-1 sm:grid-cols-2 md:grid-cols-4 gap-3 mt-4">
        <div>
          <label class="text-[11px] font-bold text-muted-foreground uppercase tracking-wider block mb-1">
            Tipo
          </label>
          <select v-model="selectedType" class="h-9 w-full rounded-lg border border-input bg-card px-2.5 text-xs font-medium text-foreground">
            <option value="ALL">Todo (Ofertas y Necesidades)</option>
            <option value="OFFERS">Propuestas para aprender</option>
            <option value="NEEDS">Aprendizajes buscados</option>
          </select>
        </div>

        <div>
          <label class="text-[11px] font-bold text-muted-foreground uppercase tracking-wider block mb-1">
            Categoría
          </label>
          <select v-model="selectedCategory" class="h-9 w-full rounded-lg border border-input bg-card px-2.5 text-xs font-medium text-foreground">
            <option v-for="cat in categories" :key="cat" :value="cat">
              {{ cat === 'ALL' ? 'Todas las categorías' : cat }}
            </option>
          </select>
        </div>

        <div>
          <label class="text-[11px] font-bold text-muted-foreground uppercase tracking-wider block mb-1">
            Nivel
          </label>
          <select v-model="selectedLevel" class="h-9 w-full rounded-lg border border-input bg-card px-2.5 text-xs font-medium text-foreground">
            <option v-for="lvl in levels" :key="lvl" :value="lvl">
              {{ lvl === 'ALL' ? 'Todos los niveles' : lvl }}
            </option>
          </select>
        </div>

        <div>
          <label class="text-[11px] font-bold text-muted-foreground uppercase tracking-wider block mb-1">
            Modalidad
          </label>
          <select v-model="selectedModality" class="h-9 w-full rounded-lg border border-input bg-card px-2.5 text-xs font-medium text-foreground">
            <option v-for="mod in modalities" :key="mod" :value="mod">
              {{ mod === 'ALL' ? 'Todas las modalidades' : mod }}
            </option>
          </select>
        </div>
      </div>
    </div>

    <!-- Results Count -->
    <div class="flex items-center justify-between text-xs font-semibold text-muted-foreground">
      <span>{{ filteredResults.length }} resultados encontrados</span>
    </div>

    <!-- Results Grid -->
    <div v-if="filteredResults.length > 0" class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-5">
      <Card
        v-for="item in filteredResults"
        :key="item.id"
        class="p-5 flex flex-col justify-between hover:border-primary/40 hover:shadow-md transition-all"
      >
        <div>
          <div class="flex items-center justify-between mb-3">
            <Badge :variant="item.resultType === 'OFFER' ? 'info' : 'warning'">
              {{ item.resultType === 'OFFER' ? 'Propuesta para aprender' : 'Aprendizaje buscado' }}
            </Badge>
            <span class="text-xs text-muted-foreground">{{ item.category }} · {{ item.modality }}</span>
          </div>

          <h3 class="text-base font-bold text-foreground mb-2 leading-snug">{{ item.title }}</h3>
          <p class="text-xs text-muted-foreground line-clamp-3 mb-4 leading-relaxed">
            {{ item.resultType === 'OFFER' ? item.description : item.goal }}
          </p>
        </div>

        <div class="pt-4 border-t border-border flex items-center justify-between">
          <span class="text-xs font-medium text-muted-foreground">Por {{ item.userName }}</span>
          <Button
            size="sm"
            @click="router.push({
              name: item.resultType === 'OFFER' ? 'offer-detail' : 'need-detail',
              params: { id: item.id }
            })"
          >
            Ver
            <ArrowRight class="h-3.5 w-3.5 ml-1" />
          </Button>
        </div>
      </Card>
    </div>

    <!-- Empty State -->
    <div v-else class="rounded-2xl border border-dashed border-border p-12 text-center text-muted-foreground">
      <Inbox class="h-8 w-8 mx-auto mb-3 opacity-40" />
      <h3 class="text-base font-bold text-foreground">No se encontraron resultados</h3>
      <p class="text-xs mt-1 max-w-sm mx-auto">
        Prueba cambiando las palabras clave o restableciendo los filtros de categoría y modalidad.
      </p>
      <Button variant="outline" size="sm" class="mt-4" @click="clearFilters">
        Restablecer filtros
      </Button>
    </div>
  </div>
</template>
