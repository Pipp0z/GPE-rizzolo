<script setup lang="ts">
import type { Product } from '~/utils/site'

const selected = ref<Product | null>(null)

function close() {
  selected.value = null
}

function onKey(e: KeyboardEvent) {
  if (e.key === 'Escape') close()
}

watch(selected, (value) => {
  document.body.style.overflow = value ? 'hidden' : ''
})

onMounted(() => document.addEventListener('keydown', onKey))
onBeforeUnmount(() => {
  document.removeEventListener('keydown', onKey)
  document.body.style.overflow = ''
})
</script>

<template>
  <section id="produzione" class="mx-auto max-w-[100rem] px-[5.5%] py-[70px] md:py-[100px]">
    <div v-reveal class="mb-11 items-end justify-between gap-8 md:flex">
      <div>
        <div class="eyebrow">Cosa realizziamo</div>
        <h2 class="section-title">Il profilo giusto.<br>Per ogni progetto.</h2>
      </div>
      <p class="mt-4 max-w-[380px] text-[13px] leading-[1.8] text-muted md:mt-0">
        Una gamma di lavorazioni per professionisti, aziende e progettisti. Esplora le nostre principali famiglie
        di prodotto e trova il punto di partenza per la tua idea.
      </p>
    </div>

    <div class="grid grid-cols-2 gap-2.5 lg:grid-cols-4 lg:gap-3.5">
      <button
        v-for="(product, i) in products"
        :key="product.name"
        v-reveal="i * 80"
        type="button"
        class="group relative isolate min-h-[230px] overflow-hidden bg-[#d6b18e] text-left sm:min-h-[300px] lg:min-h-[350px]"
        @click="selected = product"
      >
        <img :src="product.image" :alt="product.name" loading="lazy" class="absolute inset-0 -z-20 size-full object-cover transition duration-[600ms] group-hover:scale-[1.06]">
        <div class="absolute inset-0 -z-10 bg-gradient-to-br from-brand/15 to-transparent to-55%" />
        <div class="absolute inset-x-0 bottom-0 top-[35%] -z-10 bg-gradient-to-b from-transparent to-[#171b16d9]" />
        <span class="absolute right-2.5 top-2.5 grid size-[29px] place-items-center rounded-full border border-brand bg-brand text-white sm:right-4 sm:top-4 sm:size-[35px]">↗</span>
        <div class="absolute inset-x-3 bottom-3 text-white sm:inset-x-5 sm:bottom-5">
          <small class="text-[9px] uppercase tracking-[.16em] text-[#ffc18f]">{{ product.tag }}</small>
          <h3 class="my-2 font-serif text-xl font-normal sm:text-[28px]">{{ product.name }}</h3>
          <p class="text-[10px] leading-normal text-[#e8e8df] sm:text-[11px]">{{ product.teaser }}</p>
        </div>
      </button>
    </div>

    <p class="mt-6 text-[11px] text-muted">
      Disponibili anche: <span class="lowercase">{{ otherProducts.join(', ') }}</span>.
    </p>

    <HomeMaterialStrip />

    <Teleport to="body">
      <Transition
        enter-active-class="transition duration-300"
        leave-active-class="transition duration-300"
        enter-from-class="opacity-0"
        leave-to-class="opacity-0"
      >
        <div v-if="selected" class="fixed inset-0 z-[60] grid place-items-center bg-[#17120fe0] p-4 backdrop-blur-sm" @click.self="close">
          <div
            class="relative grid max-h-[calc(100vh-2rem)] w-full max-w-[900px] overflow-auto bg-paper shadow-[0_30px_100px_#0004] md:grid-cols-2"
            role="dialog"
            aria-modal="true"
            aria-labelledby="modal-title"
          >
            <button class="absolute right-3 top-3 z-10 size-10 rounded-full bg-paper text-2xl" aria-label="Chiudi dettagli" @click="close">×</button>
            <div class="relative min-h-[230px] bg-cover bg-center md:min-h-[440px]" :style="{ backgroundImage: `url('${selected.image}')` }">
              <span class="absolute bottom-6 left-6 text-[9px] tracking-[.15em] text-white [text-shadow:0_2px_10px_#000]">G.P.E. RIZZOLO · DAL {{ company.since }}</span>
            </div>
            <div class="flex flex-col justify-center p-8 md:p-14">
              <div class="eyebrow">Le nostre lavorazioni</div>
              <h2 id="modal-title" class="my-5 font-serif text-[clamp(2.1rem,4vw,3.1rem)] font-normal leading-none">{{ selected.name }}</h2>
              <p class="text-[13px] leading-[1.8] text-muted">{{ selected.description }}</p>
              <ul class="mb-7 mt-5 grid gap-3 text-[11px] text-[#65554a]">
                <li>↗ Possibilità su misura</li>
                <li>↗ Confronto tecnico dedicato</li>
                <li>↗ Richieste per aziende e professionisti</li>
              </ul>
              <a class="btn self-start" :href="mailto(`Richiesta informazioni - ${selected.name}`)">Parliamone ↗</a>
            </div>
          </div>
        </div>
      </Transition>
    </Teleport>
  </section>
</template>
