<template>
  <section id="home" class="blueprint relative overflow-hidden">
    <div class="wrap grid gap-12 px-[5.5%] pb-16 pt-10 lg:grid-cols-12 lg:gap-8 lg:pb-24 lg:pt-16">
      <div class="relative z-10 lg:col-span-7">
        <p class="kicker"><b>01</b> {{ $t('hero.kicker', { city: company.address.city, prov: company.address.province }) }}</p>

        <h1 class="display mt-6 text-[clamp(3.8rem,11vw,10rem)] !text-ink">
          {{ $t('hero.h1a') }}<br>
          <template v-if="$t('hero.h1b')">{{ $t('hero.h1b') }}<br></template>
          <span class="relative inline-block bg-brand px-3 pb-1 pt-1.5 md:px-5">{{ $t('hero.h1hl') }}</span>
        </h1>

        <div class="mt-10 grid gap-8 md:grid-cols-[1fr_auto] md:items-end">
          <i18n-t keypath="hero.p" tag="p" class="max-w-[520px] text-[18px] leading-[1.65] text-[#3a332c]" scope="global">
            <template #essence><strong class="text-ink">{{ $t('hero.essence') }}</strong></template>
            <template #year>{{ company.since }}</template>
          </i18n-t>
          <div class="flex flex-wrap gap-3">
            <NuxtLinkLocale class="btn group" to="/contatti">{{ $t('hero.cta') }} <span class="transition group-hover:translate-x-1">→</span></NuxtLinkLocale>
            <NuxtLinkLocale class="btn btn-secondary" to="/prodotti">{{ $t('hero.products') }}</NuxtLinkLocale>
          </div>
        </div>
      </div>

      <div class="relative lg:col-span-5">
        <div class="relative h-[420px] overflow-hidden bg-ink md:h-[600px]">
          <NuxtImg format="webp" src="/images/hero.jpg" :alt="$t('hero.alt')" width="1000" height="665" fetchpriority="high" loading="eager" class="size-full object-cover object-[60%_bottom] saturate-[1.2] contrast-105 sepia-[.2]" />
          <div class="absolute inset-0 bg-gradient-to-t from-ink/60 via-transparent to-brand/20 mix-blend-multiply" />
          <span class="absolute bottom-4 left-4 bg-ink px-2 py-1 font-mono text-[11px] uppercase tracking-[.12em] text-white">{{ $t('hero.fig') }}</span>
        </div>

        <!-- Scheda tecnica sovrapposta -->
        <div class="absolute -bottom-8 right-4 w-[62%] max-w-[300px] border-2 border-ink bg-paper p-4 shadow-[8px_8px_0_#ee7623] md:right-6">
          <p class="mb-1 font-mono text-[11px] uppercase tracking-[.12em] text-muted">{{ $t('hero.section') }}</p>
          <ProfileDrawing shape="cornice" />
        </div>

        <div class="absolute -left-2 -top-4 grid size-[96px] place-items-center bg-brand text-ink md:-left-6 md:size-[120px]">
          <div class="text-center">
            <div class="font-mono text-[10px] uppercase tracking-[.16em]">{{ $t('hero.since') }}</div>
            <div class="font-display text-[44px] font-extrabold leading-none md:text-[56px]">{{ company.since }}</div>
          </div>
        </div>
      </div>
    </div>
  </section>
</template>
