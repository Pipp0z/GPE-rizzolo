<script setup lang="ts">
withDefaults(defineProps<{ dark?: boolean }>(), { dark: false })

const { locale, locales } = useI18n()
const switchLocalePath = useSwitchLocalePath()
const available = computed(() => locales.value.map(l => (typeof l === 'string' ? { code: l, language: l } : l)))
</script>

<template>
  <ul class="flex items-center gap-1 font-mono text-[12px] font-medium uppercase tracking-[.1em]" :aria-label="$t('nav.lang')">
    <li v-for="l in available" :key="l.code">
      <NuxtLink
        :to="switchLocalePath(l.code)"
        :hreflang="l.language"
        :lang="l.code"
        class="px-2 py-1 transition"
        :class="[
          l.code === locale ? 'bg-brand text-ink' : (dark ? 'text-white/70 hover:text-white' : 'text-ink hover:text-brand-ink'),
        ]"
        :aria-current="l.code === locale ? 'true' : undefined"
      >{{ l.code }}</NuxtLink>
    </li>
  </ul>
</template>
