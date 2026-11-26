"""SEO: titoli (<=44 car. + suffisso brand), descrizioni (<=155), pagine sottoprodotto, FAQ."""
from gen3 import T, a

def o(key, it, en, fr='', de=''):
    T[key] = (it, en, fr, de)

# --- Titoli e descrizioni delle famiglie
FAM = {
 'battiscopa': ('Battiscopa in legno su misura', 'Custom wooden skirting boards',
   'Battiscopa in legno su misura, al naturale, laccati o tinti, in qualsiasi essenza e sezione. Produzione propria a Santa Giustina in Colle (PD).',
   'Custom wooden skirting boards, natural, lacquered or stained, in any wood and profile. Made in-house in Santa Giustina in Colle, Padua.'),
 'profili-per-quadri': ('Profili in legno per cornici e quadri', 'Wooden mouldings for picture frames',
   'Profili in legno per cornici e quadri: tante sezioni e finiture, in qualsiasi essenza, anche su disegno. Produzione a Santa Giustina in Colle (PD).',
   'Wooden mouldings for picture frames: many profiles and finishes, any wood, also to your drawing. Made in Santa Giustina in Colle, Padua.'),
 'profili-per-serramenti': ('Profili in legno per serramenti', 'Wooden profiles for windows and doors',
   'Fermavetri, coprifili e profili in legno per serramenti, su misura in qualsiasi essenza. Produzione a Santa Giustina in Colle (PD), dal 1960.',
   'Glazing beads, architraves and wooden profiles for windows and doors, made to measure in any wood. Made in Santa Giustina in Colle, Padua.'),
 'perlinati': ('Perlinati e masselli piallati in legno', 'Wooden tongue-and-groove boards',
   'Perlinati, frangisole e masselli piallati in legno per rivestimenti e interni, in diverse essenze. Produzione a Santa Giustina in Colle (PD).',
   'Tongue-and-groove boards, sunshades and planed solid timber for cladding and interiors, in many woods. Made in Santa Giustina in Colle, Padua.'),
 'profili-per-saune': ('Profili in legno per saune', 'Wooden profiles for saunas',
   'Profili in legno per saune su misura, in diverse essenze e sezioni. Produzione a Santa Giustina in Colle (PD): richiedi un preventivo.',
   'Made-to-measure wooden profiles for saunas, in different woods and sections. Made in Santa Giustina in Colle, Padua: request a quote.'),
 'semilavorati': ('Semilavorati in legno su misura', 'Semi-finished wood products',
   'Semilavorati in legno di varie sezioni e lunghezze, in qualsiasi essenza, anche su misura. Produzione a Santa Giustina in Colle (PD).',
   'Semi-finished wood products in various sections and lengths, in any wood, also made to measure. Made in Santa Giustina in Colle, Padua.'),
 'profili-di-finitura': ('Profili di finitura in legno', 'Wooden finishing profiles',
   'Profili di finitura in legno: tondi, angolari e corrimano in diverse essenze e finiture. Produzione a Santa Giustina in Colle (PD).',
   'Wooden finishing profiles: round profiles, angle profiles and handrails in many woods and finishes. Made in Santa Giustina in Colle, Padua.'),
 'boiserie': ('Boiserie e cornici in legno', 'Wooden wall panelling and mouldings',
   'Boiserie, cornici e modanature in legno per pareti e soffitti, in diverse essenze e finiture. Produzione a Santa Giustina in Colle (PD).',
   'Wooden wall panelling, cornices and mouldings for walls and ceilings, in many woods and finishes. Made in Santa Giustina in Colle, Padua.'),
}
for slug, (ti, te, di, de_) in FAM.items():
    o(f'families.{slug}.seoTitle', ti, te); o(f'families.{slug}.seoDescription', di, de_)

# --- Altre pagine
o('seo.home.desc',
  'Profili in legno su misura prodotti a Santa Giustina in Colle (PD): quadri, battiscopa, serramenti, perlinati, saune, boiserie. Dal 1960.',
  'Made-to-measure wood profiles made in Santa Giustina in Colle (Padua): picture frames, skirting boards, windows, panelling, saunas. Since 1960.')
o('seo.prods.desc',
  'Battiscopa, profili per quadri, serramenti, perlinati, saune, semilavorati, profili di finitura e boiserie: produzione su misura G.P.E. Rizzolo.',
  'Skirting boards, picture frame mouldings, window profiles, tongue-and-groove boards, saunas, finishing profiles and panelling. By G.P.E. Rizzolo.')
o('seo.company.desc',
  'G.P.E. Rizzolo produce profili in legno dal 1960 a Santa Giustina in Colle (PD). Tre generazioni di esperienza e attenzione al cliente.',
  'G.P.E. Rizzolo has made wood profiles since 1960 in Santa Giustina in Colle (Padua). Three generations of experience and customer focus.')

# --- Sottoprodotti: SEO + contenuti
CH = {
 'fermavetri': dict(
  it=('Fermavetri in legno su misura', 'Fermavetri in legno in molte sagome e sezioni, in qualsiasi essenza, forniti in asta. Produzione a Santa Giustina in Colle (PD).',
      'I fermavetri in legno trattengono il vetro nel serramento e ne completano l’estetica. Li produciamo in molte sagome e sezioni, in asta, pronti per il taglio e il montaggio.',
      'Lavoriamo qualsiasi essenza e possiamo sviluppare una sagoma dedicata partendo dal vostro serramento, da un disegno o da un campione.',
      ['Serramenti e infissi in legno','Produttori di finestre e porte-finestre','Falegnamerie','Sagome su disegno']),
  en=('Custom wooden glazing beads', 'Wooden glazing beads in many shapes and sections, in any wood, supplied in lengths. Made in Santa Giustina in Colle, Padua.',
      'Wooden glazing beads hold the glass in a window frame and complete its look. We make them in many shapes and sections, in lengths, ready to be cut and fitted.',
      'We work with any wood and can develop a dedicated profile from your window, a drawing or a sample.',
      ['Wooden windows and frames','Window and French-door manufacturers','Joinery workshops','Profiles to your drawing'])),
 'coprifili': dict(
  it=('Coprifili in legno su misura', 'Coprifili in legno per serramenti e porte, in diverse sezioni ed essenze, anche su disegno. Produzione a Santa Giustina in Colle (PD).',
      'I coprifili coprono il giunto tra serramento e muro e rifiniscono l’apertura. Produciamo coprifili in legno in diverse sezioni, al naturale o colorati.',
      'Essenze, sezioni e lunghezze si concordano con il cliente, in serie o su disegno.',
      ['Porte e finestre interne','Ristrutturazioni e nuove costruzioni','Falegnamerie e posatori','Finiture colorate su richiesta']),
  en=('Custom wooden architraves', 'Wooden architraves for doors and windows, in different sections and woods, also to your drawing. Made in Santa Giustina in Colle, Padua.',
      'Architraves cover the joint between frame and wall and finish the opening. We make wooden architraves in different sections, natural or coloured.',
      'Woods, sections and lengths are agreed with the customer, in series or to your drawing.',
      ['Interior doors and windows','Renovations and new builds','Joiners and fitters','Coloured finishes on request'])),
 'frangisole': dict(
  it=('Frangisole in legno', 'Profili in legno per frangisole e rivestimenti esterni, in diverse sagome ed essenze. Produzione a Santa Giustina in Colle (PD).',
      'I frangisole in legno schermano la luce e valorizzano le facciate. Produciamo profili per frangisole e rivestimenti esterni in diverse sagome e finiture.',
      'Possiamo sviluppare la sezione più adatta al progetto di architettura, nell’essenza richiesta.',
      ['Facciate e rivestimenti esterni','Schermature solari','Progetti di architettura','Sezioni su disegno']),
  en=('Wooden sunshade profiles', 'Wooden profiles for sunshades and exterior cladding, in different shapes and woods. Made in Santa Giustina in Colle, Padua.',
      'Wooden sunshades filter the light and enhance façades. We make profiles for sunshades and exterior cladding in different shapes and finishes.',
      'We can develop the section best suited to your architectural project, in the wood you require.',
      ['Façades and exterior cladding','Solar shading','Architectural projects','Sections to your drawing'])),
 'masselli-piallati': dict(
  it=('Masselli piallati in legno', 'Masselli e listelli piallati in legno, di varie sezioni e lunghezze, in diverse essenze. Produzione a Santa Giustina in Colle (PD).',
      'I masselli piallati sono travetti e listelli in legno pieno con superfici lisce, pronti per le lavorazioni successive. Li forniamo in diverse sezioni e lunghezze.',
      'Possiamo preparare essenze, misure e quantità secondo le esigenze della vostra produzione.',
      ['Falegnamerie e carpenterie','Semilavorati per porte e arredo','Listelli e traversi','Sezioni su misura']),
  en=('Planed solid timber', 'Planed solid timber and battens in various sections and lengths, in different woods. Made in Santa Giustina in Colle, Padua.',
      'Planed solid timber is beams and battens of solid wood with smooth surfaces, ready for further processing. We supply it in different sections and lengths.',
      'We can prepare woods, sizes and quantities to suit your production.',
      ['Joinery and carpentry','Semi-finished parts for doors and furniture','Battens and rails','Custom sections'])),
 'profili-tondi': dict(
  it=('Profili tondi in legno', 'Tondini e profili tondi torniti in legno, in varie misure ed essenze, anche su disegno. Produzione a Santa Giustina in Colle (PD).',
      'Produciamo tondini e profili tondi in legno, anche con teste e lavorazioni accessorie, in diversi diametri e lunghezze.',
      'Essenza e misure si definiscono secondo il vostro disegno o campione.',
      ['Tondini e aste','Componenti per arredo','Lavorazioni torniti','Pezzi su disegno']),
  en=('Round wooden profiles', 'Wooden dowels and turned round profiles in various sizes and woods, also to your drawing. Made in Santa Giustina in Colle, Padua.',
      'We make wooden dowels and round profiles, also with heads and extra machining, in different diameters and lengths.',
      'Wood and sizes are defined from your drawing or sample.',
      ['Dowels and rods','Furniture components','Turned parts','Pieces to your drawing'])),
 'angolari': dict(
  it=('Angolari in legno', 'Angolari in legno in diverse essenze e tinte, al naturale o colorati, per finire e proteggere gli spigoli. Produzione a Santa Giustina (PD).',
      'Gli angolari in legno rifiniscono e proteggono gli spigoli di pareti, arredi e scale. Li produciamo in diverse sezioni, al naturale o tinti.',
      'Essenze, tinte e misure su richiesta, anche in serie dedicate.',
      ['Finiture di interni','Protezione degli spigoli','Arredo e falegnameria','Colorazioni personalizzate']),
  en=('Wooden angle profiles', 'Wooden angle profiles in many woods and colours, natural or coloured, to finish and protect edges. Made in Santa Giustina in Colle, Padua.',
      'Wooden angle profiles finish and protect the edges of walls, furniture and stairs. We make them in different sections, natural or stained.',
      'Woods, colours and sizes on request, also in dedicated series.',
      ['Interior finishing','Edge protection','Furniture and joinery','Custom colours'])),
 'corrimano': dict(
  it=('Corrimano in legno massello', 'Corrimano in legno massello per scale e balaustre, dal chiaro naturale al noce scuro, anche su misura. Produzione a Santa Giustina in Colle (PD).',
      'I corrimano in legno massello hanno sagome ergonomiche e superfici curate, per scale interne e balaustre. Sono disponibili in diverse essenze e tonalità.',
      'Forniamo scalifici, falegnamerie e imprese, anche con lunghezze e sezioni dedicate.',
      ['Scale interne','Balaustre e parapetti','Scalifici e falegnamerie','Essenze e tinte a scelta']),
  en=('Solid wood handrails', 'Solid wood handrails for staircases and balustrades, from light natural to dark walnut, also made to measure. Made in Santa Giustina in Colle, Padua.',
      'Solid wood handrails have ergonomic profiles and finely finished surfaces, for interior staircases and balustrades. Available in different woods and shades.',
      'We supply stair makers, joiners and building firms, also with dedicated lengths and sections.',
      ['Interior staircases','Balustrades and railings','Stair makers and joiners','Woods and stains of your choice'])),
}
for slug, d in CH.items():
    for idx, lang in ((0, 'it'), (1, 'en')):
        ti, de_, b1, b2, uses = d[lang]
        vals = {'seoTitle': ti, 'seoDescription': de_, 'body1': b1, 'body2': b2}
        for i, u in enumerate(uses, 1): vals[f'use{i}'] = u
        for k, v in vals.items():
            key = f'children.{slug}.{k}'
            cur = list(T.get(key, ('', '', '', '')))
            cur[idx] = v; T[key] = tuple(cur)

# --- FAQ (comuni a tutte le schede) e sezione "come richiedere"
o('faq.title', 'Domande frequenti', 'Frequently asked questions', 'Questions fréquentes', 'Häufige Fragen')
o('faq.1q', '{name}: posso ordinarli su misura?', '{name}: can I order them made to measure?', '{name} : puis-je les commander sur mesure ?', '{name}: kann ich sie nach Maß bestellen?')
o('faq.1a', 'Sì. Produciamo su disegno, su campione o secondo le tue specifiche, in qualsiasi sezione e lunghezza concordata.', 'Yes. We produce to your drawing, sample or specifications, in any agreed section and length.', 'Oui. Nous produisons sur plan, sur échantillon ou selon vos spécifications, dans toute section et longueur convenues.', 'Ja. Wir fertigen nach Zeichnung, Muster oder Ihren Vorgaben, in jedem vereinbarten Querschnitt und jeder Länge.')
o('faq.2q', 'In quali essenze di legno producete?', 'Which woods do you work with?', 'Dans quelles essences de bois produisez-vous ?', 'In welchen Holzarten fertigen Sie?')
o('faq.2a', 'In qualsiasi essenza di legno, ad esempio abete, pino, larice, meranti, okumè, rovere e frassino. Altre essenze su richiesta.', 'In any kind of wood, for example fir, pine, larch, meranti, okoumé, oak and ash. Other woods on request.', "Dans toutes les essences de bois, par exemple sapin, pin, mélèze, méranti, okoumé, chêne et frêne. Autres essences sur demande.", 'In jeder Holzart, zum Beispiel Tanne, Kiefer, Lärche, Meranti, Okoume, Eiche und Esche. Weitere Holzarten auf Anfrage.')
o('faq.3q', 'Dove vengono prodotti?', 'Where are they made?', 'Où sont-ils fabriqués ?', 'Wo werden sie hergestellt?')
o('faq.3a', 'Tutta la produzione avviene nella nostra sede di Santa Giustina in Colle, in provincia di Padova.', 'All production takes place at our site in Santa Giustina in Colle, in the province of Padua.', 'Toute la production a lieu dans notre site de Santa Giustina in Colle, dans la province de Padoue.', 'Die gesamte Fertigung erfolgt an unserem Standort in Santa Giustina in Colle in der Provinz Padua.')
o('faq.4q', 'Avete prodotti certificati FSC®?', 'Do you have FSC®-certified products?', 'Avez-vous des produits certifiés FSC® ?', 'Haben Sie FSC®-zertifizierte Produkte?')
o('faq.4a', 'Sì, prodotti certificati FSC® sono disponibili su richiesta.', 'Yes, FSC®-certified products are available on request.', 'Oui, des produits certifiés FSC® sont disponibles sur demande.', 'Ja, FSC®-zertifizierte Produkte sind auf Anfrage erhältlich.')
o('faq.5q', 'Come posso richiedere un preventivo?', 'How can I request a quote?', 'Comment demander un devis ?', 'Wie kann ich ein Angebot anfordern?')
o('faq.5a', 'Compila il modulo indicando prodotto, essenza e quantità, oppure chiamaci al {phone}. Ti rispondiamo il prima possibile.', 'Fill in the form with product, wood and quantity, or call us on {phone}. We will reply as soon as possible.', 'Remplissez le formulaire en indiquant produit, essence et quantité, ou appelez-nous au {phone}. Nous vous répondons au plus vite.', 'Füllen Sie das Formular mit Produkt, Holzart und Menge aus oder rufen Sie uns unter {phone} an. Wir antworten so schnell wie möglich.')
o('prod.how', 'Come richiedere un preventivo', 'How to request a quote', 'Comment demander un devis', 'So fordern Sie ein Angebot an')
o('prod.sibling', 'Anche in {name}', 'Also in {name}', 'Aussi dans {name}', 'Auch in {name}')
o('prod.back', '← Torna a {name}', '← Back to {name}', '← Retour à {name}', '← Zurück zu {name}')
o('prod.sheet', 'Scheda tecnica →', 'Technical sheet →', 'Fiche technique →', 'Datenblatt →')
