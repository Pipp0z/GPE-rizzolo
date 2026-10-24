<template>
  <section id="home" class="blueprint relative overflow-hidden">
    <div class="wrap grid gap-12 px-[5.5%] pb-16 pt-10 lg:grid-cols-12 lg:gap-8 lg:pb-24 lg:pt-16">
      <div class="relative z-10 lg:col-span-7">
        <p class="kicker"><b>01</b> Produttore · {{ company.address.city }} ({{ company.address.province }})</p>

        <h1 class="display mt-6 text-[clamp(3.8rem,11vw,10rem)] !text-ink">
          Profili<br>in legno<br>
          <span class="relative inline-block bg-brand px-3 pb-1 pt-1.5 md:px-5">su misura</span>
        </h1>

        <div class="mt-10 grid gap-8 md:grid-cols-[1fr_auto] md:items-end">
          <p class="max-w-[520px] text-[18px] leading-[1.65] text-[#3a332c]">
            Profilatura in asta in <strong class="text-ink">qualsiasi essenza</strong>, dal {{ company.since }}.
            Profili per quadri, battiscopa, serramenti, corrimano e pezzi speciali: in serie o su vostro disegno.
          </p>
          <div class="flex flex-wrap gap-3">
            <NuxtLink class="btn group" to="/contatti">Richiedi preventivo <span class="transition group-hover:translate-x-1">→</span></NuxtLink>
            <NuxtLink class="btn btn-secondary" to="/prodotti">Prodotti</NuxtLink>
          </div>
        </div>
      </div>

      <div class="relative lg:col-span-5">
        <div class="relative h-[420px] overflow-hidden bg-ink md:h-[600px]">
          <NuxtImg format="webp" src="/images/hero.jpg" alt="Blocchetti di legno massello in fila" width="1000" height="665" fetchpriority="high" loading="eager" class="size-full object-cover object-[60%_bottom] saturate-[1.2] contrast-105 sepia-[.2]" />
          <div class="absolute inset-0 bg-gradient-to-t from-ink/60 via-transparent to-brand/20 mix-blend-multiply" />
          <span class="absolute bottom-4 left-4 bg-ink px-2 py-1 font-mono text-[11px] uppercase tracking-[.12em] text-white">Fig. 01 — Massello</span>
        </div>

        <!-- Scheda tecnica sovrapposta -->
        <div class="absolute -bottom-8 right-4 w-[62%] max-w-[300px] border-2 border-ink bg-paper p-4 shadow-[8px_8px_0_#ee7623] md:right-6">
          <p class="mb-1 font-mono text-[11px] uppercase tracking-[.12em] text-muted">Sezione · profilo per cornici</p>
          <ProfileDrawing shape="cornice" />
        </div>

        <div class="absolute -left-2 -top-4 grid size-[96px] place-items-center bg-brand text-ink md:-left-6 md:size-[120px]">
          <div class="text-center">
            <div class="font-mono text-[10px] uppercase tracking-[.16em]">Dal</div>
            <div class="font-display text-[44px] font-extrabold leading-none md:text-[56px]">{{ company.since }}</div>
          </div>
        </div>
      </div>
    </div>
  </section>
</template>
