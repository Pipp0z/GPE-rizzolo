<template>
  <div class="fixed inset-x-0 bottom-0 z-40 grid grid-cols-2 border-t-2 border-ink bg-paper md:hidden">
    <a :href="company.phoneHref" class="py-3.5 text-center font-mono text-[13px] font-medium uppercase tracking-[.08em] text-ink">☎ Chiama</a>
    <NuxtLink to="/contatti" class="bg-brand py-3.5 text-center font-mono text-[13px] font-medium uppercase tracking-[.08em] text-ink">Preventivo →</NuxtLink>
  </div>
</template>
