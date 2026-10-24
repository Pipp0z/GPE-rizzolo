<script setup lang="ts">
const open = ref(false)
const scrolled = ref(false)
const progress = ref(0)

function onScroll() {
  const max = document.documentElement.scrollHeight - window.innerHeight
  progress.value = max > 0 ? (window.scrollY / max) * 100 : 0
  scrolled.value = window.scrollY > 10
}

onMounted(() => {
  window.addEventListener('scroll', onScroll, { passive: true })
  onScroll()
})
onBeforeUnmount(() => window.removeEventListener('scroll', onScroll))
</script>

<template>
  <div>
    <div class="fixed left-0 top-0 z-50 h-[3px] bg-brand shadow-[0_0_12px_#e8752470]" :style="{ width: `${progress}%` }" />

    <div class="flex justify-center gap-4 bg-ink px-[5.5%] py-2.5 text-center text-[9px] uppercase tracking-[.12em] text-[#fff2e8] sm:justify-between sm:text-[11px]">
      <span>Produzione di profili in legno dal {{ company.since }}</span>
      <span class="hidden text-[#ffb276] sm:inline">Competenza artigianale · Precisione industriale</span>
    </div>

    <header
      class="sticky top-0 z-40 flex h-[72px] items-center justify-between border-b border-line px-[5.5%] transition sm:h-[86px]"
      :class="scrolled ? 'bg-paper/90 shadow-[0_8px_30px_#211d1910] backdrop-blur-md' : 'bg-paper'"
    >
      <a href="#home" aria-label="G.P.E. Rizzolo - Home">
        <img :src="images.logo" alt="G.P.E. Rizzolo" width="900" height="257" class="h-9 w-auto sm:h-11">
      </a>

      <nav
        class="absolute inset-x-0 top-[72px] flex-col items-stretch gap-1 border-b border-line bg-paper px-[5.5%] py-5 text-[13px] font-semibold md:static md:flex md:flex-row md:items-center md:gap-7 md:border-0 md:bg-transparent md:p-0"
        :class="open ? 'flex' : 'hidden md:flex'"
      >
        <a
          v-for="link in navLinks"
          :key="link.href"
          :href="link.href"
          class="py-2 transition hover:text-brand md:py-0"
          @click="open = false"
        >{{ link.label }}</a>
        <a href="#contatti" class="btn" @click="open = false">Parliamo del tuo progetto ↗</a>
      </nav>

      <button
        class="text-2xl md:hidden"
        :aria-label="open ? 'Chiudi menu' : 'Apri menu'"
        :aria-expanded="open"
        @click="open = !open"
      >{{ open ? '✕' : '☰' }}</button>
    </header>
  </div>
</template>
