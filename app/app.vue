<script setup lang="ts">
const siteUrl = useRuntimeConfig().public.siteUrl as string

useHead({
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
      'description': 'Produzione di profili in legno su misura: profili per quadri, battiscopa, serramenti, corrimano, boiserie e lavorazioni speciali. Dal 1960.',
      'foundingDate': String(company.since),
      'vatID': `IT${company.vat}`,
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
    <a href="#contenuto" class="sr-only focus:not-sr-only focus:absolute focus:left-2 focus:top-2 focus:z-[70] focus:bg-white focus:p-3">Vai al contenuto</a>
    <AppHeader />
    <main id="contenuto">
      <NuxtPage />
    </main>
    <AppFooter />
    <MobileContactBar />
  </div>
</template>
