<script setup>
import { X } from '@lucide/vue'
import { cn } from '../../utils/cn'

const props = defineProps({
  open: { type: Boolean, default: false },
  title: { type: String, default: '' },
  description: { type: String, default: '' },
  class: { type: String, default: '' }
})

const emit = defineEmits(['update:open', 'close'])

function close() {
  emit('update:open', false)
  emit('close')
}
</script>

<template>
  <Teleport to="body">
    <div
      v-if="open"
      class="fixed inset-0 z-50 flex items-center justify-center p-4 bg-black/50 backdrop-blur-sm animate-in fade-in duration-200"
      @click.self="close"
    >
      <div
        :class="cn(
          'relative w-full max-w-lg rounded-2xl border border-border bg-card p-6 text-card-foreground shadow-2xl animate-in zoom-in-95 duration-200',
          $props.class
        )"
      >
        <button
          type="button"
          class="absolute right-4 top-4 rounded-sm opacity-70 transition-opacity hover:opacity-100 focus:outline-none cursor-pointer border-none bg-transparent text-muted-foreground hover:text-foreground"
          @click="close"
        >
          <X class="h-4 w-4" />
          <span class="sr-only">Cerrar</span>
        </button>

        <div v-if="title || description" class="flex flex-col space-y-1.5 text-left mb-4">
          <h2 v-if="title" class="text-lg font-semibold leading-none tracking-tight text-foreground">
            {{ title }}
          </h2>
          <p v-if="description" class="text-xs text-muted-foreground">
            {{ description }}
          </p>
        </div>

        <slot />
      </div>
    </div>
  </Teleport>
</template>
