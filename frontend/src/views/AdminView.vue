<script setup>
import { computed, ref } from 'vue'
import Card from 'primevue/card'
import DataTable from 'primevue/datatable'
import Column from 'primevue/column'
import Select from 'primevue/select'
import Button from 'primevue/button'
import Tag from 'primevue/tag'
import Dialog from 'primevue/dialog'
import Textarea from 'primevue/textarea'
import Message from 'primevue/message'
import { usePlatformStore } from '../stores/platformStore'

const store = usePlatformStore()
const { state, isAdmin } = store
const statusFilter = ref(null)
const actionDialog = ref(false)
const selectedUser = ref(null)
const reason = ref('')
const success = ref('')
const offerDialog = ref(false)
const selectedOffer = ref(null)
const filteredUsers = computed(() => state.users.filter((user) => !statusFilter.value || user.status === statusFilter.value))

function openUserAction(user) { selectedUser.value = user; reason.value = ''; actionDialog.value = true }
function applyUserAction() {
  if (!reason.value.trim()) return
  const status = selectedUser.value.status === 'ACTIVE' ? 'SUSPENDED' : 'ACTIVE'
  store.setUserStatus(selectedUser.value.id, status)
  actionDialog.value = false
  success.value = `Cuenta ${status === 'ACTIVE' ? 'reactivada' : 'suspendida'} con revisión humana registrada.`
}
function openOfferAction(offer) { selectedOffer.value = offer; reason.value = ''; offerDialog.value = true }
function hideOffer() {
  if (!reason.value.trim()) return
  store.hideOffer(selectedOffer.value.id)
  offerDialog.value = false
  success.value = 'Propuesta ocultada con motivo administrativo registrado en el mock.'
}
</script>

<template>
  <section class="flex flex-column gap-4">
    <div><h1 class="mb-2">Administración y seguridad</h1><p class="text-color-secondary mt-0">Revisión mínima de denuncias, contenido y cuentas.</p></div>
    <Message v-if="!isAdmin" severity="error" :closable="false">No tenés autorización administrativa.</Message>
    <template v-else>
      <Message v-if="success" severity="success" :closable="false">{{ success }}</Message>
      <Card><template #title>Denuncias</template><template #content><DataTable :value="state.reports" responsive-layout="scroll"><template #empty>No hay denuncias.</template><Column field="targetLabel" header="Recurso" /><Column field="reasonCode" header="Motivo" /><Column field="description" header="Detalle" /><Column header="Estado"><template #body="{data}"><Tag :value="data.status" :severity="data.status === 'OPEN' ? 'warn' : 'success'" /></template></Column><Column header="Acción"><template #body="{data}"><Button v-if="data.status === 'OPEN'" label="Marcar revisada" size="small" @click="store.resolveReport(data.id)" /></template></Column></DataTable></template></Card>
      <Card><template #title>Usuarios</template><template #subtitle><Select v-model="statusFilter" :options="['ACTIVE','SUSPENDED']" placeholder="Filtrar estado" show-clear /></template><template #content><DataTable :value="filteredUsers" responsive-layout="scroll"><Column field="name" header="Nombre" /><Column field="email" header="Correo" /><Column field="role" header="Rol" /><Column header="Estado"><template #body="{data}"><Tag :value="data.status" :severity="data.status === 'ACTIVE' ? 'success' : 'danger'" /></template></Column><Column header="Acción"><template #body="{data}"><Button v-if="data.id !== 'usr-admin'" :label="data.status === 'ACTIVE' ? 'Suspender' : 'Reactivar'" size="small" :severity="data.status === 'ACTIVE' ? 'danger' : 'success'" @click="openUserAction(data)" /></template></Column></DataTable></template></Card>
      <Card><template #title>Propuestas públicas</template><template #content><DataTable :value="state.offers"><Column field="title" header="Propuesta" /><Column field="authorDisplayName" header="Autor" /><Column field="category" header="Categoría" /><Column header="Acción"><template #body="{data}"><Button label="Ocultar" size="small" text severity="danger" @click="openOfferAction(data)" /></template></Column></DataTable></template></Card>
    </template>
    <Dialog v-model:visible="actionDialog" modal header="Confirmar revisión de cuenta" class="w-11 md:w-5"><Message severity="warn" :closable="false">Esta acción administrativa requiere revisión humana y quedará representada en el mock.</Message><Textarea v-model="reason" rows="4" class="w-full mt-3" placeholder="Motivo obligatorio" /><template #footer><Button label="Cancelar" text @click="actionDialog = false" /><Button label="Confirmar acción" :disabled="!reason.trim()" @click="applyUserAction" /></template></Dialog>
    <Dialog v-model:visible="offerDialog" modal header="Ocultar propuesta" class="w-11 md:w-5"><Message severity="warn" :closable="false">Confirmá el motivo antes de retirar esta propuesta de la vista pública.</Message><Textarea v-model="reason" rows="4" class="w-full mt-3" placeholder="Motivo obligatorio" /><template #footer><Button label="Cancelar" text @click="offerDialog = false" /><Button label="Ocultar propuesta" severity="danger" :disabled="!reason.trim()" @click="hideOffer" /></template></Dialog>
  </section>
</template>
