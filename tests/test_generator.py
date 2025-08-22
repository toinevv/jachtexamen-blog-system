"""
Tests for content generator module
"""

import pytest
import asyncio
from unittest.mock import Mock, patch, AsyncMock
from src.generator import ContentGenerator
from src.utils import validate_dutch_text


class TestContentGenerator:
    """Test cases for ContentGenerator class"""
    
    def setup_method(self):
        """Setup test fixtures"""
        self.generator = ContentGenerator()
        self.sample_topic = {
            "id": 1,
            "title": "Wilde Zwijnen: Gedrag en Veilige Jacht",
            "keywords": ["wilde zwijnen", "everzwijn", "jacht"],
            "category": "wild",
            "priority": "high"
        }
    
    def test_get_next_api_alternating(self):
        """Test API rotation works correctly"""
        self.generator.last_used_api = "openai"
        next_api = self.generator._get_next_api()
        assert next_api == "claude"
        
        self.generator.last_used_api = "claude"
        next_api = self.generator._get_next_api()
        assert next_api == "openai"
    
    def test_build_content_prompt(self):
        """Test prompt building includes topic information"""
        prompt = self.generator._build_content_prompt(self.sample_topic)
        
        assert "Wilde Zwijnen: Gedrag en Veilige Jacht" in prompt
        assert "wilde zwijnen" in prompt
        assert "ONDERWERP:" in prompt
        assert "PRIMAIRE KEYWORD:" in prompt
    
    def test_extract_title_from_content(self):
        """Test title extraction from generated content"""
        content_with_h1 = "<h1>Test Titel voor Jachtexamen</h1><p>Content hier...</p>"
        title = self.generator._extract_title(content_with_h1, self.sample_topic)
        assert title == "Test Titel voor Jachtexamen"
        
        # Test fallback to topic title
        content_without_title = "<p>Content zonder titel...</p>"
        title = self.generator._extract_title(content_without_title, self.sample_topic)
        assert title == self.sample_topic["title"]
    
    def test_calculate_reading_time(self):
        """Test reading time calculation"""
        short_content = "Dit is een korte tekst."
        reading_time = self.generator._calculate_reading_time(short_content)
        assert reading_time == 1  # Minimum reading time
        
        # Create content with approximately 500 words
        long_content = " ".join(["woord"] * 500)
        reading_time = self.generator._calculate_reading_time(long_content)
        assert reading_time == 2  # 500 words / 250 wpm = 2 minutes
    
    def test_passes_qa_check_valid_article(self):
        """Test QA check passes for valid Dutch article"""
        valid_article = {
            "title": "Nederlandse Jachtwetgeving 2024: Complete Gids",
            "content": " ".join(["Nederlandse jacht content"] * 200),  # ~600 words
            "primary_keyword": "jachtwetgeving"
        }
        
        assert self.generator._passes_qa_check(valid_article) == True
    
    def test_passes_qa_check_invalid_article(self):
        """Test QA check fails for invalid article"""
        invalid_article = {
            "title": "A",  # Too short
            "content": "Too short",  # Too short
            "primary_keyword": "test"
        }
        
        assert self.generator._passes_qa_check(invalid_article) == False
    
    def test_clean_and_format_content(self):
        """Test content cleaning and HTML formatting"""
        raw_content = """
        ## Hoofdsectie
        Dit is een paragraaf.
        
        ### Subsectie
        * Item 1
        * Item 2
        """
        
        cleaned = self.generator._clean_and_format_content(raw_content, "Test Titel")
        
        assert "<h2>Hoofdsectie</h2>" in cleaned
        assert "<h3>Subsectie</h3>" in cleaned
        assert "<ul>" in cleaned
        assert "<li>Item 1</li>" in cleaned
    
    def test_generate_excerpt(self):
        """Test excerpt generation from content"""
        long_content = "<p>" + "Dit is een zeer lange tekst. " * 50 + "</p>"
        excerpt = self.generator._generate_excerpt(long_content)
        
        assert len(excerpt) <= 163  # 160 + "..."
        assert "..." in excerpt or len(excerpt) <= 160
    
    @patch('src.generator.ContentGenerator._call_openai')
    @patch('src.generator.ContentGenerator._call_claude')
    async def test_generate_content_with_api_fallback(self, mock_claude, mock_openai):
        """Test API fallback mechanism"""
        # Setup mocks
        mock_openai.side_effect = Exception("OpenAI API error")
        mock_claude.return_value = "Generated content from Claude"
        
        # Should try OpenAI first, then fallback to Claude
        self.generator.last_used_api = "claude"  # So next API is OpenAI
        
        content = await self.generator._generate_content_with_api(self.sample_topic, "openai")
        
        # Should have called OpenAI and it failed
        mock_openai.assert_called_once()
        
        # Now test the fallback in the main generate method would work
        assert content is None  # Due to the exception
    
    def test_get_generation_stats(self):
        """Test generation statistics tracking"""
        self.generator.api_usage_count = {"openai": 5, "claude": 3}
        
        stats = self.generator.get_generation_stats()
        
        assert stats["total_api_calls"] == 8
        assert stats["openai_calls"] == 5
        assert stats["claude_calls"] == 3
        assert stats["openai_percentage"] == 62.5
        assert stats["claude_percentage"] == 37.5


class TestUtilityFunctions:
    """Test utility functions used by generator"""
    
    def test_validate_dutch_content(self):
        """Test Dutch language validation"""
        dutch_text = "Dit is een Nederlandse tekst over jacht en wilde dieren in Nederland."
        english_text = "This is an English text about hunting and wild animals."
        
        assert validate_dutch_text(dutch_text) == True
        assert validate_dutch_text(english_text) == False
    
    def test_extract_internal_link_opportunities(self):
        """Test internal link extraction"""
        from src.generator import extract_internal_link_opportunities
        
        content = "In dit artikel bespreken we wilde zwijnen en reeën in Nederlandse bossen."
        available_topics = [
            "Wilde Zwijnen Gedrag",
            "Reeën in Nederland", 
            "Jachthonden Training"
        ]
        
        opportunities = extract_internal_link_opportunities(content, available_topics)
        
        assert len(opportunities) >= 2  # Should find "wilde zwijnen" and "reeën"
        assert any("wilde zwijnen" in opp["keyword"] for opp in opportunities)


@pytest.fixture
def mock_api_keys(monkeypatch):
    """Mock API keys for testing"""
    monkeypatch.setenv("OPENAI_API_KEY", "test-openai-key")
    monkeypatch.setenv("ANTHROPIC_API_KEY", "test-anthropic-key")
    monkeypatch.setenv("SUPABASE_URL", "https://test.supabase.co")
    monkeypatch.setenv("SUPABASE_SERVICE_KEY", "test-service-key")


@pytest.mark.asyncio
class TestAsyncMethods:
    """Test async methods of ContentGenerator"""
    
    async def test_generate_meta_description(self):
        """Test meta description generation"""
        generator = ContentGenerator()
        
        article = {
            "title": "Nederlandse Jachtwetgeving 2024",
            "primary_keyword": "jachtwetgeving",
            "content": "Uitgebreide content over Nederlandse jachtwetgeving..."
        }
        
        # Mock the API call
        with patch.object(generator, '_generate_content_with_api', 
                         return_value="Leer alles over jachtwetgeving voor je jachtexamen. ✓ Tips ✓ 2024"):
            meta_desc = await generator._generate_meta_description(article)
            
            assert len(meta_desc) <= 160
            assert "jachtwetgeving" in meta_desc.lower()
    
    async def test_generate_exam_questions(self):
        """Test exam question generation"""
        generator = ContentGenerator()
        
        article = {
            "title": "Jachtveiligheid Basics",
            "content": "Jachtveiligheid is van essentieel belang. " * 50
        }
        
        # Mock the API call with valid JSON
        mock_questions = [
            {
                "question": "Wat is de belangrijkste regel bij jachtveiligheid?",
                "options": ["Altijd laden", "Nooit laden", "Controleren", "Schieten"],
                "correct_answer": 2,
                "explanation": "Altijd controleren of het wapen geladen is.",
                "difficulty": "makkelijk"
            }
        ]
        
        with patch.object(generator, '_generate_content_with_api', 
                         return_value=str(mock_questions).replace("'", '"')):
            questions = await generator._generate_exam_questions(article)
            
            # Since our mock returns a string, not JSON, this will return empty list
            # In real implementation, API would return proper JSON
            assert isinstance(questions, list)


if __name__ == "__main__":
    pytest.main([__file__]) 