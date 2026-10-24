<script setup lang="ts">
const items = [
  { big: '60+', text: 'anni di esperienza' },
  { big: '01', text: 'partner per il tuo progetto' },
  { big: '∞', text: 'possibilità di personalizzazione' },
  { big: '✓', text: 'cura del dettaglio, sempre' },
]
</script>

<template>
  <div class="flex flex-wrap items-center justify-between gap-x-6 gap-y-4 bg-brand px-[5.5%] py-6">
    <template v-for="(item, i) in items" :key="item.text">
      <div class="flex w-[calc(50%-12px)] items-center gap-3 text-[10px] text-[#fff0e4] sm:w-auto sm:text-xs">
        <b class="font-serif text-[26px] font-normal text-brand-soft">{{ item.big }}</b>
        <span>{{ item.text }}</span>
      </div>
      <div v-if="i < items.length - 1" class="hidden h-7 w-px bg-white/25 sm:block" />
    </template>
  </div>
</template>
