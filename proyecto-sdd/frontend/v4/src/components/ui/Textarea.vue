<script setup>
import { cn } from '../../utils/cn'

defineProps({
  modelValue: { type: String, default: '' },
  rows: { type: [Number, String], default: 3 },
  placeholder: { type: String, default: '' },
  class: { type: String, default: '' },
  disabled: { type: Boolean, default: false }
})

defineEmits(['update:modelValue'])
</script>

<template>
  <textarea
    :rows="rows"
    :value="modelValue"
    :placeholder="placeholder"
    :disabled="disabled"
    :class="cn(
      'flex min-h-[70px] w-full rounded-lg border border-input bg-card px-3 py-2 text-sm shadow-sm placeholder:text-muted-foreground focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-ring disabled:cursor-not-allowed disabled:opacity-50 text-foreground',
      $props.class
    )"
    @input="$emit('update:modelValue', $event.target.value)"
  ></textarea>
</template>
