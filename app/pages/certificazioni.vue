<script setup lang="ts">
usePageSeo({
  title: 'Certificazioni FSC® e ISO 14001',
  description: 'G.P.E. Rizzolo è certificata FSC® (C184281) e ISO 14001:2015 (UKAS). Prodotti in legno certificati FSC® disponibili su richiesta.',
  path: '/certificazioni',
  jsonLd: [breadcrumbLd([{ name: 'Home', path: '/' }, { name: 'Certificazioni', path: '/certificazioni' }])],
})
</script>

<template>
  <div>
    <PageHeader title="Certificazioni" :crumbs="[{ name: 'Certificazioni' }]" />
    <HomeCertifications />
    <HomeContactCta />
  </div>
</template>
