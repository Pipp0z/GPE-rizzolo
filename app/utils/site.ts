export const company = {
  name: 'G.P.E. Rizzolo',
  legalName: 'G.P.E. Rizzolo snc',
  since: 1960,
  address: {
    street: 'Via Pio X°, 35',
    zip: '35010',
    city: 'Santa Giustina in Colle',
    province: 'PD',
  },
  phone: '+39 049 5790523',
  phoneHref: 'tel:+390495790523',
  email: 'info@gperizzolo.it',
  vat: '00042850289',
  partners: ['Paolo', 'Elio', 'Samuel', 'Steven'],
}

export const socials = [
  { name: 'Instagram', href: 'https://www.instagram.com/gpe_rizzolo/' },
  { name: 'YouTube', href: 'https://www.youtube.com/channel/UCQkj1cOTQMWi18hqT2lkp6A' },
  { name: 'Facebook', href: 'https://www.facebook.com/profile.php?id=100077918561946' },
]

export const navLinks = [
  { key: 'products', href: '/prodotti' },
  { key: 'custom', href: '/#su-misura' },
  { key: 'company', href: '/azienda' },
  { key: 'certs', href: '/certificazioni' },
  { key: 'contacts', href: '/contatti' },
]

export const img = (name: string) => `/images/${name}.jpg`

export const images = {
  hero: img('blocchetti-legno-massello-gpe-rizzolo'),
  custom: img('su-misura'),
  essenze: img('essenze-legno-abete-pino-larice-rovere-frassino'),
  logo: '/images/logo.png',
  logoWhite: '/images/logo-bianco.png',
}

export interface SpecRow {
  label: string
  value: string
}

export interface FamilyChild {
  slug: string
  name: string
  /** Frase breve (card e intro della pagina) */
  text: string
  seoTitle: string
  seoDescription: string
  body: string[]
  uses: string[]
  image: string
  /** Righe della scheda tecnica: sovrascrivono/integrano quelle di default */
  specs?: SpecRow[]
  /** Link a una scheda tecnica scaricabile (PDF) */
  pdf?: string
}

export interface Family {
  slug: string
  name: string
  /** Titolo SEO (senza suffisso brand) */
  seoTitle: string
  /** Meta description */
  seoDescription: string
  intro: string
  body: string[]
  uses: string[]
  image: string
  cover?: string
  gallery?: string[]
  /** Prodotti compresi in questa categoria */
  children?: FamilyChild[]
}

/** Struttura delle famiglie: i testi stanno nei file di traduzione (i18n/locales). */
export const familyBase: { slug: string, image: string, cover?: string, gallery?: string[], children?: { slug: string, image: string }[] }[] = [
  { slug: 'battiscopa', image: img('battiscopa-legno-naturale-laccato-tinto'), cover: img('cover-battiscopa') },
  { slug: 'profili-per-quadri', image: img('profili-legno-per-cornici-quadri'), cover: img('cover-profili-per-quadri'), gallery: [img('profili-legno-cornici-quadri-2'), img('profili-legno-cornici-quadri-3'), img('profili-legno-cornici-quadri-4')] },
  {
    slug: 'profili-per-serramenti', image: img('profili-legno-per-serramenti'), cover: img('cover-profili-per-serramenti'),
    children: [{ slug: 'fermavetri', image: img('fermavetri-legno-sagome') }, { slug: 'coprifili', image: img('coprifili-fermavetri-legno-serramenti') }],
  },
  {
    slug: 'perlinati', image: img('perlinati-legno-tavole-incastro'), cover: img('cover-perlinati'),
    children: [{ slug: 'frangisole', image: img('frangisole-legno-larice') }, { slug: 'masselli-piallati', image: img('masselli-piallati-legno') }],
  },
  { slug: 'profili-per-saune', image: img('frangisole-legno-larice'), cover: img('cover-profili-per-saune') },
  { slug: 'semilavorati', image: img('masselli-piallati-legno'), cover: img('cover-semilavorati') },
  {
    slug: 'profili-di-finitura', image: img('angolari-legno-essenze-tinte'), cover: img('cover-profili-di-finitura'),
    children: [
      { slug: 'profili-tondi', image: img('profili-tondi-legno') },
      { slug: 'angolari', image: img('angolari-legno-essenze-tinte') },
      { slug: 'corrimano', image: img('corrimano-legno-massello') },
    ],
  },
  { slug: 'boiserie', image: img('boiserie-cornici-legno'), cover: img('cover-boiserie') },
]

export const certificationImages = [
  { key: 'fsc', name: 'FSC® C184281', image: '/images/cert-fsc.jpg' },
  { key: 'iso', name: 'ISO 14001:2015', image: '/images/cert-ukas.jpg' },
]

export const brochureFiles = [
  { key: 'it', href: '/docs/brochure-gpe-it.pdf' },
  { key: 'en', href: '/docs/brochure-gpe-en.pdf' },
]

export const mailto = (subject: string) =>
  `mailto:${company.email}?subject=${encodeURIComponent(subject)}`
