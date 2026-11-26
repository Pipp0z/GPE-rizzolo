<script setup lang="ts">
const { t } = useI18n()
const siteUrl = useRuntimeConfig().public.siteUrl as string

// html lang/dir, hreflang e canonical per ogni lingua
const i18nHead = useLocaleHead({ dir: true, seo: true })

useHead({
  htmlAttrs: { lang: i18nHead.value.htmlAttrs?.lang },
  link: [...(i18nHead.value.link ?? [])],
  meta: [...(i18nHead.value.meta ?? [])],
  script: [{
    type: 'application/ld+json',
    innerHTML: JSON.stringify({
      '@context': 'https://schema.org',
      '@type': ['Organization', 'LocalBusiness'],
      '@id': `${siteUrl}/#organization`,
      'name': company.legalName,
      'alternateName': company.name,
      'url': siteUrl,
      'logo': `${siteUrl}${images.logo}`,
      'image': `${siteUrl}${images.hero}`,
      'description': t('seo.home.desc'),
      'foundingDate': String(company.since),
      'vatID': `IT${company.vat}`,
      'sameAs': socials.map(s => s.href),
      'telephone': company.phone,
      'email': company.email,
      'address': {
        '@type': 'PostalAddress',
        'streetAddress': company.address.street,
        'postalCode': company.address.zip,
        'addressLocality': company.address.city,
        'addressRegion': company.address.province,
        'addressCountry': 'IT',
      },
    }),
  }],
})
</script>

<template>
  <div class="pb-[52px] md:pb-0">
    <NuxtRouteAnnouncer />
    <a href="#contenuto" class="sr-only focus:not-sr-only focus:absolute focus:left-2 focus:top-2 focus:z-[70] focus:bg-white focus:p-3">{{ $t('nav.skip') }}</a>
    <AppHeader />
    <main id="contenuto">
      <NuxtPage />
    </main>
    <AppFooter />
    <MobileContactBar />
  </div>
</template>
