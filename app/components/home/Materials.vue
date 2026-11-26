<script setup lang="ts">
const { essences } = useContent()
</script>

<template>
  <section id="materia" class="section-pad overflow-hidden bg-sand">
    <div class="wrap grid items-center gap-12 lg:grid-cols-12 lg:gap-8">
      <div v-reveal class="lg:col-span-5">
        <p class="kicker"><b>03</b> {{ $t('mat.kicker') }}</p>
        <h2 class="display mt-5 text-[clamp(3rem,7vw,6rem)]">{{ $t('mat.t1') }}<br>{{ $t('mat.t2') }}</h2>
        <p class="mt-6 max-w-[460px] text-[17px] leading-[1.7]">{{ $t('mat.p') }}</p>

        <ol class="mt-8 border-t-2 border-ink">
          <li v-for="(e, i) in essences" :key="e" class="flex items-baseline gap-4 border-b border-line py-2.5">
            <span class="w-7 font-mono text-[12px] text-brand-ink">{{ String(i + 1).padStart(2, '0') }}</span>
            <span class="display text-[26px] text-ink">{{ e }}</span>
          </li>
        </ol>
        <p class="mt-3 font-mono text-[12px] uppercase tracking-[.1em] text-muted">{{ $t('mat.note') }}</p>
      </div>

      <div v-reveal class="relative lg:col-span-7">
        <div class="absolute -right-3 top-6 h-full w-full border-2 border-ink" />
        <div class="relative bg-paper">
          <NuxtImg format="webp" :src="images.essenze" :alt="$t('mat.alt')" width="1600" height="1132" loading="lazy" class="photo-ink w-full" />
        </div>
      </div>
    </div>
  </section>
</template>
