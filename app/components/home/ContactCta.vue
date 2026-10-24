<template>
  <section class="relative overflow-hidden bg-brand px-[5.5%] py-16 text-ink md:py-24">
    <div class="wrap relative grid items-end gap-10 lg:grid-cols-12">
      <div class="lg:col-span-8">
        <p class="kicker !text-ink"><b class="!bg-ink !text-white">→</b> Il prossimo passo</p>
        <h2 class="display mt-5 text-[clamp(2.8rem,7.4vw,7rem)] !text-ink">Parliamo del tuo<br>prossimo progetto.</h2>
      </div>
      <div class="flex flex-col gap-5 lg:col-span-4">
        <p class="text-[17px] leading-relaxed">Raccontaci cosa ti serve: profilo, essenza, quantità. Ti rispondiamo il prima possibile.</p>
        <div class="flex flex-wrap gap-3">
          <NuxtLink class="btn !border-ink !bg-ink !text-white hover:!bg-white hover:!text-ink" to="/contatti">Richiedi preventivo →</NuxtLink>
          <a class="btn btn-secondary" :href="company.phoneHref">☎ {{ company.phone }}</a>
        </div>
      </div>
    </div>
  </section>
</template>
