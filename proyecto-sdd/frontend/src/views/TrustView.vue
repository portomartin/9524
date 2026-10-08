<script setup>
import { reactive, ref } from 'vue'
import Card from 'primevue/card'
import DataTable from 'primevue/datatable'
import Column from 'primevue/column'
import Rating from 'primevue/rating'
import Tag from 'primevue/tag'
import Message from 'primevue/message'
import Button from 'primevue/button'
import Dialog from 'primevue/dialog'
import Select from 'primevue/select'
import Textarea from 'primevue/textarea'
import { usePlatformStore } from '../stores/platformStore'

const store = usePlatformStore()
const { state } = store
const trending = [...state.offers].slice(0, 3)
const reportDialog = ref(false)
const selectedPerson = ref(null)
const reportSent = ref(false)
const report = reactive({ reasonCode: 'INAPPROPRIATE', description: '' })
function openReport(person) { selectedPerson.value = person; report.description = ''; reportDialog.value = true }
function sendReport() {
  store.report({ targetType: 'USER', targetId: selectedPerson.value.userId, targetLabel: selectedPerson.value.userName, reasonCode: report.reasonCode, description: report.description })
  reportDialog.value = false
  reportSent.value = true
}
</script>

<template>
  <section class="flex flex-column gap-4">
    <div><h1 class="mb-2">Confianza pública</h1><p class="text-color-secondary mt-0">Referencias públicas sin exponer acuerdos ni información privada.</p></div>
    <Message v-if="reportSent" severity="success" :closable="false">Recibimos tu denuncia para revisión.</Message>
    <div class="grid">
      <div class="col-12 lg:col-6">
        <Card class="h-full">
          <template #title>Personas destacadas</template>
          <template #content>
            <DataTable :value="state.ratings" responsive-layout="scroll">
              <Column field="userName" header="Persona" />
              <Column header="Reputación">
                <template #body="{ data }"><div class="flex align-items-center gap-2"><Rating :model-value="Math.round(data.score)" readonly /><span>{{ data.score }} ({{ data.count }})</span></div></template>
              </Column>
              <Column header=""><template #body="{ data }"><Button icon="pi pi-flag" text severity="danger" aria-label="Denunciar usuario" @click="openReport(data)" /></template></Column>
            </DataTable>
          </template>
        </Card>
      </div>
      <div class="col-12 lg:col-6">
        <Card class="h-full">
          <template #title>Contenido con actividad reciente</template>
          <template #content>
            <div class="flex flex-column gap-3">
              <div v-for="offer in trending" :key="offer.id" class="surface-50 border-round p-3">
                <div class="font-semibold mb-2">{{ offer.title }}</div>
                <Tag :value="offer.category" />
              </div>
              <Message v-if="trending.length === 0" severity="secondary" :closable="false">Todavía no hay datos públicos suficientes.</Message>
            </div>
          </template>
        </Card>
      </div>
    </div>
    <Card>
      <template #title>Agendas públicas</template>
      <template #subtitle>Solo se muestran horarios libres; nunca acuerdos ni participantes.</template>
      <template #content>
        <DataTable :value="state.publicAgendas" responsive-layout="scroll">
          <template #empty>No hay horarios públicos disponibles.</template>
          <Column field="userName" header="Persona" />
          <Column field="date" header="Fecha" />
          <Column field="startTime" header="Hora" />
          <Column header="Duración"><template #body="{ data }">{{ data.durationMinutes }} min</template></Column>
        </DataTable>
      </template>
    </Card>
    <Dialog v-model:visible="reportDialog" modal header="Denunciar usuario" class="w-11 md:w-5"><Message severity="warn" :closable="false">La denuncia será revisada antes de tomar una medida.</Message><div class="flex flex-column gap-3 mt-3"><Select v-model="report.reasonCode" :options="[{label:'Conducta inapropiada',value:'INAPPROPRIATE'},{label:'Identidad engañosa',value:'MISLEADING'},{label:'Otro motivo',value:'OTHER'}]" option-label="label" option-value="value" /><Textarea v-model="report.description" rows="4" placeholder="Descripción obligatoria" /></div><template #footer><Button label="Cancelar" text @click="reportDialog = false" /><Button label="Enviar denuncia" severity="danger" :disabled="!report.description.trim()" @click="sendReport" /></template></Dialog>
  </section>
</template>
