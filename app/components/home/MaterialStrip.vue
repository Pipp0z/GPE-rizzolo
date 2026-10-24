<template>
  <div v-reveal class="mt-14 grid items-stretch gap-3 md:grid-cols-[1.1fr_1.6fr]">
    <div class="flex flex-col justify-center bg-sand p-6 md:p-8">
      <span class="eyebrow">La materia prima</span>
      <h3 class="my-4 font-serif text-[30px] font-normal leading-[1.05]">Ogni venatura<br>ha la sua storia.</h3>
      <p class="text-[11px] leading-[1.7] text-muted">
        Lavoriamo qualsiasi essenza di legno, dalla scelta del materiale alla profilatura, con attenzione a
        precisione e qualità della finitura.
      </p>
      <ul class="mt-5 flex flex-wrap gap-1.5">
        <li v-for="e in essences" :key="e" class="border border-[#d9c6b5] px-2.5 py-1 text-[10px] text-[#5b4b3e]">{{ e }}</li>
      </ul>
    </div>
    <img :src="images.essenze" alt="Alcune tipologie di legno: abete, pino, larice, meranti, okumè, rovere, frassino" loading="lazy" class="h-[260px] w-full object-cover md:h-full md:min-h-[320px]">
  </div>
</template>
