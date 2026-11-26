<script setup lang="ts">
const props = defineProps<{ family: Family, child: FamilyChild | null }>()
const { specSheet } = useContent()
const emit = defineEmits<{ close: [] }>()

const dialog = ref<HTMLElement | null>(null)

function onKey(e: KeyboardEvent) {
  if (e.key === 'Escape') emit('close')
}

watch(() => props.child, async (child) => {
  document.body.style.overflow = child ? 'hidden' : ''
  if (child) {
    await nextTick()
    dialog.value?.focus()
  }
})

onMounted(() => document.addEventListener('keydown', onKey))
onBeforeUnmount(() => {
  document.removeEventListener('keydown', onKey)
  document.body.style.overflow = ''
})
</script>

<template>
  <Teleport to="body">
    <Transition
      enter-active-class="transition duration-300"
      leave-active-class="transition duration-200"
      enter-from-class="opacity-0"
      leave-to-class="opacity-0"
    >
      <div v-if="child" class="fixed inset-0 z-[60] grid place-items-center bg-ink/85 p-4 backdrop-blur-sm" @click.self="emit('close')">
        <div
          ref="dialog"
          role="dialog"
          aria-modal="true"
          :aria-label="$t('modal.title', { name: child.name })"
          tabindex="-1"
          class="relative grid max-h-[calc(100vh-2rem)] w-full max-w-[1000px] overflow-auto border-2 border-ink bg-paper shadow-[12px_12px_0_#ee7623] outline-none md:grid-cols-[1fr_1.1fr]"
        >
          <button class="absolute right-3 top-3 z-10 grid size-11 place-items-center border-2 border-ink bg-paper font-mono text-lg hover:bg-ink hover:text-white" :aria-label="$t('modal.close')" @click="emit('close')">✕</button>

          <div class="relative min-h-[240px] bg-cream md:min-h-[520px]">
            <NuxtImg format="webp" :src="child.image" :alt="$t('prod.alt', { name: child.name })" width="900" height="900" class="photo-ink absolute inset-0 size-full object-cover" />
            <span class="absolute bottom-4 left-4 bg-ink px-2 py-1 font-mono text-[11px] uppercase tracking-[.12em] text-white">{{ family.name }}</span>
          </div>

          <div class="p-6 md:p-10">
            <p class="kicker"><b>↗</b> {{ $t('spec.title') }}</p>
            <h2 class="display mt-3 text-[clamp(2.2rem,4vw,3.4rem)]">{{ child.name }}</h2>
            <div class="mt-4 space-y-3 text-[16px] leading-[1.7]">
              <p>{{ child.text }}</p>
            </div>

            <dl class="mt-6 border-t-2 border-ink font-mono text-[13px]">
              <div v-for="r in specSheet(child.specs)" :key="r.label" class="grid grid-cols-[110px_1fr] gap-4 border-b border-line py-2.5">
                <dt class="uppercase tracking-[.1em] text-muted">{{ r.label }}</dt>
                <dd class="text-ink">{{ r.value }}</dd>
              </div>
            </dl>

            <div class="mt-7 flex flex-wrap gap-3">
              <NuxtLinkLocale :to="{ path: '/contatti', query: { prodotto: family.slug, dettaglio: child.name } }" class="btn" @click="emit('close')">{{ $t('cta.btn') }}</NuxtLinkLocale>
              <a v-if="child.pdf" :href="child.pdf" target="_blank" rel="noopener" download class="btn btn-secondary">{{ $t('modal.pdf') }}</a>
            </div>
          </div>
        </div>
      </div>
    </Transition>
  </Teleport>
</template>
