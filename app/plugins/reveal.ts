// v-reveal: fade/slide-in an element the first time it scrolls into view.
export default defineNuxtPlugin((nuxtApp) => {
  let io: IntersectionObserver | null = null

  if (import.meta.client) {
    const reduced = window.matchMedia('(prefers-reduced-motion: reduce)').matches
    if ('IntersectionObserver' in window && !reduced) {
      io = new IntersectionObserver((entries) => {
        for (const entry of entries) {
          if (!entry.isIntersecting) continue
          entry.target.classList.add('visible')
          io?.unobserve(entry.target)
        }
      }, { threshold: 0.12 })
    }
  }

  nuxtApp.vueApp.directive('reveal', {
    mounted(el: HTMLElement, binding) {
      if (!io) return
      el.classList.add('reveal')
      if (binding.value) el.style.transitionDelay = `${binding.value}ms`
      io.observe(el)
    },
    unmounted(el: HTMLElement) {
      io?.unobserve(el)
    },
    getSSRProps: () => ({}),
  })
})
