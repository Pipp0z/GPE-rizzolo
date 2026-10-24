<script setup lang="ts">
const route = useRoute()
const family = familyBySlug(String(route.params.slug))

if (!family) {
  throw createError({ statusCode: 404, statusMessage: 'Prodotto non trovato', fatal: true })
}

const path = `/prodotti/${family.slug}`
const related = families.filter(f => f.slug !== family.slug).slice(0, 3)

usePageSeo({
  title: family.seoTitle,
  description: family.seoDescription,
  path,
  image: family.image,
  jsonLd: [
    breadcrumbLd([
      { name: 'Home', path: '/' },
      { name: 'Prodotti', path: '/prodotti' },
      { name: family.name, path },
    ]),
  ],
})
</script>

<script lang="ts">
const SHAPES: Record<string, 'cornice' | 'battiscopa' | 'corrimano' | 'fermavetro' | 'angolare' | 'tondo'> = {
  'profili-per-quadri': 'cornice',
  'boiserie': 'cornice',
  'battiscopa': 'battiscopa',
  'corrimano': 'corrimano',
  'fermavetri': 'fermavetro',
  'profili-per-serramenti': 'fermavetro',
  'angolari': 'angolare',
  'profili-tondi': 'tondo',
}
</script>

<template>
  <div v-if="family">
    <PageHeader
      :title="family.seoTitle"
      :intro="family.intro"
      :crumbs="[{ name: 'Prodotti', to: '/prodotti' }, { name: family.name }]"
      :shape="SHAPES[family.slug] ?? 'battiscopa'"
    />

    <section class="section-pad bg-paper">
      <div class="wrap grid gap-12 lg:grid-cols-12 lg:gap-10">
        <div class="lg:col-span-7">
          <div class="border-2 border-ink bg-cream">
            <NuxtImg format="webp" :src="family.image" :alt="`${family.name} in legno - G.P.E. Rizzolo`" width="1400" height="933" fetchpriority="high" class="photo-ink aspect-[3/2] w-full object-cover" />
          </div>
          <div v-if="family.gallery" class="mt-3 grid grid-cols-3 gap-3">
            <div v-for="(g, i) in family.gallery" :key="g" class="border-2 border-ink bg-cream">
              <NuxtImg format="webp" :src="g" :alt="`${family.name}, esempio ${i + 1}`" width="500" height="333" loading="lazy" class="photo-ink aspect-[3/2] w-full object-cover" />
            </div>
          </div>
        </div>

        <div class="lg:col-span-5">
          <div class="space-y-4 text-[17px] leading-[1.75]">
            <p v-for="p in family.body" :key="p">{{ p }}</p>
          </div>

          <h2 class="display mt-10 text-[32px]">Scheda tecnica</h2>
          <dl class="mt-3 border-t-2 border-ink font-mono text-[13px]">
            <div class="grid grid-cols-[110px_1fr] gap-4 border-b border-line py-3">
              <dt class="uppercase tracking-[.1em] text-muted">Essenze</dt><dd class="text-ink">Qualsiasi essenza di legno</dd>
            </div>
            <div class="grid grid-cols-[110px_1fr] gap-4 border-b border-line py-3">
              <dt class="uppercase tracking-[.1em] text-muted">Produzione</dt><dd class="text-ink">In asta, in serie o su disegno</dd>
            </div>
            <div class="grid grid-cols-[110px_1fr] gap-4 border-b border-line py-3">
              <dt class="uppercase tracking-[.1em] text-muted">Misure</dt><dd class="text-ink">Su richiesta</dd>
            </div>
            <div class="grid grid-cols-[110px_1fr] gap-4 border-b border-line py-3">
              <dt class="uppercase tracking-[.1em] text-muted">Finiture</dt><dd class="text-ink">Su richiesta</dd>
            </div>
            <div class="grid grid-cols-[110px_1fr] gap-4 border-b border-line py-3">
              <dt class="uppercase tracking-[.1em] text-muted">Certificazione</dt><dd class="text-ink">FSC® disponibile su richiesta</dd>
            </div>
          </dl>

          <h2 class="display mt-10 text-[32px]">Applicazioni</h2>
          <ul class="mt-3 grid gap-2 text-[16px]">
            <li v-for="u in family.uses" :key="u" class="flex gap-3"><span class="font-mono text-brand-ink">→</span>{{ u }}</li>
          </ul>

          <div class="mt-10 flex flex-wrap gap-3">
            <NuxtLink :to="{ path: '/contatti', query: { prodotto: family.slug } }" class="btn">Richiedi preventivo →</NuxtLink>
            <a :href="company.phoneHref" class="btn btn-secondary">☎ {{ company.phone }}</a>
          </div>
        </div>
      </div>
    </section>

    <section class="section-pad bg-sand">
      <div class="wrap">
        <h2 class="display text-[clamp(2.4rem,5vw,4rem)]">Altri prodotti</h2>
        <ul class="mt-8 grid gap-5 sm:grid-cols-3">
          <li v-for="f in related" :key="f.slug">
            <NuxtLink :to="`/prodotti/${f.slug}`" class="group block border-2 border-ink bg-paper">
              <NuxtImg format="webp" :src="f.image" :alt="f.name" width="500" height="333" loading="lazy" class="photo-ink aspect-[3/2] w-full object-cover" />
              <span class="display block border-t-2 border-ink p-4 text-[28px] transition group-hover:bg-brand">{{ f.name }}</span>
            </NuxtLink>
          </li>
        </ul>
      </div>
    </section>
    <HomeContactCta />
  </div>
</template>
