# 🎯 Automated Dutch Hunting Exam Blog System

An intelligent, automated blog content generation system specifically designed for Dutch hunting exam (jachtexamen) preparation platforms. This system automatically generates high-quality, SEO-optimized Dutch articles about hunting topics every 3 days.

## 🚀 **Features**

### **🤖 AI-Powered Content Generation**
- Rotating OpenAI GPT-4 and Claude API integration
- 1200+ word articles in perfect Dutch
- Hunting exam-focused content
- Quality assurance and validation

### **🎯 SEO Optimization**
- Automatic title optimization (50-60 characters)
- Meta description generation (150-160 characters)
- Keyword density analysis (1-2%)
- Schema markup (Article, Educational, HowTo)
- Internal linking suggestions

### **📚 Smart Topic Management**
- 30+ pre-loaded hunting exam topics
- Category rotation (Wild, Planten, Jachthonden, Regelgeving, Vuurwapens, Examenvorbereiding)
- Priority-based topic selection
- Google News integration for trending topics
- Automatic topic replenishment

### **💾 Database Integration**
- Supabase database with rich metadata
- Automatic article storage and tracking
- Backup and recovery systems
- Performance analytics

### **⏰ Automated Scheduling**
- Railway deployment with fixed 3-day intervals
- Continuous monitoring and health checks
- Error handling and recovery
- Maintenance automation

## 🏗️ **System Architecture**

```
┌─────────────────┐    ┌─────────────────┐    ┌─────────────────┐
│   Topic Pool    │    │  AI Generation  │    │ SEO Optimizer   │
│  30+ Topics     │ -> │ OpenAI + Claude │ -> │  Meta + Schema  │
└─────────────────┘    └─────────────────┘    └─────────────────┘
                                                        │
┌─────────────────┐    ┌─────────────────┐    ┌─────────────────┐
│ Railway Worker  │ <- │ Supabase Store  │ <- │ Content + SEO   │
│ 3 Day Cycle     │    │ Full Metadata   │    │  Rich Data      │
└─────────────────┘    └─────────────────┘    └─────────────────┘
```

## 📊 **Content Categories**

| **Category** | **Topics** | **Examples** |
|--------------|------------|--------------|
| **Wild** | Animal behavior, species identification | Reeën, wilde zwijnen, watervogels |
| **Planten** | Botany, plant identification | Giftige planten, eetbare wilde planten |
| **Jachthonden** | Dog training, breeds | Nederlandse jachthondenrassen, training |
| **Regelgeving** | Laws, regulations | Jachtwet 2024, jachtseizoen, vergunningen |
| **Vuurwapens** | Firearms, safety | Jachtvuurwapens, veiligheid, munitie |
| **Examenvorbereiding** | Study tips, practice | Examenvragen, tips, fouten |

## 🚂 **Railway Deployment**

### **Quick Setup**

1. **Fork this repository**
2. **Connect to Railway**: [railway.app](https://railway.app)
3. **Deploy from GitHub**
4. **Add environment variables** (see below)
5. **Run database migration** (see `database_migration.sql`)
6. **Done!** 🎉

### **Environment Variables**

```bash
# Required API Keys
OPENAI_API_KEY=your_openai_api_key_here
ANTHROPIC_API_KEY=your_claude_api_key_here

# Supabase Database
SUPABASE_URL=https://your-project.supabase.co
SUPABASE_SERVICE_KEY=your_supabase_service_key_here

# Optional
GOOGLE_NEWS_API_KEY=your_google_news_api_key_here

# Railway Settings
RAILWAY_RUN_MODE=continuous
DAYS_BETWEEN_POSTS=3
ENVIRONMENT=production
```

## 📈 **Performance**

### **Output Quality**
- ✅ 1200-1500 words per article
- ✅ 85+ SEO score
- ✅ Native Dutch language
- ✅ Exam-relevant content
- ✅ Rich metadata and analytics

### **Resource Usage**
- **Memory**: 200-500MB during generation
- **Generation Time**: 2-5 minutes per article
- **API Costs**: ~$2-5 per article
- **Railway Cost**: ~$5-10/month

### **Reliability**
- ✅ Automatic error handling and retries
- ✅ API fallback (OpenAI ↔ Claude)
- ✅ Health monitoring
- ✅ Backup and recovery

## 🛠️ **Development**

### **Local Setup**

```bash
# Clone repository
git clone <your-repo-url>
cd jachtexamen-blog-system

# Install dependencies
pip install -r requirements.txt

# Set up environment
cp env.example .env
# Edit .env with your API keys

# Initialize system
python main.py init

# Generate test article
python main.py generate

# Check statistics
python main.py stats
```

### **Testing**

```bash
# Run tests
pytest tests/

# Check system health
python main.py check

# View statistics
python main.py stats
```

## 📁 **Project Structure**

```
jachtexamen-blog-system/
├── src/                    # Core application code
│   ├── topics.py          # Topic management
│   ├── generator.py       # AI content generation
│   ├── seo.py            # SEO optimization
│   ├── database.py       # Supabase integration
│   ├── scheduler.py      # Automation logic
│   └── utils.py          # Helper functions
├── config/                # Configuration
│   ├── settings.py       # Application settings
│   └── prompts.py        # AI prompt templates
├── data/                  # Topic and tracking data
│   ├── topics.json       # 30+ predefined topics
│   └── published.json    # Publishing tracker
├── tests/                 # Unit tests
├── railway_worker.py      # Railway deployment worker
├── health_server.py       # Health monitoring
├── database_migration.sql # Database setup
├── Dockerfile            # Container configuration
└── requirements.txt      # Python dependencies
```

## 📚 **Documentation**

- **[Railway Deployment Guide](RAILWAY_DEPLOYMENT.md)** - Complete deployment instructions
- **[Database Migration](database_migration.sql)** - SQL setup script
- **[Environment Example](env.example)** - Configuration template

## 🎊 **Results**

Once deployed, your system will automatically:

1. **🎯 Select topics** based on priority and category rotation
2. **🤖 Generate content** using AI with Dutch hunting expertise
3. **🎨 Optimize for SEO** with titles, meta descriptions, and schema
4. **💾 Store in database** with rich metadata and analytics
5. **📊 Track performance** and maintain topic pool
6. **🔄 Repeat every 3 days** for consistent content flow

## 💰 **Cost Estimation**

- **Railway hosting**: $5-10/month
- **OpenAI API**: $2-4 per article
- **Claude API**: $1-3 per article
- **Supabase**: Free tier sufficient
- **Total**: ~$25-50/month for 10-15 articles

## 🎯 **Perfect For**

- ✅ Dutch hunting exam preparation websites
- ✅ Educational content platforms
- ✅ SEO-focused blog automation
- ✅ Consistent content marketing
- ✅ Exam preparation businesses

## 🚀 **Ready to Deploy?**

1. **Star this repository** ⭐
2. **Follow the [Railway Deployment Guide](RAILWAY_DEPLOYMENT.md)**
3. **Watch your automated blog come to life!** 🎉

---

**Built with ❤️ for the Dutch hunting exam community**

*Automated, intelligent, and completely autonomous blog content generation.* 