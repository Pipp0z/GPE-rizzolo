<script setup lang="ts">
defineProps<{ rows: SpecRow[], pdf?: string }>()
</script>

<template>
  <div>
    <h2 class="display text-[32px]">{{ $t('spec.title') }}</h2>
    <dl class="mt-3 border-t-2 border-ink font-mono text-[13px]">
      <div v-for="r in rows" :key="r.label" class="grid grid-cols-[110px_1fr] gap-4 border-b border-line py-3">
        <dt class="uppercase tracking-[.1em] text-muted">{{ r.label }}</dt>
        <dd class="text-ink">{{ r.value }}</dd>
      </div>
    </dl>
    <a v-if="pdf" :href="pdf" target="_blank" rel="noopener" download class="btn btn-secondary mt-5">{{ $t('modal.pdf') }}</a>
  </div>
</template>
