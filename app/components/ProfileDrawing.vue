<script setup lang="ts">
export type ProfileShape = 'cornice' | 'battiscopa' | 'corrimano' | 'fermavetro' | 'angolare' | 'tondo'

const props = withDefaults(defineProps<{
  shape?: ProfileShape
  /** colore del tratto del profilo */
  stroke?: string
  /** colore delle quote */
  dim?: string
  label?: string
}>(), { shape: 'cornice', stroke: '#16120e', dim: '#ee7623', label: '' })

const paths: Record<ProfileShape, string> = {
  cornice: 'M14 78 V56 Q14 52 17 50 L66 14 Q72 10 78 12 L92 18 V30 H110 Q130 30 130 50 V62 H146 V78 Z',
  battiscopa: 'M12 78 V42 H40 Q52 42 52 30 Q52 18 66 18 H146 V78 Z',
  corrimano: 'M22 58 Q22 20 80 20 Q138 20 138 58 L138 64 H112 V78 H48 V64 H22 Z',
  fermavetro: 'M30 78 V26 Q30 18 38 18 H84 Q94 18 94 28 V78 Z',
  angolare: 'M26 16 H62 V56 H136 V78 H26 Z',
  tondo: 'M80 14 a32 32 0 1 0 0.01 0 Z',
}

const d = computed(() => paths[props.shape])
</script>

<template>
  <svg viewBox="0 0 160 100" fill="none" role="img" :aria-label="label || `Sezione del profilo ${shape}`" class="w-full">
    <!-- Profilo -->
    <path :d="d" pathLength="1" class="draw" :stroke="stroke" stroke-width="1.6" stroke-linejoin="round" />
    <path v-if="shape === 'tondo'" d="M80 40 V88 M56 64 H104" pathLength="1" class="draw" :stroke="dim" stroke-width=".5" stroke-dasharray="2 1.5" />
    <!-- Quote -->
    <g :stroke="dim" stroke-width=".6" fill="none">
      <path d="M12 90 H148 M12 87 V93 M148 87 V93" />
      <path d="M156 14 V78 M153 14 H159 M153 78 H159" />
    </g>
    <g :fill="dim" font-family="'JetBrains Mono', monospace" font-size="5">
      <text x="80" y="98" text-anchor="middle">A</text>
      <text x="158" y="50" text-anchor="start" dx="-2" transform="rotate(90 158 46)">B</text>
    </g>
  </svg>
</template>
