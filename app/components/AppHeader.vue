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
    <div class="fixed left-0 top-0 z-50 h-[3px] bg-brand" :style="{ width: `${progress}%` }" />

    <div class="flex justify-between gap-4 bg-ink px-[5.5%] py-2 font-mono text-[11px] uppercase tracking-[.12em] text-white/70">
      <span class="hidden sm:inline">{{ company.address.city }} ({{ company.address.province }}) · Dal {{ company.since }}</span>
      <span class="sm:hidden">Profili in legno dal {{ company.since }}</span>
      <a :href="company.phoneHref" class="font-medium text-brand hover:text-white">{{ company.phone }}</a>
    </div>

    <header
      class="sticky top-0 z-40 flex h-[68px] items-center justify-between border-b px-[5.5%] transition md:h-[80px]"
      :class="scrolled ? 'border-line bg-paper/90 backdrop-blur-md' : 'border-line bg-paper'"
    >
      <NuxtLink to="/" aria-label="G.P.E. Rizzolo - Home">
        <NuxtImg format="png" :src="images.logo" alt="G.P.E. Rizzolo" width="900" height="257" class="h-10 w-auto md:h-[50px]" />
      </NuxtLink>

      <nav
        class="absolute inset-x-0 top-[68px] flex-col items-stretch gap-0 border-b border-line bg-paper px-[5.5%] py-3 md:static md:flex md:flex-row md:items-center md:gap-8 md:border-0 md:bg-transparent md:p-0"
        :class="open ? 'flex' : 'hidden md:flex'"
      >
        <NuxtLink
          v-for="link in navLinks"
          :key="link.href"
          :to="link.href"
          class="border-b border-line py-3.5 font-mono text-[13px] font-medium uppercase tracking-[.1em] text-ink transition hover:text-brand-ink md:border-0 md:py-0"
          :exact-active-class="link.href.includes('#') ? '' : '!text-brand-ink'"
          @click="open = false"
        >{{ link.label }}</NuxtLink>
        <NuxtLink to="/contatti" class="btn mt-3 !py-2.5 md:mt-0" @click="open = false">Preventivo <span>→</span></NuxtLink>
      </nav>

      <button
        class="grid size-11 place-items-center border-2 border-ink md:hidden"
        :aria-label="open ? 'Chiudi menu' : 'Apri menu'"
        :aria-expanded="open"
        @click="open = !open"
      >
        <span class="font-mono text-lg leading-none">{{ open ? '✕' : '☰' }}</span>
      </button>
    </header>
  </div>
</template>
