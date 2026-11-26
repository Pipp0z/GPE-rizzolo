<script setup lang="ts">
const { t } = useI18n()
const address = `${company.address.street}, ${company.address.zip} ${company.address.city} (${company.address.province})`

usePageSeo({
  title: t('seo.contact.title'),
  description: t('seo.contact.desc', { address, phone: company.phone }),
  path: '/contatti',
  jsonLd: [{ '@type': 'ContactPage', 'name': `${company.name} - ${t('nav.contacts')}` }, breadcrumbLd([{ name: t('crumb.home'), path: '/' }, { name: t('nav.contacts'), path: '/contatti' }])],
})

const mapQuery = encodeURIComponent(`${company.address.street}, ${company.address.zip} ${company.address.city} ${company.address.province}`)
</script>

<template>
  <div>
    <PageHeader
      :title="$t('contact.title')"
      :intro="$t('contact.intro')"
      :crumbs="[{ name: $t('nav.contacts') }]"
    />
    <section class="section-pad bg-paper">
     <div class="wrap grid gap-12 lg:grid-cols-[1.3fr_.7fr] lg:gap-16">
      <ContactForm />

      <aside class="space-y-6 border-t-2 border-ink pt-6 text-[16px] leading-relaxed lg:border-l-2 lg:border-t-0 lg:pl-10 lg:pt-0">
        <div>
          <h2 class="display text-[34px]">{{ company.legalName }}</h2>
          <address class="mt-3 not-italic text-muted">
            {{ company.address.street }}<br>
            {{ company.address.zip }} {{ company.address.city }} ({{ company.address.province }})<br>
            {{ $t('footer.vat', { vat: company.vat }) }}
          </address>
        </div>
        <ul class="space-y-2 font-semibold">
          <li><a :href="company.phoneHref" class="text-brand-ink hover:underline">☎ {{ company.phone }}</a></li>
          <li><a :href="`mailto:${company.email}`" class="text-brand-ink hover:underline">✉ {{ company.email }}</a></li>
        </ul>
        <div>
          <p class="mb-3 font-mono text-[12px] uppercase tracking-[.14em] text-muted">{{ $t('footer.follow') }}</p>
          <SocialLinks />
        </div>
        <a :href="`https://www.google.com/maps/search/?api=1&query=${mapQuery}`" target="_blank" rel="noopener" class="btn btn-secondary">{{ $t('contact.maps') }}</a>
      </aside>
     </div>
    </section>
  </div>
</template>
