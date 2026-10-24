import tailwindcss from '@tailwindcss/vite'

const baseURL = process.env.NUXT_APP_BASE_URL || '/'

// https://nuxt.com/docs/api/configuration/nuxt-config
export default defineNuxtConfig({
  compatibilityDate: '2025-07-15',
  devtools: { enabled: true },
  modules: ['@nuxt/image', '@nuxt/fonts', '@nuxtjs/sitemap', '@nuxtjs/robots'],
  css: ['~/assets/css/main.css'],
  vite: {
    plugins: [tailwindcss()]
  },

  site: {
    url: process.env.NUXT_PUBLIC_SITE_URL || 'https://www.gperizzolo.it',
    name: 'G.P.E. Rizzolo',
    defaultLocale: 'it'
  },

  runtimeConfig: {
    // Server-only: configurazione SMTP per il form contatti
    smtp: {
      host: '',
      port: 587,
      user: '',
      pass: '',
      from: '',
      to: 'info@gperizzolo.it'
    },
    public: {
      siteUrl: process.env.NUXT_PUBLIC_SITE_URL || 'https://www.gperizzolo.it'
    }
  },

  sitemap: {
    sources: ['/api/__sitemap__/urls'],
    exclude: ['/privacy']
  },

  image: {
    format: ['webp'],
    screens: { xs: 320, sm: 640, md: 768, lg: 1024, xl: 1280, xxl: 1536 },
    quality: 78
  },

  fonts: {
    families: [
      { name: 'DM Sans', provider: 'google', weights: [400, 500, 600, 700] },
      { name: 'Barlow Condensed', provider: 'google', weights: [600, 700, 800] },
      { name: 'JetBrains Mono', provider: 'google', weights: [400, 500] }
    ]
  },

  // Redirect permanenti dagli URL del vecchio sito WordPress
  routeRules: {
    '/chi-siamo': { redirect: { to: '/azienda', statusCode: 301 } },
    '/chi-siamo/': { redirect: { to: '/azienda', statusCode: 301 } },
    '/la-nostra-produzione': { redirect: { to: '/prodotti', statusCode: 301 } },
    '/la-nostra-produzione/': { redirect: { to: '/prodotti', statusCode: 301 } },
    '/news': { redirect: { to: '/', statusCode: 301 } },
    '/news/': { redirect: { to: '/', statusCode: 301 } },
    '/lazienda-gpe-rizzolo-snc-profili-in-legno-di-qualita-dal-1960-31010-fratte-di-santa-giustina-in-colle-pd-profili-per-quadri-angolari-battiscopa-masselli-vari-corrimano-realizzazioni-speciali-varie-pro': { redirect: { to: '/azienda', statusCode: 301 } },
    '/lazienda-gpe-rizzolo-snc-profili-in-legno-di-qualita-dal-1960-31010-fratte-di-santa-giustina-in-colle-pd-profili-per-quadri-angolari-battiscopa-masselli-vari-corrimano-realizzazioni-speciali-varie-pro/': { redirect: { to: '/azienda', statusCode: 301 } },
  },

  app: {
    baseURL,
    head: {
      htmlAttrs: { lang: 'it' },
      meta: [{ name: 'theme-color', content: '#e87524' }],
      link: [{ rel: 'icon', type: 'image/png', href: `${baseURL}favicon.png` }]
    }
  }
})
