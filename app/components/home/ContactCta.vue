<template>
  <section class="relative overflow-hidden bg-brand px-[5.5%] py-16 text-ink md:py-24">
    <div class="wrap relative grid items-end gap-10 lg:grid-cols-12">
      <div class="lg:col-span-8">
        <p class="kicker !text-ink"><b class="!bg-ink !text-white">→</b> {{ $t('cta.kicker') }}</p>
        <h2 class="display mt-5 text-[clamp(2.8rem,7.4vw,7rem)] !text-ink">{{ $t('cta.t1') }}<br>{{ $t('cta.t2') }}</h2>
      </div>
      <div class="flex flex-col gap-5 lg:col-span-4">
        <p class="text-[17px] leading-relaxed">{{ $t('cta.p') }}</p>
        <div class="flex flex-wrap gap-3">
          <NuxtLinkLocale class="btn !border-ink !bg-ink !text-white hover:!bg-white hover:!text-ink" to="/contatti">{{ $t('cta.btn') }}</NuxtLinkLocale>
          <a class="btn btn-secondary" :href="company.phoneHref">☎ {{ company.phone }}</a>
        </div>
      </div>
    </div>
  </section>
</template>
