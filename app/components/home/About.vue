<script setup lang="ts">
withDefaults(defineProps<{ showHeading?: boolean }>(), { showHeading: true })

const { t } = useI18n()
const facts = computed(() => [
  { value: '3', label: t('fact.1') },
  { value: '6', label: t('fact.2') },
  { value: '1', label: t('fact.3') },
])
</script>

<template>
  <section id="azienda" class="section-pad relative overflow-hidden bg-paper">
    <div class="wrap grid gap-10 lg:grid-cols-12 lg:gap-8">
      <div v-if="showHeading" v-reveal class="lg:col-span-6">
        <p class="kicker"><b>05</b> {{ $t('about.kicker') }}</p>
        <p class="mt-4 font-mono text-[12px] uppercase tracking-[.14em] text-muted">{{ $t('about.sub') }}</p>
        <p class="display mt-4 select-none text-[clamp(8rem,22vw,20rem)] leading-[.8] text-transparent [-webkit-text-stroke:2px_#16120e]">{{ company.since }}</p>
        <p class="display mt-6 max-w-[520px] !text-ink text-[clamp(2rem,3.4vw,3rem)]">{{ $t('about.h') }}</p>
      </div>

      <div v-reveal :class="showHeading ? 'lg:col-span-6' : 'lg:col-span-9'">
        <div v-if="showHeading" class="blueprint-dark mb-10 flex items-center gap-6 border-2 border-ink bg-ink p-5 shadow-[10px_10px_0_#ee7623] md:p-7">
          <div class="w-[46%] shrink-0"><ProfileDrawing shape="angolare" stroke="#ffffff" /></div>
          <div>
            <p class="font-mono text-[11px] uppercase tracking-[.14em] text-brand">{{ $t('about.card1') }}</p>
            <p class="display mt-2 text-[clamp(1.8rem,3vw,2.6rem)] !text-white">{{ $t('about.card2a') }}<br>{{ $t('about.card2b') }}</p>
          </div>
        </div>

        <div class="space-y-5 text-[17px] leading-[1.75]">
          <i18n-t keypath="about.p1" tag="p" scope="global">
            <template #asta><strong class="text-ink">{{ $t('about.asta') }}</strong></template>
          </i18n-t>
          <p v-if="!showHeading">{{ $t('about.p2') }}</p>
          <p>{{ $t('about.p3') }}</p>
        </div>

        <NuxtLinkLocale v-if="showHeading" to="/azienda" class="btn btn-secondary mt-8">{{ $t('about.btn') }}</NuxtLinkLocale>

        <div v-else class="mt-10 border-t-2 border-ink">
          <p class="py-3 font-mono text-[12px] uppercase tracking-[.14em] text-muted">{{ $t('about.partners') }}</p>
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
