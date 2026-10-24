<template>
  <section id="certificazioni" class="bg-sand px-[5.5%] py-[70px] md:py-[90px]">
    <div v-reveal class="mx-auto grid max-w-[100rem] items-center gap-8 md:grid-cols-[1fr_1.2fr] md:gap-[8%]">
      <div>
        <div class="eyebrow">Qualità certificata</div>
        <h2 class="section-title">Legno responsabile,<br>processi controllati.</h2>
        <p class="mt-5 max-w-[420px] text-[13px] leading-[1.8] text-muted">
          Prodotti certificati FSC® disponibili su richiesta. Impegno etico e politica ambientale sono
          consultabili sul <a href="https://www.gperizzolo.it" class="font-bold text-brand hover:underline" target="_blank" rel="noopener">sito aziendale</a>.
        </p>
      </div>

      <div class="grid grid-cols-2 gap-3">
        <a
          v-for="c in certifications"
          :key="c.name"
          :href="c.image"
          target="_blank"
          rel="noopener"
          class="group border border-line bg-paper p-4 transition hover:-translate-y-1"
        >
          <img :src="c.image" :alt="c.alt" loading="lazy" class="h-52 w-full object-contain sm:h-72">
          <h3 class="mt-3 font-serif text-xl font-normal text-brand">{{ c.name }}</h3>
          <p class="mt-1 text-[11px] leading-[1.6] text-muted">{{ c.text }}</p>
        </a>
      </div>
    </div>
  </section>
</template>
