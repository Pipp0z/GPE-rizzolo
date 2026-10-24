import tailwindcss from '@tailwindcss/vite'

// https://nuxt.com/docs/api/configuration/nuxt-config
export default defineNuxtConfig({
  compatibilityDate: '2025-07-15',
  devtools: { enabled: true },
  css: ['~/assets/css/main.css'],
  vite: {
    plugins: [tailwindcss()]
  },
  app: {
    head: {
      htmlAttrs: { lang: 'it' },
      title: 'G.P.E. Rizzolo | Profili in legno dal 1960',
      meta: [
        { name: 'description', content: 'Profili in legno di qualità dal 1960. Produzione di profili per quadri, serramenti, battiscopa, corrimani, boiserie e lavorazioni speciali su misura.' },
        { name: 'theme-color', content: '#e87524' }
      ],
      link: [
        { rel: 'preconnect', href: 'https://fonts.googleapis.com' },
        { rel: 'preconnect', href: 'https://fonts.gstatic.com', crossorigin: '' },
        { rel: 'stylesheet', href: 'https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;500;600;700;800&display=swap' }
      ]
    }
  }
})
