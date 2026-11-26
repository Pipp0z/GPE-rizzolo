<script setup lang="ts">
const { nav, families } = useContent()
</script>

<template>
  <footer class="blueprint-dark bg-ink px-[5.5%] pb-8 pt-16 text-white/70">
    <div class="wrap">
      <div class="grid gap-12 md:grid-cols-[1.4fr_1fr_1fr_1.2fr]">
        <div>
          <NuxtLinkLocale to="/" :aria-label="$t('nav.homeAria')">
            <NuxtImg format="png" :src="images.logoWhite" alt="G.P.E. Rizzolo" width="900" height="262" loading="lazy" class="h-14 w-auto" />
          </NuxtLinkLocale>
          <p class="mt-5 max-w-[320px] text-[15px] leading-relaxed">
            {{ $t('footer.desc', { year: company.since }) }}
          </p>
          <p class="mb-3 mt-6 font-mono text-[12px] uppercase tracking-[.14em] text-brand">{{ $t('footer.follow') }}</p>
          <SocialLinks dark />
        </div>

        <div>
          <h4 class="mb-4 font-mono text-[12px] uppercase tracking-[.14em] text-brand">{{ $t('footer.explore') }}</h4>
          <ul class="space-y-2 text-[15px]">
            <li v-for="link in nav" :key="link.href"><NuxtLinkLocale :to="link.href" class="hover:text-white">{{ link.label }}</NuxtLinkLocale></li>
          </ul>
        </div>

        <div>
          <h4 class="mb-4 font-mono text-[12px] uppercase tracking-[.14em] text-brand">{{ $t('footer.products') }}</h4>
          <ul class="space-y-2 text-[15px]">
            <li v-for="f in families.slice(0, 6)" :key="f.slug"><NuxtLinkLocale :to="`/prodotti/${f.slug}`" class="hover:text-white">{{ f.name }}</NuxtLinkLocale></li>
            <li><NuxtLinkLocale to="/prodotti" class="font-semibold text-white">{{ $t('footer.all') }}</NuxtLinkLocale></li>
          </ul>
        </div>

        <div>
          <h4 class="mb-4 font-mono text-[12px] uppercase tracking-[.14em] text-brand">{{ $t('footer.contacts') }}</h4>
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
        <span>© {{ new Date().getFullYear() }} {{ company.legalName }} · {{ $t('footer.vat', { vat: company.vat }) }}</span>
        <NuxtLinkLocale to="/privacy" class="hover:text-white">{{ $t('footer.privacy') }}</NuxtLinkLocale>
      </div>
    </div>
  </footer>
</template>
