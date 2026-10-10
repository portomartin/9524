<script setup>
import { computed } from 'vue'
import { useRouter } from 'vue-router'
import {
  ArrowLeft,
  Calendar,
  Clock,
  Lock,
  Star,
  ShieldCheck,
  UserX
} from 'lucide-vue-next'
import { usePlatformStore } from '../stores/platformStore'
import { mockStorage } from '../services/mockStorage'
import Button from '../components/ui/Button.vue'
import Badge from '../components/ui/Badge.vue'
import Card from '../components/ui/Card.vue'

const props = defineProps({
  id: { type: String, required: true }
})

const router = useRouter()
const platformStore = usePlatformStore()

const user = computed(() => {
  return mockStorage.findUserById(props.id)
})

const freeSlots = computed(() => {
  return platformStore.getPublicUserSlots(props.id)
})
</script>

<template>
  <div class="max-w-2xl mx-auto flex flex-col gap-6">
    <Button variant="ghost" size="sm" class="w-fit" @click="router.back()">
      <ArrowLeft class="h-4 w-4 mr-1" />
      Volver
    </Button>

    <div v-if="!user" class="rounded-2xl border border-border bg-card p-12 text-center">
      <UserX class="h-8 w-8 text-amber-500 mx-auto mb-2" />
      <h2 class="text-base font-bold text-foreground">Usuario no encontrado</h2>
    </div>

    <Card v-else class="p-6 sm:p-8 flex flex-col gap-6">
      <div class="flex flex-wrap items-center justify-between gap-4 border-b border-border pb-6">
        <div>
          <span class="text-[10px] font-bold uppercase tracking-wider text-muted-foreground">
            Agenda Pública de Disponibilidad
          </span>
          <h1 class="text-2xl font-black text-foreground mt-0.5">{{ user.name }}</h1>
          <p class="text-xs text-muted-foreground mt-0.5">{{ user.bio || 'Miembro de la comunidad' }}</p>
        </div>

        <div class="text-right">
          <span class="text-[10px] uppercase font-bold text-muted-foreground block">Reputación</span>
          <div class="flex items-center gap-1 font-bold text-sm text-foreground justify-end mt-0.5">
            <Star class="h-3.5 w-3.5 fill-amber-400 text-amber-400" />
            <span>{{ user.reputationScore }} ({{ user.reviewsCount }} calificaciones)</span>
          </div>
        </div>
      </div>

      <!-- Visibility Check -->
      <div v-if="!user.agendaPublic" class="rounded-2xl border border-amber-200/60 bg-amber-50/50 p-8 text-center">
        <Lock class="h-8 w-8 text-amber-600 mx-auto mb-2" />
        <h3 class="text-sm font-bold text-amber-900">Agenda configurada como privada</h3>
        <p class="text-xs text-amber-800 mt-1 max-w-sm mx-auto">
          Este participante prefiere acordar las fechas de forma individual tras recibir una solicitud de intercambio.
        </p>
      </div>

      <!-- Free Slots List -->
      <div v-else>
        <div class="rounded-xl border border-blue-200/60 bg-blue-50/50 p-3.5 text-xs text-blue-900 flex items-center gap-2 mb-6">
          <ShieldCheck class="h-4 w-4 shrink-0 text-blue-600" />
          <span>
            Esta vista expone <strong>únicamente franjas horarias libres de 1 hora</strong>. Los compromisos tomados permanecen privados.
          </span>
        </div>

        <div v-if="freeSlots.length > 0" class="flex flex-col gap-2.5">
          <div
            v-for="slot in freeSlots"
            :key="slot.id"
            class="p-3.5 rounded-xl border border-border bg-card flex items-center justify-between hover:border-primary/40 hover:bg-muted/30 transition-all"
          >
            <div class="flex items-center gap-3">
              <div class="h-8 w-8 rounded-lg bg-primary/10 text-primary flex items-center justify-center">
                <Clock class="h-4 w-4" />
              </div>
              <div>
                <span class="font-bold text-sm text-foreground block">{{ slot.date }}</span>
                <span class="text-xs text-muted-foreground font-medium">{{ slot.startTime }} hs · Duración: 1 hora</span>
              </div>
            </div>

            <Badge variant="success">Disponible</Badge>
          </div>
        </div>

        <div v-else class="rounded-xl border border-dashed border-border p-8 text-center text-xs text-muted-foreground">
          No hay franjas libres configuradas en este momento.
        </div>
      </div>
    </Card>
  </div>
</template>
