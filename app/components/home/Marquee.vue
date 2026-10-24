<script setup lang="ts">
const words = [...families.map(f => f.name), ...essences]
</script>

<template>
  <div class="marquee overflow-hidden border-y-2 border-ink bg-brand py-3.5" aria-hidden="true">
    <div class="marquee-track flex w-max">
      <div v-for="n in 2" :key="n" class="flex shrink-0 items-center">
        <span v-for="(w, i) in words" :key="`${n}-${w}`" class="display flex items-center whitespace-nowrap text-[30px] text-ink md:text-[38px]">
          <span class="px-5" :class="i % 2 ? 'outline-text' : ''">{{ w }}</span><span class="text-[22px]">✦</span>
        </span>
      </div>
    </div>
  </div>
</template>
