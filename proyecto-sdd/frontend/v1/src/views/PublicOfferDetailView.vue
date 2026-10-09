<script setup>
import { onMounted, reactive, ref } from 'vue'
import { useRouter } from 'vue-router'
import Message from 'primevue/message'
import Button from 'primevue/button'
import Skeleton from 'primevue/skeleton'
import Dialog from 'primevue/dialog'
import Select from 'primevue/select'
import Textarea from 'primevue/textarea'
import PublicContentDetail from '../components/PublicContentDetail.vue'
import { usePublicDetail } from '../composables/usePublicDetail'
import { publicCatalogService } from '../services/publicCatalogService'
import { usePlatformStore } from '../stores/platformStore'

const props = defineProps({ offerId: { type: String, required: true } })
const router = useRouter()
const store = usePlatformStore()
const { item, isLoading, error, load } = usePublicDetail(() => publicCatalogService.getOffer(props.offerId))
const reportDialog = ref(false)
const reportSent = ref(false)
const report = reactive({ reasonCode: 'INAPPROPRIATE', description: '' })

onMounted(load)

function requestSession() {
  if (!store.isAuthenticated.value) {
    router.push({ name: 'auth', query: { redirect: `/mi-espacio/matches?offerId=${props.offerId}` } })
    return
  }
  router.push({ name: 'workspace', params: { section: 'matches' }, query: { offerId: props.offerId } })
}

function sendReport() {
  store.report({ targetType: 'OFFER', targetId: props.offerId, targetLabel: item.value.title, reasonCode: report.reasonCode, description: report.description })
  reportDialog.value = false
  reportSent.value = true
}
</script>

<template>
  <Skeleton v-if="isLoading" height="28rem" border-radius="12px" aria-label="Cargando propuesta" />
  <Message v-else-if="error" severity="error" :closable="false"><div class="flex flex-column gap-3"><span>{{ error.message }}</span><Button label="Reintentar" icon="pi pi-refresh" class="align-self-start" @click="load" /></div></Message>
  <div v-else-if="item" class="flex flex-column gap-3">
    <Message v-if="reportSent" severity="success" :closable="false">Recibimos tu denuncia para revisión.</Message>
    <PublicContentDetail :item="item" kind-label="Propuesta para aprender" />
    <div class="flex flex-wrap gap-2 justify-content-end"><Button label="Denunciar contenido" icon="pi pi-flag" text severity="danger" @click="reportDialog = true" /><Button label="Solicitar sesión" icon="pi pi-calendar-plus" @click="requestSession" /></div>
  </div>
  <Dialog v-model:visible="reportDialog" modal header="Denunciar propuesta" class="w-11 md:w-5">
    <Message severity="warn" :closable="false">Usá este canal solo para contenido que incumpla las reglas de aprendizaje seguro.</Message>
    <div class="flex flex-column gap-3 mt-3"><Select v-model="report.reasonCode" :options="[{label:'Contenido inapropiado',value:'INAPPROPRIATE'},{label:'Información engañosa',value:'MISLEADING'},{label:'Otro motivo',value:'OTHER'}]" option-label="label" option-value="value" /><Textarea v-model="report.description" rows="4" placeholder="Contanos qué deberíamos revisar" /></div>
    <template #footer><Button label="Cancelar" text @click="reportDialog = false" /><Button label="Enviar denuncia" severity="danger" :disabled="!report.description.trim()" @click="sendReport" /></template>
  </Dialog>
</template>
