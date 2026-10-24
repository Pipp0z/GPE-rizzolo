import { families } from '../../../app/utils/site'

// URL dinamici delle schede prodotto per la sitemap.
export default defineSitemapEventHandler(() =>
  families.map(f => ({ loc: `/prodotti/${f.slug}`, changefreq: 'monthly' as const, priority: 0.8 })),
)
