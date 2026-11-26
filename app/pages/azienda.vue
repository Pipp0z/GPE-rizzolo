<script setup lang="ts">
usePageSeo({
  title: 'L’azienda: storia, valori e obiettivi',
  description: 'G.P.E. Rizzolo produce profili in legno dal 1960 a Santa Giustina in Colle (PD). Tre generazioni di esperienza, valori e obiettivi: qualità, serietà e soddisfazione del cliente.',
  path: '/azienda',
  jsonLd: [breadcrumbLd([{ name: 'Home', path: '/' }, { name: 'Azienda', path: '/azienda' }])],
})
</script>

<template>
  <div>
    <PageHeader
      title="Tre generazioni di legno"
      intro="Nobile arte che attraversa tre generazioni: dal 1960 profili in legno di qualità, su misura."
      :crumbs="[{ name: 'Azienda' }]"
    />

    <HomeAbout :show-heading="false" />

    <!-- Storia -->
    <section id="storia" class="section-pad bg-sand">
      <div class="wrap">
        <div v-reveal>
          <p class="kicker"><b>01</b> La nostra storia</p>
          <h2 class="display mt-5 text-[clamp(3rem,7vw,6rem)]">Dal 1960,<br>di padre in figlio.</h2>
          <p class="mt-6 max-w-[620px] text-[17px] leading-[1.75]">
            Passione, esperienza, qualità, serietà, puntualità e dedizione sono i sei punti cardine tramandati da papà
            Guerrino ai figli Paolo ed Elio e oggi al nipote Samuel, su cui G.P.E. Rizzolo si fonda.
          </p>
        </div>

        <ol class="mt-14 grid gap-0 md:grid-cols-4">
          <li v-for="(h, i) in history" :key="h.label" v-reveal="i * 100" class="relative border-t-2 border-ink pb-10 pt-6 md:pr-6">
            <span class="absolute -top-[9px] left-0 size-4 bg-brand" />
            <p class="font-mono text-[12px] uppercase tracking-[.14em] text-brand-ink">{{ h.label }}</p>
            <h3 class="display mt-2 text-[34px]">{{ h.title }}</h3>
            <p class="mt-2 text-[15px] leading-relaxed text-[#3a332c]">{{ h.text }}</p>
          </li>
        </ol>
      </div>
    </section>

    <!-- Valori -->
    <section id="valori" class="section-pad bg-paper">
      <div class="wrap">
        <div v-reveal class="max-w-[760px]">
          <p class="kicker"><b>02</b> I nostri valori</p>
          <h2 class="display mt-5 text-[clamp(3rem,7vw,6rem)]">Sei punti cardine.</h2>
        </div>

        <ul class="mt-12 grid gap-0 border-t-2 border-ink sm:grid-cols-2 lg:grid-cols-3">
          <li v-for="(v, i) in values" :key="v.name" v-reveal="(i % 3) * 80" class="border-b-2 border-ink py-7 sm:pr-8 lg:[&:not(:nth-child(3n+1))]:border-l-2 lg:[&:not(:nth-child(3n+1))]:pl-8">
            <p class="font-mono text-[12px] text-brand-ink">{{ String(i + 1).padStart(2, '0') }}</p>
            <h3 class="display mt-1 text-[40px]">{{ v.name }}</h3>
            <p class="mt-2 max-w-[320px] text-[15px] leading-relaxed text-[#3a332c]">{{ v.text }}</p>
          </li>
        </ul>
      </div>
    </section>

    <!-- Obiettivi -->
    <section id="obiettivi" class="section-pad bg-brand text-ink">
      <div class="wrap">
        <div v-reveal class="max-w-[820px]">
          <p class="kicker !text-ink"><b class="!bg-ink !text-white">03</b> I nostri obiettivi</p>
          <h2 class="display mt-5 text-[clamp(3rem,8vw,7rem)] !text-ink">Guardiamo avanti,<br>senza perdere il passato.</h2>
        </div>

        <ol class="mt-14 grid gap-0 md:grid-cols-2">
          <li v-for="(g, i) in goals" :key="g.title" v-reveal="(i % 2) * 100" class="grid grid-cols-[72px_1fr] gap-4 border-t-2 border-ink py-7 md:pr-10">
            <span class="display text-[56px] text-ink">{{ String(i + 1).padStart(2, '0') }}</span>
            <div>
              <h3 class="display text-[32px] !text-ink">{{ g.title }}</h3>
              <p class="mt-2 text-[16px] leading-relaxed">{{ g.text }}</p>
            </div>
          </li>
        </ol>
      </div>
    </section>

    <!-- Brochure -->
    <section class="section-pad bg-paper">
      <div class="wrap grid items-center gap-8 lg:grid-cols-12">
        <div v-reveal class="lg:col-span-7">
          <p class="kicker"><b>04</b> Documentazione</p>
          <h2 class="display mt-5 text-[clamp(2.6rem,5vw,4.5rem)]">Scarica la nostra brochure.</h2>
          <p class="mt-4 max-w-[520px] text-[17px] leading-[1.7]">La presentazione completa di G.P.E. Rizzolo e dei suoi profili, in italiano e in inglese.</p>
        </div>
        <div v-reveal class="flex flex-wrap gap-3 lg:col-span-5 lg:justify-end">
          <a v-for="b in brochures" :key="b.href" :href="b.href" target="_blank" rel="noopener" download class="btn btn-secondary">{{ b.label }} ↓</a>
        </div>
      </div>
    </section>

    <HomeContactCta />
  </div>
</template>
