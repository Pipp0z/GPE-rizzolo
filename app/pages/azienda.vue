<script setup lang="ts">
usePageSeo({
  title: 'L’azienda: profili in legno dal 1960',
  description: 'G.P.E. Rizzolo produce profili in legno dal 1960 a Santa Giustina in Colle (PD). Profilatura in asta in qualsiasi essenza, su disegno o campione.',
  path: '/azienda',
  jsonLd: [breadcrumbLd([{ name: 'Home', path: '/' }, { name: 'Azienda', path: '/azienda' }])],
})
</script>

<template>
  <div>
    <PageHeader title="L’azienda" :crumbs="[{ name: 'Azienda' }]" />
    <HomeAbout :show-heading="false" />
    <HomeCustom />
    <HomeContactCta />
  </div>
</template>
