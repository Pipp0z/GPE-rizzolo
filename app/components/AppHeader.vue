<script setup lang="ts">
const { nav } = useContent()

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

    <div class="flex items-center justify-between gap-4 bg-ink px-[5.5%] py-1.5 font-mono text-[11px] uppercase tracking-[.12em] text-white/70">
      <span class="hidden sm:inline">{{ $t('top.loc', { city: company.address.city, prov: company.address.province, year: company.since }) }}</span>
      <span class="sm:hidden">{{ $t('top.short', { year: company.since }) }}</span>
      <div class="flex items-center gap-4">
        <LangSwitcher dark />
        <a :href="company.phoneHref" class="hidden font-medium text-brand hover:text-white sm:inline">{{ company.phone }}</a>
      </div>
    </div>

    <header
      class="sticky top-0 z-40 flex h-[68px] items-center justify-between border-b px-[5.5%] transition md:h-[80px]"
      :class="scrolled ? 'border-line bg-paper/90 backdrop-blur-md' : 'border-line bg-paper'"
    >
      <NuxtLinkLocale to="/" :aria-label="$t('nav.homeAria')">
        <NuxtImg format="png" :src="images.logo" alt="G.P.E. Rizzolo" width="900" height="257" class="h-10 w-auto md:h-[50px]" />
      </NuxtLinkLocale>

      <nav
        class="absolute inset-x-0 top-[68px] flex-col items-stretch gap-0 border-b border-line bg-paper px-[5.5%] py-3 md:static md:flex md:flex-row md:items-center md:gap-8 md:border-0 md:bg-transparent md:p-0"
        :class="open ? 'flex' : 'hidden md:flex'"
      >
        <NuxtLinkLocale
          v-for="link in nav"
          :key="link.href"
          :to="link.href"
          class="border-b border-line py-3.5 font-mono text-[13px] font-medium uppercase tracking-[.1em] text-ink transition hover:text-brand-ink md:border-0 md:py-0"
          :exact-active-class="link.href.includes('#') ? '' : '!text-brand-ink'"
          @click="open = false"
        >{{ link.label }}</NuxtLinkLocale>
        <NuxtLinkLocale to="/contatti" class="btn mt-3 !py-2.5 md:mt-0" @click="open = false">{{ $t('nav.quote') }} <span>→</span></NuxtLinkLocale>
      </nav>

      <button
        class="grid size-11 place-items-center border-2 border-ink md:hidden"
        :aria-label="open ? $t('nav.close') : $t('nav.open')"
        :aria-expanded="open"
        @click="open = !open"
      >
        <span class="font-mono text-lg leading-none">{{ open ? '✕' : '☰' }}</span>
      </button>
    </header>
  </div>
</template>
