import { familyBase } from '../../../app/utils/site'

// URL dinamici delle schede prodotto per la sitemap (replicate in ogni lingua).
export default defineSitemapEventHandler(() =>
  familyBase.map(f => ({
    loc: `/prodotti/${f.slug}`,
    changefreq: 'monthly' as const,
    priority: 0.8,
    _i18nTransform: true,
  })),
)
