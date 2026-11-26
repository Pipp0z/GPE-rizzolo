interface PageSeo {
  /** Titolo già tradotto. Il suffisso del brand viene aggiunto, salvo `home`. */
  title: string
  description: string
  /** Percorso senza prefisso di lingua, es. "/prodotti" */
  path: string
  image?: string
  home?: boolean
  /** Extra JSON-LD nodes per la pagina */
  jsonLd?: Record<string, unknown>[]
}

export function usePageSeo({ title, description, path, image = '/images/blocchetti-legno-massello-gpe-rizzolo.jpg', home = false, jsonLd = [] }: PageSeo) {
  const siteUrl = useRuntimeConfig().public.siteUrl as string
  const localePath = useLocalePath()
  const { localeProperties } = useI18n()
  const url = `${siteUrl}${localePath(path)}`
  const ogImage = `${siteUrl}${image}`
  const fullTitle = home ? title : `${title} | ${company.name}`

  useSeoMeta({
    title: fullTitle,
    description,
    ogTitle: fullTitle,
    ogDescription: description,
    ogType: 'website',
    ogUrl: url,
    ogImage,
    ogLocale: (localeProperties.value.language ?? 'it-IT').replace('-', '_'),
    ogSiteName: company.name,
    twitterCard: 'summary_large_image',
  })

  useHead({
    script: jsonLd.map(node => ({
      type: 'application/ld+json',
      innerHTML: JSON.stringify({ '@context': 'https://schema.org', ...node }),
    })),
  })
}

export function faqLd(items: { q: string, a: string }[]) {
  return {
    '@type': 'FAQPage',
    'mainEntity': items.map(i => ({ '@type': 'Question', 'name': i.q, 'acceptedAnswer': { '@type': 'Answer', 'text': i.a } })),
  }
}

export function breadcrumbLd(items: { name: string, path: string }[]) {
  const siteUrl = useRuntimeConfig().public.siteUrl as string
  const localePath = useLocalePath()
  return {
    '@type': 'BreadcrumbList',
    'itemListElement': items.map((item, i) => ({
      '@type': 'ListItem',
      'position': i + 1,
      'name': item.name,
      'item': `${siteUrl}${localePath(item.path)}`,
    })),
  }
}
