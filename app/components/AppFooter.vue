<template>
  <footer class="blueprint-dark bg-ink px-[5.5%] pb-8 pt-16 text-white/70">
    <div class="wrap">
      <div class="grid gap-12 md:grid-cols-[1.4fr_1fr_1fr_1.2fr]">
        <div>
          <NuxtLink to="/" aria-label="G.P.E. Rizzolo - Home">
            <NuxtImg format="png" :src="images.logoWhite" alt="G.P.E. Rizzolo" width="900" height="262" loading="lazy" class="h-14 w-auto" />
          </NuxtLink>
          <p class="mt-5 max-w-[320px] text-[15px] leading-relaxed">
            Profili in legno di qualità dal {{ company.since }}. Profilatura in asta, in qualsiasi essenza, su disegno o campione.
          </p>
        </div>

        <div>
          <h4 class="mb-4 font-mono text-[12px] uppercase tracking-[.14em] text-brand">Esplora</h4>
          <ul class="space-y-2 text-[15px]">
            <li v-for="link in navLinks" :key="link.href"><NuxtLink :to="link.href" class="hover:text-white">{{ link.label }}</NuxtLink></li>
          </ul>
        </div>

        <div>
          <h4 class="mb-4 font-mono text-[12px] uppercase tracking-[.14em] text-brand">Prodotti</h4>
          <ul class="space-y-2 text-[15px]">
            <li v-for="f in families.slice(0, 6)" :key="f.slug"><NuxtLink :to="`/prodotti/${f.slug}`" class="hover:text-white">{{ f.name }}</NuxtLink></li>
            <li><NuxtLink to="/prodotti" class="font-semibold text-white">Tutti i prodotti →</NuxtLink></li>
          </ul>
        </div>

        <div>
          <h4 class="mb-4 font-mono text-[12px] uppercase tracking-[.14em] text-brand">Contatti</h4>
          <address class="space-y-1 text-[15px] not-italic">
            <p class="text-white">{{ company.legalName }}</p>
            <p>{{ company.address.street }}</p>
            <p>{{ company.address.zip }} {{ company.address.city }} ({{ company.address.province }})</p>
            <p class="pt-2"><a :href="company.phoneHref" class="hover:text-white">{{ company.phone }}</a></p>
            <p><a :href="`mailto:${company.email}`" class="hover:text-white">{{ company.email }}</a></p>
          </address>
        </div>
      </div>

      <div class="mt-14 flex flex-col gap-3 border-t border-white/15 pt-6 font-mono text-[12px] uppercase tracking-[.08em] md:flex-row md:justify-between">
        <span>© {{ new Date().getFullYear() }} {{ company.legalName }} · P.IVA {{ company.vat }}</span>
        <NuxtLink to="/privacy" class="hover:text-white">Privacy</NuxtLink>
      </div>
    </div>
  </footer>
</template>
