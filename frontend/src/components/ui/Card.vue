<script setup>
import { cn } from '../../utils/cn'
defineProps({ class: { type: [String, Array, Object], default: '' } })
</script>

<template>
  <div :class="cn('rounded-xl border bg-card text-card-foreground shadow-sm', $props.class)"><slot /></div>
</template>
