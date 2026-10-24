<template>
  <section id="home" class="relative mx-auto grid max-w-[100rem] items-center gap-9 overflow-hidden px-[5.5%] pb-12 pt-10 md:grid-cols-[.92fr_1.08fr] md:gap-[5%] md:pb-20 md:pt-12">
    <div class="pointer-events-none absolute -left-36 top-2.5 size-[360px] rounded-full border border-brand/20" />

    <div class="relative z-10">
      <div class="eyebrow">Il legno, fatto bene. Da generazioni.</div>
      <h1 class="my-6 max-w-[680px] font-serif text-[clamp(3.6rem,7vw,6.5rem)] font-normal leading-[.99] tracking-[-.055em]">
        Su misura.<br><em class="text-brand">Senza</em><br>compromessi.
      </h1>
      <p class="max-w-[440px] text-[15px] leading-[1.8] text-[#63685f]">
        Realizziamo profili in legno che danno forma alle idee. Dalla produzione standard ai pezzi speciali,
        uniamo esperienza, cura del dettaglio e flessibilità produttiva.
      </p>
      <div class="mt-7 flex flex-wrap items-center gap-3">
        <a class="btn" href="#produzione">Scopri la produzione <span>↘</span></a>
        <a class="btn btn-secondary" href="#contatti">Richiedi informazioni ↗</a>
      </div>
      <div class="mt-10 flex items-center gap-4 text-[11px] leading-normal text-muted">
        <strong class="font-serif text-2xl font-normal text-ink">{{ company.since }}</strong>
        <span>Oltre sei decenni di esperienza<br>nella lavorazione del legno</span>
      </div>
    </div>

    <div class="relative h-[410px] overflow-hidden bg-[#b86c38] shadow-[10px_10px_0_#f1dfce] sm:h-[490px] md:h-[650px] md:shadow-[24px_24px_0_#f1dfce]">
      <img src="/images/hero.jpg" alt="Blocchetti di legno massello in fila" class="size-full object-cover">
      <div class="absolute inset-0 bg-gradient-to-b from-transparent from-50% to-ink/45" />
      <div class="absolute right-0 top-0 bg-brand px-3 py-4 text-[10px] font-bold tracking-[.14em] text-white [writing-mode:vertical-rl]">
        MATERIA · PRECISIONE · ESPERIENZA
      </div>
      <div class="absolute inset-x-5 bottom-5 flex items-end justify-between text-[10px] uppercase tracking-[.12em] text-white [text-shadow:0_1px_12px_#0008]">
        <span>La qualità si vede nei dettagli</span>
        <span>01 / 03</span>
      </div>
    </div>
  </section>
</template>
