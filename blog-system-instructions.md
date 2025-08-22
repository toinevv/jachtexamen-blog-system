# 🚀 Automated Blog System for Jachtexamen Platform - Complete Instructions

## System Architecture Overview

```
Topic List → AI Content Generation → SEO Optimization → Supabase Storage → Website Display
     ↓                                                           ↑
Google News API (fallback for new topics) ──────────────────────┘
```

## 1. Cursor Development Prompt

```markdown
Create an automated blog writing system for a Dutch hunting exam (jachtexamen) platform with these specifications:

CORE REQUIREMENTS:
- Python-based system with async capabilities
- Rotating use of OpenAI GPT-4 and Claude API for content generation
- Dutch language content only
- Automatic SEO optimization
- Supabase integration for storage
- Topic management with Google News fallback

SYSTEM COMPONENTS:
1. Topic Manager (topics.py)
   - Maintain JSON file with blog topics
   - Check for used/unused topics
   - Google News API integration for trending hunting/nature topics
   - Topic validation and deduplication

2. Content Generator (generator.py)
   - Alternate between OpenAI and Claude APIs
   - Generate 1000-1500 word articles in Dutch
   - Include HTML formatting
   - Add internal linking suggestions
   - Generate meta descriptions

3. SEO Optimizer (seo.py)
   - Title optimization (50-60 characters)
   - Meta description generation (150-160 characters)
   - Keyword density checking
   - Schema markup generation
   - Internal linking recommendations

4. Database Manager (database.py)
   - Supabase client setup
   - CRUD operations for blog_articles table
   - Duplicate checking
   - Publishing queue management

5. Scheduler (scheduler.py)
   - Cron job setup for daily/weekly publishing
   - Rate limiting for API calls
   - Error handling and retry logic
```

## 2. Database Schema for Supabase

```sql
CREATE TABLE blog_articles (
  id UUID DEFAULT gen_random_uuid() PRIMARY KEY,
  title TEXT NOT NULL,
  slug TEXT UNIQUE NOT NULL,
  content TEXT NOT NULL,
  excerpt TEXT,
  meta_description TEXT,
  tags TEXT[],
  cover_image_url TEXT,
  cover_image_alt TEXT,
  primary_keyword TEXT,
  secondary_keywords TEXT[],
  internal_links JSONB,
  schema_markup JSONB,
  published_at TIMESTAMP WITH TIME ZONE DEFAULT NOW(),
  created_at TIMESTAMP WITH TIME ZONE DEFAULT NOW(),
  updated_at TIMESTAMP WITH TIME ZONE DEFAULT NOW(),
  status TEXT DEFAULT 'published',
  author TEXT DEFAULT 'Jachtexamen Expert',
  read_time INTEGER,
  geo_targeting TEXT[] DEFAULT ARRAY['Nederland', 'België'],
  language TEXT DEFAULT 'nl-NL'
);

-- Indexes for performance
CREATE INDEX idx_blog_slug ON blog_articles(slug);
CREATE INDEX idx_blog_published ON blog_articles(published_at DESC);
CREATE INDEX idx_blog_tags ON blog_articles USING GIN(tags);
CREATE INDEX idx_blog_status ON blog_articles(status);
```

## 3. Topic Management Strategy

### Initial Topics JSON Structure

```json
{
  "topics": [
    {
      "id": 1,
      "title": "Complete Gids Nederlandse Jachtwetgeving 2024",
      "keywords": ["jachtwet", "wetgeving", "regels"],
      "used": false,
      "category": "regelgeving"
    },
    {
      "id": 2,
      "title": "Wilde Zwijnen: Gedrag, Habitat en Veilige Jacht",
      "keywords": ["wilde zwijnen", "everzwijn", "jacht"],
      "used": false,
      "category": "wild"
    }
  ],
  "categories": ["wild", "planten", "jachthonden", "regelgeving", "vuurwapens", "examenvorbereiding", "seizoenen", "veiligheid"],
  "google_news_keywords": ["jacht nederland", "natuurbeheer", "wildbeheer", "jachtseizoen", "fauna beheer"]
}
```

### 100+ Blog Topic Ideas

#### Wildlife Knowledge (Wild)
1. De Complete Gids voor Nederlandse Zoogdieren - Jachtexamen 2024
2. Watervogels Herkennen: 15 Soorten die Je Moet Kennen
3. Bosvogels en Hun Gedrag - Essentiële Kennis voor Jagers
4. Reeën in Nederland: Gedrag, Habitat en Jachttechnieken
5. Wilde Zwijnen: Alles over Gedrag en Veilige Jacht
6. Fazanten en Patrijzen: Verschillen en Jachtstrategieën
7. Nederlandse Eendachtigen: Complete Overzicht
8. Hazen vs Konijnen: Herkenning en Jachttechnieken
9. Damherten: Leefwijze en Populatiebeheer
10. Vossen in Nederland: Gedrag en Beheer

#### Plant Knowledge (Planten)
11. Giftige Planten in Nederlandse Bossen - Veiligheid voor Jagers
12. Eetbare Wilde Planten: Wat Mag en Wat Niet
13. Boombomen Herkennen: 20 Belangrijkste Soorten
14. Struiken en Heesters in Nederlandse Jachtgebieden
15. Paddenstoelen in het Bos: Veilig Verzamelen
16. Voedselplanten voor Wild: Aanleg en Onderhoud
17. Beschermde Plantensoorten: Wat Je Moet Weten
18. Seizoensgebonden Flora in Jachtgebieden
19. Bomen en Hun Vruchten: Voedsel voor Wild
20. Invasieve Plantensoorten en Hun Impact

#### Hunting Dogs (Jachthonden)
21. Nederlandse Jachthondenrassen: Complete Overzicht
22. Training van Jachthonden: Basis Technieken
23. Gezondheid en Verzorging van Jachthonden
24. Verschillende Jachttypen en Bijbehorende Honden
25. Puppy tot Jachthond: Het Complete Traject
26. EHBO voor Jachthonden in het Veld
27. Voeding voor Actieve Jachthonden
28. Zweethonden vs Brakhonden: Wanneer Welke Inzetten
29. Apporteeroefeningen voor Beginners
30. Gedragsproblemen bij Jachthonden Oplossen

#### Regulations (Regelgeving)
31. Nederlandse Jachtwet 2024: Alle Belangrijke Wijzigingen
32. Jachtseizoen Kalender: Wanneer Mag Je Wat Jagen
33. Jachtakte Voorwaarden en Verplichtingen
34. Wildschade en Aansprakelijkheid
35. Jachtpacht en Toestemming: Wat Moet Je Weten
36. Europese Wetgeving en Nederlandse Jacht
37. Provinciale Verschillen in Jachtregels
38. Nachtzichtkijkers: Wat Mag Wel en Niet
39. Verzekeringen voor Jagers: Complete Gids
40. Boetes en Sancties bij Overtredingen

#### Firearms (Vuurwapens)
41. Jachtvuurwapens: Kalibers en Toepassingen
42. Veilig Omgaan met Jachtwapens
43. Munitie Keuze voor Verschillende Wildsoorten
44. Onderhoud van Jachtvuurwapens
45. Kogelgeweer vs Hagelgeweer: Wanneer Wat
46. Vizieren en Richtkijkers: Keuze en Afstelling
47. Ballistiek voor Jagers: Basiskennis
48. Gehoorbescherming: Waarom en Welke
49. Wapenkluis Vereisten en Veiligheid
50. Transport van Jachtvuurwapens: Regels en Tips

#### Exam Preparation
51. Jachtexamen Voorbereiding: 10 Essentiële Tips
52. Meest Gemaakte Fouten bij het Jachtexamen
53. Praktijkexamen Jacht: Wat te Verwachten
54. Theorie-examen Strategieën die Werken
55. Examenvragen Wild Herkenning: Oefenmateriaal
56. Tijdsmanagement tijdens het Jachtexamen
57. Stress Verminderen voor je Examen
58. Laatste Week voor het Examen: Checklist
59. Herexamen Strategie: Tweede Kans Benutten
60. Online vs Klassikaal Leren: Wat Werkt Beter

#### Seasonal Topics
61. Voorjaarsjacht: Kansen en Beperkingen
62. Zomerbeheer: Schadepreventie en Monitoring
63. Najaarsjacht: Optimale Voorbereiding
64. Wintervoedering: Do's en Don'ts
65. Broedseizoen: Wat Betekent Dit voor Jagers
66. Brunfttijd: Veiligheid en Mogelijkheden
67. Trekvogels: Seizoenspatronen Begrijpen
68. IJsgang: Jagen bij Winterse Omstandigheden
69. Droogteperiodes: Impact op Wild en Jacht
70. Stormschade: Veiligheid in het Veld

#### Safety & Ethics
71. Veiligheidsprotocollen tijdens Drijfjachten
72. Ethisch Jagen: Moderne Principes
73. Eerste Hulp in het Veld: Basisvaardigheden
74. Communicatie tijdens Groepsjachten
75. Klimmen in Hoogzitten: Veilig Werken
76. Schootsafstand: Verantwoorde Keuzes
77. Wildbraak: Hygiënisch Verwerken
78. Respect voor Natuur en Medejagers
79. Ongevallen Voorkomen: Risk Assessment
80. Noodprocedures: Wat Te Doen Bij Calamiteiten

#### Advanced Topics
81. Wildbeheer en Klimaatverandering
82. Technologie in de Moderne Jacht
83. Wildtellingen: Methoden en Interpretatie
84. Habitatverbetering: Praktische Projecten
85. Predator-Prooi Relaties Begrijpen
86. Populatiedynamiek: Basis voor Beheer
87. Natuurbeheer vs Jacht: Samenwerking
88. Wildbraak: Van Veld tot Bord
89. Trofeeënbeoordeling: CIC Formules
90. Internationale Jacht: Regels en Culturen

#### Practical Skills
91. Sporenzoeken: Wild Tracks Herkennen
92. Aanzitten: Locatiekeuze en Technieken
93. Lokroepen: Effectief Wild Lokken
94. Camouflage: Onzichtbaar in het Veld
95. Windrichting: Cruciale Factor bij Jacht
96. Afstandsschatting zonder Hulpmiddelen
97. Veldbiologie: Gedrag Observeren
98. Weersinvloeden op Wildactiviteit
99. Nachtzicht: Natuurlijk Zien in het Donker
100. Wildbraken: Stap-voor-Stap Handleiding

## 4. Content Generation Prompt Template

```python
BLOG_PROMPT_TEMPLATE = """
Schrijf een uitgebreid blogartikel in het Nederlands voor een jachtexamen voorbereidingsplatform.

ONDERWERP: {topic}
PRIMAIRE KEYWORD: {primary_keyword}
SECUNDAIRE KEYWORDS: {secondary_keywords}

STRUCTUUR VEREISTEN:
1. Pakkende titel (50-60 karakters) met primaire keyword
2. Inleiding (150-200 woorden) - introducer het onderwerp en waarom het belangrijk is voor het jachtexamen
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
"""
```

## 5. SEO Best Practices Configuration

```python
SEO_CONFIG = {
    "title_template": "{keyword} - Jachtexamen {year} | Complete Gids",
    "meta_description_template": "Leer alles over {topic} voor je jachtexamen. ✓ Praktische tips ✓ Examenvragen ✓ {year} update. Start nu met oefenen!",
    
    "target_keywords": {
        "primary": ["jachtexamen", "jachtdiploma", "jacht examen"],
        "location": ["nederland", "nederlandse", "nl"],
        "intent": ["leren", "oefenen", "voorbereiding", "tips", "gids"]
    },
    
    "internal_linking_rules": {
        "min_links": 3,
        "max_links": 7,
        "anchor_text_variation": True,
        "relevant_categories_only": True
    },
    
    "schema_types": [
        "Article",
        "EducationalOccupationalProgram",
        "HowTo",
        "FAQPage"
    ],
    
    "geo_targeting": {
        "primary": "Nederland",
        "secondary": ["België", "Vlaanderen"],
        "language": "nl-NL"
    }
}
```

## 6. Google News Integration Configuration

```python
GOOGLE_NEWS_CONFIG = {
    "search_queries": [
        "jacht nederland nieuws",
        "wildbeheer actueel",
        "jachtseizoen {current_year}",
        "natuurbeheer nederland",
        "faunabeheer nieuws"
    ],
    "relevance_keywords": [
        "jacht", "wild", "natuur", "beheer", "seizoen",
        "wetgeving", "vergunning", "examen"
    ],
    "exclude_keywords": [
        "ongeval", "protest", "verbod", "kritiek"
    ],
    "min_relevance_score": 0.7
}
```

## 7. Content Calendar & Publishing Schedule

```python
PUBLISHING_SCHEDULE = {
    "frequency": "daily",
    "optimal_times": ["09:00", "14:00"],  # CET/CEST
    "posts_per_week": 5,
    "categories_rotation": True,
    
    "seasonal_topics": {
        "lente": ["broedseizoen", "natuurbeheer", "flora"],
        "zomer": ["examenvorbereiding", "hondenttraining"],
        "herfst": ["jachtseizoen", "wild herkenning"],
        "winter": ["veiligheid", "wapenverzorging"]
    }
}
```

## 8. Environment Variables (.env)

```bash
# API Keys
OPENAI_API_KEY=your_openai_api_key_here
ANTHROPIC_API_KEY=your_claude_api_key_here
GOOGLE_NEWS_API_KEY=your_google_news_api_key_here

# Supabase
SUPABASE_URL=your_supabase_url_here
SUPABASE_ANON_KEY=your_supabase_anon_key_here
SUPABASE_SERVICE_KEY=your_supabase_service_key_here

# Configuration
ENVIRONMENT=production
LOG_LEVEL=INFO
TIMEZONE=Europe/Amsterdam
```

## 9. Quality Assurance Checklist

Before publishing, each article must pass:

- [ ] Minimum 1000 words
- [ ] Correct Dutch spelling and grammar
- [ ] Primary keyword in title, H1, first paragraph
- [ ] At least 3 internal link suggestions
- [ ] Mobile-friendly HTML formatting
- [ ] Unique slug verification
- [ ] Cover image alt text includes keyword
- [ ] Meta description within character limit
- [ ] Schema markup validity
- [ ] No duplicate content
- [ ] Factual accuracy verified
- [ ] Legal compliance checked

## 10. API Configuration Details

```python
API_CONFIG = {
    "openai": {
        "model": "gpt-4-turbo-preview",
        "temperature": 0.7,
        "max_tokens": 2500,
        "top_p": 0.9,
        "frequency_penalty": 0.3,
        "presence_penalty": 0.3
    },
    "claude": {
        "model": "claude-3-opus-20240229",
        "temperature": 0.7,
        "max_tokens": 2500,
        "top_p": 0.9
    },
    "rotation_pattern": "alternating",
    "rate_limits": {
        "requests_per_minute": 3,
        "requests_per_day": 100,
        "retry_attempts": 3,
        "retry_delay": 60  # seconds
    }
}
```

## 11. Example Python Project Structure

```
jachtexamen-blog-system/
│
├── src/
│   ├── __init__.py
│   ├── topics.py           # Topic management
│   ├── generator.py        # Content generation
│   ├── seo.py             # SEO optimization
│   ├── database.py        # Supabase operations
│   ├── scheduler.py       # Cron job management
│   └── utils.py           # Helper functions
│
├── config/
│   ├── __init__.py
│   ├── settings.py        # Configuration management
│   └── prompts.py         # AI prompt templates
│
├── data/
│   ├── topics.json        # Topic database
│   └── published.json     # Published articles tracker
│
├── logs/
│   └── blog_system.log    # System logs
│
├── tests/
│   ├── test_generator.py
│   ├── test_seo.py
│   └── test_database.py
│
├── requirements.txt       # Python dependencies
├── .env                  # Environment variables
├── .gitignore           # Git ignore file
├── README.md            # Project documentation
└── main.py              # Entry point
```

## 12. Required Python Dependencies

```txt
# requirements.txt
openai==1.12.0
anthropic==0.18.1
supabase==2.3.0
python-dotenv==1.0.0
schedule==1.2.0
beautifulsoup4==4.12.3
googlenews==1.6.8
langdetect==1.0.9
schema==0.7.5
python-slugify==8.0.4
aiohttp==3.9.3
asyncio==3.4.3
tenacity==8.2.3
loguru==0.7.2
pydantic==2.6.1
pytest==8.0.2
black==24.2.0
```

## 13. Monitoring & Analytics Dashboard

Track these KPIs:

### Content Metrics
- Total articles published
- Articles per category distribution
- Average word count
- Publishing frequency adherence
- Topic coverage percentage

### SEO Performance
- Average title length
- Keyword density compliance
- Internal links per article
- Schema markup implementation rate
- Meta description optimization score

### Technical Metrics
- API success rate
- Average generation time
- Error rate by API provider
- Retry frequency
- Database query performance

### Cost Analysis
- Cost per article (API usage)
- Monthly API spend
- Cost per 1000 words
- ROI based on traffic generation

## 14. Error Handling & Recovery

```python
ERROR_HANDLING = {
    "api_errors": {
        "max_retries": 3,
        "backoff_factor": 2,
        "fallback_to_alternate_api": True
    },
    "database_errors": {
        "retry_on_connection_error": True,
        "queue_failed_writes": True,
        "alert_on_persistent_failure": True
    },
    "content_validation_errors": {
        "min_word_count_fallback": 800,
        "regenerate_on_quality_fail": True,
        "manual_review_queue": True
    }
}
```

## 15. Security Best Practices

1. **API Key Management**
   - Never commit API keys to version control
   - Use environment variables for all secrets
   - Rotate API keys regularly
   - Implement key usage monitoring

2. **Database Security**
   - Use Supabase Row Level Security (RLS)
   - Implement proper authentication
   - Regular backup procedures
   - Audit log for all write operations

3. **Content Security**
   - Sanitize all HTML output
   - Implement CSRF protection
   - Rate limit public endpoints
   - Monitor for suspicious activity

## 16. Deployment Instructions

### Local Development
```bash
# Clone repository
git clone https://github.com/yourusername/jachtexamen-blog-system.git
cd jachtexamen-blog-system

# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Set up environment variables
cp .env.example .env
# Edit .env with your API keys

# Run initial setup
python setup.py

# Start the system
python main.py
```

### Production Deployment (VPS/Cloud)
```bash
# Use PM2 for process management
npm install -g pm2

# Start the application
pm2 start main.py --name jachtexamen-blog-system

# Set up cron job for scheduler
pm2 start scheduler.py --name blog-scheduler --cron "0 9,14 * * *"

# Monitor logs
pm2 logs jachtexamen-blog-system
```

## 17. Maintenance Schedule

### Daily
- Monitor API usage and costs
- Check for failed article generations
- Review publishing queue

### Weekly
- Analyze content performance metrics
- Update topic list based on trends
- Review and approve queued articles

### Monthly
- Full system backup
- API key rotation
- Performance optimization review
- Cost analysis and optimization

### Quarterly
- Major topic list refresh
- SEO strategy review
- System architecture evaluation
- Dependency updates

---

## Support & Troubleshooting

For common issues and solutions, refer to the troubleshooting guide in the project wiki. For urgent support, contact the development team.

**Version:** 1.0.0  
**Last Updated:** January 2025  
**License:** MIT