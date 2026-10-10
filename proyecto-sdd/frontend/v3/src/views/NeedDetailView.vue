<script setup>
import { ref, computed } from 'vue'
import { useRoute, useRouter } from 'vue-router'
import {
  ArrowLeft,
  Flag,
  Calendar,
  HandHelping,
  AlertCircle,
  CheckCircle2
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

const need = computed(() => {
  return platformStore.needs.find(n => n.id === props.id) || mockStorage.needs.find(n => n.id === props.id)
})

const student = computed(() => {
  if (!need.value) return null
  return mockStorage.findUserById(need.value.userId)
})

const showReportDialog = ref(false)
const reportReason = ref('Contenido inapropiado')
const reportDetails = ref('')
const reportSuccess = ref(false)

function handleOfferTeaching() {
  if (authStore.isGuest) {
    router.push({ path: '/auth', query: { redirect: route.fullPath } })
    return
  }

  if (need.value.userId === authStore.currentUser.id) {
    alert('Este es tu propio aprendizaje buscado.')
    return
  }

  router.push({
    name: 'workspace',
    query: {
      tab: 'sessions',
      action: 'offer',
      studentId: need.value.userId,
      topic: need.value.title
    }
  })
}

function handleReportClick() {
  if (authStore.isGuest) {
    router.push({ path: '/auth', query: { redirect: route.fullPath } })
    return
  }
  showReportDialog.value = true
}

function submitReport() {
  platformStore.submitReport({
    targetType: 'NEED',
    targetId: need.value.id,
    targetTitle: need.value.title,
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

    <div v-if="!need" class="rounded-2xl border border-border bg-card p-12 text-center">
      <AlertCircle class="h-8 w-8 text-amber-500 mx-auto mb-3" />
      <h2 class="text-lg font-bold text-foreground">Aprendizaje buscado no encontrado</h2>
      <Button variant="outline" class="mt-4" @click="router.push({ name: 'explore' })">Ver catálogo</Button>
    </div>

    <div v-else class="flex flex-col gap-6">
      <Card class="p-6 sm:p-8">
        <div class="flex items-start justify-between gap-4 mb-3">
          <Badge variant="warning">{{ need.category }}</Badge>
          <button
            class="text-xs text-muted-foreground hover:text-destructive flex items-center gap-1 border-none bg-transparent cursor-pointer transition-colors"
            @click="handleReportClick"
          >
            <Flag class="h-3 w-3" />
            <span>Denunciar</span>
          </button>
        </div>

        <h1 class="text-2xl sm:text-3xl font-black text-foreground mb-4 leading-tight">
          {{ need.title }}
        </h1>

        <div class="flex flex-wrap items-center gap-2 text-xs font-semibold text-muted-foreground mb-6">
          <span class="rounded-md bg-muted px-2.5 py-1">Nivel buscado: {{ need.level }}</span>
          <span class="rounded-md bg-muted px-2.5 py-1">Modalidad: {{ need.modality }}</span>
        </div>

        <div class="rounded-xl border border-amber-200/60 bg-amber-50/50 p-4 text-sm text-foreground mb-6">
          <strong class="text-[11px] uppercase tracking-wider text-amber-800 block mb-1">
            Objetivo a alcanzar:
          </strong>
          {{ need.goal }}
        </div>

        <!-- Student Info -->
        <div v-if="student" class="border-t border-border pt-6 mt-2">
          <div class="text-[11px] uppercase tracking-wider font-bold text-muted-foreground mb-3">
            Publicado por:
          </div>
          <div class="flex flex-wrap items-center justify-between gap-4">
            <div>
              <div class="text-base font-bold text-foreground">{{ student.name }}</div>
              <p class="text-xs text-muted-foreground mt-0.5 max-w-md">{{ student.bio || 'Miembro de la comunidad' }}</p>
              <div class="flex items-center gap-2 mt-2">
                <RatingStars :modelValue="student.reputationScore" readonly />
                <span class="text-xs font-bold text-foreground">
                  {{ student.reputationScore }} ({{ student.reviewsCount }} calificaciones)
                </span>
              </div>
            </div>

            <Button
              variant="outline"
              size="sm"
              @click="router.push({ name: 'public-availability', params: { id: student.id } })"
            >
              <Calendar class="h-3.5 w-3.5 mr-1" />
              Ver Agenda Pública
            </Button>
          </div>
        </div>

        <div class="pt-6 border-t border-border flex flex-wrap items-center justify-between gap-4 mt-4">
          <span class="text-xs text-muted-foreground">
            ¿Sabes enseñar este tema? Inicia un intercambio directo con el solicitante.
          </span>
          <Button size="lg" @click="handleOfferTeaching">
            <HandHelping class="h-4 w-4 mr-1.5" />
            Ofrecerme a Enseñar
          </Button>
        </div>
      </Card>
    </div>

    <!-- Dialog Denuncia -->
    <Dialog
      :open="showReportDialog"
      title="Denunciar Aprendizaje Buscado"
      description="Reporta esta publicación al equipo de moderación."
      @update:open="showReportDialog = $event"
    >
      <div v-if="reportSuccess" class="py-6 text-center">
        <CheckCircle2 class="h-10 w-10 text-emerald-500 mx-auto mb-2" />
        <h3 class="text-base font-bold text-foreground">Denuncia registrada</h3>
      </div>
      <div v-else class="flex flex-col gap-3">
        <select v-model="reportReason" class="h-9 w-full rounded-lg border border-input bg-card px-3 text-xs text-foreground">
          <option value="Contenido inapropiado">Contenido inapropiado</option>
          <option value="Spam / Publicidad comercial">Spam o Publicidad</option>
          <option value="Conducta engañosa">Conducta engañosa</option>
        </select>
        <Textarea v-model="reportDetails" placeholder="Detalles de la denuncia..." />
        <div class="flex justify-end gap-2 pt-2 border-t border-border mt-2">
          <Button variant="ghost" size="sm" @click="showReportDialog = false">Cancelar</Button>
          <Button variant="destructive" size="sm" @click="submitReport">Enviar</Button>
        </div>
      </div>
    </Dialog>
  </div>
</template>
