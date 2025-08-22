# 🚂 Railway Deployment Guide

Complete guide to deploy the Jachtexamen Blog System on Railway for automated content generation every 3 days.

## 🎯 **Why Railway?**

✅ **Perfect for our use case:**
- Unlimited execution time (vs 30sec Supabase Edge limit)
- Full Python environment support
- Built-in cron scheduling
- GitHub integration
- Persistent storage for logs
- Easy environment variable management

## 🚀 **Deployment Steps**

### **1. Prepare Your Database**

Run this SQL in your Supabase SQL editor to add missing columns:

```sql
-- Add missing columns to existing table
ALTER TABLE public.blog_articles
ADD COLUMN IF NOT EXISTS excerpt TEXT,
ADD COLUMN IF NOT EXISTS meta_description TEXT,
ADD COLUMN IF NOT EXISTS cover_image_alt TEXT,
ADD COLUMN IF NOT EXISTS primary_keyword TEXT,
ADD COLUMN IF NOT EXISTS secondary_keywords TEXT[],
ADD COLUMN IF NOT EXISTS internal_links JSONB,
ADD COLUMN IF NOT EXISTS schema_markup JSONB,
ADD COLUMN IF NOT EXISTS updated_at TIMESTAMP WITH TIME ZONE DEFAULT NOW(),
ADD COLUMN IF NOT EXISTS status TEXT DEFAULT 'published',
ADD COLUMN IF NOT EXISTS author TEXT DEFAULT 'Jachtexamen Expert',
ADD COLUMN IF NOT EXISTS read_time INTEGER,
ADD COLUMN IF NOT EXISTS geo_targeting TEXT[] DEFAULT ARRAY['Nederland', 'België'],
ADD COLUMN IF NOT EXISTS language TEXT DEFAULT 'nl-NL',
ADD COLUMN IF NOT EXISTS category TEXT,
ADD COLUMN IF NOT EXISTS topic_id INTEGER,
ADD COLUMN IF NOT EXISTS seo_score INTEGER,
ADD COLUMN IF NOT EXISTS keyword_analysis JSONB;

-- Add performance indexes
CREATE INDEX IF NOT EXISTS idx_blog_published ON public.blog_articles(published_at DESC);
CREATE INDEX IF NOT EXISTS idx_blog_category ON public.blog_articles(category);
CREATE INDEX IF NOT EXISTS idx_blog_status ON public.blog_articles(status);
```

### **2. Update Code for Production**

Change this line in `main.py`:
```python
# Change from:
from src.database_mock import DatabaseManager

# To:
from src.database import DatabaseManager
```

### **3. Push to GitHub**

```bash
git add .
git commit -m "Add Railway deployment configuration"
git push origin main
```

### **4. Deploy to Railway**

1. **Go to Railway.app** and sign in
2. **Click "New Project"**
3. **Select "Deploy from GitHub repo"**
4. **Choose your repository**
5. **Railway will auto-detect the Dockerfile**

### **5. Configure Environment Variables**

In Railway dashboard, go to **Variables** tab and add:

```bash
# Required API Keys
OPENAI_API_KEY=your_openai_api_key_here
ANTHROPIC_API_KEY=your_claude_api_key_here

# Supabase Database
SUPABASE_URL=https://your-project.supabase.co
SUPABASE_SERVICE_KEY=your_supabase_service_key_here

# Optional: Google News (leave blank if you don't have it)
GOOGLE_NEWS_API_KEY=your_google_news_api_key_here

# Application Settings
ENVIRONMENT=production
LOG_LEVEL=INFO
TIMEZONE=Europe/Amsterdam

# Railway-specific Settings
RAILWAY_RUN_MODE=continuous
DAYS_BETWEEN_POSTS=3
```

### **6. Configure Railway Cron**

**Option A: Continuous Mode (Recommended)**
- Set `RAILWAY_RUN_MODE=continuous`
- App runs continuously, checks every hour
- Generates articles every 1-3 days randomly

**Option B: Railway Cron Service**
- Create a separate Railway service
- Add this to your Railway deployment:
```bash
# In Railway dashboard, create a new service
# Set the start command to:
python railway_worker.py
```

## 📊 **Monitoring & Management**

### **View Logs**
- Railway Dashboard → Your Service → **Logs**
- Filter for specific log levels
- Real-time log streaming

### **Manual Trigger**
Connect to Railway and run:
```bash
python railway_worker.py
```

### **Check System Status**
```bash
python main.py stats
python main.py check
```

## ⚙️ **Configuration Options**

### **Posting Frequency**
Control via environment variables:
```bash
MIN_DAYS_BETWEEN_POSTS=1    # Minimum 1 day
MAX_DAYS_BETWEEN_POSTS=3    # Maximum 3 days
```

### **Content Categories**
The system automatically rotates through:
- Wild (animals, wildlife)
- Planten (plants, botany)  
- Jachthonden (hunting dogs)
- Regelgeving (laws, regulations)
- Vuurwapens (firearms, safety)
- Examenvorbereiding (exam prep)

### **Quality Settings**
Configured in `config/settings.py`:
```python
QA_REQUIREMENTS = {
    "min_words": 1000,        # Minimum article length
    "max_words": 2500,        # Maximum article length
    "keyword_density_min": 0.01,  # 1% minimum
    "keyword_density_max": 0.02   # 2% maximum
}
```

## 🔍 **Troubleshooting**

### **Common Issues**

**1. API Client Errors**
```bash
# Check API keys are set
echo $OPENAI_API_KEY
echo $ANTHROPIC_API_KEY
```

**2. Database Connection Issues**
```bash
# Verify Supabase credentials
echo $SUPABASE_URL
echo $SUPABASE_SERVICE_KEY
```

**3. No Topics Available**
```bash
# Check topic status
python -c "
from src.topics import TopicManager
tm = TopicManager()
stats = tm.get_topic_statistics()
print(f'Available topics: {stats[\"unused_topics\"]}/{stats[\"total_topics\"]}')
"
```

**4. Generation Failures**
- Check Railway logs for detailed errors
- Verify API quotas aren't exceeded
- Ensure database table has all required columns

### **Emergency Fixes**

**Reset Topic Usage:**
```python
# In Python console
from src.topics import TopicManager
tm = TopicManager()
for topic in tm.topics_data["topics"]:
    topic["used"] = False
tm._save_topics()
```

**Manual Article Generation:**
```bash
python main.py generate --category wild
```

## 📈 **Expected Performance**

### **Resource Usage**
- **Memory**: ~200-500MB during generation
- **CPU**: High during AI API calls (2-5 minutes)
- **Storage**: Minimal (logs + topic tracking)
- **Network**: API calls to OpenAI/Claude/Supabase

### **Timing**
- **Article Generation**: 2-5 minutes per article
- **Check Frequency**: Every hour
- **Actual Generation**: Every 1-3 days
- **Maintenance**: Weekly

### **Cost Estimation**
- **Railway**: ~$5-10/month (starter plan sufficient)
- **OpenAI API**: ~$2-5 per article
- **Claude API**: ~$1-3 per article
- **Total**: ~$20-50/month for 10-15 articles

## 🎊 **Success Indicators**

Your deployment is successful when you see:

✅ **Railway Logs Show:**
```
🚀 Railway Blog Worker Starting...
🔧 Running maintenance tasks...
📊 Database: X total articles
📊 Topics: Y/30 available
📋 Selected topic: [Topic Title]
🎯 SEO Score: 85/100
✅ Article published successfully
🎉 Blog generation cycle completed successfully!
```

✅ **Supabase Database:**
- New articles appearing in `blog_articles` table
- All columns populated with rich metadata
- SEO data, keywords, schema markup included

✅ **System Health:**
```bash
python main.py check
# Shows all systems healthy
```

## 🔄 **Ongoing Maintenance**

### **Weekly Tasks**
1. Check Railway logs for any errors
2. Verify articles are being generated
3. Monitor API usage and costs
4. Review topic availability

### **Monthly Tasks**
1. Update topic list with new hunting exam content
2. Review and adjust posting frequency
3. Analyze article performance
4. Update dependencies if needed

### **Scaling Options**
- **More Frequent**: Decrease `MIN_DAYS_BETWEEN_POSTS`
- **Multiple Categories**: Run separate Railway services
- **Higher Quality**: Increase word count requirements
- **More Topics**: Add seasonal or trending topics

---

**Your automated Dutch hunting exam blog system is now running in the cloud! 🚀**

Every 1-3 days, it will automatically:
1. 🎯 Select a high-priority topic
2. 🤖 Generate 1000+ word Dutch content
3. 🎨 Optimize for SEO (titles, meta, schema)
4. 💾 Save to your Supabase database
5. 📊 Track performance and statistics

The system is completely autonomous and will keep your blog fresh with high-quality, exam-focused content! 