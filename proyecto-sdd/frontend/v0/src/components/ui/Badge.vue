<script setup>
import { cn } from '../../utils/cn'
defineProps({ variant: { type: String, default: 'default' }, class: { type: [String, Array, Object], default: '' } })
</script>

<template>
  <span :class="cn('inline-flex items-center rounded-full border px-2.5 py-0.5 text-xs font-semibold', variant === 'default' ? 'border-transparent bg-primary text-primary-foreground' : 'bg-secondary text-secondary-foreground', $props.class)"><slot /></span>
</template>
