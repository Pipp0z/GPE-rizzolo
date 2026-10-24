interface PageSeo {
  title: string
  description: string
  path: string
  image?: string
  /** Extra JSON-LD nodes per la pagina */
  jsonLd?: Record<string, unknown>[]
}

export function usePageSeo({ title, description, path, image = '/images/hero.jpg', jsonLd = [] }: PageSeo) {
  const siteUrl = useRuntimeConfig().public.siteUrl as string
  const url = `${siteUrl}${path}`
  const ogImage = `${siteUrl}${image}`
  const fullTitle = path === '/' ? title : `${title} | ${company.name}`

  useSeoMeta({
    title: fullTitle,
    description,
    ogTitle: fullTitle,
    ogDescription: description,
    ogType: 'website',
    ogUrl: url,
    ogImage,
    ogLocale: 'it_IT',
    ogSiteName: company.name,
    twitterCard: 'summary_large_image',
  })

  useHead({
    link: [{ rel: 'canonical', href: url }],
    script: jsonLd.map(node => ({
      type: 'application/ld+json',
      innerHTML: JSON.stringify({ '@context': 'https://schema.org', ...node }),
    })),
  })
}

export function breadcrumbLd(items: { name: string, path: string }[]) {
  const siteUrl = useRuntimeConfig().public.siteUrl as string
  return {
    '@type': 'BreadcrumbList',
    'itemListElement': items.map((item, i) => ({
      '@type': 'ListItem',
      'position': i + 1,
      'name': item.name,
      'item': `${siteUrl}${item.path}`,
    })),
  }
}
