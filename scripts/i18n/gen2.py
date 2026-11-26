from gen1 import T, a

# --- Form
a('form.name', 'Nome e cognome *', 'Full name *', 'Nom et prénom *', 'Vor- und Nachname *')
a('form.company', 'Azienda', 'Company', 'Entreprise', 'Unternehmen')
a('form.email', 'Email *', 'Email *', 'E-mail *', 'E-Mail *')
a('form.phone', 'Telefono', 'Phone', 'Téléphone', 'Telefon')
a('form.product', 'Prodotto di interesse', 'Product of interest', 'Produit concerné', 'Gewünschtes Produkt')
a('form.select', 'Seleziona…', 'Select…', 'Sélectionner…', 'Auswählen…')
a('form.other', 'Altro / su disegno', 'Other / to drawing', 'Autre / sur plan', 'Sonstiges / nach Zeichnung')
a('form.essence', 'Essenza di legno', 'Wood species', 'Essence de bois', 'Holzart')
a('form.essencePh', 'es. rovere, abete…', 'e.g. oak, fir…', 'ex. chêne, sapin…', 'z. B. Eiche, Tanne…')
a('form.message', 'Descrivi la tua richiesta *', 'Describe your request *', 'Décrivez votre demande *', 'Beschreiben Sie Ihre Anfrage *')
a('form.messagePh', 'Sezione, lunghezza, quantità, finitura… Puoi anche rispondere alla nostra email con un disegno o una foto.',
  'Section, length, quantity, finish… You can also reply to our email with a drawing or a photo.',
  'Section, longueur, quantité, finition… Vous pouvez aussi répondre à notre e-mail avec un plan ou une photo.',
  'Querschnitt, Länge, Menge, Oberfläche… Sie können auch auf unsere E-Mail mit einer Zeichnung oder einem Foto antworten.')
a('form.privacy', 'Ho letto l’{link} e acconsento al trattamento dei dati per rispondere alla richiesta. *',
  'I have read the {link} and consent to the processing of my data to answer my request. *',
  "J'ai lu la {link} et j'accepte le traitement de mes données pour répondre à ma demande. *",
  'Ich habe die {link} gelesen und stimme der Verarbeitung meiner Daten zur Beantwortung meiner Anfrage zu. *')
a('form.privacyLink', 'informativa privacy', 'privacy notice', 'politique de confidentialité', 'Datenschutzerklärung')
a('form.send', 'Invia richiesta ↗', 'Send request ↗', 'Envoyer la demande ↗', 'Anfrage senden ↗')
a('form.sending', 'Invio in corso…', 'Sending…', 'Envoi en cours…', 'Wird gesendet…')
a('form.sentTitle', 'Richiesta inviata', 'Request sent', 'Demande envoyée', 'Anfrage gesendet')
a('form.sentText', 'Grazie {name}, abbiamo ricevuto la tua richiesta e ti risponderemo il prima possibile.',
  'Thank you {name}, we have received your request and will reply as soon as possible.',
  'Merci {name}, nous avons bien reçu votre demande et vous répondrons au plus vite.',
  'Vielen Dank {name}, wir haben Ihre Anfrage erhalten und antworten so schnell wie möglich.')
a('form.errValid', 'Compila nome, email valida e messaggio.', 'Please fill in your name, a valid email and a message.', 'Veuillez renseigner votre nom, un e-mail valide et un message.', 'Bitte geben Sie Namen, eine gültige E-Mail-Adresse und eine Nachricht an.')
a('form.errUnavail', 'Invio non disponibile al momento. Scrivici a {email}.', 'Sending is currently unavailable. Please write to {email}.', "L'envoi n'est pas disponible pour le moment. Écrivez-nous à {email}.", 'Der Versand ist derzeit nicht verfügbar. Schreiben Sie uns an {email}.')
a('form.errGeneric', 'Invio non riuscito. Riprova o scrivici a {email}.', 'Sending failed. Try again or write to {email}.', "L'envoi a échoué. Réessayez ou écrivez-nous à {email}.", 'Senden fehlgeschlagen. Versuchen Sie es erneut oder schreiben Sie an {email}.')
a('form.prefill', 'Richiesta per: {detail}', 'Request for: {detail}', 'Demande pour : {detail}', 'Anfrage für: {detail}')

# --- Scheda tecnica / modale / pagina prodotto
a('spec.title', 'Scheda tecnica', 'Technical sheet', 'Fiche technique', 'Datenblatt')
a('spec.essences', 'Essenze', 'Woods', 'Essences', 'Holzarten')
a('spec.essencesV', 'Qualsiasi essenza di legno', 'Any wood species', 'Toutes les essences de bois', 'Jede Holzart')
a('spec.origin', 'Provenienza', 'Origin', 'Origine', 'Herkunft')
a('spec.originV', 'Produzione interamente a Santa Giustina in Colle (PD), Italia', 'Produced entirely in Santa Giustina in Colle (Padua), Italy', 'Produit entièrement à Santa Giustina in Colle (Padoue), Italie', 'Vollständig in Santa Giustina in Colle (Padua), Italien gefertigt')
a('spec.production', 'Produzione', 'Production', 'Production', 'Fertigung')
a('spec.productionV', 'In asta, in serie o su disegno', 'In lengths, in series or to drawing', 'En barres, en série ou sur plan', 'Als Stangenware, in Serie oder nach Zeichnung')
a('spec.sizes', 'Misure', 'Sizes', 'Dimensions', 'Maße')
a('spec.finishes', 'Finiture', 'Finishes', 'Finitions', 'Oberflächen')
a('spec.onRequest', 'Su richiesta', 'On request', 'Sur demande', 'Auf Anfrage')
a('spec.cert', 'Certificazione', 'Certification', 'Certification', 'Zertifizierung')
a('spec.certV', 'FSC® disponibile su richiesta', 'FSC® available on request', 'FSC® disponible sur demande', 'FSC® auf Anfrage')
a('modal.title', 'Scheda tecnica {name}', 'Technical sheet {name}', 'Fiche technique {name}', 'Datenblatt {name}')
a('modal.close', 'Chiudi', 'Close', 'Fermer', 'Schließen')
a('modal.pdf', 'Scheda PDF ↓', 'PDF sheet ↓', 'Fiche PDF ↓', 'Datenblatt PDF ↓')
a('prod.alt', '{name} in legno - G.P.E. Rizzolo', '{name} in wood - G.P.E. Rizzolo', '{name} en bois - G.P.E. Rizzolo', '{name} aus Holz - G.P.E. Rizzolo')
a('prod.uses', 'Applicazioni', 'Applications', 'Applications', 'Anwendungen')
a('prod.related', 'Altri prodotti', 'Other products', 'Autres produits', 'Weitere Produkte')
a('prod.inCat', 'In questa categoria', 'In this category', 'Dans cette catégorie', 'In dieser Kategorie')
a('prod.includes', 'Cosa comprende', 'What it includes', 'Ce que cela comprend', 'Das gehört dazu')
a('prod.open', 'Apri scheda tecnica +', 'Open technical sheet +', 'Ouvrir la fiche technique +', 'Datenblatt öffnen +')
a('prod.notFound', 'Prodotto non trovato', 'Product not found', 'Produit introuvable', 'Produkt nicht gefunden')
a('prods.title', 'I nostri profili in legno', 'Our wooden profiles', 'Nos profils en bois', 'Unsere Holzprofile')
a('prods.intro', 'La profilatura in asta è la nostra attività principale. Lavoriamo qualsiasi essenza di legno, in serie o su disegno.',
  'Profiling in lengths is our core business. We work any kind of wood, in series or to your drawing.',
  'Le profilage en barres est notre activité principale. Nous travaillons toutes les essences de bois, en série ou sur plan.',
  'Das Profilieren von Stangenware ist unsere Hauptaufgabe. Wir verarbeiten jede Holzart, in Serie oder nach Zeichnung.')
a('prods.also', 'Produciamo anche: {list}. {link} per la tua richiesta.', 'We also produce: {list}. {link} with your request.', 'Nous fabriquons aussi : {list}. {link} pour votre demande.', 'Wir fertigen außerdem: {list}. {link} für Ihre Anfrage.')
a('prods.contact', 'Contattaci', 'Contact us', 'Contactez-nous', 'Kontaktieren Sie uns')

# --- Contatti
a('contact.title', 'Richiedi un preventivo', 'Request a quote', 'Demander un devis', 'Angebot anfragen')
a('contact.intro', 'Raccontaci cosa ti serve: profilo, essenza, quantità. Se hai un disegno o un campione, mandacelo e valutiamo insieme.',
  'Tell us what you need: profile, wood, quantity. If you have a drawing or a sample, send it to us and we will assess it together.',
  "Dites-nous ce dont vous avez besoin : profil, essence, quantité. Si vous avez un plan ou un échantillon, envoyez-le-nous et nous l'étudierons ensemble.",
  'Sagen Sie uns, was Sie brauchen: Profil, Holzart, Menge. Wenn Sie eine Zeichnung oder ein Muster haben, senden Sie es uns – wir prüfen es gemeinsam.')
a('contact.maps', 'Apri su Google Maps ↗', 'Open in Google Maps ↗', 'Ouvrir dans Google Maps ↗', 'In Google Maps öffnen ↗')

# --- Pagine: SEO e titoli
a('seo.home.title', "G.P.E. Rizzolo {'|'} Profili in legno su misura dal 1960", "G.P.E. Rizzolo {'|'} Made-to-measure wood profiles since 1960", "G.P.E. Rizzolo {'|'} Profils en bois sur mesure depuis 1960", "G.P.E. Rizzolo {'|'} Holzprofile nach Maß seit 1960")
a('seo.home.desc', 'Produzione di profili in legno su misura a Santa Giustina in Colle (PD): profili per quadri, battiscopa, serramenti, corrimano, boiserie e lavorazioni speciali. Dal 1960. Produzione interamente locale.',
  'Made-to-measure wood profiles manufactured in Santa Giustina in Colle (Padua, Italy): picture frame mouldings, skirting boards, window profiles, handrails, wall panelling and special pieces. Since 1960. All production is local.',
  'Fabrication de profils en bois sur mesure à Santa Giustina in Colle (Padoue, Italie) : moulures pour cadres, plinthes, profils pour menuiseries, mains courantes, boiseries et pièces spéciales. Depuis 1960. Production entièrement locale.',
  'Herstellung von Holzprofilen nach Maß in Santa Giustina in Colle (Padua, Italien): Bilderrahmenprofile, Sockelleisten, Fensterprofile, Handläufe, Wandvertäfelungen und Sonderanfertigungen. Seit 1960. Gesamte Fertigung vor Ort.')
a('seo.prods.title', 'Profili in legno: tutti i prodotti', 'Wooden profiles: all products', 'Profils en bois : tous les produits', 'Holzprofile: alle Produkte')
a('seo.prods.desc', 'Battiscopa, profili per quadri, serramenti, perlinati, saune, semilavorati, profili di finitura e boiserie: produzione su misura G.P.E. Rizzolo.',
  'Skirting boards, picture frame mouldings, window profiles, tongue-and-groove boards, saunas, semi-finished products, finishing profiles and wall panelling: made-to-measure production by G.P.E. Rizzolo.',
  'Plinthes, moulures pour cadres, profils pour menuiseries, lambris, saunas, produits semi-finis, profils de finition et boiseries : fabrication sur mesure G.P.E. Rizzolo.',
  'Sockelleisten, Bilderrahmenprofile, Fenster- und Türprofile, Profilbretter, Saunen, Halbfabrikate, Abschlussprofile und Wandvertäfelungen: Fertigung nach Maß von G.P.E. Rizzolo.')
a('seo.contact.title', 'Contatti e richiesta preventivo', 'Contact and quote request', 'Contact et demande de devis', 'Kontakt und Angebotsanfrage')
a('seo.contact.desc', 'Richiedi un preventivo per profili in legno su misura. G.P.E. Rizzolo, {address}. Tel. {phone}.',
  'Request a quote for made-to-measure wood profiles. G.P.E. Rizzolo, {address}. Tel. {phone}.',
  'Demandez un devis pour des profils en bois sur mesure. G.P.E. Rizzolo, {address}. Tél. {phone}.',
  'Fordern Sie ein Angebot für Holzprofile nach Maß an. G.P.E. Rizzolo, {address}. Tel. {phone}.')
a('seo.company.title', 'L’azienda: storia, valori e obiettivi', 'The company: history, values and goals', "L'entreprise : histoire, valeurs et objectifs", 'Das Unternehmen: Geschichte, Werte und Ziele')
a('seo.company.desc', 'G.P.E. Rizzolo produce profili in legno dal 1960 a Santa Giustina in Colle (PD). Tre generazioni di esperienza, valori e obiettivi: qualità, serietà e soddisfazione del cliente.',
  'G.P.E. Rizzolo has produced wood profiles since 1960 in Santa Giustina in Colle (Padua). Three generations of experience, values and goals: quality, reliability and customer satisfaction.',
  "G.P.E. Rizzolo fabrique des profils en bois depuis 1960 à Santa Giustina in Colle (Padoue). Trois générations d'expérience, de valeurs et d'objectifs : qualité, sérieux et satisfaction du client.",
  'G.P.E. Rizzolo fertigt seit 1960 Holzprofile in Santa Giustina in Colle (Padua). Drei Generationen Erfahrung, Werte und Ziele: Qualität, Zuverlässigkeit und Kundenzufriedenheit.')
a('seo.certs.title', 'Certificazioni FSC® e ISO 14001', 'FSC® and ISO 14001 certifications', 'Certifications FSC® et ISO 14001', 'Zertifizierungen FSC® und ISO 14001')
a('seo.certs.desc', 'G.P.E. Rizzolo è certificata FSC® (C184281) e ISO 14001:2015 (UKAS). Prodotti in legno certificati FSC® disponibili su richiesta.',
  'G.P.E. Rizzolo is FSC® (C184281) and ISO 14001:2015 (UKAS) certified. FSC®-certified wood products available on request.',
  'G.P.E. Rizzolo est certifiée FSC® (C184281) et ISO 14001:2015 (UKAS). Produits en bois certifiés FSC® disponibles sur demande.',
  'G.P.E. Rizzolo ist nach FSC® (C184281) und ISO 14001:2015 (UKAS) zertifiziert. FSC®-zertifizierte Holzprodukte auf Anfrage.')
a('seo.privacy.title', 'Informativa privacy', 'Privacy notice', 'Politique de confidentialité', 'Datenschutzerklärung')
a('seo.privacy.desc', 'Informativa sul trattamento dei dati personali raccolti tramite il sito di G.P.E. Rizzolo.', 'Information on the processing of personal data collected through the G.P.E. Rizzolo website.', 'Informations sur le traitement des données personnelles collectées via le site de G.P.E. Rizzolo.', 'Informationen zur Verarbeitung personenbezogener Daten über die Website von G.P.E. Rizzolo.')
a('page.company', 'Tre generazioni di legno', 'Three generations of wood', 'Trois générations de bois', 'Drei Generationen Holz')
a('page.companyIntro', 'Nobile arte che attraversa tre generazioni: dal 1960 profili in legno di qualità, su misura.',
  'A noble craft spanning three generations: quality wood profiles, made to measure, since 1960.',
  'Un noble métier qui traverse trois générations : depuis 1960, des profils en bois de qualité, sur mesure.',
  'Ein edles Handwerk über drei Generationen: seit 1960 hochwertige Holzprofile nach Maß.')
a('hist.kicker', 'La nostra storia', 'Our history', 'Notre histoire', 'Unsere Geschichte')
a('hist.t1', 'Dal 1960,', 'Since 1960,', 'Depuis 1960,', 'Seit 1960,')
a('hist.t2', 'di padre in figlio.', 'from father to son.', 'de père en fils.', 'von Generation zu Generation.')
a('hist.p', 'Passione, esperienza, qualità, serietà, puntualità e dedizione sono i sei punti cardine tramandati da papà Guerrino ai figli Paolo ed Elio e oggi al nipote Samuel, su cui G.P.E. Rizzolo si fonda.',
  'Passion, experience, quality, reliability, punctuality and dedication are the six cornerstones handed down by father Guerrino to his sons Paolo and Elio and today to his grandson Samuel, on which G.P.E. Rizzolo is built.',
  "La passion, l'expérience, la qualité, le sérieux, la ponctualité et le dévouement sont les six piliers transmis par papa Guerrino à ses fils Paolo et Elio et aujourd'hui à son petit-fils Samuel, sur lesquels G.P.E. Rizzolo est fondée.",
  'Leidenschaft, Erfahrung, Qualität, Zuverlässigkeit, Pünktlichkeit und Hingabe sind die sechs Grundpfeiler, die Vater Guerrino an die Söhne Paolo und Elio und heute an den Enkel Samuel weitergegeben hat und auf denen G.P.E. Rizzolo gründet.')
a('hist.1l', '1960', '1960', '1960', '1960')
a('hist.1t', 'Nasce G.P.E. Rizzolo', 'G.P.E. Rizzolo is founded', 'Naissance de G.P.E. Rizzolo', 'Gründung von G.P.E. Rizzolo')
a('hist.1', 'Inizia a Santa Giustina in Colle la produzione di profili in legno.', 'Production of wood profiles begins in Santa Giustina in Colle.', 'La production de profils en bois commence à Santa Giustina in Colle.', 'In Santa Giustina in Colle beginnt die Herstellung von Holzprofilen.')
a('hist.2l', 'Prima generazione', 'First generation', 'Première génération', 'Erste Generation')
a('hist.2t', 'Guerrino', 'Guerrino', 'Guerrino', 'Guerrino')
a('hist.2', 'Il mestiere e i suoi valori vengono tramandati di padre in figlio.', 'The craft and its values are handed down from father to son.', 'Le métier et ses valeurs se transmettent de père en fils.', 'Das Handwerk und seine Werte werden vom Vater an den Sohn weitergegeben.')
a('hist.3l', 'Seconda generazione', 'Second generation', 'Deuxième génération', 'Zweite Generation')
a('hist.3t', 'Paolo ed Elio', 'Paolo and Elio', 'Paolo et Elio', 'Paolo und Elio')
a('hist.3', 'I figli portano avanti l’azienda, tra filosofia del passato e innovazione.', 'The sons carry the company forward, between the philosophy of the past and innovation.', "Les fils font avancer l'entreprise, entre philosophie du passé et innovation.", 'Die Söhne führen das Unternehmen weiter – zwischen Philosophie der Vergangenheit und Innovation.')
a('hist.4l', 'Oggi', 'Today', "Aujourd'hui", 'Heute')
a('hist.4t', 'I nipoti', 'The grandchildren', 'Les petits-enfants', 'Die Enkel')
a('hist.4', 'Con i nipoti entra la terza generazione: tradizione e sguardo al futuro.', 'With the grandchildren the third generation arrives: tradition and a look to the future.', "Avec les petits-enfants arrive la troisième génération : tradition et regard vers l'avenir.", 'Mit den Enkeln kommt die dritte Generation: Tradition und Blick in die Zukunft.')
a('values.kicker', 'I nostri valori', 'Our values', 'Nos valeurs', 'Unsere Werte')
a('values.t', 'Sei punti cardine.', 'Six cornerstones.', 'Six piliers.', 'Sechs Grundpfeiler.')
V = [
 ('Passione', 'Passion', 'Passion', 'Leidenschaft', 'Il legno è il nostro mestiere da oltre sessant’anni, e si vede nei dettagli.', 'Wood has been our trade for over sixty years, and it shows in the details.', 'Le bois est notre métier depuis plus de soixante ans, et cela se voit dans les détails.', 'Holz ist seit über sechzig Jahren unser Handwerk – und das sieht man an den Details.'),
 ('Esperienza', 'Experience', 'Expérience', 'Erfahrung', 'Tre generazioni di competenza nella profilatura in asta.', 'Three generations of expertise in profiling lengths.', 'Trois générations de savoir-faire dans le profilage en barres.', 'Drei Generationen Kompetenz im Profilieren von Stangenware.'),
 ('Qualità', 'Quality', 'Qualité', 'Qualität', 'Precisione e accuratezza delle finiture, su qualsiasi essenza.', 'Precision and accuracy of finishes, on any wood.', 'Précision et soin des finitions, sur toutes les essences.', 'Präzision und Sorgfalt bei den Oberflächen, in jeder Holzart.'),
 ('Serietà', 'Reliability', 'Sérieux', 'Zuverlässigkeit', 'Ascoltiamo, ci impegniamo e manteniamo quello che promettiamo.', 'We listen, we commit and we keep our promises.', 'Nous écoutons, nous nous engageons et nous tenons nos promesses.', 'Wir hören zu, setzen uns ein und halten, was wir versprechen.'),
 ('Puntualità', 'Punctuality', 'Ponctualité', 'Pünktlichkeit', 'Rispettiamo i tempi concordati, perché i vostri tempi sono i nostri.', 'We keep to agreed deadlines, because your deadlines are ours.', 'Nous respectons les délais convenus, car vos délais sont les nôtres.', 'Wir halten vereinbarte Termine ein, denn Ihre Termine sind unsere.'),
 ('Dedizione', 'Dedication', 'Dévouement', 'Hingabe', 'Ogni richiesta, standard o su disegno, riceve la stessa cura.', 'Every request, standard or to drawing, receives the same care.', 'Chaque demande, standard ou sur plan, reçoit le même soin.', 'Jede Anfrage, ob Standard oder nach Zeichnung, erhält die gleiche Sorgfalt.'),
]
for i, v in enumerate(V, 1):
    a(f'value.{i}', v[0], v[1], v[2], v[3]); a(f'value.{i}t', v[4], v[5], v[6], v[7])
a('goals.kicker', 'I nostri obiettivi', 'Our goals', 'Nos objectifs', 'Unsere Ziele')
a('goals.t1', 'Guardiamo avanti,', 'We look ahead,', "Nous regardons vers l'avenir,", 'Wir schauen nach vorn,')
a('goals.t2', 'senza perdere il passato.', 'without losing the past.', 'sans perdre le passé.', 'ohne die Vergangenheit zu verlieren.')
G = [
 ('Soddisfazione del cliente', 'Customer satisfaction', 'Satisfaction du client', 'Kundenzufriedenheit', 'Ogni prodotto nasce con un solo obiettivo: soddisfare chi lo ordina.', 'Every product is made with one goal: to satisfy whoever orders it.', 'Chaque produit naît avec un seul objectif : satisfaire celui qui le commande.', 'Jedes Produkt entsteht mit einem Ziel: den zufriedenzustellen, der es bestellt.'),
 ('Tradizione e innovazione', 'Tradition and innovation', 'Tradition et innovation', 'Tradition und Innovation', 'Restiamo saldi alla filosofia del passato, con un occhio attento alle innovazioni tecnologiche e al futuro.', 'We remain faithful to the philosophy of the past, with an eye on technological innovation and the future.', "Nous restons fidèles à la philosophie du passé, avec un œil attentif aux innovations technologiques et à l'avenir.", 'Wir bleiben der Philosophie der Vergangenheit treu – mit Blick auf technische Neuerungen und die Zukunft.'),
 ('Su misura come standard', 'Made to measure as standard', 'Le sur-mesure comme standard', 'Maßanfertigung als Standard', 'Trasformare disegni, campioni e idee in profili precisi, in qualsiasi essenza di legno.', 'Turning drawings, samples and ideas into precise profiles, in any kind of wood.', 'Transformer plans, échantillons et idées en profils précis, dans toutes les essences de bois.', 'Zeichnungen, Muster und Ideen in präzise Profile verwandeln, in jeder Holzart.'),
 ('Legno responsabile', 'Responsible wood', 'Bois responsable', 'Verantwortungsvolles Holz', 'Lavorare nel rispetto dell’ambiente, con prodotti certificati FSC® disponibili su richiesta.', 'Working with respect for the environment, with FSC®-certified products available on request.', "Travailler dans le respect de l'environnement, avec des produits certifiés FSC® disponibles sur demande.", 'Arbeiten im Respekt vor der Umwelt, mit FSC®-zertifizierten Produkten auf Anfrage.'),
]
for i, g in enumerate(G, 1):
    a(f'goal.{i}', g[0], g[1], g[2], g[3]); a(f'goal.{i}t', g[4], g[5], g[6], g[7])
a('brochure.kicker', 'Documentazione', 'Documentation', 'Documentation', 'Dokumentation')
a('brochure.t', 'Scarica la nostra brochure.', 'Download our brochure.', 'Téléchargez notre brochure.', 'Laden Sie unsere Broschüre herunter.')
a('brochure.p', 'La presentazione completa di G.P.E. Rizzolo e dei suoi profili, in italiano e in inglese.', 'The complete presentation of G.P.E. Rizzolo and its profiles, in Italian and English.', 'La présentation complète de G.P.E. Rizzolo et de ses profils, en italien et en anglais.', 'Die vollständige Vorstellung von G.P.E. Rizzolo und seinen Profilen, auf Italienisch und Englisch.')
a('brochure.it', 'Brochure aziendale (italiano)', 'Company brochure (Italian)', "Brochure de l'entreprise (italien)", 'Firmenbroschüre (Italienisch)')
a('brochure.en', 'Company brochure (English)', 'Company brochure (English)', "Brochure de l'entreprise (anglais)", 'Firmenbroschüre (Englisch)')

# --- Privacy (bozza)
a('privacy.controller', 'Titolare del trattamento:', 'Data controller:', 'Responsable du traitement :', 'Verantwortlicher:')
a('privacy.controllerText', '{name}, {address}, P.IVA {vat}, email {email}.', '{name}, {address}, VAT No. {vat}, email {email}.', '{name}, {address}, TVA {vat}, e-mail {email}.', '{name}, {address}, USt-IdNr. {vat}, E-Mail {email}.')
a('privacy.data', 'Dati raccolti:', 'Data collected:', 'Données collectées :', 'Erhobene Daten:')
a('privacy.dataText', 'attraverso il modulo di richiesta preventivo raccogliamo nome, azienda, email, telefono e il contenuto del messaggio.', 'through the quote request form we collect name, company, email, phone number and the content of the message.', 'via le formulaire de demande de devis, nous collectons nom, entreprise, e-mail, téléphone et le contenu du message.', 'über das Angebotsformular erheben wir Name, Unternehmen, E-Mail, Telefonnummer und den Inhalt der Nachricht.')
a('privacy.purpose', 'Finalità e base giuridica:', 'Purpose and legal basis:', 'Finalité et base juridique :', 'Zweck und Rechtsgrundlage:')
a('privacy.purposeText', 'rispondere alle richieste inviate dall’utente (art. 6.1.b GDPR, misure precontrattuali).', 'to reply to requests sent by the user (Art. 6(1)(b) GDPR, pre-contractual measures).', "répondre aux demandes envoyées par l'utilisateur (art. 6.1.b RGPD, mesures précontractuelles).", 'zur Beantwortung der vom Nutzer gesendeten Anfragen (Art. 6 Abs. 1 lit. b DSGVO, vorvertragliche Maßnahmen).')
a('privacy.retention', 'Conservazione:', 'Retention:', 'Conservation :', 'Speicherdauer:')
a('privacy.retentionText', 'i dati sono conservati per il tempo necessario a gestire la richiesta e gli eventuali rapporti commerciali conseguenti.', 'data is kept for as long as necessary to handle the request and any resulting business relationship.', "les données sont conservées le temps nécessaire pour traiter la demande et les éventuelles relations commerciales qui en découlent.", 'die Daten werden so lange gespeichert, wie es für die Bearbeitung der Anfrage und etwaige daraus folgende Geschäftsbeziehungen erforderlich ist.')
a('privacy.rights', 'Diritti:', 'Rights:', 'Droits :', 'Rechte:')
a('privacy.rightsText', 'l’utente può chiedere accesso, rettifica, cancellazione, limitazione e opposizione scrivendo a {email}, e può proporre reclamo al Garante per la protezione dei dati personali.', 'users may request access, rectification, erasure, restriction and objection by writing to {email}, and may lodge a complaint with the Italian Data Protection Authority (Garante).', "l'utilisateur peut demander l'accès, la rectification, l'effacement, la limitation et s'opposer au traitement en écrivant à {email}, et peut introduire une réclamation auprès de l'autorité italienne de protection des données (Garante).", 'Nutzer können Auskunft, Berichtigung, Löschung, Einschränkung und Widerspruch verlangen, indem sie an {email} schreiben, und können Beschwerde bei der italienischen Datenschutzbehörde (Garante) einlegen.')
a('privacy.cookies', 'Cookie:', 'Cookies:', 'Cookies :', 'Cookies:')
a('privacy.cookiesText', 'questo sito utilizza solo cookie tecnici e non installa strumenti di profilazione o analitici.', 'this website uses only technical cookies and does not install profiling or analytics tools.', "ce site utilise uniquement des cookies techniques et n'installe aucun outil de profilage ou d'analyse.", 'diese Website verwendet nur technisch notwendige Cookies und installiert keine Profiling- oder Analyse-Tools.')

# --- Altri prodotti (elenco)
for i, (it, en, fr, de) in enumerate([
    ('Copri alluminio', 'Aluminium covers', 'Cache-aluminium', 'Aluminiumabdeckungen'),
    ('Piattine', 'Flat strips', 'Plats', 'Flachleisten'),
    ('Masselli per porte', 'Door blanks', 'Bois massifs pour portes', 'Türrohlinge'),
    ('Colorazioni', 'Colours', 'Teintes', 'Farben')], 1):
    a(f'other.{i}', it, en, fr, de)

# --- Lingue
a('lang.it', 'Italiano', 'Italiano', 'Italiano', 'Italiano')
