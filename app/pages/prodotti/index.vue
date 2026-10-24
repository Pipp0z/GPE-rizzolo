<script setup lang="ts">
usePageSeo({
  title: 'Profili in legno: tutti i prodotti',
  description: 'Profili per quadri, battiscopa, boiserie, serramenti, fermavetri, angolari, corrimano, masselli, perlinati, frangisole, tondi e doghe: produzione su misura G.P.E. Rizzolo.',
  path: '/prodotti',
  jsonLd: [breadcrumbLd([{ name: 'Home', path: '/' }, { name: 'Prodotti', path: '/prodotti' }])],
})
</script>

<template>
  <div>
    <PageHeader
      title="I nostri profili in legno"
      intro="La profilatura in asta è la nostra attività principale. Lavoriamo qualsiasi essenza di legno, in serie o su disegno."
      :crumbs="[{ name: 'Prodotti' }]"
      shape="battiscopa"
    />
    <section class="section-pad bg-paper">
      <ul class="wrap grid gap-x-5 gap-y-10 sm:grid-cols-2 lg:grid-cols-3">
        <li v-for="(f, i) in families" :key="f.slug">
          <NuxtLink :to="`/prodotti/${f.slug}`" class="group block">
            <div class="relative overflow-hidden border-2 border-ink bg-cream">
              <NuxtImg format="webp" :src="f.image" :alt="`${f.name} in legno - G.P.E. Rizzolo`" width="700" height="467" loading="lazy" class="photo-ink aspect-[3/2] w-full object-cover transition duration-500 group-hover:scale-105" />
              <span class="absolute left-0 top-0 bg-ink px-2.5 py-1 font-mono text-[12px] text-white">{{ String(i + 1).padStart(2, '0') }}</span>
              <span class="absolute bottom-0 right-0 grid size-11 place-items-center bg-brand font-mono text-lg text-ink transition group-hover:bg-ink group-hover:text-white">→</span>
            </div>
            <h2 class="display mt-4 text-[34px] transition group-hover:text-brand-ink">{{ f.name }}</h2>
            <p class="mt-1.5 text-[15px] leading-relaxed text-muted">{{ f.intro }}</p>
          </NuxtLink>
        </li>
      </ul>
      <p class="wrap mt-14 border-t-2 border-ink pt-5 text-[15px] text-muted">
        Produciamo anche: {{ otherProducts.join(', ').toLowerCase() }}.
        <NuxtLink to="/contatti" class="font-bold text-brand-ink underline underline-offset-4">Contattaci</NuxtLink> per la tua richiesta.
      </p>
    </section>
    <HomeContactCta />
  </div>
</template>
