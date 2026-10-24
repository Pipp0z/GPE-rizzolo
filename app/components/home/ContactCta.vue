<template>
  <section id="contatti" class="relative mx-[5.5%] mb-[60px] mt-[70px] overflow-hidden bg-ink px-[7%] py-10 text-white md:mb-[90px] md:flex md:items-center md:justify-between md:gap-8 md:px-[6%] md:py-14">
    <span class="pointer-events-none absolute -bottom-11 right-[4%] select-none font-serif text-[clamp(100px,18vw,240px)] font-bold leading-none text-white/[.03]">G.P.E.</span>

    <div class="relative">
      <div class="eyebrow !text-brand-soft">Il prossimo passo</div>
      <h2 class="my-3 font-serif text-[clamp(2.1rem,4vw,3.25rem)] font-normal leading-[1.05] tracking-[-.04em]">
        Parliamo del tuo<br>prossimo progetto.
      </h2>
      <p class="max-w-[430px] text-xs leading-[1.7] text-[#e7d6ca]">
        Hai bisogno di un profilo specifico, vuoi approfondire una lavorazione o stai cercando un partner produttivo?
        Raccontaci cosa ti serve.
      </p>
    </div>

    <div class="relative mt-5 flex flex-col gap-3 md:mt-0 md:items-end">
      <a class="btn whitespace-nowrap" :href="mailto('Richiesta informazioni - G.P.E. Rizzolo')">Contattaci via email ↗</a>
      <a class="text-xs font-semibold text-brand-soft hover:underline" :href="company.phoneHref">oppure chiama il {{ company.phone }}</a>
    </div>
  </section>
</template>
