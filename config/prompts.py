"""
AI Prompt templates for content generation
"""

BLOG_PROMPT_TEMPLATE = """
Schrijf een uitgebreid blogartikel in het Nederlands voor een jachtexamen voorbereidingsplatform.

ONDERWERP: {topic}
PRIMAIRE KEYWORD: {primary_keyword}
SECUNDAIRE KEYWORDS: {secondary_keywords}

STRUCTUUR VEREISTEN:
1. Pakkende titel (50-60 karakters) met primaire keyword
2. Inleiding (150-200 woorden) - introduceer het onderwerp en waarom het belangrijk is voor het jachtexamen
3. 4-6 hoofdsecties met H2 koppen
4. Minimaal 2 subsecties per hoofdsectie met H3 koppen
5. Bullet points of genummerde lijsten waar relevant
6. Praktische voorbeelden en examenvragen
7. Conclusie met call-to-action naar oefenexamens

SEO VEREISTEN:
- Keyword dichtheid: 1-2% voor primaire keyword
- Natuurlijke integratie van secundaire keywords
- Interne link suggesties naar gerelateerde onderwerpen
- Meta beschrijving (150-160 karakters)

TONE OF VOICE:
- Professioneel maar toegankelijk
- Educatief en informatief
- Gericht op examenkandidaten
- Gebruik Nederlandse jacht terminologie

OUTPUT FORMAAT:
- HTML geformatteerd
- Inclusief schema markup suggesties
- Leestijd berekening

Begin nu met het schrijven van het artikel:
"""

TITLE_GENERATION_PROMPT = """
Genereer 5 SEO-geoptimaliseerde titels voor een jachtexamen blog artikel over het onderwerp: {topic}

Vereisten:
- 50-60 karakters lang
- Bevat de primaire keyword: {primary_keyword}
- Aantrekkelijk voor examenkandidaten
- Nederlandse taal
- Call-to-action element waar mogelijk

Voorbeelden van goede titels:
- "Wilde Zwijnen Herkennen - Jachtexamen Tips 2024"
- "Jachtwetgeving Nederland: Complete Gids 2024"
- "Reeën Gedrag: Alles voor je Jachtexamen"

Geef alleen de 5 titels, elk op een nieuwe regel:
"""

META_DESCRIPTION_PROMPT = """
Schrijf een SEO-geoptimaliseerde meta beschrijving voor dit jachtexamen blog artikel:

TITEL: {title}
PRIMAIRE KEYWORD: {primary_keyword}
ARTICLE TOPIC: {topic}

Vereisten:
- Exact 150-160 karakters
- Bevat primaire keyword
- Gebruik actionable woorden
- Include benefits/value proposition
- Nederlandse taal
- Emoji's waar passend (✓, 🎯, 📚)

Format: Geef alleen de meta beschrijving terug, geen extra tekst.
"""

INTERNAL_LINKS_PROMPT = """
Analyseer dit blog artikel en suggereer interne links naar gerelateerde jachtexamen onderwerpen.

ARTIKEL CONTENT: {content}
HOOFDONDERWERP: {main_topic}
BESCHIKBARE CATEGORIEËN: {available_categories}

Genereer 3-7 interne link suggesties met:
1. Anchor tekst (natuurlijk in de context)
2. Doelpagina onderwerp
3. Relevantie score (1-10)
4. Positie in artikel (paragraaf nummer)

Format als JSON:
[
  {
    "anchor_text": "Nederlandse jachtwetgeving",
    "target_topic": "Jachtwet Nederland 2024",
    "relevance": 9,
    "paragraph": 3
  }
]
"""

SCHEMA_MARKUP_PROMPT = """
Genereer JSON-LD schema markup voor dit jachtexamen blog artikel:

TITEL: {title}
CONTENT: {content_excerpt}
AUTHOR: Jachtexamen Expert
PUBLISH_DATE: {publish_date}
CATEGORY: {category}

Vereiste schema types:
- Article
- EducationalOccupationalProgram (voor examen content)
- HowTo (indien van toepassing)

Return alleen de JSON-LD, geen extra tekst.
"""

CONTENT_OPTIMIZATION_PROMPT = """
Optimaliseer deze blog content voor SEO en leesbaarheid:

ORIGINELE CONTENT: {original_content}
DOELKEYWORD: {target_keyword}
HUIDIGE KEYWORD DICHTHEID: {current_density}%
DOEL DICHTHEID: 1-2%

Verbeteringen aanbrengen voor:
1. Keyword dichtheid optimalisatie
2. Leesbaarheid verbeteren
3. Header structuur optimaliseren
4. Call-to-action toevoegen
5. Nederlandse grammatica en spelling

Geef de geoptimaliseerde versie terug in HTML formaat.
"""

TOPIC_RELEVANCE_PROMPT = """
Beoordeel de relevantie van dit nieuws artikel voor jachtexamen content:

NIEUWS ARTIKEL: {news_content}
TITEL: {news_title}

Beoordeling criteria:
1. Direct gerelateerd aan jacht/wildlife (score 1-10)
2. Educatieve waarde voor examenkandidaten (score 1-10)
3. Nederlandse context (score 1-10)
4. Actualiteit waarde (score 1-10)

Geef ook suggesties voor:
- Blog artikel titel
- Hoofdonderwerpen om te behandelen
- Keywords om te targeten

Format als JSON:
{
  "relevance_score": 8.5,
  "direct_hunting_relation": 9,
  "educational_value": 8,
  "dutch_context": 9,
  "actuality": 8,
  "suggested_title": "...",
  "main_topics": ["...", "..."],
  "target_keywords": ["...", "..."]
}
"""

EXAM_QUESTION_PROMPT = """
Genereer 3-5 examenvragen gebaseerd op dit blog artikel content:

ARTIKEL CONTENT: {article_content}
HOOFDONDERWERP: {main_topic}

Voor elke vraag:
1. Multiple choice vraag (4 antwoordopties)
2. Correcte antwoord markeren
3. Korte uitleg bij het juiste antwoord
4. Moeilijkheidsgraad (makkelijk/gemiddeld/moeilijk)

Format als JSON array:
[
  {
    "question": "Wat is de minimale leeftijd voor het jachtexamen?",
    "options": ["16 jaar", "18 jaar", "21 jaar", "25 jaar"],
    "correct_answer": 1,
    "explanation": "In Nederland moet je minimaal 18 jaar zijn om het jachtexamen af te leggen.",
    "difficulty": "makkelijk"
  }
]
""" 