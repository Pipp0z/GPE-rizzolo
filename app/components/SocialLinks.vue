<script setup lang="ts">
withDefaults(defineProps<{ dark?: boolean }>(), { dark: false })
</script>

<template>
  <ul class="flex gap-3">
    <li v-for="s in socials" :key="s.name">
      <a
        :href="s.href"
        target="_blank"
        rel="noopener noreferrer"
        :aria-label="$t('social.aria', { name: s.name, company: company.name })"
        :title="s.name"
        class="grid size-11 place-items-center border-2 transition hover:-translate-y-0.5 hover:border-brand hover:bg-brand hover:text-ink"
        :class="dark ? 'border-white/40 text-white' : 'border-ink text-ink'"
      >
        <svg v-if="s.name === 'Facebook'" viewBox="0 0 24 24" class="size-5" fill="currentColor" aria-hidden="true">
          <path d="M14 8V6.5c0-.8.2-1 1-1h2V2h-3c-3 0-4.5 1.7-4.5 4.4V8H7v3.6h2.5V22H14V11.6h3l.5-3.6H14Z" />
        </svg>
        <svg v-else-if="s.name === 'Instagram'" viewBox="0 0 24 24" class="size-5" fill="none" stroke="currentColor" stroke-width="2" aria-hidden="true">
          <rect x="3" y="3" width="18" height="18" rx="5" />
          <circle cx="12" cy="12" r="4.2" />
          <circle cx="17.2" cy="6.8" r="1.1" fill="currentColor" stroke="none" />
        </svg>
        <svg v-else viewBox="0 0 24 24" class="size-5" fill="currentColor" aria-hidden="true">
          <path d="M22 8.2c-.2-1-.9-1.7-1.9-2C18.4 5.7 12 5.7 12 5.7s-6.4 0-8.1.5c-1 .3-1.7 1-1.9 2C1.6 10 1.6 12 1.6 12s0 2 .4 3.8c.2 1 .9 1.7 1.9 2 1.7.5 8.1.5 8.1.5s6.4 0 8.1-.5c1-.3 1.7-1 1.9-2 .4-1.8.4-3.8.4-3.8s0-2-.4-3.8ZM10 15.2V8.8l5.4 3.2-5.4 3.2Z" />
        </svg>
      </a>
    </li>
  </ul>
</template>
