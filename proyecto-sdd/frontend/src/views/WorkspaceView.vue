<script setup>
import { computed, reactive, ref, watch } from 'vue'
import { useRoute, useRouter } from 'vue-router'
import Tabs from 'primevue/tabs'
import TabList from 'primevue/tablist'
import Tab from 'primevue/tab'
import TabPanels from 'primevue/tabpanels'
import TabPanel from 'primevue/tabpanel'
import Card from 'primevue/card'
import InputText from 'primevue/inputtext'
import Textarea from 'primevue/textarea'
import Select from 'primevue/select'
import InputNumber from 'primevue/inputnumber'
import Button from 'primevue/button'
import Message from 'primevue/message'
import Tag from 'primevue/tag'
import DataTable from 'primevue/datatable'
import Column from 'primevue/column'
import ToggleSwitch from 'primevue/toggleswitch'
import DatePicker from 'primevue/datepicker'
import Dialog from 'primevue/dialog'
import Rating from 'primevue/rating'
import { usePlatformStore } from '../stores/platformStore'

const route = useRoute()
const router = useRouter()
const store = usePlatformStore()
const { state, currentUser } = store
const sections = ['profile', 'content', 'matches', 'agenda', 'sessions', 'activity']
const activeSection = ref(sections.includes(route.params.section) ? route.params.section : 'profile')
const success = ref('')
const error = ref('')

watch(activeSection, (section) => router.replace({ name: 'workspace', params: { section } }))

const profile = reactive({
  name: currentUser.value.name,
  description: currentUser.value.description,
  generalLocation: currentUser.value.generalLocation,
  teachingTopicsText: currentUser.value.teachingTopics.join(', '),
  learningTopicsText: currentUser.value.learningTopics.join(', '),
})
const offer = reactive({ id: '', topic: '', title: '', description: '', category: '', level: 'Inicial', modality: 'Virtual', durationMinutes: 60, exchangeCondition: 'CREDITS', creditCost: 1, status: 'DRAFT' })
const need = reactive({ id: '', topic: '', title: '', description: '', objective: '', category: '', level: 'Inicial', modality: 'Virtual', durationMinutes: 60, availabilitySummary: '', status: 'ACTIVE' })
const slot = reactive({ date: null, startTime: '18:00', durationMinutes: 60 })
const batchDates = ref('')
const visibility = computed({ get: () => state.availabilityPublic, set: (value) => store.setAvailabilityVisibility(value) })
const requestDialog = ref(false)
const selectedMatch = ref(null)
const request = reactive({ proposedDate: null, startTime: '18:00', durationMinutes: 60, modality: 'Virtual', exchangeType: 'RECIPROCAL', creditCost: 1, message: '' })
const ratingDialog = ref(false)
const selectedSession = ref(null)
const rating = reactive({ score: 5, comment: '' })
const activityFilter = ref('ALL')

const compatibilities = computed(() => state.offers.map((item, index) => ({
  ...item,
  score: 92 - index * 8,
  reasons: index === 0 ? ['Tema relacionado con tus intereses', 'Modalidad compatible', 'Duración adecuada'] : ['Nivel compatible', 'Modalidad disponible'],
  reciprocal: index === 1,
})))
const historyItems = computed(() => {
  const items = [
    ...state.sessions.map((item) => ({ id: item.id, type: 'SESSION', date: item.proposedDate, label: item.title, status: item.status })),
    ...state.creditMovements.map((item) => ({ id: item.id, type: 'CREDIT', date: item.date, label: item.description, status: item.amount > 0 ? `+${item.amount}` : `${item.amount}` })),
    ...state.ownOffers.map((item) => ({ id: item.id, type: 'OFFER', date: item.publishedAt?.slice(0, 10) || '—', label: item.title, status: item.status })),
    ...state.ownLearningNeeds.map((item) => ({ id: item.id, type: 'LEARNING', date: item.publishedAt?.slice(0, 10) || '—', label: item.title, status: item.status })),
  ]
  return activityFilter.value === 'ALL' ? items : items.filter((item) => item.type === activityFilter.value)
})

function notify(message) { success.value = message; error.value = ''; window.setTimeout(() => { success.value = '' }, 2500) }
function fail(message) { error.value = message; success.value = '' }
function dateValue(value) { return value instanceof Date ? value.toISOString().slice(0, 10) : value }

function saveProfile() {
  store.updateProfile({
    name: profile.name, description: profile.description, generalLocation: profile.generalLocation,
    teachingTopics: profile.teachingTopicsText.split(',').map((item) => item.trim()).filter(Boolean),
    learningTopics: profile.learningTopicsText.split(',').map((item) => item.trim()).filter(Boolean),
  })
  notify('Perfil guardado correctamente.')
}

function saveOffer(status) {
  if (!offer.title || !offer.description || !offer.category) return fail('Completá título, descripción y categoría.')
  store.saveOffer({ ...offer, topic: offer.topic || offer.title, status })
  Object.assign(offer, { id: '', topic: '', title: '', description: '', category: '', level: 'Inicial', modality: 'Virtual', durationMinutes: 60, exchangeCondition: 'CREDITS', creditCost: 1, status: 'DRAFT' })
  notify(status === 'PUBLISHED' ? 'Propuesta publicada.' : 'Borrador guardado.')
}

function saveNeed() {
  if (!need.title || !need.objective) return fail('Completá título y objetivo de aprendizaje.')
  store.saveLearningNeed({ ...need, topic: need.topic || need.title })
  Object.assign(need, { id: '', topic: '', title: '', description: '', objective: '', category: '', level: 'Inicial', modality: 'Virtual', durationMinutes: 60, availabilitySummary: '', status: 'ACTIVE' })
  notify('Aprendizaje buscado guardado.')
}

function editOffer(item) { Object.assign(offer, item); notify('Propuesta cargada para edición.') }
function editNeed(item) { Object.assign(need, item); notify('Aprendizaje cargado para edición.') }

function addSlot(date = slot.date) {
  if (!date) return fail('Elegí una fecha concreta.')
  store.addAvailability({ date: dateValue(date), startTime: slot.startTime, durationMinutes: slot.durationMinutes })
  notify('Franja agregada.')
}

function addBatch() {
  const dates = batchDates.value.split(/[\s,;]+/).map((value) => value.trim()).filter(Boolean)
  if (!dates.length) return fail('Ingresá al menos una fecha en formato AAAA-MM-DD.')
  dates.forEach((date) => store.addAvailability({ date, startTime: slot.startTime, durationMinutes: slot.durationMinutes }))
  batchDates.value = ''
  notify(`${dates.length} franjas concretas agregadas; no se guardó ninguna recurrencia.`)
}

function openRequest(item) { selectedMatch.value = item; requestDialog.value = true }
function sendRequest() {
  if (!request.proposedDate) return fail('Elegí una fecha para la sesión.')
  store.createSession({ offerId: selectedMatch.value.id, proposedDate: dateValue(request.proposedDate), startTime: request.startTime, durationMinutes: request.durationMinutes, modality: request.modality, exchangeType: request.exchangeType, creditCost: request.exchangeType === 'CREDITS' ? request.creditCost : 0, message: request.message })
  requestDialog.value = false
  activeSection.value = 'sessions'
  notify('Solicitud creada y pendiente de confirmación.')
}

function transition(session, status) {
  store.transitionSession(session.id, status)
  if (status === 'FINALIZADA' && session.exchangeType === 'CREDITS' && session.creditCost) {
    state.creditBalance -= session.creditCost
    state.creditMovements.unshift({ id: `mov-${Date.now()}`, date: new Date().toISOString().slice(0, 10), description: session.title, amount: -session.creditCost })
  }
  notify(`Sesión actualizada a ${status}.`)
}

function openRating(session) { selectedSession.value = session; rating.score = 5; rating.comment = ''; ratingDialog.value = true }
function submitRating() {
  try { store.rateSession(selectedSession.value.id, rating.score, rating.comment); ratingDialog.value = false; notify('Calificación registrada.') }
  catch (ratingError) { fail(ratingError.message) }
}

function statusSeverity(status) {
  return ({ SOLICITADA: 'warn', CONFIRMADA: 'info', EN_CURSO: 'contrast', FINALIZADA: 'success', CANCELADA: 'danger' })[status] || 'secondary'
}
</script>

<template>
  <section class="flex flex-column gap-4">
    <div><h1 class="mb-2">Mi espacio</h1><p class="text-color-secondary mt-0">Gestioná lo necesario para ofrecer, aprender y concretar intercambios.</p></div>
    <Message v-if="route.query.denied" severity="error" :closable="false">No tenés permisos para acceder al área administrativa.</Message>
    <Message v-if="success" severity="success" :closable="false">{{ success }}</Message>
    <Message v-if="error" severity="error" :closable="false">{{ error }}</Message>

    <Tabs v-model:value="activeSection" scrollable>
      <TabList>
        <Tab value="profile">Perfil</Tab><Tab value="content">Publicaciones</Tab><Tab value="matches">Compatibilidades</Tab>
        <Tab value="agenda">Agenda</Tab><Tab value="sessions">Sesiones</Tab><Tab value="activity">Créditos e historial</Tab>
      </TabList>
      <TabPanels>
        <TabPanel value="profile">
          <Card><template #title>Perfil básico</template><template #subtitle>Podés guardar información parcial y editarla después.</template><template #content>
            <form class="grid" @submit.prevent="saveProfile">
              <div class="col-12 md:col-6 flex flex-column gap-2"><label for="name">Nombre público</label><InputText id="name" v-model="profile.name" /></div>
              <div class="col-12 md:col-6 flex flex-column gap-2"><label for="location">Ubicación general</label><InputText id="location" v-model="profile.generalLocation" /></div>
              <div class="col-12 flex flex-column gap-2"><label for="description">Presentación</label><Textarea id="description" v-model="profile.description" rows="3" /></div>
              <div class="col-12 md:col-6 flex flex-column gap-2"><label for="teaching">Qué podés enseñar</label><InputText id="teaching" v-model="profile.teachingTopicsText" placeholder="Separá los temas con comas" /></div>
              <div class="col-12 md:col-6 flex flex-column gap-2"><label for="learning">Qué querés aprender</label><InputText id="learning" v-model="profile.learningTopicsText" placeholder="Separá los temas con comas" /></div>
              <div class="col-12"><Button type="submit" label="Guardar perfil" icon="pi pi-save" /></div>
            </form>
          </template></Card>
        </TabPanel>

        <TabPanel value="content">
          <div class="grid">
            <div class="col-12 lg:col-6"><Card><template #title>Crear propuesta</template><template #content>
              <form class="flex flex-column gap-3" @submit.prevent="saveOffer('PUBLISHED')">
                <InputText v-model="offer.title" placeholder="Título o tema" /><Textarea v-model="offer.description" rows="3" placeholder="Qué vas a enseñar" />
                <InputText v-model="offer.category" placeholder="Categoría" />
                <div class="grid"><div class="col-6"><Select v-model="offer.level" :options="['Inicial','Básico','Intermedio','Avanzado']" class="w-full" /></div><div class="col-6"><Select v-model="offer.modality" :options="['Virtual','Presencial','Virtual o presencial']" class="w-full" /></div></div>
                <div class="grid"><div class="col-6"><InputNumber v-model="offer.durationMinutes" suffix=" min" :min="30" class="w-full" /></div><div class="col-6"><InputNumber v-model="offer.creditCost" suffix=" créditos" :min="0" class="w-full" /></div></div>
                <div class="flex gap-2"><Button type="button" label="Guardar borrador" severity="secondary" @click="saveOffer('DRAFT')" /><Button type="submit" label="Publicar" icon="pi pi-send" /></div>
              </form>
              <div v-if="state.ownOffers.length" class="mt-4 flex flex-column gap-2"><div v-for="item in state.ownOffers" :key="item.id" class="surface-50 border-round p-3 flex justify-content-between align-items-center"><div><span>{{ item.title }}</span><Tag :value="item.status" class="ml-2" /></div><div class="flex gap-1"><Button icon="pi pi-pencil" text rounded aria-label="Editar propuesta" @click="editOffer(item)" /><Button v-if="item.status === 'PUBLISHED'" icon="pi pi-eye" text rounded aria-label="Ver propuesta pública" @click="router.push({name:'public-offer-detail',params:{offerId:item.id}})" /></div></div></div>
            </template></Card></div>
            <div class="col-12 lg:col-6"><Card><template #title>Aprendizaje buscado</template><template #content>
              <form class="flex flex-column gap-3" @submit.prevent="saveNeed">
                <InputText v-model="need.title" placeholder="Qué querés aprender" /><Textarea v-model="need.objective" rows="3" placeholder="Objetivo de aprendizaje" />
                <InputText v-model="need.category" placeholder="Categoría" />
                <div class="grid"><div class="col-6"><Select v-model="need.level" :options="['Inicial','Básico','Intermedio','Avanzado']" class="w-full" /></div><div class="col-6"><Select v-model="need.modality" :options="['Virtual','Presencial','Virtual o presencial']" class="w-full" /></div></div>
                <InputText v-model="need.availabilitySummary" placeholder="Resumen de disponibilidad" />
                <Button type="submit" label="Guardar aprendizaje" icon="pi pi-save" />
              </form>
              <div v-if="state.ownLearningNeeds.length" class="mt-4 flex flex-column gap-2"><div v-for="item in state.ownLearningNeeds" :key="item.id" class="surface-50 border-round p-3"><div class="flex justify-content-between align-items-center"><span>{{ item.title }}</span><div class="flex gap-2"><Button icon="pi pi-pencil" text rounded aria-label="Editar aprendizaje" @click="editNeed(item)" /><Button icon="pi pi-pause" text rounded aria-label="Pausar" @click="store.setLearningNeedStatus(item.id, item.status === 'PAUSED' ? 'ACTIVE' : 'PAUSED')" /><Button icon="pi pi-trash" text rounded severity="danger" aria-label="Eliminar" @click="store.removeLearningNeed(item.id)" /></div></div><Tag :value="item.status" class="mt-2" /></div></div>
            </template></Card></div>
          </div>
        </TabPanel>

        <TabPanel value="matches">
          <Message severity="info" :closable="false" class="mb-3">Las compatibilidades son orientativas: explican coincidencias, pero no garantizan una sesión exitosa.</Message>
          <div class="grid"><div v-for="item in compatibilities" :key="item.id" class="col-12 md:col-6 lg:col-4"><Card class="h-full"><template #title>{{ item.title }}</template><template #subtitle>{{ item.score }}% de compatibilidad</template><template #content><div class="flex flex-column gap-2"><Tag v-if="item.reciprocal" value="Intercambio recíproco posible" severity="success" /><span v-for="reason in item.reasons" :key="reason"><i class="pi pi-check-circle text-primary mr-2" />{{ reason }}</span></div></template><template #footer><Button label="Solicitar sesión" class="w-full" @click="openRequest(item)" /></template></Card></div></div>
        </TabPanel>

        <TabPanel value="agenda">
          <div class="grid">
            <div class="col-12 lg:col-5"><Card><template #title>Agregar disponibilidad</template><template #subtitle>Las franjas son fechas concretas; no se guarda recurrencia.</template><template #content><div class="flex flex-column gap-3"><DatePicker v-model="slot.date" date-format="yy-mm-dd" placeholder="Fecha" show-icon /><InputText v-model="slot.startTime" type="time" /><InputNumber v-model="slot.durationMinutes" suffix=" min" :min="60" :step="60" /><Button label="Agregar franja" @click="addSlot()" /><Textarea v-model="batchDates" rows="3" placeholder="Carga múltiple: 2026-11-01, 2026-11-03" /><Button label="Agregar fechas concretas" severity="secondary" @click="addBatch" /></div></template></Card></div>
            <div class="col-12 lg:col-7"><Card><template #title>Mi agenda</template><template #subtitle><div class="flex align-items-center gap-2"><ToggleSwitch v-model="visibility" input-id="visibility" /><label for="visibility">Agenda pública</label></div></template><template #content><Message severity="secondary" :closable="false" class="mb-3">{{ visibility ? 'El público ve únicamente estas franjas libres.' : 'Tu agenda está privada; nadie puede consultar tus horarios.' }}</Message><DataTable :value="state.availability" responsive-layout="scroll"><template #empty>No agregaste disponibilidad todavía.</template><Column field="date" header="Fecha" /><Column field="startTime" header="Hora" /><Column field="durationMinutes" header="Duración"><template #body="{data}">{{ data.durationMinutes }} min</template></Column><Column header=""><template #body="{data}"><Button icon="pi pi-trash" text severity="danger" aria-label="Eliminar franja" @click="store.removeAvailability(data.id)" /></template></Column></DataTable></template></Card></div>
          </div>
        </TabPanel>

        <TabPanel value="sessions">
          <DataTable :value="state.sessions" responsive-layout="scroll"><template #empty>No hay sesiones todavía.</template><Column field="title" header="Sesión" /><Column field="counterpart" header="Con" /><Column header="Fecha"><template #body="{data}">{{ data.proposedDate }} · {{ data.startTime }}</template></Column><Column header="Estado"><template #body="{data}"><Tag :value="data.status" :severity="statusSeverity(data.status)" /></template></Column><Column header="Acciones"><template #body="{data}"><div class="flex flex-wrap gap-1"><Button v-if="data.status === 'SOLICITADA'" label="Confirmar" size="small" @click="transition(data,'CONFIRMADA')" /><Button v-if="data.status === 'CONFIRMADA'" label="Iniciar" size="small" @click="transition(data,'EN_CURSO')" /><Button v-if="data.status === 'EN_CURSO'" label="Finalizar" size="small" severity="success" @click="transition(data,'FINALIZADA')" /><Button v-if="!['FINALIZADA','CANCELADA'].includes(data.status)" label="Cancelar" size="small" text severity="danger" @click="transition(data,'CANCELADA')" /><Button v-if="data.status === 'FINALIZADA' && !data.rated" label="Calificar" size="small" text @click="openRating(data)" /></div></template></Column></DataTable>
        </TabPanel>

        <TabPanel value="activity">
          <div class="grid"><div class="col-12 md:col-4"><Card><template #title>Saldo</template><template #content><div class="text-5xl font-bold text-primary">{{ state.creditBalance }}</div><p class="text-color-secondary">Créditos internos; no representan dinero.</p></template></Card></div><div class="col-12 md:col-8"><Card><template #title>Movimientos de créditos</template><template #content><DataTable :value="state.creditMovements"><Column field="date" header="Fecha" /><Column field="description" header="Detalle" /><Column header="Movimiento"><template #body="{data}"><Tag :value="`${data.amount > 0 ? '+' : ''}${data.amount}`" :severity="data.amount > 0 ? 'success' : 'warn'" /></template></Column></DataTable></template></Card></div></div>
          <Card class="mt-3"><template #title>Historial de actividad</template><template #subtitle><Select v-model="activityFilter" :options="[{label:'Todo',value:'ALL'},{label:'Sesiones',value:'SESSION'},{label:'Créditos',value:'CREDIT'},{label:'Propuestas',value:'OFFER'},{label:'Aprendizajes',value:'LEARNING'}]" option-label="label" option-value="value" /></template><template #content><DataTable :value="historyItems" paginator :rows="5"><template #empty>No hay actividad para este filtro.</template><Column field="date" header="Fecha" /><Column field="type" header="Tipo" /><Column field="label" header="Actividad" /><Column header="Estado"><template #body="{data}"><Tag :value="data.status" /></template></Column></DataTable></template></Card>
        </TabPanel>
      </TabPanels>
    </Tabs>

    <Dialog v-model:visible="requestDialog" modal header="Confirmar solicitud" class="w-11 md:w-6">
      <div v-if="selectedMatch" class="flex flex-column gap-3"><Message severity="info" :closable="false">Vas a solicitar: {{ selectedMatch.title }}</Message><DatePicker v-model="request.proposedDate" date-format="yy-mm-dd" placeholder="Fecha propuesta" show-icon /><InputText v-model="request.startTime" type="time" /><InputNumber v-model="request.durationMinutes" suffix=" min" :min="30" /><Select v-model="request.modality" :options="['Virtual','Presencial']" /><Select v-model="request.exchangeType" :options="['RECIPROCAL','CREDITS']" /><InputNumber v-if="request.exchangeType === 'CREDITS'" v-model="request.creditCost" suffix=" créditos" :min="1" /><Textarea v-model="request.message" rows="3" placeholder="Mensaje opcional" /></div>
      <template #footer><Button label="Volver" text @click="requestDialog = false" /><Button label="Enviar solicitud" icon="pi pi-send" @click="sendRequest" /></template>
    </Dialog>
    <Dialog v-model:visible="ratingDialog" modal header="Calificar sesión" class="w-11 md:w-5"><div class="flex flex-column gap-3"><Rating v-model="rating.score" /><Textarea v-model="rating.comment" rows="4" placeholder="Comentario opcional" /></div><template #footer><Button label="Cancelar" text @click="ratingDialog = false" /><Button label="Confirmar calificación" @click="submitRating" /></template></Dialog>
  </section>
</template>
