<template>
  <section id="azienda" class="mx-auto max-w-[100rem] px-[5.5%] py-[70px] md:py-[100px]">
    <div v-reveal class="grid items-start gap-6 md:grid-cols-[.75fr_1.25fr] md:gap-[10%]">
      <div>
        <div class="eyebrow">{{ company.name }} · Dal {{ company.since }}</div>
        <p class="mt-4 font-serif text-[clamp(2.4rem,4vw,3.6rem)] leading-[1.08] tracking-[-.04em]">
          La tradizione non è restare fermi. È <em class="text-brand">sapere come andare avanti.</em>
        </p>
      </div>

      <div>
        <p class="max-w-[620px] text-sm leading-[1.9] text-muted">
          Da oltre sessant'anni il legno è il nostro mestiere. La nostra attività principale è la profilatura in asta,
          svolta con grande attenzione alla precisione e alla qualità della finitura, su qualsiasi essenza di legno:
          coprifili, fermavetri, copri alluminio, piattine, masselli per porte, angolari, zoccolini, perlinati e profili su misura.
        </p>
        <p class="mt-5 max-w-[620px] text-sm leading-[1.9] text-muted">
          L'azienda è guidata da {{ company.partners.slice(0, -1).join(', ') }} e {{ company.partners.at(-1) }}. Il nostro
          approccio è concreto: ascoltare, capire il bisogno e costruire una risposta.
        </p>

        <dl class="mt-8 flex gap-6 md:gap-11">
          <div>
            <dd class="font-serif text-[31px] font-normal text-brand md:text-[37px]">{{ company.since }}</dd>
            <dt class="text-[10px] uppercase tracking-[.09em] text-muted">Anno di fondazione</dt>
          </div>
          <div>
            <dd class="font-serif text-[31px] font-normal text-brand md:text-[37px]">Su misura</dd>
            <dt class="text-[10px] uppercase tracking-[.09em] text-muted">Il nostro standard</dt>
          </div>
          <div>
            <dd class="font-serif text-[31px] font-normal text-brand md:text-[37px]">Legno</dd>
            <dt class="text-[10px] uppercase tracking-[.09em] text-muted">La nostra materia</dt>
          </div>
        </dl>
      </div>
    </div>
  </section>
</template>
