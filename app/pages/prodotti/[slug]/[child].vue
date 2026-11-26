<script setup lang="ts">
const route = useRoute()
const { t } = useI18n()
const { familyBySlug, specSheet, steps, faq } = useContent()

const family = computed(() => familyBySlug(String(route.params.slug)))
const child = computed(() => family.value?.children?.find(c => c.slug === String(route.params.child)))

if (!family.value || !child.value) {
  throw createError({ statusCode: 404, statusMessage: t('prod.notFound'), fatal: true })
}

const siblings = computed(() => (family.value?.children ?? []).filter(c => c.slug !== child.value?.slug))

watchEffect(() => {
  const f = family.value
  const c = child.value
  if (!f || !c) return
  const path = `/prodotti/${f.slug}/${c.slug}`
  usePageSeo({
    title: c.seoTitle,
    description: c.seoDescription,
    path,
    image: c.image,
    jsonLd: [
      breadcrumbLd([
        { name: t('crumb.home'), path: '/' },
        { name: t('nav.products'), path: '/prodotti' },
        { name: f.name, path: `/prodotti/${f.slug}` },
        { name: c.name, path },
      ]),
      faqLd(faq(c.name)),
    ],
  })
})
</script>

<template>
  <div v-if="family && child">
    <PageHeader
      :title="child.seoTitle"
      :intro="child.text"
      :crumbs="[{ name: $t('nav.products'), to: '/prodotti' }, { name: family.name, to: `/prodotti/${family.slug}` }, { name: child.name }]"
      shape="angolare"
    />

    <section class="section-pad bg-paper">
      <div class="wrap grid gap-12 lg:grid-cols-12 lg:gap-10">
        <div class="lg:col-span-7">
          <div class="border-2 border-ink bg-cream">
            <NuxtImg format="webp" :src="child.image" :alt="$t('prod.alt', { name: child.name })" width="1400" height="933" fetchpriority="high" class="photo-ink aspect-[3/2] w-full object-cover" />
          </div>
        </div>

        <div class="lg:col-span-5">
          <div class="space-y-4 text-[17px] leading-[1.75]">
            <p v-for="p in child.body" :key="p">{{ p }}</p>
          </div>

          <SpecSheet class="mt-10" :rows="specSheet()" />

          <h2 class="display mt-10 text-[32px]">{{ $t('prod.uses') }}</h2>
          <ul class="mt-3 grid gap-2 text-[16px]">
            <li v-for="u in child.uses" :key="u" class="flex gap-3"><span class="font-mono text-brand-ink">→</span>{{ u }}</li>
          </ul>

          <div class="mt-10 flex flex-wrap gap-3">
            <NuxtLinkLocale :to="{ path: '/contatti', query: { prodotto: family.slug, dettaglio: child.name } }" class="btn">{{ $t('cta.btn') }}</NuxtLinkLocale>
            <a :href="company.phoneHref" class="btn btn-secondary">☎ {{ company.phone }}</a>
          </div>
        </div>
      </div>
    </section>

    <section v-if="siblings.length" class="section-pad bg-sand">
      <div class="wrap">
        <h2 class="display text-[clamp(2.4rem,5vw,4rem)]">{{ $t('prod.sibling', { name: family.name }) }}</h2>
        <ul class="mt-8 grid gap-5 sm:grid-cols-3">
          <li v-for="c in siblings" :key="c.slug">
            <NuxtLinkLocale :to="`/prodotti/${family.slug}/${c.slug}`" class="group block border-2 border-ink bg-paper">
              <NuxtImg format="webp" :src="c.image" :alt="c.name" width="500" height="333" loading="lazy" class="photo-ink aspect-[3/2] w-full object-cover" />
              <span class="display block border-t-2 border-ink p-4 text-[28px] transition group-hover:bg-brand">{{ c.name }}</span>
            </NuxtLinkLocale>
          </li>
        </ul>
        <p class="mt-8"><NuxtLinkLocale :to="`/prodotti/${family.slug}`" class="font-mono text-[13px] font-medium uppercase tracking-[.1em] text-brand-ink underline underline-offset-4">{{ $t('prod.back', { name: family.name }) }}</NuxtLinkLocale></p>
      </div>
    </section>

    <section class="section-pad bg-brand text-ink">
      <div class="wrap grid items-start gap-10 lg:grid-cols-12">
        <h2 class="display text-[clamp(2.4rem,5vw,4rem)] !text-ink lg:col-span-4">{{ $t('prod.how') }}</h2>
        <ol class="grid gap-0 sm:grid-cols-3 lg:col-span-8">
          <li v-for="s in steps" :key="s.n" class="border-t-2 border-ink py-5 sm:pr-6">
            <span class="display text-[44px]">{{ s.n }}</span>
            <h3 class="display text-[26px] !text-ink">{{ s.title }}</h3>
            <p class="mt-1 text-[15px]">{{ s.text }}</p>
          </li>
        </ol>
      </div>
    </section>

    <ProductFaq :items="faq(child.name)" />
    <HomeContactCta />
  </div>
</template>
