"""
Mock Database Manager for testing without Supabase
"""

import json
from datetime import datetime
from typing import Dict, List, Optional
from loguru import logger


class DatabaseManager:
    """Mock database manager for testing without Supabase"""
    
    def __init__(self):
        self.table_name = "blog_articles"
        self.articles = []  # In-memory storage
        self.mock_id_counter = 1
        logger.info("Using mock database manager (no Supabase connection)")
        
    async def create_article(self, article_data: Dict) -> Optional[Dict]:
        """Create a new blog article in mock storage"""
        try:
            # Add mock ID and save to memory
            article_data["id"] = f"mock_{self.mock_id_counter}"
            article_data["created_at"] = datetime.now().isoformat()
            article_data["published_at"] = datetime.now().isoformat()
            
            self.articles.append(article_data)
            self.mock_id_counter += 1
            
            logger.info(f"Mock: Created article: {article_data['title']}")
            return article_data
                
        except Exception as e:
            logger.error(f"Mock: Error creating article: {e}")
            return None
    
    async def get_article(self, article_id: str = None, slug: str = None) -> Optional[Dict]:
        """Get article by ID or slug from mock storage"""
        try:
            for article in self.articles:
                if (article_id and article.get("id") == article_id) or \
                   (slug and article.get("slug") == slug):
                    return article
            return None
            
        except Exception as e:
            logger.error(f"Mock: Error getting article: {e}")
            return None
    
    async def get_statistics(self) -> Dict:
        """Get mock statistics"""
        try:
            return {
                "total_articles": len(self.articles),
                "published_articles": len(self.articles),
                "draft_articles": 0,
                "category_distribution": {},
                "recent_articles_7_days": len(self.articles),
                "last_updated": datetime.now().isoformat()
            }
            
        except Exception as e:
            logger.error(f"Mock: Error getting statistics: {e}")
            return {}
    
    async def backup_articles(self, filename: str = None) -> str:
        """Create mock backup"""
        try:
            if not filename:
                timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
                filename = f"mock_backup_{timestamp}.json"
            
            backup_data = {
                "created_at": datetime.now().isoformat(),
                "total_articles": len(self.articles),
                "articles": self.articles
            }
            
            with open(filename, 'w', encoding='utf-8') as f:
                json.dump(backup_data, f, ensure_ascii=False, indent=2)
            
            logger.info(f"Mock: Backup created: {filename}")
            return filename
            
        except Exception as e:
            logger.error(f"Mock: Error creating backup: {e}")
            return ""
    
    # Add other required methods as simple mocks
    async def update_article(self, article_id: str, updates: Dict) -> Optional[Dict]:
        """Mock update article"""
        logger.info(f"Mock: Would update article {article_id}")
        return {"id": article_id, **updates}
    
    async def delete_article(self, article_id: str) -> bool:
        """Mock delete article"""
        logger.info(f"Mock: Would delete article {article_id}")
        return True
    
    async def list_articles(self, **kwargs) -> List[Dict]:
        """Mock list articles"""
        return self.articles
    
    async def search_articles(self, search_term: str, limit: int = 20) -> List[Dict]:
        """Mock search articles"""
        return self.articles[:limit]
    
    async def get_articles_by_category(self, category: str, limit: int = 10) -> List[Dict]:
        """Mock get articles by category"""
        return [a for a in self.articles if a.get("category") == category][:limit]
    
    async def get_popular_articles(self, days: int = 30, limit: int = 10) -> List[Dict]:
        """Mock get popular articles"""
        return self.articles[:limit]
    
    async def get_related_articles(self, article_id: str, limit: int = 5) -> List[Dict]:
        """Mock get related articles"""
        return self.articles[:limit]
    
    async def batch_update_articles(self, updates: List[Dict]) -> List[Dict]:
        """Mock batch update"""
        logger.info(f"Mock: Would batch update {len(updates)} articles")
        return updates
    
    async def cleanup_old_drafts(self, days: int = 30) -> int:
        """Mock cleanup"""
        logger.info("Mock: Would cleanup old drafts")
        return 0
    
    async def get_publishing_queue(self, limit: int = 10) -> List[Dict]:
        """Mock publishing queue"""
        return []
    
    async def publish_article(self, article_id: str) -> bool:
        """Mock publish article"""
        logger.info(f"Mock: Would publish article {article_id}")
        return True 