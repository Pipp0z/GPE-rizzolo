<script setup lang="ts">
const { t } = useI18n()
const address = `${company.address.street}, ${company.address.zip} ${company.address.city} (${company.address.province})`

usePageSeo({
  title: t('seo.privacy.title'),
  description: t('seo.privacy.desc'),
  path: '/privacy',
})
useHead({ meta: [{ name: 'robots', content: 'noindex' }] })
</script>

<template>
  <div>
    <PageHeader :title="$t('seo.privacy.title')" :crumbs="[{ name: 'Privacy' }]" />
    <section class="section-pad mx-auto max-w-[900px] space-y-5 text-[16px] leading-[1.8]">
      <!-- BOZZA: da far verificare dal titolare / consulente privacy prima della pubblicazione -->
      <p><strong class="text-ink">{{ $t('privacy.controller') }}</strong> {{ $t('privacy.controllerText', { name: company.legalName, address, vat: company.vat, email: company.email }) }}</p>
      <p><strong class="text-ink">{{ $t('privacy.data') }}</strong> {{ $t('privacy.dataText') }}</p>
      <p><strong class="text-ink">{{ $t('privacy.purpose') }}</strong> {{ $t('privacy.purposeText') }}</p>
      <p><strong class="text-ink">{{ $t('privacy.retention') }}</strong> {{ $t('privacy.retentionText') }}</p>
      <p><strong class="text-ink">{{ $t('privacy.rights') }}</strong> {{ $t('privacy.rightsText', { email: company.email }) }}</p>
      <p><strong class="text-ink">{{ $t('privacy.cookies') }}</strong> {{ $t('privacy.cookiesText') }}</p>
    </section>
  </div>
</template>
