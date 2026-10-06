<script setup>
import { computed } from 'vue'
import { useRouter } from 'vue-router'
import Card from 'primevue/card'
import Tag from 'primevue/tag'
import Button from 'primevue/button'
import { formatDuration, formatPublishedAt } from '../utils/publicContentFormatters'

const props = defineProps({
  item: { type: Object, required: true },
  type: { type: String, required: true, validator: (value) => ['offer', 'learning-need'].includes(value) },
})

const router = useRouter()
const isOffer = computed(() => props.type === 'offer')
const kindLabel = computed(() => (isOffer.value ? 'Propuesta para aprender' : 'Aprendizaje buscado'))

function openDetail() {
  router.push(isOffer.value
    ? { name: 'public-offer-detail', params: { offerId: props.item.id } }
    : { name: 'public-learning-need-detail', params: { learningNeedId: props.item.id } })
}
</script>

<template>
  <Card class="h-full border-1 surface-border shadow-1">
    <template #title><span class="text-xl line-height-2">{{ item.title }}</span></template>
    <template #subtitle>{{ kindLabel }} · {{ item.authorDisplayName }}</template>
    <template #content>
      <p class="line-height-3 mt-0">{{ item.description }}</p>
      <div class="flex flex-wrap gap-2 mb-3">
        <Tag :value="item.category" />
        <Tag :value="item.level" severity="secondary" />
        <Tag :value="item.modality" severity="info" />
      </div>
      <div class="flex flex-column gap-2 text-sm text-color-secondary">
        <span><i class="pi pi-clock mr-2" aria-hidden="true" />{{ formatDuration(item.durationMinutes) }}</span>
        <span><i class="pi pi-calendar mr-2" aria-hidden="true" />Publicado el {{ formatPublishedAt(item.publishedAt) }}</span>
      </div>
    </template>
    <template #footer>
      <Button label="Ver detalle" icon="pi pi-arrow-right" icon-pos="right" outlined class="w-full" @click="openDetail" />
    </template>
  </Card>
</template>
