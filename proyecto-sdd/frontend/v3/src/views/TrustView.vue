<script setup>
import { computed } from 'vue'
import { useRouter } from 'vue-router'
import {
  ShieldCheck,
  Trophy,
  TrendingUp,
  Calendar,
  Star,
  Info
} from 'lucide-vue-next'
import { usePlatformStore } from '../stores/platformStore'
import Button from '../components/ui/Button.vue'
import Badge from '../components/ui/Badge.vue'
import Card from '../components/ui/Card.vue'

const router = useRouter()
const platformStore = usePlatformStore()

const rankings = computed(() => platformStore.rankings)
const trending = computed(() => platformStore.trending)
</script>

<template>
  <div class="max-w-7xl mx-auto flex flex-col gap-8">
    <!-- Header -->
    <div class="rounded-3xl border border-border bg-card p-6 md:p-10 shadow-xs">
      <Badge variant="outline" class="mb-3 text-emerald-700 border-emerald-300 bg-emerald-50">
        <ShieldCheck class="h-3 w-3 mr-1" />
        Transparencia y Reputación Comunitaria
      </Badge>
      <h1 class="text-3xl md:text-4xl font-black tracking-tight text-foreground mb-2">
        Confianza y Rankings Públicos
      </h1>
      <p class="text-sm text-muted-foreground max-w-2xl leading-relaxed">
        La reputación de cada miembro se calcula a partir de calificaciones reales otorgadas al finalizar sesiones acordadas.
        No se exponen acuerdos privados ni detalles confidenciales.
      </p>
    </div>

    <!-- Grid: Rankings and Trending -->
    <div class="grid grid-cols-1 md:grid-cols-12 gap-6">
      <!-- Rankings Column -->
      <Card class="p-6 md:col-span-7 flex flex-col justify-between">
        <div>
          <div class="flex items-center justify-between mb-4">
            <div>
              <h2 class="text-lg font-bold text-foreground">Miembros con Mejor Reputación</h2>
              <p class="text-xs text-muted-foreground">Calificación promedio basada en intercambios completados</p>
            </div>
            <Trophy class="h-5 w-5 text-amber-500" />
          </div>

          <div v-if="rankings.length > 0" class="flex flex-col gap-3">
            <div
              v-for="(user, idx) in rankings"
              :key="user.id"
              class="flex items-center justify-between p-3 rounded-xl border border-border/60 bg-muted/20 hover:bg-muted/50 transition-colors"
            >
              <div class="flex items-center gap-3">
                <div
                  class="h-7 w-7 rounded-full flex items-center justify-center text-xs font-black"
                  :class="idx === 0 ? 'bg-amber-100 text-amber-800' : idx === 1 ? 'bg-slate-200 text-slate-800' : 'bg-blue-100 text-blue-800'"
                >
                  #{{ idx + 1 }}
                </div>
                <div>
                  <div class="text-xs font-bold text-foreground">{{ user.name }}</div>
                  <div class="text-[11px] text-muted-foreground">
                    {{ user.skillsToTeach.slice(0, 2).join(', ') || 'Miembro general' }}
                  </div>
                </div>
              </div>

              <div class="flex items-center gap-3">
                <div class="text-right">
                  <div class="flex items-center gap-1 text-xs font-bold text-foreground justify-end">
                    <Star class="h-3 w-3 fill-amber-400 text-amber-400" />
                    <span>{{ user.reputationScore }}</span>
                  </div>
                  <span class="text-[10px] text-muted-foreground">{{ user.reviewsCount }} reseñas</span>
                </div>

                <Button
                  variant="ghost"
                  size="icon"
                  title="Ver agenda libre"
                  @click="router.push({ name: 'public-availability', params: { id: user.id } })"
                >
                  <Calendar class="h-4 w-4 text-muted-foreground" />
                </Button>
              </div>
            </div>
          </div>

          <div v-else class="text-center p-8 text-xs text-muted-foreground">
            Aún no hay suficientes calificaciones para mostrar el ranking.
          </div>
        </div>
      </Card>

      <!-- Trending Categories Column -->
      <Card class="p-6 md:col-span-5 flex flex-col justify-between">
        <div>
          <div class="flex items-center justify-between mb-4">
            <div>
              <h2 class="text-lg font-bold text-foreground">Temáticas en Tendencia</h2>
              <p class="text-xs text-muted-foreground">Conocimientos más demandados y ofrecidos</p>
            </div>
            <TrendingUp class="h-5 w-5 text-blue-500" />
          </div>

          <div v-if="trending.length > 0" class="flex flex-col gap-2 mb-6">
            <div
              v-for="item in trending"
              :key="item.category"
              class="flex items-center justify-between p-2.5 rounded-lg bg-muted/40 text-xs font-medium"
            >
              <span class="text-foreground">{{ item.category }}</span>
              <span class="rounded-full bg-primary/10 text-primary font-bold px-2 py-0.5 text-[11px]">
                {{ item.count }} propuestas
              </span>
            </div>
          </div>
        </div>

        <div class="rounded-xl border border-blue-200/60 bg-blue-50/50 p-3.5 text-xs text-blue-900 flex items-start gap-2.5">
          <Info class="h-4 w-4 shrink-0 text-blue-600 mt-0.5" />
          <div class="leading-relaxed">
            <strong>Seguridad y Privacidad:</strong> La plataforma nunca muestra las fechas que ya fueron tomadas por otros participantes ni datos personales privados.
          </div>
        </div>
      </Card>
    </div>
  </div>
</template>
