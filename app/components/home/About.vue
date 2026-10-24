<script setup lang="ts">
withDefaults(defineProps<{ showHeading?: boolean }>(), { showHeading: true })
</script>

<template>
  <section id="azienda" class="section-pad relative overflow-hidden bg-paper">
    <div class="wrap grid gap-10 lg:grid-cols-12 lg:gap-8">
      <div v-if="showHeading" v-reveal class="lg:col-span-6">
        <p class="kicker"><b>05</b> L’azienda</p>
        <p class="display mt-4 select-none text-[clamp(8rem,22vw,20rem)] leading-[.8] text-transparent [-webkit-text-stroke:2px_#16120e]">{{ company.since }}</p>
        <p class="display mt-6 max-w-[520px] !text-ink text-[clamp(2rem,3.4vw,3rem)]">La tradizione non è restare fermi. È sapere come andare avanti.</p>
      </div>

      <div v-reveal :class="showHeading ? 'lg:col-span-6' : 'lg:col-span-9'">
        <div class="space-y-5 text-[17px] leading-[1.75]">
          <p>
            Da oltre sessant’anni il legno è il nostro mestiere. La nostra attività principale è la
            <strong class="text-ink">profilatura in asta</strong>, svolta con grande attenzione alla precisione e alla qualità
            della finitura, su qualsiasi essenza di legno.
          </p>
          <p>
            Produciamo coprifili, fermavetri, copri alluminio, piattine, masselli per porte, angolari, zoccolini,
            perlinati e profili su misura.
          </p>
        </div>

        <div class="mt-10 border-t-2 border-ink">
          <p class="py-3 font-mono text-[12px] uppercase tracking-[.14em] text-muted">I soci</p>
          <ul class="grid grid-cols-2 border-t border-line sm:grid-cols-4">
            <li v-for="(n, i) in company.partners" :key="n" class="border-b border-line py-4 pr-4" :class="i ? 'sm:border-l sm:pl-4' : ''">
              <span class="display text-[34px] text-ink">{{ n }}</span>
            </li>
          </ul>
        </div>
      </div>
    </div>
  </section>
</template>
