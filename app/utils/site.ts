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
  note: string
}

const COMMON_OPTIONS = 'Misure, essenze e finiture su richiesta.'

export const families: Family[] = [
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
  {
    slug: 'profili-per-serramenti',
    name: 'Profili per serramenti',
    seoTitle: 'Profili in legno per serramenti',
    seoDescription:
      'Profili in legno per serramenti, coprifili e componenti per infissi: produzione su misura in qualsiasi essenza. G.P.E. Rizzolo, Santa Giustina in Colle (PD).',
    intro: 'Profili e coprifili in legno per infissi, con attenzione a dimensioni e finitura.',
    body: [
      'Produciamo profili in legno per serramenti: coprifili, copri alluminio e componenti per infissi, in dimensioni e finiture concordate con il cliente.',
      'La profilatura in asta è la nostra attività principale e viene eseguita con grande attenzione alla precisione.',
    ],
    uses: ['Produttori di serramenti', 'Coprifili e copri alluminio', 'Componenti per infissi', 'Serie e pezzi su misura'],
    image: img('serramenti'),
    note: COMMON_OPTIONS,
  },
  {
    slug: 'fermavetri',
    name: 'Fermavetri',
    seoTitle: 'Fermavetri in legno',
    seoDescription:
      'Fermavetri in legno in molte sagome e sezioni, per serramenti e infissi. Produzione su misura G.P.E. Rizzolo, Padova.',
    intro: 'Fermavetro in legno in molte sagome e sezioni.',
    body: [
      'I fermavetri sono tra le nostre produzioni storiche: diverse sagome, in varie essenze, forniti in asta.',
      'Sviluppiamo anche sezioni dedicate in base al serramento o al disegno del cliente.',
    ],
    uses: ['Serramenti in legno', 'Falegnamerie', 'Sagome su disegno'],
    image: img('fermavetri'),
    note: COMMON_OPTIONS,
  },
  {
    slug: 'angolari',
    name: 'Angolari',
    seoTitle: 'Angolari in legno',
    seoDescription:
      'Angolari in legno in diverse essenze e tinte: produzione su misura G.P.E. Rizzolo a Santa Giustina in Colle (PD).',
    intro: 'Angolari in legno in diverse essenze e tinte.',
    body: [
      'Produciamo angolari in legno in varie sezioni, al naturale o tinti, per finiture e protezione degli spigoli.',
      'Su richiesta realizziamo misure e colorazioni dedicate.',
    ],
    uses: ['Finiture di interni', 'Protezione degli spigoli', 'Arredo e falegnameria', 'Colorazioni personalizzate'],
    image: img('angolari'),
    note: COMMON_OPTIONS,
  },
  {
    slug: 'corrimano',
    name: 'Corrimano',
    seoTitle: 'Corrimano in legno massello',
    seoDescription:
      'Corrimano in legno massello per scale e balaustre, in diverse essenze e finiture. Produzione G.P.E. Rizzolo, profili in legno dal 1960.',
    intro: 'Corrimano in legno massello per scale e balaustre.',
    body: [
      'Realizziamo corrimano in legno massello con sagome ergonomiche, in diverse essenze e tonalità: dal chiaro naturale al noce scuro.',
      'Forniamo scalifici, falegnamerie e imprese, con produzioni su misura.',
    ],
    uses: ['Scale interne', 'Balaustre', 'Scalifici e falegnamerie', 'Essenze e tinte a scelta'],
    image: img('corrimano'),
    note: COMMON_OPTIONS,
  },
  {
    slug: 'masselli',
    name: 'Masselli',
    seoTitle: 'Masselli e listelli in legno',
    seoDescription:
      'Masselli e listelli in legno di varie sezioni, in qualsiasi essenza, anche per porte. G.P.E. Rizzolo, Santa Giustina in Colle (PD).',
    intro: 'Masselli e listelli di varie sezioni, anche per porte.',
    body: [
      'Produciamo masselli e listelli in legno in diverse sezioni e lunghezze, comprese le lavorazioni per porte.',
      'Possiamo fornire diverse essenze in base al vostro progetto.',
    ],
    uses: ['Masselli per porte', 'Semilavorati per falegnameria', 'Listelli e piattine', 'Sezioni su misura'],
    image: img('masselli'),
    note: COMMON_OPTIONS,
  },
  {
    slug: 'perlinati',
    name: 'Perlinati',
    seoTitle: 'Perlinati e tavole a incastro in legno',
    seoDescription:
      'Perlinati e tavole in legno a incastro, per rivestimenti di pareti e soffitti. Produzione G.P.E. Rizzolo, Padova.',
    intro: 'Perlinati e tavole a incastro per pareti e soffitti.',
    body: [
      'Produciamo perlinati e tavole a incastro in legno, adatti a rivestimenti interni di pareti e soffitti.',
      'Diverse essenze e misure disponibili su richiesta.',
    ],
    uses: ['Rivestimenti di pareti', 'Soffitti in legno', 'Interni e mansarde'],
    image: img('perlinati'),
    note: COMMON_OPTIONS,
  },
  {
    slug: 'frangisole',
    name: 'Frangisole',
    seoTitle: 'Profili in legno per frangisole',
    seoDescription:
      'Profili in legno per frangisole e rivestimenti esterni, in diverse sagome e essenze. G.P.E. Rizzolo, Santa Giustina in Colle (PD).',
    intro: 'Profili per frangisole e rivestimenti esterni.',
    body: [
      'Realizziamo profili in legno per frangisole e rivestimenti esterni, in diverse sagome e finiture.',
      'Possiamo sviluppare la sezione più adatta al vostro progetto.',
    ],
    uses: ['Frangisole', 'Facciate e rivestimenti esterni', 'Progetti di architettura'],
    image: img('frangisole'),
    note: COMMON_OPTIONS,
  },
  {
    slug: 'profili-tondi',
    name: 'Profili tondi',
    seoTitle: 'Profili tondi e tondini in legno',
    seoDescription:
      'Profili tondi e tondini in legno torniti in varie misure e essenze. G.P.E. Rizzolo, produzione su misura a Padova.',
    intro: 'Tondini e profili torniti in legno.',
    body: [
      'Produciamo profili tondi e tondini in legno, anche con teste e lavorazioni accessorie, secondo disegno.',
      'Diverse essenze e diametri disponibili.',
    ],
    uses: ['Tondini e aste', 'Lavorazioni torniti', 'Componenti per arredo'],
    image: img('tondi'),
    note: COMMON_OPTIONS,
  },
  {
    slug: 'doghe-per-panchine',
    name: 'Doghe per panchine',
    seoTitle: 'Doghe in legno per panchine',
    seoDescription:
      'Doghe in legno per panchine e arredo urbano,. G.P.E. Rizzolo, Santa Giustina in Colle (PD).',
    intro: 'Doghe in legno per panchine e arredo urbano.',
    body: [
      'Forniamo doghe in legno per panchine e arredo urbano, in sezioni e lunghezze concordate.',
      'Su richiesta prodotti certificati FSC®.',
    ],
    uses: ['Arredo urbano', 'Parchi e giardini', 'Aziende produttrici di panchine'],
    image: img('doghe'),
    note: 'Misure ed essenze su richiesta. Prodotti certificati FSC® disponibili su richiesta.',
  },
  {
    slug: 'realizzazioni-speciali',
    name: 'Realizzazioni speciali',
    seoTitle: 'Realizzazioni speciali in legno su disegno',
    seoDescription:
      'Lavorazioni e pezzi speciali in legno realizzati su disegno o campione, in qualsiasi essenza. G.P.E. Rizzolo, Padova.',
    intro: 'Pezzi speciali in legno realizzati su disegno o campione.',
    body: [
      'Quando un progetto non entra in un catalogo, sviluppiamo la soluzione insieme al cliente: portabottiglie, blocchi torniti, componenti con fori e incastri, supporti e molto altro.',
      'Ci raccontate l’idea, definiamo insieme sezioni e lavorazioni e realizziamo il pezzo in qualsiasi essenza di legno.',
    ],
    uses: ['Componenti per arredo', 'Prototipi e piccole serie', 'Pezzi con fori e incastri', 'Su disegno o campione'],
    image: img('realizzazioni'),
    gallery: [img('realizzazioni-2'), img('su-misura'), img('realizzazioni-4')],
    note: COMMON_OPTIONS,
  },
]

export const familyBySlug = (slug: string) => families.find(f => f.slug === slug)

/** Le quattro famiglie mostrate in home. */
export const featuredSlugs = ['profili-per-quadri', 'battiscopa', 'profili-per-serramenti', 'realizzazioni-speciali']

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
    name: 'ISO 14001:2015',
    text: 'Sistema di gestione ambientale, certificato con accreditamento UKAS.',
    image: '/images/cert-ukas.jpg',
    alt: 'Certificato UKAS G.P.E. Rizzolo',
  },
]

export const mailto = (subject: string) =>
  `mailto:${company.email}?subject=${encodeURIComponent(subject)}`
