<script setup>
import { computed } from 'vue'
import { useRouter } from 'vue-router'
import { ArrowRight, CalendarDays, Clock3 } from '@lucide/vue'
import UiBadge from './ui/Badge.vue'
import UiButton from './ui/Button.vue'
import UiCard from './ui/Card.vue'
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
  <UiCard class="group flex h-full flex-col overflow-hidden transition duration-200 hover:-translate-y-1 hover:shadow-lg">
    <div class="flex flex-1 flex-col p-6">
      <div class="mb-4 flex items-start justify-between gap-3">
        <UiBadge variant="secondary">{{ kindLabel }}</UiBadge>
        <span class="text-xs text-muted-foreground">{{ item.authorDisplayName }}</span>
      </div>
      <h3 class="text-xl font-bold leading-snug tracking-tight">{{ item.title }}</h3>
      <p class="mt-3 flex-1 text-sm leading-6 text-muted-foreground">{{ item.description }}</p>
      <div class="mt-4 flex flex-wrap gap-2">
        <UiBadge>{{ item.category }}</UiBadge>
        <UiBadge variant="secondary">{{ item.level }}</UiBadge>
        <UiBadge variant="secondary">{{ item.modality }}</UiBadge>
      </div>
      <div class="mt-5 grid gap-2 border-t pt-4 text-xs text-muted-foreground">
        <span class="flex items-center gap-2"><Clock3 :size="14" />{{ formatDuration(item.durationMinutes) }}</span>
        <span class="flex items-center gap-2"><CalendarDays :size="14" />Publicado el {{ formatPublishedAt(item.publishedAt) }}</span>
      </div>
    </div>
    <div class="px-6 pb-6">
      <UiButton variant="outline" class="w-full group-hover:border-primary group-hover:text-primary" @click="openDetail">Ver detalle<ArrowRight :size="16" /></UiButton>
    </div>
  </UiCard>
</template>
