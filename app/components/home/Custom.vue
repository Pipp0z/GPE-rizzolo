<template>
  <section id="su-misura" class="grid items-center gap-[5%] bg-cream px-[5.5%] md:grid-cols-2 md:gap-[7%]">
    <div v-reveal class="relative h-[320px] overflow-hidden shadow-[-9px_9px_0_#e87524] md:h-[560px] md:shadow-[-18px_18px_0_#e87524]">
      <img :src="images.custom" alt="Portabottiglie in rovere realizzato su misura" loading="lazy" class="size-full object-cover">
      <span class="absolute bottom-0 left-0 bg-brand px-[18px] py-3.5 text-[9px] font-bold tracking-[.15em] text-white">LAVORAZIONI SU MISURA</span>
    </div>

    <div v-reveal class="pb-[60px] pt-[45px] md:py-[65px]">
      <div class="eyebrow">La differenza è nel dettaglio</div>
      <h2 class="my-[18px] font-serif text-[clamp(2.7rem,4.8vw,4rem)] font-normal leading-[1.04] tracking-[-.05em]">
        Hai un disegno.<br><em class="text-brand">Noi gli diamo forma.</em>
      </h2>
      <p class="max-w-[450px] text-sm leading-[1.9] text-muted">
        Non tutti i progetti entrano in un catalogo. Per questo il su misura è al centro del nostro modo di lavorare:
        ascoltiamo le esigenze, valutiamo il profilo e lavoriamo per trovare la soluzione più adatta.
      </p>

      <ol class="mt-9 grid grid-cols-3 gap-3.5 md:gap-5">
        <li v-for="step in steps" :key="step.n" class="border-t-2 border-brand pt-4">
          <b class="font-serif text-2xl font-normal text-brand">{{ step.n }}</b>
          <h3 class="mb-1.5 mt-3 text-[11px] font-bold md:text-[13px]">{{ step.title }}</h3>
          <p class="text-[10px] leading-[1.6] md:text-[11px]">{{ step.text }}</p>
        </li>
      </ol>

      <a class="btn mt-8" href="#contatti">Parliamo del tuo progetto ↗</a>
    </div>
  </section>
</template>
