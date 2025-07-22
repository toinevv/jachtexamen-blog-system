"""
Google Sheets Integration for Jachtexamen Blog System
Provides visibility and control over topics and generated content
"""

import json
import os
from datetime import datetime
from typing import Dict, List, Optional
from loguru import logger

try:
    import gspread
    from google.oauth2.service_account import Credentials
    SHEETS_AVAILABLE = True
except ImportError:
    SHEETS_AVAILABLE = False
    logger.warning("Google Sheets integration not available. Install: pip install gspread google-auth")


class SheetsManager:
    """Manages Google Sheets integration for topic and article tracking"""
    
    def __init__(self):
        self.sheets_available = SHEETS_AVAILABLE
        self.client = None
        self.spreadsheet = None
        self.topics_sheet = None
        self.articles_sheet = None
        
        if self.sheets_available:
            self._initialize_sheets()
    
    def _initialize_sheets(self):
        """Initialize Google Sheets connection"""
        try:
            # Check for service account credentials
            creds_path = os.getenv('GOOGLE_SHEETS_CREDENTIALS_PATH', 'google_credentials.json')
            spreadsheet_id = os.getenv('GOOGLE_SHEETS_ID')
            
            if not spreadsheet_id:
                logger.warning("GOOGLE_SHEETS_ID environment variable not set")
                return
            
            if os.path.exists(creds_path):
                # Use service account file
                scope = [
                    'https://www.googleapis.com/auth/spreadsheets',
                    'https://www.googleapis.com/auth/drive'
                ]
                creds = Credentials.from_service_account_file(creds_path, scopes=scope)
                self.client = gspread.authorize(creds)
            else:
                # Try using service account JSON from environment variable
                creds_json = os.getenv('GOOGLE_SHEETS_CREDENTIALS_JSON')
                if creds_json:
                    scope = [
                        'https://www.googleapis.com/auth/spreadsheets',
                        'https://www.googleapis.com/auth/drive'
                    ]
                    creds_info = json.loads(creds_json)
                    creds = Credentials.from_service_account_info(creds_info, scopes=scope)
                    self.client = gspread.authorize(creds)
                else:
                    logger.warning("No Google Sheets credentials found")
                    return
            
            # Open spreadsheet
            self.spreadsheet = self.client.open_by_key(spreadsheet_id)
            
            # Get or create worksheets
            self._setup_worksheets()
            
            logger.info("✅ Google Sheets integration initialized successfully")
            
        except Exception as e:
            logger.error(f"Failed to initialize Google Sheets: {e}")
            self.sheets_available = False
    
    def _setup_worksheets(self):
        """Set up the required worksheets"""
        try:
            # Try to get existing sheets or create them
            try:
                self.topics_sheet = self.spreadsheet.worksheet("Topics Management")
            except:
                logger.info("Creating 'Topics Management' worksheet...")
                self.topics_sheet = self.spreadsheet.add_worksheet(
                    title="Topics Management", 
                    rows=100, 
                    cols=20
                )
                self._setup_topics_headers()
            
            try:
                self.articles_sheet = self.spreadsheet.worksheet("Generated Articles")
            except:
                logger.info("Creating 'Generated Articles' worksheet...")
                self.articles_sheet = self.spreadsheet.add_worksheet(
                    title="Generated Articles", 
                    rows=500, 
                    cols=25
                )
                self._setup_articles_headers()
            
            # Setup prompts sheet for experimentation
            try:
                self.prompts_sheet = self.spreadsheet.worksheet("Prompts & Settings")
            except:
                logger.info("Creating 'Prompts & Settings' worksheet...")
                self.prompts_sheet = self.spreadsheet.add_worksheet(
                    title="Prompts & Settings",
                    rows=50,
                    cols=10
                )
                self._setup_prompts_headers()
                
        except Exception as e:
            logger.error(f"Error setting up worksheets: {e}")
    
    def _setup_topics_headers(self):
        """Set up headers for topics sheet"""
        headers = [
            "ID", "Title", "Category", "Keywords", "Priority", "Used", 
            "Times Used", "Last Used", "SEO Score Avg", "Performance",
            "Created Date", "Notes"
        ]
        
        try:
            self.topics_sheet.update('A1:L1', [headers])
            
            # Add some formatting (bold headers)
            self.topics_sheet.format('A1:L1', {
                'textFormat': {'bold': True},
                'backgroundColor': {'red': 0.9, 'green': 0.9, 'blue': 0.9}
            })
            
            logger.info("✅ Topics sheet headers configured")
            
        except Exception as e:
            logger.error(f"Error setting up topics headers: {e}")
    
    def _setup_articles_headers(self):
        """Set up headers for articles sheet"""
        headers = [
            "Date Generated", "Title", "Slug", "Category", "Topic ID",
            "Word Count", "SEO Score", "Primary Keyword", "Secondary Keywords",
            "Meta Description", "Read Time", "API Used", "Generation Time",
            "Content Preview", "Schema Markup", "Internal Links", "Status",
            "Published Date", "Performance Score", "Notes"
        ]
        
        try:
            self.articles_sheet.update('A1:T1', [headers])
            
            # Add formatting
            self.articles_sheet.format('A1:T1', {
                'textFormat': {'bold': True},
                'backgroundColor': {'red': 0.8, 'green': 0.9, 'blue': 1.0}
            })
            
            logger.info("✅ Articles sheet headers configured")
            
        except Exception as e:
            logger.error(f"Error setting up articles headers: {e}")
    
    def _setup_prompts_headers(self):
        """Set up prompts and settings sheet"""
        try:
            # Add headers and initial content
            initial_data = [
                ["Setting", "Value", "Description", "Last Updated"],
                ["", "", "", ""],
                ["OPENAI SPECIFIC PROMPT", "", "Optimized prompt for OpenAI GPT-4", ""],
                ["", "", "", ""],
                ["TITLE GENERATION PROMPT", "", "Prompt for generating SEO titles", ""],
                ["", "", "", ""],
                ["META DESCRIPTION PROMPT", "", "Prompt for meta descriptions", ""],
                ["", "", "", ""],
                ["CLAUDE SPECIFIC PROMPT", "", "Optimized prompt for Claude", ""],
                ["", "", "", ""],
                ["POSTING FREQUENCY", "1-3 days", "How often to post", ""],
                ["MIN WORDS", "500", "Minimum article length (quality focused)", ""],
                ["MAX WORDS", "3000", "Maximum article length (increased)", ""],
                ["TARGET SEO SCORE", "80", "Minimum SEO score target", ""],
                ["", "", "", ""],
                ["STATUS", "IMPROVED PROMPTS ACTIVE", "System status", ""],
            ]
            
            self.prompts_sheet.update('A1:D15', initial_data)
            
            # Format headers
            self.prompts_sheet.format('A1:D1', {
                'textFormat': {'bold': True},
                'backgroundColor': {'red': 1.0, 'green': 0.9, 'blue': 0.8}
            })
            
            # Load current prompts
            self._load_current_prompts()
            
            logger.info("✅ Prompts sheet configured")
            
        except Exception as e:
            logger.error(f"Error setting up prompts sheet: {e}")
    
    def _load_current_prompts(self):
        """Load current API-specific prompts from config into sheets"""
        try:
            from config.prompts import (
                BLOG_PROMPT_TEMPLATE, 
                TITLE_GENERATION_PROMPT, 
                EXPERIMENTAL_SAMPLE_PROMPT,
                OPENAI_SPECIFIC_PROMPT,
                CLAUDE_SPECIFIC_PROMPT
            )
            
            # Update the sheet with current prompts
            self.prompts_sheet.update('B3', OPENAI_SPECIFIC_PROMPT[:2000])  # Show OpenAI prompt
            self.prompts_sheet.update('B5', TITLE_GENERATION_PROMPT[:500])
            self.prompts_sheet.update('B9', CLAUDE_SPECIFIC_PROMPT[:2000])  # Show Claude prompt in experimental field
            self.prompts_sheet.update('D3', datetime.now().strftime("%Y-%m-%d %H:%M"))
            self.prompts_sheet.update('D5', datetime.now().strftime("%Y-%m-%d %H:%M"))
            self.prompts_sheet.update('D9', datetime.now().strftime("%Y-%m-%d %H:%M"))
            
            logger.info("✅ Loaded NEW API-specific prompts into Google Sheets")
            
        except Exception as e:
            logger.error(f"Error loading current prompts: {e}")
    
    def sync_topics_to_sheet(self, topics_data: Dict) -> bool:
        """Sync topics from local JSON to Google Sheets"""
        if not self.sheets_available or not self.topics_sheet:
            return False
        
        try:
            # Clear existing data (except headers)
            self.topics_sheet.clear()
            self._setup_topics_headers()
            
            # Prepare data for batch update
            rows_data = []
            
            for topic in topics_data.get("topics", []):
                row = [
                    topic.get("id", ""),
                    topic.get("title", ""),
                    topic.get("category", ""),
                    ", ".join(topic.get("keywords", [])),
                    topic.get("priority", "medium"),
                    "Yes" if topic.get("used", False) else "No",
                    topic.get("times_used", 0),
                    topic.get("last_used", ""),
                    topic.get("avg_seo_score", ""),
                    topic.get("performance_score", ""),
                    topic.get("created_date", ""),
                    topic.get("notes", "")
                ]
                rows_data.append(row)
            
            # Batch update
            if rows_data:
                range_name = f'A2:L{len(rows_data) + 1}'
                self.topics_sheet.update(range_name, rows_data)
            
            logger.info(f"✅ Synced {len(rows_data)} topics to Google Sheets")
            return True
            
        except Exception as e:
            logger.error(f"Error syncing topics to sheet: {e}")
            return False
    
    def sync_topics_from_sheet(self) -> Optional[Dict]:
        """Sync topics from Google Sheets back to local data"""
        if not self.sheets_available or not self.topics_sheet:
            return None
        
        try:
            # Get all data from sheet
            all_values = self.topics_sheet.get_all_values()
            
            if len(all_values) < 2:  # No data rows
                return None
            
            topics = []
            headers = all_values[0]
            
            for row in all_values[1:]:  # Skip header row
                if not row or not row[0]:  # Skip empty rows
                    continue
                
                # Map row data to topic structure
                topic = {
                    "id": int(row[0]) if row[0] else len(topics) + 1,
                    "title": row[1] if len(row) > 1 else "",
                    "category": row[2] if len(row) > 2 else "general",
                    "keywords": [k.strip() for k in row[3].split(",")] if len(row) > 3 and row[3] else [],
                    "priority": row[4] if len(row) > 4 else "medium",
                    "used": row[5].lower() == "yes" if len(row) > 5 else False,
                    "times_used": int(row[6]) if len(row) > 6 and row[6] else 0,
                    "last_used": row[7] if len(row) > 7 else "",
                    "avg_seo_score": row[8] if len(row) > 8 else "",
                    "performance_score": row[9] if len(row) > 9 else "",
                    "created_date": row[10] if len(row) > 10 else datetime.now().strftime("%Y-%m-%d"),
                    "notes": row[11] if len(row) > 11 else ""
                }
                
                topics.append(topic)
            
            # Return in the expected format
            synced_data = {
                "topics": topics,
                "categories": list(set(topic["category"] for topic in topics)),
                "last_synced": datetime.now().isoformat()
            }
            
            logger.info(f"✅ Synced {len(topics)} topics from Google Sheets")
            return synced_data
            
        except Exception as e:
            logger.error(f"Error syncing topics from sheet: {e}")
            return None
    
    def log_generated_article(self, article_data: Dict) -> bool:
        """Log a generated article to Google Sheets"""
        if not self.sheets_available or not self.articles_sheet:
            return False
        
        try:
            # Prepare article data for the sheet
            row_data = [
                datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                article_data.get("title", ""),
                article_data.get("slug", ""),
                article_data.get("category", ""),
                article_data.get("topic_id", ""),
                article_data.get("word_count", ""),
                article_data.get("seo_score", ""),
                article_data.get("primary_keyword", ""),
                ", ".join(article_data.get("secondary_keywords", [])),
                article_data.get("meta_description", "")[:100] + "..." if len(article_data.get("meta_description", "")) > 100 else article_data.get("meta_description", ""),
                article_data.get("read_time", ""),
                article_data.get("api_used", ""),
                article_data.get("generation_time", ""),
                article_data.get("content", "")[:200] + "..." if len(article_data.get("content", "")) > 200 else article_data.get("content", ""),
                "Yes" if article_data.get("schema_markup") else "No",
                str(len(article_data.get("internal_links", []))),
                article_data.get("status", "generated"),
                article_data.get("published_at", ""),
                article_data.get("performance_score", ""),
                ""  # Notes column
            ]
            
            # Append to the sheet
            self.articles_sheet.append_row(row_data)
            
            logger.info(f"✅ Logged article to Google Sheets: {article_data.get('title', 'Unknown')}")
            return True
            
        except Exception as e:
            logger.error(f"Error logging article to sheet: {e}")
            return False
    
    def get_custom_prompt(self, prompt_type: str = "blog") -> Optional[str]:
        """Get custom prompt from Google Sheets if available"""
        if not self.sheets_available or not self.prompts_sheet:
            return None
        
        try:
            # Get all values from prompts sheet
            all_values = self.prompts_sheet.get_all_values()
            
            # Map prompt types to row numbers based on our new structure
            prompt_map = {
                "blog": 3,           # Row 3 - OpenAI prompt (backward compatibility)
                "openai": 3,         # Row 3 - OpenAI Specific Prompt  
                "title": 5,          # Row 5 - Title Generation Prompt
                "meta": 7,           # Row 7 - Meta Description Prompt
                "claude": 9,         # Row 9 - Claude Specific Prompt
                "experimental": 9    # Row 9 - Claude prompt (backward compatibility)
            }
            
            row_index = prompt_map.get(prompt_type, 3)
            
            if len(all_values) > row_index and len(all_values[row_index]) > 1:
                custom_prompt = all_values[row_index][1]  # Column B
                if custom_prompt.strip():
                    logger.info(f"📝 Using custom {prompt_type} prompt from Google Sheets")
                    return custom_prompt
            
            return None
            
        except Exception as e:
            logger.error(f"Error getting custom prompt: {e}")
            return None
    
    def update_topic_usage(self, topic_id: int, seo_score: int = None) -> bool:
        """Update topic usage statistics in Google Sheets"""
        if not self.sheets_available or not self.topics_sheet:
            return False
        
        try:
            # Find the row with the matching topic ID
            all_values = self.topics_sheet.get_all_values()
            
            for i, row in enumerate(all_values):
                if i == 0:  # Skip header
                    continue
                    
                if row and str(row[0]) == str(topic_id):
                    # Update usage data
                    row_num = i + 1
                    
                    # Update "Used" column (F)
                    self.topics_sheet.update(f'F{row_num}', "Yes")
                    
                    # Update "Times Used" column (G)
                    current_count = int(row[6]) if row[6] else 0
                    self.topics_sheet.update(f'G{row_num}', current_count + 1)
                    
                    # Update "Last Used" column (H)
                    self.topics_sheet.update(f'H{row_num}', datetime.now().strftime("%Y-%m-%d"))
                    
                    # Update "SEO Score Avg" column (I) if provided
                    if seo_score:
                        current_avg = row[8] if row[8] else "0"
                        try:
                            current_avg_float = float(current_avg)
                            # Simple running average (could be improved)
                            new_avg = (current_avg_float + seo_score) / 2
                            self.topics_sheet.update(f'I{row_num}', f"{new_avg:.1f}")
                        except:
                            self.topics_sheet.update(f'I{row_num}', str(seo_score))
                    
                    logger.info(f"✅ Updated topic {topic_id} usage in Google Sheets")
                    return True
            
            logger.warning(f"Topic {topic_id} not found in Google Sheets")
            return False
            
        except Exception as e:
            logger.error(f"Error updating topic usage: {e}")
            return False
    
    def get_sheet_url(self) -> Optional[str]:
        """Get the URL to the Google Sheets dashboard"""
        if self.spreadsheet:
            return f"https://docs.google.com/spreadsheets/d/{self.spreadsheet.id}"
        return None
    
    def is_available(self) -> bool:
        """Check if Google Sheets integration is available"""
        return self.sheets_available and self.client is not None 