<template>
  <section id="certificazioni" class="section-pad bg-sand">
    <div class="wrap grid items-start gap-10 lg:grid-cols-12 lg:gap-8">
      <div v-reveal class="lg:col-span-5">
        <p class="kicker"><b>06</b> Certificazioni</p>
        <h2 class="display mt-5 text-[clamp(3rem,6.5vw,5.5rem)]">Legno<br>responsabile.</h2>
        <p class="mt-6 max-w-[440px] text-[17px] leading-[1.7]">
          Prodotti certificati FSC® disponibili su richiesta. Impegno etico e politica ambientale sono consultabili sul
          <a href="https://www.gperizzolo.it" class="font-bold text-brand-ink underline underline-offset-4" target="_blank" rel="noopener">sito aziendale</a>.
        </p>
      </div>

      <div class="grid grid-cols-2 gap-4 lg:col-span-7">
        <a
          v-for="c in certifications"
          :key="c.name"
          v-reveal
          :href="c.image"
          target="_blank"
          rel="noopener"
          class="group block border-2 border-ink bg-paper p-4 transition hover:-translate-y-1 hover:shadow-[8px_8px_0_#ee7623]"
        >
          <NuxtImg format="webp" :src="c.image" :alt="c.alt" width="600" height="840" loading="lazy" class="photo-ink h-52 w-full object-contain sm:h-80" />
          <h3 class="display mt-4 text-[28px]">{{ c.name }}</h3>
          <p class="mt-1 text-[14px] leading-snug text-muted">{{ c.text }}</p>
        </a>
      </div>
    </div>
  </section>
</template>
