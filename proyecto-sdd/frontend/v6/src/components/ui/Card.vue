<script setup>
import { cn } from '../../utils/cn'

defineProps({
  class: { type: String, default: '' }
})
</script>

<template>
  <div :class="cn('rounded-xl border border-border bg-card text-card-foreground shadow-sm transition-all', $props.class)">
    <slot />
  </div>
</template>
