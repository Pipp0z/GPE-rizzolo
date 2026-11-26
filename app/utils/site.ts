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
  { label: 'Prodotti', href: '/prodotti' },
  { label: 'Su misura', href: '/#su-misura' },
  { label: 'Azienda', href: '/azienda' },
  { label: 'Certificazioni', href: '/certificazioni' },
  { label: 'Contatti', href: '/contatti' },
]

export const img = (name: string) => `/images/${name}.jpg`

export const images = {
  hero: img('hero'),
  custom: img('su-misura'),
  essenze: img('essenze'),
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
  text: string
  image: string
  /** Paragrafi della pagina di dettaglio (default: solo `text`) */
  body?: string[]
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
  gallery?: string[]
  /** Prodotti compresi in questa categoria */
  children?: FamilyChild[]
  note: string
}

const COMMON_OPTIONS = 'Misure, essenze e finiture su richiesta.'

export const families: Family[] = [
  {
    slug: 'battiscopa',
    name: 'Battiscopa',
    seoTitle: 'Battiscopa in legno',
    seoDescription:
      'Battiscopa e zoccolini in legno su misura: al naturale, laccati o tinti, in diverse essenze e sezioni. Produzione G.P.E. Rizzolo, Padova.',
    intro: 'Zoccolini in legno al naturale, laccati o tinti, in varie sezioni.',
    body: [
      'I nostri battiscopa in legno sono disponibili in diverse sezioni e sagome, al naturale oppure colorati: bianchi, tinti noce o con finiture personalizzate.',
      'Forniamo rivenditori, falegnamerie, imprese e progettisti, anche con quantità e misure dedicate.',
    ],
    uses: ['Pavimenti in parquet e laminato', 'Ristrutturazioni e nuove costruzioni', 'Rivenditori e falegnamerie', 'Finiture colorate su richiesta'],
    image: img('battiscopa'),
    note: COMMON_OPTIONS,
  },
  {
    slug: 'profili-per-quadri',
    name: 'Profili per quadri',
    seoTitle: 'Profili in legno per cornici e quadri',
    seoDescription:
      'Profili in legno per cornici e quadri prodotti a Santa Giustina in Colle (PD): varie sezioni e finiture, in qualsiasi essenza, anche su disegno.',
    intro: 'Profili in asta per cornici e incorniciatura, in diverse sezioni e finiture.',
    body: [
      'Produciamo profili in legno per cornici e quadri destinati a laboratori di incorniciatura, aziende e progettisti. Le sezioni vanno dal profilo semplice alla modanatura più elaborata, in asta, pronti per essere tagliati e assemblati.',
      'Lavoriamo qualsiasi essenza di legno e possiamo sviluppare una sagoma nuova partendo da un vostro disegno o da un campione.',
    ],
    uses: ['Cornici per quadri e specchi', 'Laboratori di incorniciatura', 'Arredo e decorazione', 'Sagome personalizzate su disegno'],
    image: img('quadri'),
    gallery: [img('quadri-2'), img('quadri-3'), img('quadri-4')],
    note: COMMON_OPTIONS,
  },
  {
    slug: 'profili-per-serramenti',
    name: 'Profili per serramenti',
    seoTitle: 'Profili in legno per serramenti',
    seoDescription:
      'Profili in legno per serramenti: fermavetri, coprifili e componenti per infissi, su misura in qualsiasi essenza. G.P.E. Rizzolo, Santa Giustina in Colle (PD).',
    intro: 'Fermavetri, coprifili e profili per infissi, con attenzione a dimensioni e finitura.',
    body: [
      'Produciamo profili in legno per serramenti, in dimensioni e finiture concordate con il cliente. La profilatura in asta è la nostra attività principale e viene eseguita con grande attenzione alla precisione.',
      'Nella categoria rientrano fermavetri e coprifili, in diverse sagome e essenze.',
    ],
    uses: ['Produttori di serramenti', 'Falegnamerie', 'Componenti per infissi', 'Serie e pezzi su misura'],
    image: img('serramenti'),
    children: [
      { slug: 'fermavetri', name: 'Fermavetri', text: 'Fermavetro in legno in molte sagome e sezioni, forniti in asta.', image: img('fermavetri') },
      { slug: 'coprifili', name: 'Coprifili', text: 'Coprifili in legno per serramenti e infissi, in diverse sezioni.', image: img('serramenti-fermavetro') },
    ],
    note: COMMON_OPTIONS,
  },
  {
    slug: 'perlinati',
    name: 'Perlinati',
    seoTitle: 'Perlinati, frangisole e masselli piallati in legno',
    seoDescription:
      'Perlinati, profili per frangisole e masselli piallati in legno, per rivestimenti e interni. Produzione G.P.E. Rizzolo, Padova.',
    intro: 'Perlinati e tavole a incastro, frangisole e masselli piallati.',
    body: [
      'Produciamo perlinati e tavole a incastro in legno, adatti a rivestimenti interni di pareti e soffitti.',
      'Nella categoria rientrano anche i profili per frangisole e i masselli piallati, in diverse essenze e misure.',
    ],
    uses: ['Rivestimenti di pareti', 'Soffitti in legno', 'Frangisole e rivestimenti esterni', 'Falegnameria e carpenteria'],
    image: img('perlinati'),
    children: [
      { slug: 'frangisole', name: 'Frangisole', text: 'Profili per frangisole e rivestimenti esterni, in diverse sagome e finiture.', image: img('frangisole') },
      { slug: 'masselli-piallati', name: 'Masselli piallati', text: 'Masselli e listelli piallati di varie sezioni, in diverse essenze.', image: img('masselli') },
    ],
    note: COMMON_OPTIONS,
  },
  {
    slug: 'profili-per-saune',
    name: 'Profili per saune',
    seoTitle: 'Profili in legno per saune',
    seoDescription:
      'Profili in legno per saune: produzione su misura in diverse essenze e sezioni. G.P.E. Rizzolo, Santa Giustina in Colle (PD).',
    intro: 'Profili in legno per la realizzazione e la finitura di saune.',
    body: [
      'Produciamo profili in legno per saune, nell’essenza e nella sezione richieste dal progetto.',
      'Contattaci per descriverci il tuo progetto: valutiamo insieme la soluzione più adatta.',
    ],
    uses: ['Costruttori di saune', 'Rivestimenti e finiture', 'Sezioni su disegno'],
    image: img('frangisole'),
    note: COMMON_OPTIONS,
  },
  {
    slug: 'semilavorati',
    name: 'Semilavorati',
    seoTitle: 'Semilavorati in legno',
    seoDescription:
      'Semilavorati in legno di varie sezioni e lunghezze, in qualsiasi essenza. G.P.E. Rizzolo, Santa Giustina in Colle (PD).',
    intro: 'Semilavorati in legno di varie sezioni, in qualsiasi essenza.',
    body: [
      'Forniamo semilavorati in legno in diverse sezioni e lunghezze, pronti per le lavorazioni successive.',
      'Possiamo preparare le misure e le essenze richieste dal vostro ciclo produttivo.',
    ],
    uses: ['Falegnamerie e industrie del legno', 'Masselli per porte', 'Piattine e listelli', 'Sezioni su misura'],
    image: img('masselli'),
    note: COMMON_OPTIONS,
  },
  {
    slug: 'profili-di-finitura',
    name: 'Profili di finitura',
    seoTitle: 'Profili di finitura in legno: tondi, angolari, corrimano',
    seoDescription:
      'Profili di finitura in legno: profili tondi, angolari e corrimano in diverse essenze e finiture. G.P.E. Rizzolo, produzione su misura a Padova.',
    intro: 'Profili tondi, angolari e corrimano in diverse essenze e finiture.',
    body: [
      'Realizziamo profili di finitura in legno per completare arredi, scale e interni: profili tondi, angolari e corrimano.',
      'Ogni profilo può essere prodotto nell’essenza, nella sezione e nella tinta richieste.',
    ],
    uses: ['Scale e balaustre', 'Protezione degli spigoli', 'Arredo e falegnameria', 'Colorazioni personalizzate'],
    image: img('angolari'),
    children: [
      { slug: 'profili-tondi', name: 'Profili tondi', text: 'Tondini e profili torniti in legno, in varie misure e essenze.', image: img('tondi') },
      { slug: 'angolari', name: 'Angolari', text: 'Angolari in legno in diverse essenze e tinte, al naturale o colorati.', image: img('angolari') },
      { slug: 'corrimano', name: 'Corrimano', text: 'Corrimano in legno massello per scale e balaustre, dal chiaro naturale al noce scuro.', image: img('corrimano') },
    ],
    note: COMMON_OPTIONS,
  },
  {
    slug: 'boiserie',
    name: 'Boiserie',
    seoTitle: 'Boiserie e cornici in legno',
    seoDescription:
      'Boiserie, cornici e modanature in legno per rivestimenti e soffitti, in diverse essenze e finiture. G.P.E. Rizzolo, profili in legno dal 1960.',
    intro: 'Cornici e modanature in legno per rivestimenti, soffitti e interni.',
    body: [
      'Realizziamo boiserie, cornici e modanature in legno per dare carattere agli ambienti, dal dettaglio lineare alla decorazione più ricca.',
      'Ogni profilo può essere prodotto nell’essenza e nella finitura richiesta.',
    ],
    uses: ['Rivestimenti a parete', 'Cornici per soffitti', 'Interni residenziali e commerciali', 'Restauri'],
    image: img('boiserie'),
    note: COMMON_OPTIONS,
  },
]

export const familyBySlug = (slug: string) => families.find(f => f.slug === slug)

export const childBySlug = (family: Family, slug: string) => family.children?.find(c => c.slug === slug)

/** Scheda tecnica di default, integrata dalle righe specifiche del prodotto. */
export function specSheet(extra: SpecRow[] = []): SpecRow[] {
  const rows: SpecRow[] = [
    { label: 'Essenze', value: 'Qualsiasi essenza di legno' },
    { label: 'Produzione', value: 'In asta, in serie o su disegno' },
    { label: 'Misure', value: 'Su richiesta' },
    { label: 'Finiture', value: 'Su richiesta' },
    { label: 'Certificazione', value: 'FSC® disponibile su richiesta' },
  ]
  for (const row of extra) {
    const i = rows.findIndex(r => r.label.toLowerCase() === row.label.toLowerCase())
    if (i >= 0) rows[i] = row
    else rows.push(row)
  }
  return rows
}

export const essences = ['Abete', 'Pino', 'Larice', 'Meranti', 'Okumè', 'Rovere', 'Frassino']

export const otherProducts = [
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
    name: 'ISO 14001:2015',
    text: 'Sistema di gestione ambientale, certificato con accreditamento UKAS.',
    image: '/images/cert-ukas.jpg',
    alt: 'Certificato UKAS G.P.E. Rizzolo',
  },
]

export const mailto = (subject: string) =>
  `mailto:${company.email}?subject=${encodeURIComponent(subject)}`
