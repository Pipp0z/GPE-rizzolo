<script setup lang="ts">
const activeSlug = ref(families[0]!.slug)
const active = computed(() => families.find(f => f.slug === activeSlug.value)!)
const pad = (n: number) => String(n).padStart(2, '0')
</script>

<template>
  <section id="prodotti" class="blueprint-dark bg-ink section-pad text-white">
    <div class="wrap">
      <div v-reveal class="mb-12 flex flex-col justify-between gap-6 md:flex-row md:items-end">
        <div>
          <p class="kicker !text-brand"><b>02</b> Prodotti</p>
          <h2 class="display mt-5 text-[clamp(3rem,8vw,7rem)] !text-white">Ogni profilo,<br>una sezione.</h2>
        </div>
        <p class="max-w-[360px] text-[16px] leading-relaxed text-white/70">
          {{ families.length }} famiglie di prodotto, tutte realizzabili nell’essenza e nella sezione che serve al tuo progetto.
        </p>
      </div>

      <div class="grid gap-10 lg:grid-cols-[1.15fr_.85fr] lg:gap-14">
        <ul class="border-b border-white/15" @mouseleave="activeSlug = activeSlug">
          <li v-for="(f, i) in families" :key="f.slug" class="border-t border-white/15">
            <NuxtLink
              :to="`/prodotti/${f.slug}`"
              class="group flex items-center gap-4 py-4 transition md:gap-6 md:py-5"
              @mouseenter="activeSlug = f.slug"
              @focus="activeSlug = f.slug"
            >
              <span class="w-8 font-mono text-[13px] text-white/40 transition group-hover:text-brand">{{ pad(i + 1) }}</span>
              <span
                class="display flex-1 text-[clamp(1.9rem,4.2vw,3.4rem)] transition duration-300 group-hover:translate-x-2"
                :class="f.slug === activeSlug ? '!text-brand' : '!text-white'"
              >{{ f.name }}</span>
              <NuxtImg format="webp" :src="f.image" alt="" width="96" height="64" loading="lazy" class="h-12 w-[72px] shrink-0 object-cover lg:hidden" />
              <span class="hidden font-mono text-xl text-white/40 transition group-hover:translate-x-1 group-hover:text-brand lg:inline">→</span>
            </NuxtLink>
          </li>
        </ul>

        <!-- Anteprima (desktop) -->
        <div class="relative hidden lg:block">
          <div class="sticky top-28">
            <div class="relative aspect-[4/5] overflow-hidden bg-ink-2">
              <Transition
                mode="out-in"
                enter-active-class="transition duration-300"
                leave-active-class="transition duration-150"
                enter-from-class="opacity-0 scale-[1.03]"
                leave-to-class="opacity-0"
              >
                <NuxtImg
                  :key="active.slug"
                  format="webp"
                  :src="active.image"
                  :alt="`${active.name} in legno`"
                  width="900"
                  height="1125"
                  class="absolute inset-0 size-full object-cover"
                />
              </Transition>
              <span class="absolute left-4 top-4 bg-brand px-2 py-1 font-mono text-[11px] font-medium uppercase tracking-[.12em] text-ink">Fig. {{ pad(families.indexOf(active) + 1) }}</span>
              <div class="absolute inset-x-0 bottom-0 bg-gradient-to-t from-ink via-ink/80 to-transparent p-6 pt-24">
                <p class="text-[15px] leading-relaxed text-white/85">{{ active.intro }}</p>
                <NuxtLink :to="`/prodotti/${active.slug}`" class="mt-3 inline-block font-mono text-[12px] font-medium uppercase tracking-[.12em] text-brand underline underline-offset-4">Vai alla scheda →</NuxtLink>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </section>
</template>
