<script setup>
import { useRouter } from 'vue-router'
import Card from 'primevue/card'
import Tag from 'primevue/tag'
import Button from 'primevue/button'
import { formatDuration, formatPublishedAt } from '../utils/publicContentFormatters'

defineProps({
  item: { type: Object, required: true },
  kindLabel: { type: String, required: true },
})

const router = useRouter()
</script>

<template>
  <div class="flex flex-column gap-4">
    <Button label="Volver a explorar" icon="pi pi-arrow-left" text class="align-self-start" @click="router.push({ name: 'explore' })" />
    <Card>
      <template #title>{{ item.title }}</template>
      <template #subtitle>{{ kindLabel }} · Publicado el {{ formatPublishedAt(item.publishedAt) }}</template>
      <template #content>
        <div class="flex flex-wrap gap-2 mb-4">
          <Tag :value="item.category" />
          <Tag :value="item.level" severity="secondary" />
          <Tag :value="item.modality" severity="info" />
        </div>
        <p class="line-height-3 text-lg">{{ item.description }}</p>
        <div class="grid mt-4">
          <div class="col-12 md:col-6">
            <Card>
              <template #title><span class="text-base">Duración</span></template>
              <template #content><i class="pi pi-clock mr-2" aria-hidden="true" />{{ formatDuration(item.durationMinutes) }}</template>
            </Card>
          </div>
          <div class="col-12 md:col-6">
            <Card>
              <template #title><span class="text-base">Publicado por</span></template>
              <template #content><i class="pi pi-user mr-2" aria-hidden="true" />{{ item.authorDisplayName }}</template>
            </Card>
          </div>
        </div>
      </template>
    </Card>
  </div>
</template>
