<template>
  <footer class="border-t-8 border-brand bg-cream px-[5.5%] pb-6 pt-14">
    <div class="grid grid-cols-2 gap-x-4 gap-y-7 text-[11px] leading-[1.9] text-muted md:grid-cols-[1.3fr_1fr_1fr_1fr] md:gap-8">
      <div class="col-span-2 md:col-span-1">
        <a href="#home" aria-label="G.P.E. Rizzolo - Home">
          <img :src="images.logo" alt="G.P.E. Rizzolo" width="900" height="257" loading="lazy" class="h-12 w-auto">
        </a>
        <p class="mt-3">
          Profili in legno di qualità dal {{ company.since }}.<br>
          Esperienza, precisione e lavorazioni su misura.
        </p>
      </div>

      <div>
        <h4 class="mb-3.5 text-[10px] uppercase tracking-[.12em] text-ink">Esplora</h4>
        <ul>
          <li v-for="link in navLinks" :key="link.href"><a :href="link.href" class="hover:text-brand">{{ link.label }}</a></li>
        </ul>
      </div>

      <div>
        <h4 class="mb-3.5 text-[10px] uppercase tracking-[.12em] text-ink">Produzione</h4>
        <ul>
          <li v-for="p in products" :key="p.name">{{ p.name }}</li>
        </ul>
      </div>

      <div>
        <h4 class="mb-3.5 text-[10px] uppercase tracking-[.12em] text-ink">Contatti</h4>
        <address class="not-italic">
          {{ company.legalName }}<br>
          {{ company.address.street }}<br>
          {{ company.address.zip }} {{ company.address.city }} ({{ company.address.province }})<br>
          <a :href="company.phoneHref" class="hover:text-brand">{{ company.phone }}</a><br>
          <a :href="`mailto:${company.email}`" class="hover:text-brand">{{ company.email }}</a>
        </address>
      </div>
    </div>

    <div class="mt-10 flex flex-col gap-3 border-t border-line pt-[18px] text-[10px] text-muted md:flex-row md:justify-between">
      <span>© {{ new Date().getFullYear() }} {{ company.legalName }} · P.IVA {{ company.vat }}</span>
      <span>Privacy · Cookie policy</span>
    </div>
  </footer>
</template>
