<script setup lang="ts">
const { t } = useI18n()
const items = computed(() => [
  { big: String(company.since), text: t('trust.1') },
  { big: t('trust.2v'), text: t('trust.2') },
  { big: t('trust.3v'), text: t('trust.3') },
  { big: 'FSC®', text: t('trust.4') },
])
</script>

<template>
  <div class="bg-ink text-white">
    <dl class="wrap grid grid-cols-2 lg:grid-cols-4">
      <div v-for="(item, i) in items" :key="item.text" class="flex flex-col-reverse gap-1 border-white/15 px-[5.5%] py-7 lg:px-8" :class="[i % 2 ? 'border-l' : '', i > 1 ? 'border-t lg:border-t-0' : '', i > 0 ? 'lg:border-l' : '']">
        <dt class="font-mono text-[12px] uppercase tracking-[.12em] text-white/60">{{ item.text }}</dt>
        <dd class="display text-[40px] text-brand md:text-[52px]">{{ item.big }}</dd>
      </div>
    </dl>
  </div>
</template>
