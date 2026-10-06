<script setup>
import { computed } from 'vue'
import { Primitive } from 'reka-ui'
import { cva } from 'class-variance-authority'
import { cn } from '../../utils/cn'

const props = defineProps({
  variant: { type: String, default: 'default' },
  size: { type: String, default: 'default' },
  as: { type: [String, Object], default: 'button' },
  class: { type: [String, Array, Object], default: '' },
})

const variants = cva('inline-flex items-center justify-center gap-2 whitespace-nowrap rounded-md text-sm font-semibold transition-colors focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-ring disabled:pointer-events-none disabled:opacity-50', {
  variants: {
    variant: {
      default: 'bg-primary text-primary-foreground shadow-sm hover:brightness-95',
      secondary: 'bg-secondary text-secondary-foreground hover:bg-accent',
      outline: 'border bg-card hover:bg-accent hover:text-accent-foreground',
      ghost: 'hover:bg-accent hover:text-accent-foreground',
      destructive: 'bg-destructive text-white hover:brightness-95',
    },
    size: {
      default: 'h-10 px-4 py-2',
      sm: 'h-9 rounded-md px-3',
      lg: 'h-11 rounded-lg px-6 text-base',
      icon: 'size-10',
    },
  },
  defaultVariants: { variant: 'default', size: 'default' },
})

const classes = computed(() => cn(variants({ variant: props.variant, size: props.size }), props.class))
</script>

<template>
  <Primitive :as="as" :class="classes"><slot /></Primitive>
</template>
