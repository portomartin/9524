<script setup>
import { ref, computed } from 'vue'
import { useRoute, useRouter } from 'vue-router'
import {
  ArrowLeft,
  Flag,
  Calendar,
  Clock,
  Send,
  CheckCircle2,
  AlertCircle,
  Coins
} from 'lucide-vue-next'
import { usePlatformStore } from '../stores/platformStore'
import { useAuthStore } from '../stores/authStore'
import { mockStorage } from '../services/mockStorage'
import Button from '../components/ui/Button.vue'
import Badge from '../components/ui/Badge.vue'
import Card from '../components/ui/Card.vue'
import Dialog from '../components/ui/Dialog.vue'
import Textarea from '../components/ui/Textarea.vue'
import RatingStars from '../components/ui/RatingStars.vue'

const props = defineProps({
  id: { type: String, required: true }
})

const route = useRoute()
const router = useRouter()
const platformStore = usePlatformStore()
const authStore = useAuthStore()

const offer = computed(() => {
  return platformStore.offers.find(o => o.id === props.id) || mockStorage.getPublicOfferById(props.id)
})

const author = computed(() => {
  if (!offer.value) return null
  return mockStorage.findUserById(offer.value.userId)
})

const authorFreeSlots = computed(() => {
  if (!offer.value) return []
  return platformStore.getPublicUserSlots(offer.value.userId)
})

// Dialogs state
const showRequestDialog = ref(false)
const selectedSlotId = ref('')
const selectedModality = ref('VIRTUAL')
const exchangeType = ref('CREDITS')
const requestError = ref('')
const requestSuccess = ref(false)

const showReportDialog = ref(false)
const reportReason = ref('Contenido inapropiado')
const reportDetails = ref('')
const reportSuccess = ref(false)

function handleRequestSessionClick() {
  if (authStore.isGuest) {
    router.push({ path: '/auth', query: { redirect: route.fullPath } })
    return
  }

  if (offer.value.userId === authStore.currentUser.id) {
    alert('Esta es tu propia propuesta de enseñanza.')
    return
  }

  if (authorFreeSlots.value.length > 0) {
    selectedSlotId.value = authorFreeSlots.value[0].id
  } else {
    selectedSlotId.value = ''
  }
  selectedModality.value = offer.value.modality
  exchangeType.value = 'CREDITS'
  requestError.value = ''
  requestSuccess.value = false
  showRequestDialog.value = true
}

function submitSessionRequest() {
  requestError.value = ''
  try {
    const slot = authorFreeSlots.value.find(s => s.id === selectedSlotId.value)
    if (!slot) {
      throw new Error('Debes seleccionar una franja horaria disponible.')
    }

    platformStore.requestSession({
      teacherId: offer.value.userId,
      offerId: offer.value.id,
      topic: offer.value.title,
      date: slot.date,
      time: slot.startTime,
      modality: selectedModality.value,
      exchangeType: exchangeType.value
    })

    requestSuccess.value = true
    setTimeout(() => {
      showRequestDialog.value = false
      router.push({ name: 'workspace', query: { tab: 'sessions' } })
    }, 1200)
  } catch (err) {
    requestError.value = err.message
  }
}

function handleReportClick() {
  if (authStore.isGuest) {
    router.push({ path: '/auth', query: { redirect: route.fullPath } })
    return
  }
  reportDetails.value = ''
  reportReason.value = 'Contenido inapropiado'
  reportSuccess.value = false
  showReportDialog.value = true
}

function submitReport() {
  platformStore.submitReport({
    targetType: 'OFFER',
    targetId: offer.value.id,
    targetTitle: offer.value.title,
    reason: reportReason.value,
    details: reportDetails.value
  })
  reportSuccess.value = true
  setTimeout(() => {
    showReportDialog.value = false
  }, 1200)
}
</script>

<template>
  <div class="max-w-3xl mx-auto flex flex-col gap-6">
    <Button variant="ghost" size="sm" class="w-fit" @click="router.push({ name: 'explore' })">
      <ArrowLeft class="h-4 w-4 mr-1" />
      Volver a explorar
    </Button>

    <div v-if="!offer" class="rounded-2xl border border-border bg-card p-12 text-center">
      <AlertCircle class="h-8 w-8 text-amber-500 mx-auto mb-3" />
      <h2 class="text-lg font-bold text-foreground">Propuesta no disponible</h2>
      <p class="text-xs text-muted-foreground mt-1">Es posible que haya sido pausada o moderada.</p>
      <Button variant="outline" class="mt-4" @click="router.push({ name: 'explore' })">Ver catálogo</Button>
    </div>

    <div v-else class="flex flex-col gap-6">
      <!-- Main Content Card -->
      <Card class="p-6 sm:p-8">
        <div class="flex items-start justify-between gap-4 mb-3">
          <Badge variant="info">{{ offer.category }}</Badge>
          <button
            class="text-xs text-muted-foreground hover:text-destructive flex items-center gap-1 border-none bg-transparent cursor-pointer transition-colors"
            @click="handleReportClick"
          >
            <Flag class="h-3 w-3" />
            <span>Denunciar</span>
          </button>
        </div>

        <h1 class="text-2xl sm:text-3xl font-black text-foreground mb-4 leading-tight">
          {{ offer.title }}
        </h1>

        <div class="flex flex-wrap items-center gap-2 text-xs font-semibold text-muted-foreground mb-6">
          <span class="rounded-md bg-muted px-2.5 py-1">Nivel: {{ offer.level }}</span>
          <span class="rounded-md bg-muted px-2.5 py-1">Modalidad: {{ offer.modality }}</span>
          <span class="rounded-md bg-muted px-2.5 py-1">Duración: {{ offer.durationMinutes }} minutos</span>
        </div>

        <div class="rounded-xl bg-muted/50 p-4 text-sm text-foreground leading-relaxed mb-6">
          <strong class="text-[11px] uppercase tracking-wider text-muted-foreground block mb-1">
            Descripción del aprendizaje:
          </strong>
          {{ offer.description }}
        </div>

        <!-- Instructor Profile -->
        <div v-if="author" class="border-t border-border pt-6 mt-2">
          <div class="text-[11px] uppercase tracking-wider font-bold text-muted-foreground mb-3">
            Sobre quien enseña:
          </div>
          <div class="flex flex-wrap items-center justify-between gap-4">
            <div>
              <div class="text-base font-bold text-foreground">{{ author.name }}</div>
              <p class="text-xs text-muted-foreground mt-0.5 max-w-md">{{ author.bio || 'Miembro de la comunidad' }}</p>
              <div class="flex items-center gap-2 mt-2">
                <RatingStars :modelValue="author.reputationScore" readonly />
                <span class="text-xs font-bold text-foreground">
                  {{ author.reputationScore }} ({{ author.reviewsCount }} calificaciones)
                </span>
              </div>
            </div>

            <Button
              variant="outline"
              size="sm"
              @click="router.push({ name: 'public-availability', params: { id: author.id } })"
            >
              <Calendar class="h-3.5 w-3.5 mr-1" />
              Ver Agenda Pública
            </Button>
          </div>
        </div>
      </Card>

      <!-- Availability Slots & Action Card -->
      <Card class="p-6 sm:p-8">
        <h2 class="text-lg font-bold text-foreground mb-1">Horarios Libres Disponibles</h2>
        <p class="text-xs text-muted-foreground mb-4">
          Franjas horarias concretas publicadas por {{ author?.name }}. Cada franja equivale a 1 hora de sesión.
        </p>

        <div v-if="authorFreeSlots.length > 0" class="flex flex-wrap gap-2 mb-6">
          <div
            v-for="slot in authorFreeSlots"
            :key="slot.id"
            class="rounded-lg border border-primary/20 bg-primary/5 px-3 py-2 text-xs font-semibold text-primary flex items-center gap-2"
          >
            <Clock class="h-3.5 w-3.5" />
            <span>{{ slot.date }} a las {{ slot.startTime }} hs</span>
          </div>
        </div>

        <div v-else class="rounded-lg bg-muted/60 p-4 text-xs text-muted-foreground mb-6">
          El autor no tiene franjas libres en este momento.
        </div>

        <div class="pt-4 border-t border-border flex flex-wrap items-center justify-between gap-4">
          <div>
            <span class="text-[10px] uppercase font-bold text-muted-foreground block tracking-wider">Costo</span>
            <span class="text-xs font-bold text-foreground">1 Crédito interno o intercambio recíproco</span>
          </div>

          <Button size="lg" @click="handleRequestSessionClick">
            <Send class="h-4 w-4 mr-1.5" />
            Solicitar Sesión de Intercambio
          </Button>
        </div>
      </Card>
    </div>

    <!-- Dialog Solicitud de Sesión (Subtarea 4.3.3) -->
    <Dialog
      :open="showRequestDialog"
      title="Resumen de Solicitud de Sesión"
      description="Verifica los detalles antes de enviar el pedido."
      @update:open="showRequestDialog = $event"
    >
      <div v-if="requestSuccess" class="py-6 text-center">
        <CheckCircle2 class="h-10 w-10 text-emerald-500 mx-auto mb-2" />
        <h3 class="text-base font-bold text-foreground">¡Solicitud enviada con éxito!</h3>
        <p class="text-xs text-muted-foreground mt-1">Redirigiendo a tu panel de sesiones...</p>
      </div>

      <div v-else class="flex flex-col gap-4">
        <div v-if="requestError" class="rounded-lg bg-destructive/10 p-3 text-xs text-destructive font-medium">
          {{ requestError }}
        </div>

        <div class="rounded-lg bg-muted p-3 text-xs text-foreground">
          <div class="font-bold text-sm mb-0.5">{{ offer?.title }}</div>
          <div class="text-muted-foreground">Instructor: {{ author?.name }} · Duración: 60 minutos</div>
        </div>

        <div class="flex flex-col gap-1.5">
          <label class="text-xs font-bold text-foreground">Seleccionar Franja Horaria</label>
          <select
            v-if="authorFreeSlots.length > 0"
            v-model="selectedSlotId"
            class="h-9 w-full rounded-lg border border-input bg-card px-3 text-xs font-medium text-foreground"
          >
            <option v-for="slot in authorFreeSlots" :key="slot.id" :value="slot.id">
              {{ slot.date }} — {{ slot.startTime }} hs (1 hora)
            </option>
          </select>
          <div v-else class="text-xs text-amber-600">
            No hay franjas libres configuradas.
          </div>
        </div>

        <div class="flex flex-col gap-1.5">
          <label class="text-xs font-bold text-foreground">Modalidad</label>
          <select
            v-model="selectedModality"
            class="h-9 w-full rounded-lg border border-input bg-card px-3 text-xs text-foreground"
          >
            <option value="VIRTUAL">Virtual (Reunión online)</option>
            <option value="PRESENCIAL">Presencial</option>
            <option value="HIBRIDA">Híbrida</option>
          </select>
        </div>

        <div class="flex flex-col gap-1.5">
          <label class="text-xs font-bold text-foreground">Método de Intercambio</label>
          <div class="grid grid-cols-2 gap-2 text-xs">
            <label
              class="flex items-center gap-2 rounded-lg border p-2.5 cursor-pointer transition-colors"
              :class="exchangeType === 'CREDITS' ? 'border-primary bg-primary/5 font-semibold text-primary' : 'border-border text-muted-foreground'"
            >
              <input type="radio" v-model="exchangeType" value="CREDITS" class="accent-primary" />
              <span>Usar 1 Crédito (Saldo: {{ authStore.credits }})</span>
            </label>
            <label
              class="flex items-center gap-2 rounded-lg border p-2.5 cursor-pointer transition-colors"
              :class="exchangeType === 'RECIPROCAL' ? 'border-primary bg-primary/5 font-semibold text-primary' : 'border-border text-muted-foreground'"
            >
              <input type="radio" v-model="exchangeType" value="RECIPROCAL" class="accent-primary" />
              <span>Reciprocidad directa</span>
            </label>
          </div>
        </div>

        <div class="rounded-lg bg-blue-50/70 border border-blue-200/60 p-3 text-[11px] text-blue-900 leading-relaxed">
          La sesión iniciará en estado <strong>SOLICITADA</strong> hasta que {{ author?.name }} la confirme.
        </div>

        <div class="flex justify-end gap-2 pt-2 border-t border-border mt-2">
          <Button variant="ghost" size="sm" @click="showRequestDialog = false">Cancelar</Button>
          <Button size="sm" :disabled="!selectedSlotId" @click="submitSessionRequest">
            Confirmar y Enviar Solicitud
          </Button>
        </div>
      </div>
    </Dialog>

    <!-- Dialog Denuncia (Subtarea 6.1.2) -->
    <Dialog
      :open="showReportDialog"
      title="Denunciar Contenido"
      description="Reporta contenido inapropiado o spam al equipo de moderación."
      @update:open="showReportDialog = $event"
    >
      <div v-if="reportSuccess" class="py-6 text-center">
        <CheckCircle2 class="h-10 w-10 text-emerald-500 mx-auto mb-2" />
        <h3 class="text-base font-bold text-foreground">Denuncia registrada</h3>
        <p class="text-xs text-muted-foreground mt-1">El equipo de moderación revisará este caso.</p>
      </div>

      <div v-else class="flex flex-col gap-3">
        <div class="flex flex-col gap-1.5">
          <label class="text-xs font-bold text-foreground">Motivo</label>
          <select v-model="reportReason" class="h-9 w-full rounded-lg border border-input bg-card px-3 text-xs text-foreground">
            <option value="Contenido inapropiado">Contenido inapropiado</option>
            <option value="Spam / Publicidad comercial">Spam o Publicidad comercial</option>
            <option value="Ausencia reiterada o estafa">Ausencia reiterada o estafa</option>
            <option value="Lenguaje ofensivo">Lenguaje ofensivo</option>
          </select>
        </div>

        <div class="flex flex-col gap-1.5">
          <label class="text-xs font-bold text-foreground">Detalles adicionales</label>
          <Textarea v-model="reportDetails" placeholder="Explica brevemente lo ocurrido..." />
        </div>

        <div class="flex justify-end gap-2 pt-2 border-t border-border mt-2">
          <Button variant="ghost" size="sm" @click="showReportDialog = false">Cancelar</Button>
          <Button variant="destructive" size="sm" @click="submitReport">Enviar Denuncia</Button>
        </div>
      </div>
    </Dialog>
  </div>
</template>
