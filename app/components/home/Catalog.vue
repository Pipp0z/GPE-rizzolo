<script setup lang="ts">
const activeKey = ref(catalog[0]!.key)
const active = computed(() => catalog.find(c => c.key === activeKey.value)!)
const index = computed(() => catalog.indexOf(active.value) + 1)
</script>

<template>
  <section id="catalogo" class="overflow-hidden bg-ink px-[5.5%] py-[72px] text-paper md:py-[100px]">
    <div v-reveal class="mx-auto mb-11 flex max-w-[1450px] flex-col justify-between gap-6 md:flex-row md:items-end md:gap-10">
      <div>
        <div class="eyebrow !text-[#ff9b55]">Il nostro catalogo</div>
        <h2 class="mt-5 font-serif text-[clamp(3rem,6vw,5.1rem)] font-normal leading-[.98] tracking-[-.055em]">
          Ogni profilo,<br><em class="text-brand">dal vero.</em>
        </h2>
      </div>
      <p class="max-w-[340px] text-[13px] leading-[1.9] text-[#c9b9ad]">
        Sfoglia le famiglie di prodotto: foto reali dei pezzi che escono dalla nostra produzione.
      </p>
    </div>

    <div v-reveal class="mx-auto grid max-w-[1450px] bg-sand text-ink shadow-[0_25px_80px_#0002] md:grid-cols-[1.25fr_.75fr]">
      <!-- Foto -->
      <div class="relative min-h-[320px] bg-[#e9e6e1] md:min-h-[560px]">
        <Transition
          mode="out-in"
          enter-active-class="transition duration-300"
          leave-active-class="transition duration-200"
          enter-from-class="opacity-0"
          leave-to-class="opacity-0"
        >
          <img
            :key="active.key"
            :src="active.image"
            :alt="active.name"
            class="absolute inset-0 size-full object-cover"
          >
        </Transition>
        <div class="absolute inset-x-6 top-6 flex justify-between text-[9px] font-bold tracking-[.16em] text-ink/60">
          <span>G.P.E. / CATALOGO</span>
          <span>{{ String(index).padStart(2, '0') }} — {{ catalog.length }}</span>
        </div>
        <div class="absolute inset-x-0 bottom-0 bg-gradient-to-t from-ink/70 to-transparent px-6 pb-5 pt-16 text-white">
          <h3 class="font-serif text-[clamp(1.6rem,2.6vw,2.2rem)] font-normal">{{ active.name }}</h3>
          <p class="mt-1 text-[12px] text-white/80">{{ active.note }}</p>
        </div>
      </div>

      <!-- Selettore -->
      <div class="flex flex-col justify-center p-6 md:p-[clamp(25px,3vw,44px)]">
        <span class="text-[9px] font-extrabold tracking-[.16em] text-[#b65a1c]">SCEGLI LA FAMIGLIA</span>
        <div class="mt-4 grid grid-cols-2 gap-2" role="group" aria-label="Famiglie di prodotto">
          <button
            v-for="item in catalog"
            :key="item.key"
            type="button"
            class="flex items-center gap-2.5 border p-1.5 text-left transition hover:bg-[#fff8f1]"
            :class="item.key === activeKey ? 'border-brand bg-paper' : 'border-transparent'"
            :aria-pressed="item.key === activeKey"
            @click="activeKey = item.key"
          >
            <img :src="item.image" alt="" loading="lazy" class="size-11 shrink-0 object-cover">
            <span class="text-[11px] font-bold leading-tight">{{ item.name }}</span>
          </button>
        </div>

        <div class="mt-6 flex flex-wrap justify-between gap-2.5 border-t border-[#e3d1c0] pt-[18px] text-[10px] text-[#7e6d60]">
          <span>Non trovi il profilo che cerchi?</span>
          <a href="#contatti" class="font-extrabold text-[#b95313]">Realizziamo su disegno ↗</a>
        </div>
      </div>
    </div>
  </section>
</template>
