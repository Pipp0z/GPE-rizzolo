export const company = {
  name: 'G.P.E. Rizzolo',
  legalName: 'G.P.E. Rizzolo snc',
  since: 1960,
  tagline: 'Su misura è il nostro standard',
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

export const navLinks = [
  { label: 'Produzione', href: '#produzione' },
  { label: 'Catalogo', href: '#catalogo' },
  { label: 'Su misura', href: '#su-misura' },
  { label: 'Azienda', href: '#azienda' },
  { label: 'Certificazioni', href: '#certificazioni' },
]

const img = (name: string) => `/images/${name}.jpg`

export const images = {
  hero: img('hero'),
  custom: img('su-misura'),
  essenze: img('essenze'),
  logo: '/images/logo.png',
  logoWhite: '/images/logo-bianco.png',
}

export interface Product {
  name: string
  tag: string
  teaser: string
  description: string
  image: string
}

export const products: Product[] = [
  {
    name: 'Profili per quadri',
    tag: '01 / Decorazione',
    teaser: 'Forme e finiture per valorizzare ogni cornice.',
    description:
      'Profili decorativi per cornici, pensati per valorizzare opere, immagini e progetti di incorniciatura.',
    image: img('quadri'),
  },
  {
    name: 'Battiscopa & boiserie',
    tag: '02 / Interior',
    teaser: 'Dettagli che definiscono lo spazio.',
    description:
      'Zoccolini e boiserie per interni che danno continuità e carattere agli ambienti, al naturale o colorati.',
    image: img('battiscopa'),
  },
  {
    name: 'Profili per serramenti',
    tag: '03 / Architettura',
    teaser: 'Componenti per finiture precise e curate.',
    description:
      'Fermavetri, coprifili e componenti in legno per serramenti, con attenzione a dimensioni e finitura richieste.',
    image: img('serramenti'),
  },
  {
    name: 'Realizzazioni speciali',
    tag: '04 / Su progetto',
    teaser: 'Quando serve una soluzione fuori standard.',
    description:
      'Pezzi sviluppati partendo da un disegno, un campione o una specifica esigenza produttiva, in qualsiasi essenza di legno.',
    image: img('realizzazioni'),
  },
]

export interface CatalogItem {
  key: string
  name: string
  note: string
  image: string
}

// Famiglie di prodotto mostrate nel catalogo interattivo.
export const catalog: CatalogItem[] = [
  { key: 'quadri', name: 'Profili per quadri', note: 'Cornici in asta, in varie sezioni e finiture.', image: img('quadri') },
  { key: 'battiscopa', name: 'Battiscopa', note: 'Zoccolini al naturale, laccati o tinti.', image: img('battiscopa') },
  { key: 'boiserie', name: 'Boiserie', note: 'Cornici e modanature per rivestimenti e soffitti.', image: img('boiserie') },
  { key: 'serramenti', name: 'Profili per serramenti', note: 'Coprifili e profili per infissi.', image: img('serramenti') },
  { key: 'fermavetri', name: 'Fermavetri', note: 'Fermavetro in legno in molte sagome.', image: img('fermavetri') },
  { key: 'angolari', name: 'Angolari', note: 'Angolari in diverse essenze e tinte.', image: img('angolari') },
  { key: 'corrimano', name: 'Corrimano', note: 'Corrimano massello per scale e balaustre.', image: img('corrimano') },
  { key: 'masselli', name: 'Masselli', note: 'Masselli e listelli di varie sezioni.', image: img('masselli') },
  { key: 'perlinati', name: 'Perlinati', note: 'Perlinati e tavole a incastro.', image: img('perlinati') },
  { key: 'frangisole', name: 'Frangisole', note: 'Profili per frangisole e rivestimenti esterni.', image: img('frangisole') },
  { key: 'tondi', name: 'Profili tondi', note: 'Tondini e profili torniti.', image: img('tondi') },
  { key: 'doghe', name: 'Doghe per panchine', note: 'Doghe per arredo urbano.', image: img('doghe') },
]

export const essences = ['Abete', 'Pino', 'Larice', 'Meranti', 'Okumè', 'Rovere', 'Frassino']

export const otherProducts = [
  'Coprifili',
  'Copri alluminio',
  'Piattine',
  'Masselli per porte',
  'Colorazioni',
]

export const steps = [
  { n: '01', title: "Ci racconti l'idea", text: 'Disegno, campione o esigenza produttiva.' },
  { n: '02', title: 'Valutiamo insieme', text: 'Confronto tecnico e definizione della richiesta.' },
  { n: '03', title: 'Prende forma', text: 'Una soluzione pensata per il tuo progetto.' },
]

export const certifications = [
  {
    name: 'FSC® C184281',
    text: 'Prodotti certificati FSC® disponibili su richiesta.',
    image: '/images/cert-fsc.jpg',
    alt: 'Certificato FSC G.P.E. Rizzolo',
  },
  {
    name: 'UKAS',
    text: 'Certificato di qualità.',
    image: '/images/cert-ukas.jpg',
    alt: 'Certificato UKAS G.P.E. Rizzolo',
  },
]

export const mailto = (subject: string) =>
  `mailto:${company.email}?subject=${encodeURIComponent(subject)}`
