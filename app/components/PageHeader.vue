<script setup lang="ts">
import type { ProfileShape } from './ProfileDrawing.vue'

defineProps<{
  title: string
  intro?: string
  crumbs?: { name: string, to?: string }[]
  shape?: ProfileShape
}>()
</script>

<template>
  <div class="blueprint-dark relative overflow-hidden border-b-4 border-brand bg-ink text-white">
    <div class="pointer-events-none absolute right-[4%] top-1/2 hidden w-[420px] -translate-y-1/2 opacity-60 md:block">
      <ProfileDrawing :shape="shape ?? 'cornice'" stroke="#ffffff" />
    </div>
    <section class="wrap relative px-[5.5%] pb-12 pt-10 md:pb-16 md:pt-14">
      <nav v-if="crumbs?.length" aria-label="Breadcrumb" class="mb-8 font-mono text-[12px] uppercase tracking-[.12em] text-white/60">
        <NuxtLink to="/" class="hover:text-brand">Home</NuxtLink>
        <template v-for="c in crumbs" :key="c.name">
          <span class="mx-2">/</span>
          <NuxtLink v-if="c.to" :to="c.to" class="hover:text-brand">{{ c.name }}</NuxtLink>
          <span v-else aria-current="page" class="text-brand">{{ c.name }}</span>
        </template>
      </nav>
      <h1 class="display max-w-[900px] text-[clamp(2.8rem,7vw,6rem)] !text-white">{{ title }}</h1>
      <p v-if="intro" class="mt-5 max-w-[600px] text-[17px] leading-[1.65] text-white/75">{{ intro }}</p>
    </section>
  </div>
</template>
