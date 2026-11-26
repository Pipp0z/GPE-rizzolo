<script setup lang="ts">
const route = useRoute()
const family = familyBySlug(String(route.params.slug))

if (!family) {
  throw createError({ statusCode: 404, statusMessage: 'Prodotto non trovato', fatal: true })
}

const openChild = ref<FamilyChild | null>(null)
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
  'profili-per-serramenti': 'fermavetro',
  'profili-di-finitura': 'angolare',
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

          <SpecSheet class="mt-10" :rows="specSheet()" />

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

    <section v-if="family.children?.length" class="section-pad bg-ink text-white">
      <div class="wrap">
        <p class="kicker !text-brand"><b>+</b> In questa categoria</p>
        <h2 class="display mt-4 text-[clamp(2.4rem,5vw,4rem)] !text-white">Cosa comprende</h2>
        <ul class="mt-10 grid gap-5 sm:grid-cols-2 lg:grid-cols-3">
          <li v-for="c in family.children" :key="c.slug">
            <button type="button" class="group block h-full w-full border-2 border-white/20 bg-ink-2 text-left transition hover:border-brand" @click="openChild = c">
              <NuxtImg format="webp" :src="c.image" :alt="`${c.name} in legno`" width="700" height="467" loading="lazy" class="aspect-[3/2] w-full object-cover" />
              <div class="p-5">
                <h3 class="display text-[30px] !text-white transition group-hover:text-brand">{{ c.name }}</h3>
                <p class="mt-2 text-[15px] leading-relaxed text-white/75">{{ c.text }}</p>
                <span class="mt-4 inline-block font-mono text-[12px] font-medium uppercase tracking-[.12em] text-brand">Apri scheda tecnica +</span>
              </div>
            </button>
          </li>
        </ul>
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
    <ChildModal :family="family" :child="openChild" @close="openChild = null" />
    <HomeContactCta />
  </div>
</template>
