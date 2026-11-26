<script setup lang="ts">
defineProps<{ items: { q: string, a: string }[] }>()
</script>

<template>
  <section class="section-pad bg-paper">
    <div class="wrap grid gap-10 lg:grid-cols-12">
      <div class="lg:col-span-4">
        <p class="kicker"><b>?</b> FAQ</p>
        <h2 class="display mt-4 text-[clamp(2.4rem,5vw,4rem)]">{{ $t('faq.title') }}</h2>
      </div>
      <div class="lg:col-span-8">
        <details v-for="(it, i) in items" :key="it.q" class="group border-t-2 border-ink py-5" :open="i === 0">
          <summary class="flex cursor-pointer list-none items-center justify-between gap-6 font-display text-[26px] font-bold uppercase leading-tight text-ink">
            {{ it.q }}
            <span class="font-mono text-2xl transition group-open:rotate-45" aria-hidden="true">+</span>
          </summary>
          <p class="mt-3 max-w-[640px] text-[16px] leading-[1.75]">{{ it.a }}</p>
        </details>
        <div class="border-t-2 border-ink" />
      </div>
    </div>
  </section>
</template>
