<script setup>
import { Star } from '@lucide/vue'

const props = defineProps({
  modelValue: { type: Number, default: 5 },
  readonly: { type: Boolean, default: false },
  max: { type: Number, default: 5 }
})

const emit = defineEmits(['update:modelValue'])

function setRating(val) {
  if (!props.readonly) {
    emit('update:modelValue', val)
  }
}
</script>

<template>
  <div class="inline-flex items-center gap-1">
    <button
      v-for="star in max"
      :key="star"
      type="button"
      :disabled="readonly"
      :class="[
        'border-none bg-transparent p-0 inline-flex items-center justify-center transition-transform',
        readonly ? 'cursor-default' : 'cursor-pointer hover:scale-110'
      ]"
      @click="setRating(star)"
    >
      <Star
        :size="18"
        :class="star <= Math.round(modelValue) ? 'fill-amber-400 text-amber-400' : 'fill-slate-100 text-slate-300'"
      />
    </button>
  </div>
</template>
