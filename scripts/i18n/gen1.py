# Traduzioni (parte 1: UI + home). Formato: (it, en, fr, de)
T = {}
def a(k, it, en, fr, de): T[k] = (it, en, fr, de)

# --- Header / footer / barra mobile
a('top.loc', '{city} ({prov}) · Dal {year}', '{city} ({prov}) · Since {year}', '{city} ({prov}) · Depuis {year}', '{city} ({prov}) · Seit {year}')
a('top.short', 'Profili in legno dal {year}', 'Wood profiles since {year}', 'Profils en bois depuis {year}', 'Holzprofile seit {year}')
a('nav.products', 'Prodotti', 'Products', 'Produits', 'Produkte')
a('nav.custom', 'Su misura', 'Made to measure', 'Sur mesure', 'Nach Maß')
a('nav.company', 'Azienda', 'Company', 'Entreprise', 'Unternehmen')
a('nav.certs', 'Certificazioni', 'Certifications', 'Certifications', 'Zertifizierungen')
a('nav.contacts', 'Contatti', 'Contact', 'Contact', 'Kontakt')
a('nav.quote', 'Preventivo', 'Quote', 'Devis', 'Angebot')
a('nav.open', 'Apri menu', 'Open menu', 'Ouvrir le menu', 'Menü öffnen')
a('nav.close', 'Chiudi menu', 'Close menu', 'Fermer le menu', 'Menü schließen')
a('nav.lang', 'Lingua', 'Language', 'Langue', 'Sprache')
a('nav.skip', 'Vai al contenuto', 'Skip to content', 'Aller au contenu', 'Zum Inhalt springen')
a('nav.homeAria', 'G.P.E. Rizzolo - Home', 'G.P.E. Rizzolo - Home', 'G.P.E. Rizzolo - Accueil', 'G.P.E. Rizzolo - Startseite')
a('bar.call', 'Chiama', 'Call', 'Appeler', 'Anrufen')
a('bar.quote', 'Preventivo', 'Quote', 'Devis', 'Angebot')
a('footer.desc', 'Profili in legno di qualità dal {year}. Profilatura in asta, in qualsiasi essenza, su disegno o campione.',
  'Quality wood profiles since {year}. Profiling in lengths, in any wood, to your drawing or sample.',
  'Profils en bois de qualité depuis {year}. Profilage en barres, dans toutes les essences, sur plan ou échantillon.',
  'Hochwertige Holzprofile seit {year}. Profilieren von Stangenware, in jeder Holzart, nach Zeichnung oder Muster.')
a('footer.follow', 'Seguici', 'Follow us', 'Suivez-nous', 'Folgen Sie uns')
a('footer.explore', 'Esplora', 'Explore', 'Explorer', 'Entdecken')
a('footer.products', 'Prodotti', 'Products', 'Produits', 'Produkte')
a('footer.all', 'Tutti i prodotti →', 'All products →', 'Tous les produits →', 'Alle Produkte →')
a('footer.contacts', 'Contatti', 'Contact', 'Contact', 'Kontakt')
a('footer.privacy', 'Privacy', 'Privacy', 'Confidentialité', 'Datenschutz')
a('footer.vat', 'P.IVA {vat}', 'VAT No. {vat}', 'TVA {vat}', 'USt-IdNr. {vat}')
a('social.aria', '{name} di {company}', '{company} on {name}', '{company} sur {name}', '{company} auf {name}')
a('crumb.home', 'Home', 'Home', 'Accueil', 'Startseite')

# --- Hero
a('hero.kicker', 'Produttore · {city} ({prov})', 'Manufacturer · {city} ({prov})', 'Fabricant · {city} ({prov})', 'Hersteller · {city} ({prov})')
a('hero.h1a', 'Profili', 'Bespoke', 'Profils', 'Holzprofile')
a('hero.h1b', 'in legno', 'wood', 'en bois', '')
a('hero.h1hl', 'su misura', 'profiles', 'sur mesure', 'nach Maß')
a('hero.essence', 'qualsiasi essenza', 'any wood', 'toutes les essences', 'jeder Holzart')
a('hero.p', 'Profilatura in asta in {essence}, dal {year}. Profili per quadri, battiscopa, serramenti, corrimano e pezzi speciali: in serie o su vostro disegno. Tutta la produzione avviene a Santa Giustina in Colle (PD).',
  'Profiling in lengths in {essence}, since {year}. Picture frame mouldings, skirting boards, window profiles, handrails and special pieces: in series or to your drawing. All production takes place in Santa Giustina in Colle (Padua).',
  'Profilage en barres dans {essence}, depuis {year}. Moulures pour cadres, plinthes, profils pour menuiseries, mains courantes et pièces spéciales : en série ou sur votre plan. Toute la production a lieu à Santa Giustina in Colle (Padoue).',
  'Profilieren von Stangenware in {essence}, seit {year}. Bilderrahmenprofile, Sockelleisten, Fensterprofile, Handläufe und Sonderanfertigungen: in Serie oder nach Ihrer Zeichnung. Die gesamte Fertigung erfolgt in Santa Giustina in Colle (Padua).')
a('hero.cta', 'Richiedi preventivo', 'Request a quote', 'Demander un devis', 'Angebot anfragen')
a('hero.products', 'Prodotti', 'Products', 'Produits', 'Produkte')
a('hero.alt', 'Blocchetti di legno massello in fila', 'Solid wood blocks in a row', 'Blocs de bois massif alignés', 'Massivholzklötze in einer Reihe')
a('hero.fig', 'Fig. 01 — Massello', 'Fig. 01 — Solid wood', 'Fig. 01 — Bois massif', 'Abb. 01 — Massivholz')
a('hero.section', 'Sezione · profilo per cornici', 'Section · frame moulding', 'Section · moulure de cadre', 'Schnitt · Rahmenleiste')
a('hero.since', 'Dal', 'Since', 'Depuis', 'Seit')
a('draw.aria', 'Sezione tecnica di un profilo', 'Technical section of a profile', "Coupe technique d'un profil", 'Technischer Querschnitt eines Profils')

# --- Trust bar
a('trust.1', 'Anno di fondazione', 'Year founded', 'Année de fondation', 'Gründungsjahr')
a('trust.2v', 'Tutte', 'Any', 'Toutes', 'Alle')
a('trust.2', 'Le essenze di legno', 'Wood species', 'Les essences de bois', 'Holzarten')
a('trust.3v', 'Locale', 'Local', 'Locale', 'Lokal')
a('trust.3', 'Tutta la produzione a Santa Giustina in Colle', 'All production in Santa Giustina in Colle', 'Toute la production à Santa Giustina in Colle', 'Gesamte Fertigung in Santa Giustina in Colle')
a('trust.4', 'Prodotti certificati su richiesta', 'Certified products on request', 'Produits certifiés sur demande', 'Zertifizierte Produkte auf Anfrage')

# --- Famiglie (home)
a('fam.kicker', 'Prodotti', 'Products', 'Produits', 'Produkte')
a('fam.t1', 'Ogni profilo,', 'Every profile,', 'Chaque profil,', 'Jedes Profil,')
a('fam.t2', 'una sezione.', 'a section.', 'une section.', 'ein Querschnitt.')
a('fam.sub', '{n} famiglie di prodotto, tutte realizzabili nell’essenza e nella sezione che serve al tuo progetto.',
  '{n} product families, all available in the wood and section your project needs.',
  "{n} familles de produits, toutes réalisables dans l'essence et la section dont votre projet a besoin.",
  '{n} Produktfamilien, alle in der Holzart und dem Querschnitt lieferbar, die Ihr Projekt braucht.')
a('fam.fig', 'Fig.', 'Fig.', 'Fig.', 'Abb.')
a('fam.go', 'Vai alla scheda →', 'View product →', 'Voir la fiche →', 'Zum Produkt →')

# --- Materia prima
a('mat.kicker', 'La materia prima', 'The raw material', 'La matière première', 'Der Rohstoff')
a('mat.t1', 'Qualsiasi', 'Any', 'Toute', 'Jede')
a('mat.t2', 'essenza.', 'wood.', 'essence.', 'Holzart.')
a('mat.p', 'Dalla scelta del legno alla profilatura: lavoriamo l’essenza che serve al tuo progetto, con attenzione a precisione e qualità della finitura.',
  'From choosing the wood to profiling: we work the wood your project needs, with attention to precision and finish quality.',
  "Du choix du bois au profilage : nous travaillons l'essence dont votre projet a besoin, avec soin pour la précision et la qualité de finition.",
  'Von der Auswahl des Holzes bis zum Profilieren: Wir verarbeiten die Holzart, die Ihr Projekt braucht – mit Sorgfalt bei Präzision und Oberflächenqualität.')
a('mat.note', 'Alcune tipologie. Altre essenze su richiesta.', 'Some of our woods. Others on request.', "Quelques essences. D'autres sur demande.", 'Einige Holzarten. Weitere auf Anfrage.')
a('mat.alt', 'Alcune tipologie di legno: abete, pino, larice, meranti, okumè, rovere, frassino',
  'Some wood types: fir, pine, larch, meranti, okoumé, oak, ash',
  'Quelques types de bois : sapin, pin, mélèze, méranti, okoumé, chêne, frêne',
  'Einige Holzarten: Tanne, Kiefer, Lärche, Meranti, Okoume, Eiche, Esche')
for i, (it, en, fr, de) in enumerate([
    ('Abete', 'Fir', 'Sapin', 'Tanne'), ('Pino', 'Pine', 'Pin', 'Kiefer'), ('Larice', 'Larch', 'Mélèze', 'Lärche'),
    ('Meranti', 'Meranti', 'Méranti', 'Meranti'), ('Okumè', 'Okoumé', 'Okoumé', 'Okoume'),
    ('Rovere', 'Oak', 'Chêne', 'Eiche'), ('Frassino', 'Ash', 'Frêne', 'Esche')], 1):
    a(f'essence.{i}', it, en, fr, de)

# --- Su misura
a('cus.kicker', 'Su misura', 'Made to measure', 'Sur mesure', 'Nach Maß')
a('cus.t1', 'Hai un disegno.', 'You have a drawing.', 'Vous avez un plan.', 'Sie haben eine Zeichnung.')
a('cus.t2', 'Noi gli diamo forma.', 'We give it shape.', 'Nous lui donnons forme.', 'Wir geben ihr Form.')
a('cus.p', 'Non tutti i progetti entrano in un catalogo. Ascoltiamo l’esigenza, valutiamo il profilo e troviamo la soluzione più adatta: da un disegno, da un campione o da una semplice idea.',
  'Not every project fits in a catalogue. We listen to your needs, assess the profile and find the most suitable solution: from a drawing, a sample or a simple idea.',
  "Tous les projets n'entrent pas dans un catalogue. Nous écoutons votre besoin, évaluons le profil et trouvons la solution la plus adaptée : à partir d'un plan, d'un échantillon ou d'une simple idée.",
  'Nicht jedes Projekt passt in einen Katalog. Wir hören zu, prüfen das Profil und finden die passende Lösung: ausgehend von einer Zeichnung, einem Muster oder einer einfachen Idee.')
a('cus.draw', 'Il tuo disegno · sezione A–B', 'Your drawing · section A–B', 'Votre plan · section A–B', 'Ihre Zeichnung · Schnitt A–B')
a('cus.shape', '→ Il pezzo prende forma', '→ The piece takes shape', '→ La pièce prend forme', '→ Das Teil nimmt Form an')
a('cus.fig', 'Fig. — Dal disegno al pezzo', 'Fig. — From drawing to piece', 'Fig. — Du plan à la pièce', 'Abb. — Von der Zeichnung zum Werkstück')
a('cus.cta', 'Parliamo del tuo progetto →', 'Let’s talk about your project →', 'Parlons de votre projet →', 'Sprechen wir über Ihr Projekt →')
a('step.1t', "Ci racconti l'idea", 'You tell us your idea', "Vous nous racontez votre idée", 'Sie erzählen uns Ihre Idee')
a('step.1', 'Disegno, campione o esigenza produttiva.', 'Drawing, sample or production need.', 'Plan, échantillon ou besoin de production.', 'Zeichnung, Muster oder Produktionsbedarf.')
a('step.2t', 'Valutiamo insieme', 'We assess together', 'Nous évaluons ensemble', 'Wir prüfen gemeinsam')
a('step.2', 'Confronto tecnico e definizione della richiesta.', 'Technical discussion and definition of the request.', 'Échange technique et définition de la demande.', 'Technischer Austausch und Festlegung der Anfrage.')
a('step.3t', 'Prende forma', 'It takes shape', 'Elle prend forme', 'Es nimmt Form an')
a('step.3', 'Una soluzione pensata per il tuo progetto.', 'A solution designed for your project.', 'Une solution pensée pour votre projet.', 'Eine Lösung, maßgeschneidert für Ihr Projekt.')

# --- Azienda (home + pagina)
a('about.kicker', 'L’azienda', 'The company', "L'entreprise", 'Das Unternehmen')
a('about.sub', 'Nobile arte che attraversa tre generazioni', 'A noble craft spanning three generations', 'Un noble métier qui traverse trois générations', 'Ein edles Handwerk über drei Generationen')
a('about.h', 'La tradizione non è restare fermi. È sapere come andare avanti.', 'Tradition doesn’t mean standing still. It means knowing how to move forward.', "La tradition, ce n'est pas rester immobile. C'est savoir comment avancer.", 'Tradition heißt nicht Stillstand. Sie heißt, zu wissen, wie es weitergeht.')
a('about.asta', 'profilatura in asta', 'profiling in lengths', 'profilage en barres', 'Profilieren von Stangenware')
a('about.p1', 'Da oltre sessant’anni il legno è il nostro mestiere. La nostra attività principale è la {asta}, con grande attenzione alla precisione e alla qualità della finitura, su qualsiasi essenza di legno.',
  'For over sixty years wood has been our trade. Our core business is {asta}, with great attention to precision and finish quality, in any kind of wood.',
  "Depuis plus de soixante ans, le bois est notre métier. Notre activité principale est le {asta}, avec une grande attention à la précision et à la qualité de finition, dans toutes les essences.",
  'Seit über sechzig Jahren ist Holz unser Handwerk. Unsere Hauptaufgabe ist das {asta}, mit großer Sorgfalt bei Präzision und Oberflächenqualität, in jeder Holzart.')
a('about.p2', 'Produciamo coprifili, fermavetri, copri alluminio, piattine, masselli per porte, angolari, zoccolini, perlinati e profili su misura. Tutta la nostra produzione è realizzata a Santa Giustina in Colle (PD).',
  'We produce architraves, glazing beads, aluminium covers, flat strips, door blanks, angle profiles, skirting boards, tongue-and-groove boards and made-to-measure profiles. All of our production is carried out in Santa Giustina in Colle (Padua).',
  'Nous fabriquons couvre-joints, parcloses, cache-aluminium, plats, bois massifs pour portes, cornières, plinthes, lambris et profils sur mesure. Toute notre production est réalisée à Santa Giustina in Colle (Padoue).',
  'Wir fertigen Deckleisten, Glasleisten, Aluminiumabdeckungen, Flachleisten, Türrohlinge, Winkelprofile, Sockelleisten, Profilbretter und Profile nach Maß. Unsere gesamte Produktion entsteht in Santa Giustina in Colle (Padua).')
a('about.p3', 'Saldi alla filosofia del passato, con un occhio attento alle innovazioni tecnologiche e al futuro: ogni nostro prodotto ha un solo obiettivo, la soddisfazione del cliente.',
  'Faithful to the philosophy of the past, with an eye on technological innovation and the future: every product we make has one goal, customer satisfaction.',
  "Fidèles à la philosophie du passé, avec un œil attentif aux innovations technologiques et à l'avenir : chacun de nos produits a un seul objectif, la satisfaction du client.",
  'Der Philosophie der Vergangenheit treu und mit Blick auf technische Neuerungen und die Zukunft: Jedes unserer Produkte hat ein Ziel – die Zufriedenheit des Kunden.')
a('about.btn', 'Scopri la nostra storia →', 'Discover our story →', 'Découvrez notre histoire →', 'Entdecken Sie unsere Geschichte →')
a('about.card1', 'Il mestiere, in sezione', 'The craft, in section', 'Le métier, en coupe', 'Das Handwerk im Querschnitt')
a('about.card2a', 'Precisione', 'Precision', 'Précision', 'Präzision')
a('about.card2b', 'tramandata.', 'handed down.', 'transmise.', 'weitergegeben.')
a('about.partners', 'I soci', 'The partners', 'Les associés', 'Die Gesellschafter')
a('fact.1', 'Generazioni in azienda', 'Generations in the company', "Générations dans l'entreprise", 'Generationen im Unternehmen')
a('fact.2', 'Valori tramandati', 'Values handed down', 'Valeurs transmises', 'Weitergegebene Werte')
a('fact.3', 'Obiettivo: la soddisfazione del cliente', 'Goal: customer satisfaction', 'Objectif : la satisfaction du client', 'Ziel: die Zufriedenheit des Kunden')

# --- Certificazioni
a('cert.kicker', 'Certificazioni', 'Certifications', 'Certifications', 'Zertifizierungen')
a('cert.t1', 'Legno', 'Responsible', 'Un bois', 'Verantwortungsvolles')
a('cert.t2', 'responsabile.', 'wood.', 'responsable.', 'Holz.')
a('cert.p', 'Prodotti certificati FSC® disponibili su richiesta. Impegno etico e politica ambientale sono consultabili sul {link}.',
  'FSC®-certified products available on request. Our ethical commitment and environmental policy can be found on the {link}.',
  "Produits certifiés FSC® disponibles sur demande. Notre engagement éthique et notre politique environnementale sont consultables sur le {link}.",
  'FSC®-zertifizierte Produkte auf Anfrage. Ethische Verpflichtung und Umweltpolitik finden Sie auf der {link}.')
a('cert.link', 'sito aziendale', 'company website', "site de l'entreprise", 'Unternehmenswebsite')
a('cert.fsc', 'Prodotti certificati FSC® disponibili su richiesta.', 'FSC®-certified products available on request.', 'Produits certifiés FSC® disponibles sur demande.', 'FSC®-zertifizierte Produkte auf Anfrage.')
a('cert.iso', 'Sistema di gestione ambientale, certificato con accreditamento UKAS.', 'Environmental management system, certified under UKAS accreditation.', 'Système de management environnemental, certifié sous accréditation UKAS.', 'Umweltmanagementsystem, zertifiziert mit UKAS-Akkreditierung.')
a('cert.fscAlt', 'Certificato FSC G.P.E. Rizzolo', 'G.P.E. Rizzolo FSC certificate', 'Certificat FSC G.P.E. Rizzolo', 'FSC-Zertifikat G.P.E. Rizzolo')
a('cert.isoAlt', 'Certificato ISO 14001 G.P.E. Rizzolo', 'G.P.E. Rizzolo ISO 14001 certificate', 'Certificat ISO 14001 G.P.E. Rizzolo', 'ISO-14001-Zertifikat G.P.E. Rizzolo')

# --- CTA
a('cta.kicker', 'Il prossimo passo', 'The next step', 'La prochaine étape', 'Der nächste Schritt')
a('cta.t1', 'Parliamo del tuo', 'Let’s talk about', 'Parlons de', 'Sprechen wir über')
a('cta.t2', 'prossimo progetto.', 'your next project.', 'votre prochain projet.', 'Ihr nächstes Projekt.')
a('cta.p', 'Raccontaci cosa ti serve: profilo, essenza, quantità. Ti rispondiamo il prima possibile.',
  'Tell us what you need: profile, wood, quantity. We’ll reply as soon as possible.',
  'Dites-nous ce dont vous avez besoin : profil, essence, quantité. Nous vous répondons au plus vite.',
  'Sagen Sie uns, was Sie brauchen: Profil, Holzart, Menge. Wir antworten so schnell wie möglich.')
a('cta.btn', 'Richiedi preventivo →', 'Request a quote →', 'Demander un devis →', 'Angebot anfragen →')
