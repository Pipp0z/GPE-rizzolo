import { familyBase } from '../../../app/utils/site'

// URL dinamici delle schede prodotto e sottoprodotto per la sitemap (replicate in ogni lingua).
export default defineSitemapEventHandler(() =>
  familyBase.flatMap(f => [
    { loc: `/prodotti/${f.slug}`, changefreq: 'monthly' as const, priority: 0.8, _i18nTransform: true },
    ...(f.children ?? []).map(c => ({
      loc: `/prodotti/${f.slug}/${c.slug}`,
      changefreq: 'monthly' as const,
      priority: 0.7,
      _i18nTransform: true,
    })),
  ]),
)
