<script setup lang="ts">
const { t } = useI18n()

usePageSeo({
  title: t('seo.home.title'),
  description: t('seo.home.desc'),
  path: '/',
  home: true,
})
</script>

<template>
  <div>
    <HomeHero />
    <HomeMarquee />
    <HomeTrustBar />
    <HomeFamilies />
    <HomeMaterials />
    <HomeCustom />
    <HomeAbout />
    <HomeCertifications />
    <HomeContactCta />
  </div>
</template>
