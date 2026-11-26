<script setup lang="ts">
withDefaults(defineProps<{ showHeading?: boolean }>(), { showHeading: true })

const facts = [
  { value: '3', label: 'Generazioni in azienda' },
  { value: '6', label: 'Valori tramandati' },
  { value: '1', label: 'Obiettivo: la soddisfazione del cliente' },
]
</script>

<template>
  <section id="azienda" class="section-pad relative overflow-hidden bg-paper">
    <div class="wrap grid gap-10 lg:grid-cols-12 lg:gap-8">
      <div v-if="showHeading" v-reveal class="lg:col-span-6">
        <p class="kicker"><b>05</b> L’azienda</p>
        <p class="mt-4 font-mono text-[12px] uppercase tracking-[.14em] text-muted">Nobile arte che attraversa tre generazioni</p>
        <p class="display mt-4 select-none text-[clamp(8rem,22vw,20rem)] leading-[.8] text-transparent [-webkit-text-stroke:2px_#16120e]">{{ company.since }}</p>
        <p class="display mt-6 max-w-[520px] !text-ink text-[clamp(2rem,3.4vw,3rem)]">La tradizione non è restare fermi. È sapere come andare avanti.</p>
      </div>

      <div v-reveal :class="showHeading ? 'lg:col-span-6' : 'lg:col-span-9'">
        <div v-if="showHeading" class="blueprint-dark mb-10 flex items-center gap-6 border-2 border-ink bg-ink p-5 shadow-[10px_10px_0_#ee7623] md:p-7">
          <div class="w-[46%] shrink-0"><ProfileDrawing shape="angolare" stroke="#ffffff" /></div>
          <div>
            <p class="font-mono text-[11px] uppercase tracking-[.14em] text-brand">Il mestiere, in sezione</p>
            <p class="display mt-2 text-[clamp(1.8rem,3vw,2.6rem)] !text-white">Precisione<br>tramandata.</p>
          </div>
        </div>

        <div class="space-y-5 text-[17px] leading-[1.75]">
          <p>
            Da oltre sessant’anni il legno è il nostro mestiere. La nostra attività principale è la
            <strong class="text-ink">profilatura in asta</strong>, con grande attenzione alla precisione e alla qualità
            della finitura, su qualsiasi essenza di legno.
          </p>
          <p v-if="!showHeading">
            Produciamo coprifili, fermavetri, copri alluminio, piattine, masselli per porte, angolari, zoccolini,
            perlinati e profili su misura.
          </p>
          <p>
            Saldi alla filosofia del passato, con un occhio attento alle innovazioni tecnologiche e al futuro:
            ogni nostro prodotto ha un solo obiettivo, la soddisfazione del cliente.
          </p>
        </div>

        <NuxtLink v-if="showHeading" to="/azienda" class="btn btn-secondary mt-8">Scopri la nostra storia →</NuxtLink>

        <div v-else class="mt-10 border-t-2 border-ink">
          <p class="py-3 font-mono text-[12px] uppercase tracking-[.14em] text-muted">I soci</p>
          <ul class="grid grid-cols-2 border-t border-line sm:grid-cols-4">
            <li v-for="(n, i) in company.partners" :key="n" class="border-b border-line py-4 pr-4" :class="i ? 'sm:border-l sm:pl-4' : ''">
              <span class="display text-[34px] text-ink">{{ n }}</span>
            </li>
          </ul>
        </div>
      </div>
    </div>

    <dl v-if="showHeading" class="wrap mt-16 grid border-2 border-ink bg-cream sm:grid-cols-3">
      <div v-for="(f, i) in facts" :key="f.label" v-reveal="i * 100" class="group flex flex-col-reverse gap-1 p-6 transition hover:bg-brand md:p-8" :class="i ? 'border-t-2 border-ink sm:border-l-2 sm:border-t-0' : ''">
        <dt class="font-mono text-[12px] uppercase tracking-[.12em] text-muted transition group-hover:text-ink">{{ f.label }}</dt>
        <dd class="display text-[clamp(3rem,6vw,5rem)] text-ink">{{ f.value }}</dd>
      </div>
    </dl>
  </section>
</template>
