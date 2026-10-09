<script setup>
import { onMounted } from 'vue'
import Message from 'primevue/message'
import Button from 'primevue/button'
import Skeleton from 'primevue/skeleton'
import PublicContentDetail from '../components/PublicContentDetail.vue'
import { usePublicDetail } from '../composables/usePublicDetail'
import { publicCatalogService } from '../services/publicCatalogService'

const props = defineProps({ learningNeedId: { type: String, required: true } })
const { item, isLoading, error, load } = usePublicDetail(() => publicCatalogService.getLearningNeed(props.learningNeedId))
onMounted(load)
</script>

<template>
  <Skeleton v-if="isLoading" height="28rem" border-radius="12px" aria-label="Cargando aprendizaje buscado" />
  <Message v-else-if="error" severity="error" :closable="false">
    <div class="flex flex-column gap-3">
      <span>{{ error.message }}</span>
      <Button label="Reintentar" icon="pi pi-refresh" class="align-self-start" @click="load" />
    </div>
  </Message>
  <PublicContentDetail v-else-if="item" :item="item" kind-label="Aprendizaje buscado" />
</template>
