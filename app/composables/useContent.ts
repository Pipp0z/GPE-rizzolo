/** Contenuti localizzati: struttura da utils/site.ts, testi dai file i18n. */
export function useContent() {
  const { t, te } = useI18n()
  const localePath = useLocalePath()

  const families = computed<Family[]>(() => familyBase.map((b) => {
    const k = `families.${b.slug}`
    // Le chiavi esistono sempre in italiano (lingua base): si contano lì.
    const list = (prefix: string) => {
      const out: string[] = []
      for (let i = 1; te(`${k}.${prefix}${i}`, 'it'); i++) out.push(t(`${k}.${prefix}${i}`))
      return out
    }
    return {
      slug: b.slug,
      image: b.image,
      cover: b.cover,
      gallery: b.gallery,
      name: t(`${k}.name`),
      seoTitle: t(`${k}.seoTitle`),
      seoDescription: t(`${k}.seoDescription`),
      intro: t(`${k}.intro`),
      body: list('body'),
      uses: list('use'),
      children: b.children?.map(c => ({
        slug: c.slug,
        image: c.image,
        name: t(`children.${c.slug}.name`),
        text: t(`children.${c.slug}.text`),
      })),
    }
  }))

  const familyBySlug = (slug: string) => families.value.find(f => f.slug === slug)

  const nav = computed(() => navLinks.map(l => ({ label: t(`nav.${l.key}`), href: l.href })))

  const essences = computed(() => Array.from({ length: 7 }, (_, i) => t(`essence.${i + 1}`)))
  const otherProducts = computed(() => Array.from({ length: 4 }, (_, i) => t(`other.${i + 1}`)))
  const steps = computed(() => [1, 2, 3].map(n => ({ n: `0${n}`, title: t(`step.${n}t`), text: t(`step.${n}`) })))
  const history = computed(() => [1, 2, 3, 4].map(n => ({ label: t(`hist.${n}l`), title: t(`hist.${n}t`), text: t(`hist.${n}`) })))
  const values = computed(() => [1, 2, 3, 4, 5, 6].map(n => ({ name: t(`value.${n}`), text: t(`value.${n}t`) })))
  const goals = computed(() => [1, 2, 3, 4].map(n => ({ title: t(`goal.${n}`), text: t(`goal.${n}t`) })))
  const certifications = computed(() => certificationImages.map(c => ({
    name: c.name,
    image: c.image,
    text: t(`cert.${c.key}`),
    alt: t(`cert.${c.key}Alt`),
  })))
  const brochures = computed(() => brochureFiles.map(b => ({ label: t(`brochure.${b.key}`), href: b.href })))

  /** Scheda tecnica di default, integrata dalle righe specifiche del prodotto. */
  function specSheet(extra: SpecRow[] = []): SpecRow[] {
    const rows: SpecRow[] = [
      { label: t('spec.essences'), value: t('spec.essencesV') },
      { label: t('spec.production'), value: t('spec.productionV') },
      { label: t('spec.origin'), value: t('spec.originV') },
      { label: t('spec.sizes'), value: t('spec.onRequest') },
      { label: t('spec.finishes'), value: t('spec.onRequest') },
      { label: t('spec.cert'), value: t('spec.certV') },
    ]
    for (const row of extra) {
      const i = rows.findIndex(r => r.label.toLowerCase() === row.label.toLowerCase())
      if (i >= 0) rows[i] = row
      else rows.push(row)
    }
    return rows
  }

  return { families, familyBySlug, nav, essences, otherProducts, steps, history, values, goals, certifications, brochures, specSheet, localePath }
}
