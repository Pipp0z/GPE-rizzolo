<script setup lang="ts">
usePageSeo({
  title: 'Contatti e richiesta preventivo',
  description: `Richiedi un preventivo per profili in legno su misura. G.P.E. Rizzolo, ${company.address.street}, ${company.address.zip} ${company.address.city} (${company.address.province}). Tel. ${company.phone}.`,
  path: '/contatti',
  jsonLd: [{ '@type': 'ContactPage', 'name': 'Contatti G.P.E. Rizzolo' }, breadcrumbLd([{ name: 'Home', path: '/' }, { name: 'Contatti', path: '/contatti' }])],
})

const mapQuery = encodeURIComponent(`${company.address.street}, ${company.address.zip} ${company.address.city} ${company.address.province}`)
</script>

<template>
  <div>
    <PageHeader
      title="Richiedi un preventivo"
      intro="Raccontaci cosa ti serve: profilo, essenza, quantità. Se hai un disegno o un campione, mandacelo e valutiamo insieme."
      :crumbs="[{ name: 'Contatti' }]"
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
            P.IVA {{ company.vat }}
          </address>
        </div>
        <ul class="space-y-2 font-semibold">
          <li><a :href="company.phoneHref" class="text-brand-ink hover:underline">☎ {{ company.phone }}</a></li>
          <li><a :href="`mailto:${company.email}`" class="text-brand-ink hover:underline">✉ {{ company.email }}</a></li>
        </ul>
        <a :href="`https://www.google.com/maps/search/?api=1&query=${mapQuery}`" target="_blank" rel="noopener" class="btn btn-secondary">Apri su Google Maps ↗</a>
      </aside>
     </div>
    </section>
  </div>
</template>
