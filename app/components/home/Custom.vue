<script setup lang="ts">
const { steps } = useContent()
</script>

<template>
  <section id="su-misura" class="section-pad bg-brand text-ink">
    <div class="wrap">
      <div v-reveal class="grid items-end gap-8 lg:grid-cols-12">
        <div class="lg:col-span-8">
          <p class="kicker !text-ink"><b class="!bg-ink !text-white">04</b> {{ $t('cus.kicker') }}</p>
          <h2 class="display mt-5 text-[clamp(3rem,8.5vw,8rem)] !text-ink">{{ $t('cus.t1') }}<br>{{ $t('cus.t2') }}</h2>
        </div>
        <p class="text-[17px] leading-[1.65] lg:col-span-4">{{ $t('cus.p') }}</p>
      </div>

      <div class="mt-14 grid gap-10 lg:grid-cols-12 lg:gap-8">
        <ol class="grid gap-0 lg:col-span-7">
          <li v-for="step in steps" :key="step.n" v-reveal class="grid grid-cols-[88px_1fr] items-baseline gap-4 border-t-2 border-ink py-6 md:grid-cols-[120px_1fr]">
            <span class="display text-[64px] text-ink md:text-[88px]">{{ step.n }}</span>
            <div>
              <h3 class="display text-[30px] !text-ink md:text-[38px]">{{ step.title }}</h3>
              <p class="mt-1 text-[16px]">{{ step.text }}</p>
            </div>
          </li>
          <li class="border-t-2 border-ink pt-8">
            <NuxtLinkLocale to="/contatti" class="btn !border-ink !bg-ink !text-white hover:!bg-white hover:!text-ink">{{ $t('cus.cta') }}</NuxtLinkLocale>
          </li>
        </ol>

        <div v-reveal class="lg:col-span-5">
          <div class="relative bg-paper p-3 shadow-[10px_10px_0_#16120e]">
            <div class="blueprint relative flex aspect-[4/3] flex-col justify-between border-2 border-ink bg-cream p-5">
              <p class="font-mono text-[11px] uppercase tracking-[.12em] text-muted">{{ $t('cus.draw') }}</p>
              <ProfileDrawing shape="modanatura" class="mx-auto w-[88%]" />
              <p class="font-mono text-[11px] uppercase tracking-[.12em] text-brand-ink">{{ $t('cus.shape') }}</p>
            </div>
            <p class="mt-2 font-mono text-[11px] uppercase tracking-[.12em] text-muted">{{ $t('cus.fig') }}</p>
          </div>
        </div>
      </div>
    </div>
  </section>
</template>
