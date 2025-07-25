"""
AI Prompt templates for content generation
"""

BLOG_PROMPT_TEMPLATE = """
Schrijf een uitgebreid en kwalitatief hoogstaand blogartikel in het Nederlands voor een jachtexamen voorbereidingsplatform.

🎯 FOCUS: Schrijf een praktisch artikel van 400-600 woorden met goede keyword integratie!

ONDERWERP: {topic}
PRIMAIRE KEYWORD: {primary_keyword}
SECUNDAIRE KEYWORDS: {secondary_keywords}

VERPLICHTE STRUCTUUR (minimaal 1500 woorden):

1. TITEL (H1): Pakkende titel (50-60 karakters) met primaire keyword

2. INLEIDING (100-150 woorden):
   - Introduceer het onderwerp helder en boeiend
   - Waarom is dit belangrijk voor het jachtexamen?
   - Wat gaat de lezer leren?
   - Maak de lezer nieuwsgierig

3. HOOFDSECTIE 1 - THEORIE & ACHTERGROND (120-180 woorden):
   - Uitleg van de basistheorie
   - Relevante wetgeving en regels
   - Praktische voorbeelden
   - Historische context indien relevant

4. HOOFDSECTIE 2 - PRAKTISCHE TOEPASSING (120-180 woorden):
   - Stap-voor-stap handleiding
   - Praktische tips en trucs
   - Do's and don'ts
   - Veelgemaakte fouten vermijden

5. HOOFDSECTIE 3 - EXAMENGERELATEERD (100-150 woorden):
   - Specifieke examenvragen
   - Leerdoelen en kennis
   - Studie-tips
   - Wat wordt er getoetst?

6. CONCLUSIE EN VERVOLGSTAPPEN (80-120 woorden):
   - Samenvatting hoofdpunten
   - Praktische vervolgstappen
   - Call-to-action naar oefenexamens
   - Motiverende afsluiting

EXTRA VEREISTEN:
- Gebruik H2 en H3 koppen voor structuur
- Voeg bullet points en genummerde lijsten toe
- Minimaal 5 concrete voorbeelden
- Minimaal 3 praktische tips per sectie
- Vermeld relevante wetten en regels
- Voeg veiligheidswaarschuwingen toe waar relevant

SEO OPTIMALISATIE:
- Keyword dichtheid: 1-2% voor primaire keyword
- Natuurlijke integratie van secundaire keywords
- Interne link suggesties naar gerelateerde onderwerpen
- Meta beschrijving (150-160 karakters)

TONE OF VOICE:
- Professioneel maar toegankelijk
- Zeer educatief en informatief
- Gericht op examenkandidaten
- Gebruik Nederlandse jacht terminologie
- Friendly en bemoedigend

💡 PRAKTISCHE FOCUS: Schrijf een informatief artikel van 400-600 woorden!

- Focus op duidelijke, praktische informatie
- Gebruik het primaire keyword natuurlijk door het artikel (minstens 2-3 keer)
- Gebruik concrete voorbeelden waar relevant  
- Schrijf voor examenkandidaten die snel willen leren
- Zorg voor goede keyword dichtheid zonder het geforceerd te laten klinken

✍️ SCHRIJF NU HET KWALITATIEVE ARTIKEL:
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

# Sample experimental prompt for Google Sheets testing
EXPERIMENTAL_SAMPLE_PROMPT = """
Schrijf een ULTRA-GEDETAILLEERD en ZEER UITGEBREID jachtexamen artikel in het Nederlands over {topic}.

🎯 VERPLICHT: Minimaal 2000 woorden! Dit is NON-NEGOTIABLE!

ONDERWERP: {topic}
KEYWORDS: {primary_keyword}, {secondary_keywords}

MEGA-UITGEBREIDE STRUCTUUR:

📖 INLEIDING (300+ woorden):
- Waarom is {topic} zo belangrijk voor jagers?
- Wat ga je in dit artikel leren?
- Historische achtergrond en ontwikkelingen
- Huidige relevantie voor het jachtexamen

🔍 THEORIE & WETGEVING (400+ woorden):
- Uitgebreide wetgeving uitleg
- Provinciale verschillen
- Europese richtlijnen
- Praktische interpretatie van regels

🛠️ PRAKTISCHE HANDLEIDING (400+ woorden):
- Stap-voor-stap instructies
- Materiaal en benodigdheden
- Seizoensgebonden aspecten
- Veiligheidsprocedures

⚠️ VEILIGHEID & ETHIEK (300+ woorden):
- Veiligheidsprocedures
- Ethische overwegingen
- Verantwoordelijkheden
- Risico's en preventie

📝 EXAMEN VOORBEREIDING (400+ woorden):
- Specifieke examenvragen met uitleg
- Oefenmateriaal en bronnen
- Veelgemaakte fouten
- Studie-tips en geheugensteuntjes

🎓 CONCLUSIE & VERVOLGSTAPPEN (200+ woorden):
- Samenvatting van alle hoofdpunten
- Praktische vervolgstappen
- Aanvullende bronnen
- Motiverende afsluiting

EXTRA DETAILS TOEVOEGEN:
- Minimaal 10 concrete voorbeelden
- 5+ praktische tips per sectie
- Tabellen en lijsten waar relevant
- Citaten van experts
- Statistieken en feiten

VERGEET NIET: Wees EXTREEM gedetailleerd. Elke paragraaf minimaal 100 woorden. Gebruik veel voorbeelden!

Schrijf nu het ultra-uitgebreide artikel:
""" 

# API-specific prompt templates for better length control
OPENAI_SPECIFIC_PROMPT = """
⚠️ CRITICAL INSTRUCTION: MINIMUM 600 WORDS REQUIRED ⚠️

You are writing for a Dutch hunting exam preparation platform. This article MUST be AT LEAST 600 words.

WORD COUNT REQUIREMENT: **MINIMUM 600 WORDS** - DO NOT STOP WRITING UNTIL YOU REACH THIS LENGTH!

TOPIC: {topic}
PRIMARY KEYWORD: {primary_keyword}
SECONDARY KEYWORDS: {secondary_keywords}

REQUIRED STRUCTURE (TOTAL 600+ WORDS):
1. **TITLE**: Include primary keyword (50-60 characters)

2. **INTRODUCTION** (150+ words):
   - Hook the reader immediately
   - Explain why this topic is crucial for the jachtexamen
   - Preview what they'll learn
   - Include primary keyword naturally

3. **MAIN SECTION 1: Theory & Background** (200+ words):
   - Detailed explanation of the topic
   - Include relevant Dutch hunting laws/regulations
   - Use primary keyword 1-2 times naturally
   - Add concrete examples and facts

4. **MAIN SECTION 2: Practical Application** (200+ words):
   - Step-by-step practical guidance
   - Real-world scenarios and case studies
   - Safety considerations and best practices
   - Include secondary keywords naturally

5. **EXAM PREPARATION SECTION** (100+ words):
   - Specific exam questions and answers
   - Study tips and memory techniques
   - What examiners look for
   - Practice recommendations

6. **CONCLUSION & NEXT STEPS** (80+ words):
   - Summarize key points
   - Motivational closing
   - Call-to-action for practice exams

CRITICAL REQUIREMENTS:
- WRITE AT LEAST 600 WORDS - Count as you write!
- Use primary keyword 3-4 times naturally throughout
- Include practical Dutch hunting terminology
- Write in professional but accessible Dutch
- Include HTML formatting (h2, h3, ul, li tags)
- Add internal linking suggestions

⚠️ FINAL CHECK: Your article MUST be at least 600 words. If it's shorter, ADD MORE CONTENT!

Write the complete article now:
"""

CLAUDE_SPECIFIC_PROMPT = """
🎯 MANDATORY LENGTH REQUIREMENT: 600+ WORDS MINIMUM 🎯

Task: Write a comprehensive Dutch hunting exam article that is AT LEAST 600 words long.

CONTEXT: You're writing for jachtexamen.nl - candidates need detailed, practical information.

TOPIC: {topic}
TARGET KEYWORDS: {primary_keyword}, {secondary_keywords}

WRITING FRAMEWORK (Aim for 600-800 words total):

**SECTION 1: Compelling Introduction (150-200 words)**
- Start with an engaging opening about why this matters for hunters
- Establish the importance for the jachtexamen
- Include your primary keyword "{primary_keyword}" naturally
- Create reader anticipation for what they'll learn

**SECTION 2: Comprehensive Theory (200-250 words)**
- Provide in-depth theoretical background
- Include relevant Dutch hunting regulations
- Explain scientific/biological aspects if applicable
- Use concrete examples from Dutch hunting scenarios
- Weave in primary keyword 1-2 more times

**SECTION 3: Hands-On Practical Guidance (200-250 words)**
- Detailed step-by-step instructions
- Real hunting situations and how to handle them
- Safety protocols and best practices
- Equipment recommendations if relevant
- Include secondary keywords: {secondary_keywords}

**SECTION 4: Exam Success Tips (100-150 words)**
- Specific questions that appear on the jachtexamen
- Memory techniques for remembering key facts
- Common mistakes to avoid
- Practice recommendations

**SECTION 5: Action-Oriented Conclusion (50-100 words)**
- Recap the most important points
- Motivate continued learning
- Direct to practice resources

QUALITY STANDARDS:
✅ Minimum 600 words (essential!)
✅ Professional Dutch language
✅ Include primary keyword 3-4 times naturally
✅ Use HTML formatting: <h2>, <h3>, <ul>, <li>
✅ Practical focus for exam candidates
✅ Include internal linking opportunities

📝 BEGIN WRITING YOUR 600+ WORD ARTICLE NOW:
""" 