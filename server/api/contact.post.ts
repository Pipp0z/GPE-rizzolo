import nodemailer from 'nodemailer'

interface ContactBody {
  name?: string
  company?: string
  email?: string
  phone?: string
  product?: string
  essence?: string
  message?: string
  privacy?: boolean
  /** honeypot: deve restare vuoto */
  website?: string
}

const clean = (v: unknown, max = 2000) => String(v ?? '').trim().slice(0, max)
const isEmail = (v: string) => /^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(v)

export default defineEventHandler(async (event) => {
  const body = await readBody<ContactBody>(event)

  // I bot compilano il campo nascosto: rispondiamo ok senza inviare nulla.
  if (body.website) return { ok: true }

  const name = clean(body.name, 120)
  const email = clean(body.email, 200)
  const message = clean(body.message)

  if (!name || !isEmail(email) || message.length < 5) {
    throw createError({ statusCode: 400, statusMessage: 'Compila nome, email valida e messaggio.' })
  }
  if (!body.privacy) {
    throw createError({ statusCode: 400, statusMessage: 'Devi accettare l’informativa privacy.' })
  }

  const { smtp } = useRuntimeConfig(event)
  if (!smtp.host) {
    console.warn('[contact] SMTP non configurato, richiesta non inviata:', { name, email })
    throw createError({ statusCode: 503, statusMessage: 'Invio non disponibile al momento. Scrivici a info@gperizzolo.it.' })
  }

  const lines = [
    `Nome: ${name}`,
    `Azienda: ${clean(body.company, 160) || '-'}`,
    `Email: ${email}`,
    `Telefono: ${clean(body.phone, 40) || '-'}`,
    `Prodotto: ${clean(body.product, 120) || '-'}`,
    `Essenza: ${clean(body.essence, 120) || '-'}`,
    '',
    message,
  ]

  const transport = nodemailer.createTransport({
    host: smtp.host,
    port: Number(smtp.port),
    secure: Number(smtp.port) === 465,
    auth: smtp.user ? { user: smtp.user, pass: smtp.pass } : undefined,
  })

  await transport.sendMail({
    from: smtp.from || smtp.user,
    to: smtp.to,
    replyTo: email,
    subject: `Richiesta preventivo dal sito - ${clean(body.product, 120) || name}`,
    text: lines.join('\n'),
  })

  return { ok: true }
})
