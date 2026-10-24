<script setup lang="ts">
const route = useRoute()

const initialProduct = familyBySlug(String(route.query.prodotto ?? ''))?.name ?? ''

const form = reactive({
  name: '',
  company: '',
  email: '',
  phone: '',
  product: initialProduct,
  essence: '',
  message: '',
  privacy: false,
  website: '',
})

const status = ref<'idle' | 'sending' | 'sent' | 'error'>('idle')
const error = ref('')

async function submit() {
  status.value = 'sending'
  error.value = ''
  try {
    await $fetch('/api/contact', { method: 'POST', body: form })
    status.value = 'sent'
  }
  catch (e: any) {
    error.value = e?.data?.statusMessage || 'Invio non riuscito. Riprova o scrivici a ' + company.email
    status.value = 'error'
  }
}

const field = 'w-full border-2 border-ink bg-cream px-3.5 py-3 text-[15px] text-ink outline-none transition focus:bg-white focus:shadow-[4px_4px_0_#ee7623]'
const label = 'mb-1.5 block font-mono text-[12px] font-medium uppercase tracking-[.1em] text-ink'
</script>

<template>
  <div v-if="status === 'sent'" class="border-2 border-ink bg-cream p-8 shadow-[8px_8px_0_#ee7623]" role="status">
    <h3 class="display text-[40px]">Richiesta inviata</h3>
    <p class="mt-3 text-[15px] leading-relaxed text-muted">
      Grazie {{ form.name }}, abbiamo ricevuto la tua richiesta e ti risponderemo il prima possibile.
    </p>
  </div>

  <form v-else class="grid gap-4 sm:grid-cols-2" novalidate @submit.prevent="submit">
    <div>
      <label for="cf-name" :class="label">Nome e cognome *</label>
      <input id="cf-name" v-model="form.name" :class="field" required autocomplete="name">
    </div>
    <div>
      <label for="cf-company" :class="label">Azienda</label>
      <input id="cf-company" v-model="form.company" :class="field" autocomplete="organization">
    </div>
    <div>
      <label for="cf-email" :class="label">Email *</label>
      <input id="cf-email" v-model="form.email" type="email" :class="field" required autocomplete="email">
    </div>
    <div>
      <label for="cf-phone" :class="label">Telefono</label>
      <input id="cf-phone" v-model="form.phone" type="tel" :class="field" autocomplete="tel">
    </div>
    <div>
      <label for="cf-product" :class="label">Prodotto di interesse</label>
      <select id="cf-product" v-model="form.product" :class="field">
        <option value="">Seleziona…</option>
        <option v-for="f in families" :key="f.slug" :value="f.name">{{ f.name }}</option>
        <option value="Altro">Altro / su disegno</option>
      </select>
    </div>
    <div>
      <label for="cf-essence" :class="label">Essenza di legno</label>
      <input id="cf-essence" v-model="form.essence" list="essences" :class="field" placeholder="es. rovere, abete…">
      <datalist id="essences"><option v-for="e in essences" :key="e" :value="e" /></datalist>
    </div>
    <div class="sm:col-span-2">
      <label for="cf-message" :class="label">Descrivi la tua richiesta *</label>
      <textarea id="cf-message" v-model="form.message" rows="5" :class="field" required placeholder="Sezione, lunghezza, quantità, finitura… Puoi anche rispondere alla nostra email con un disegno o una foto." />
    </div>

    <!-- honeypot -->
    <input v-model="form.website" class="hidden" tabindex="-1" autocomplete="off" aria-hidden="true">

    <label class="flex items-start gap-2.5 text-[13px] leading-snug text-muted sm:col-span-2">
      <input v-model="form.privacy" type="checkbox" class="mt-0.5 size-4 accent-brand" required>
      <span>Ho letto l’<NuxtLink to="/privacy" class="font-semibold text-brand-ink underline">informativa privacy</NuxtLink> e acconsento al trattamento dei dati per rispondere alla richiesta. *</span>
    </label>

    <p v-if="status === 'error'" class="text-[14px] font-semibold text-red-700 sm:col-span-2" role="alert">{{ error }}</p>

    <div class="sm:col-span-2">
      <button type="submit" class="btn disabled:opacity-60" :disabled="status === 'sending'">
        {{ status === 'sending' ? 'Invio in corso…' : 'Invia richiesta ↗' }}
      </button>
    </div>
  </form>
</template>
