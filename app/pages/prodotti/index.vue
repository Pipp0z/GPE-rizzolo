<script setup lang="ts">
const { t } = useI18n()
const { families, otherProducts, localePath } = useContent()

usePageSeo({
  title: t('seo.prods.title'),
  description: t('seo.prods.desc'),
  path: '/prodotti',
  jsonLd: [
    breadcrumbLd([{ name: t('crumb.home'), path: '/' }, { name: t('nav.products'), path: '/prodotti' }]),
    {
      '@type': 'ItemList',
      'itemListElement': families.value.map((f, i) => ({
        '@type': 'ListItem',
        'position': i + 1,
        'name': f.name,
        'url': `${useRuntimeConfig().public.siteUrl}${localePath(`/prodotti/${f.slug}`)}`,
      })),
    },
  ],
})
</script>

<template>
  <div>
    <PageHeader
      :title="$t('prods.title')"
      :intro="$t('prods.intro')"
      :crumbs="[{ name: $t('nav.products') }]"
      shape="battiscopa"
    />
    <section class="section-pad bg-paper">
      <ul class="wrap grid gap-x-5 gap-y-10 sm:grid-cols-2 lg:grid-cols-3">
        <li v-for="(f, i) in families" :key="f.slug">
          <NuxtLinkLocale :to="`/prodotti/${f.slug}`" class="group block">
            <div class="relative overflow-hidden border-2 border-ink bg-cream">
              <NuxtImg format="webp" :src="f.image" :alt="$t('prod.alt', { name: f.name })" width="700" height="467" loading="lazy" class="photo-ink aspect-[3/2] w-full object-cover transition duration-500 group-hover:scale-105" />
              <span class="absolute left-0 top-0 bg-ink px-2.5 py-1 font-mono text-[12px] text-white">{{ String(i + 1).padStart(2, '0') }}</span>
              <span class="absolute bottom-0 right-0 grid size-11 place-items-center bg-brand font-mono text-lg text-ink transition group-hover:bg-ink group-hover:text-white">→</span>
            </div>
            <h2 class="display mt-4 text-[34px] transition group-hover:text-brand-ink">{{ f.name }}</h2>
            <p class="mt-1.5 text-[15px] leading-relaxed text-muted">{{ f.intro }}</p>
          </NuxtLinkLocale>
        </li>
      </ul>
      <i18n-t keypath="prods.also" tag="p" class="wrap mt-14 border-t-2 border-ink pt-5 text-[15px] text-muted" scope="global">
        <template #list>{{ otherProducts.join(', ').toLowerCase() }}</template>
        <template #link><NuxtLinkLocale to="/contatti" class="font-bold text-brand-ink underline underline-offset-4">{{ $t('prods.contact') }}</NuxtLinkLocale></template>
      </i18n-t>
    </section>
    <HomeContactCta />
  </div>
</template>
