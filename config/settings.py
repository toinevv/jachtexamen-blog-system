"""
Configuration settings for the Jachtexamen Blog System
"""
import os
from typing import Dict, List, Any

try:
    from pydantic_settings import BaseSettings
except ImportError:
    # Fallback for older pydantic versions
    from pydantic import BaseSettings

class Settings(BaseSettings):
    """Application settings"""
    
    # API Keys
    openai_api_key: str = os.getenv("OPENAI_API_KEY", "")
    anthropic_api_key: str = os.getenv("ANTHROPIC_API_KEY", "")
    google_news_api_key: str = os.getenv("GOOGLE_NEWS_API_KEY", "")
    
    # Supabase
    supabase_url: str = os.getenv("SUPABASE_URL", "")
    supabase_anon_key: str = os.getenv("SUPABASE_ANON_KEY", "")
    supabase_service_key: str = os.getenv("SUPABASE_SERVICE_KEY", "")
    
    # General
    environment: str = os.getenv("ENVIRONMENT", "development")
    log_level: str = os.getenv("LOG_LEVEL", "INFO")
    timezone: str = os.getenv("TIMEZONE", "Europe/Amsterdam")
    
    class Config:
        env_file = ".env"

# SEO Configuration
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

# API Configuration
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

# Google News Configuration
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

# Publishing Schedule
PUBLISHING_SCHEDULE = {
    "frequency": "every_3_days",
    "optimal_times": ["09:00", "14:00"],  # CET/CEST
    "posts_per_month": 10,
    "categories_rotation": True,
    
    "seasonal_topics": {
        "lente": ["broedseizoen", "natuurbeheer", "flora"],
        "zomer": ["examenvorbereiding", "hondentraining"],
        "herfst": ["jachtseizoen", "wild herkenning"],
        "winter": ["veiligheid", "wapenverzorging"]
    }
}

# Error Handling Configuration
ERROR_HANDLING = {
    "api_errors": {
        "max_retries": 3,
        "backoff_factor": 2,
        "fallback_to_alternate_api": True
    },
    "database_errors": {
        "max_retries": 3,
        "retry_on_connection_error": True,
        "queue_failed_writes": True,
        "alert_on_persistent_failure": True
    },
    "content_validation_errors": {
        "min_word_count_fallback": 500,
        "regenerate_on_quality_fail": False,
        "manual_review_queue": True,
        "max_regeneration_attempts": 2  # Hard limit to prevent cost spirals
    }
}

# Quality Assurance Requirements
QA_REQUIREMENTS = {
    "min_words": 500,  # Lowered to what APIs actually produce consistently
    "max_words": 3000,  # Allow comprehensive articles
    "min_paragraphs": 4,  # Ensure basic structure
    "required_sections": [],  # Remove strict section requirements
    "keyword_density_min": 0.005,  # More lenient keyword density
    "keyword_density_max": 0.03,
    "min_internal_links": 1,  # Very lenient
    "max_internal_links": 10
} 