<script setup>
import { computed } from 'vue'
import { cva } from 'class-variance-authority'
import { cn } from '../../utils/cn'

const badgeVariants = cva(
  'inline-flex items-center gap-1 rounded-full border px-2.5 py-0.5 text-xs font-semibold transition-colors',
  {
    variants: {
      variant: {
        default: 'border-transparent bg-primary text-primary-foreground',
        secondary: 'border-transparent bg-secondary text-secondary-foreground',
        destructive: 'border-red-500/30 bg-red-500/15 text-red-400 font-bold',
        outline: 'text-foreground border-border bg-card/60',
        success: 'border-emerald-500/30 bg-emerald-500/15 text-emerald-300 font-bold',
        warning: 'border-amber-500/30 bg-amber-500/15 text-amber-300 font-bold',
        info: 'border-indigo-500/30 bg-indigo-500/15 text-indigo-300 font-bold',
      },
    },
    defaultVariants: {
      variant: 'default',
    },
  }
)

const props = defineProps({
  variant: { type: String, default: 'default' },
  class: { type: String, default: '' },
})

const classes = computed(() => cn(badgeVariants({ variant: props.variant }), props.class))
</script>

<template>
  <div :class="classes">
    <slot />
  </div>
</template>
