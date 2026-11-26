<script setup lang="ts">
const { t } = useI18n()

usePageSeo({
  title: t('seo.certs.title'),
  description: t('seo.certs.desc'),
  path: '/certificazioni',
  jsonLd: [breadcrumbLd([{ name: t('crumb.home'), path: '/' }, { name: t('nav.certs'), path: '/certificazioni' }])],
})
</script>

<template>
  <div>
    <PageHeader :title="$t('nav.certs')" :crumbs="[{ name: $t('nav.certs') }]" />
    <HomeCertifications />
    <HomeContactCta />
  </div>
</template>
