<script setup lang="ts">
usePageSeo({
  title: 'Informativa privacy',
  description: 'Informativa sul trattamento dei dati personali raccolti tramite il sito di G.P.E. Rizzolo.',
  path: '/privacy',
})
useHead({ meta: [{ name: 'robots', content: 'noindex' }] })
</script>

<template>
  <div>
    <PageHeader title="Informativa privacy" :crumbs="[{ name: 'Privacy' }]" />
    <section class="section-pad mx-auto max-w-[900px] space-y-5 text-[16px] leading-[1.8]">
      <!-- BOZZA: da far verificare dal titolare / consulente privacy prima della pubblicazione -->
      <p><strong class="text-ink">Titolare del trattamento:</strong> {{ company.legalName }}, {{ company.address.street }}, {{ company.address.zip }} {{ company.address.city }} ({{ company.address.province }}), P.IVA {{ company.vat }}, email <a :href="`mailto:${company.email}`" class="text-brand-ink underline">{{ company.email }}</a>.</p>
      <p><strong class="text-ink">Dati raccolti:</strong> attraverso il modulo di richiesta preventivo raccogliamo nome, azienda, email, telefono e il contenuto del messaggio.</p>
      <p><strong class="text-ink">Finalità e base giuridica:</strong> rispondere alle richieste inviate dall’utente (art. 6.1.b GDPR, misure precontrattuali).</p>
      <p><strong class="text-ink">Conservazione:</strong> i dati sono conservati per il tempo necessario a gestire la richiesta e gli eventuali rapporti commerciali conseguenti.</p>
      <p><strong class="text-ink">Diritti:</strong> l’utente può chiedere accesso, rettifica, cancellazione, limitazione e opposizione scrivendo a {{ company.email }}, e può proporre reclamo al Garante per la protezione dei dati personali.</p>
      <p><strong class="text-ink">Cookie:</strong> questo sito utilizza solo cookie tecnici e non installa strumenti di profilazione o analitici.</p>
    </section>
  </div>
</template>
