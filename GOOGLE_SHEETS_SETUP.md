# 📊 Google Sheets Dashboard Setup

Complete guide to set up your Google Sheets dashboard for topic management and article tracking.

## 🎯 **What You'll Get**

### **Dashboard with 3 Sheets:**
1. **📋 Topics Management** - View, add, edit topics and track performance
2. **📝 Generated Articles** - Real-time log of all written articles with stats
3. **⚙️ Prompts & Settings** - Experiment with AI prompts and system settings

## 🚀 **Setup Steps**

### **Step 1: Create Google Service Account**

1. **Go to Google Cloud Console**: https://console.cloud.google.com/
2. **Create new project** or select existing one
3. **Enable APIs**:
   - Go to "APIs & Services" → "Library"
   - Enable **Google Sheets API**
   - Enable **Google Drive API**

4. **Create Service Account**:
   - Go to "APIs & Services" → "Credentials"
   - Click "Create Credentials" → "Service Account"
   - Name: `jachtexamen-blog-system`
   - Click "Create and Continue"
   - Skip roles for now, click "Done"

5. **Generate Key**:
   - Click on your service account
   - Go to "Keys" tab
   - Click "Add Key" → "Create New Key"
   - Choose **JSON** format
   - Download the file (save as `google_credentials.json`)

### **Step 2: Create Google Sheets**

1. **Create new Google Sheets**: https://sheets.google.com/
2. **Name it**: `Jachtexamen Blog Dashboard`
3. **Copy the Spreadsheet ID** from URL:
   ```
   https://docs.google.com/spreadsheets/d/18Ek08nkUhgiMZku97X2Si93Vyfun1miQSHkXsfZeUgM/edit?gid=0#gid=0
   ```

### **Step 3: Share Sheet with Service Account**

1. **Open your Google Sheets**
2. **Click "Share"**
3. **Add the service account email** (found in your JSON file as `client_email`)
4. **Give "Editor" permissions**
5. **Click "Send"**

### **Step 4: Configure Railway Environment**

Add these variables in Railway Dashboard → Variables:

```bash
# Google Sheets Integration
GOOGLE_SHEETS_ID=your_spreadsheet_id_here
GOOGLE_SHEETS_CREDENTIALS_JSON={"type":"service_account","project_id":"..."}
```

**For the credentials JSON:**
1. **Open your downloaded JSON file**
2. **Copy the ENTIRE contents**
3. **Paste as one line** in the environment variable

**Alternative: Upload JSON file**
```bash
GOOGLE_SHEETS_CREDENTIALS_PATH=google_credentials.json
```

## 📊 **Sheet Structure**

### **Topics Management Sheet**
| Column | Field | Description |
|--------|-------|-------------|
| A | ID | Unique topic identifier |
| B | Title | Article title/topic |
| C | Category | wild, planten, regelgeving, etc. |
| D | Keywords | Comma-separated keywords |
| E | Priority | high, medium, low |
| F | Used | Yes/No if topic was used |
| G | Times Used | How many times generated |
| H | Last Used | Date last used |
| I | SEO Score Avg | Average SEO performance |
| J | Performance | Overall performance score |
| K | Created Date | When topic was added |
| L | Notes | Your custom notes |

### **Generated Articles Sheet**
| Column | Field | Description |
|--------|-------|-------------|
| A | Date Generated | When article was created |
| B | Title | Article title |
| C | Slug | URL slug |
| D | Category | Content category |
| E | Topic ID | Source topic ID |
| F | Word Count | Article length |
| G | SEO Score | SEO optimization score |
| H | Primary Keyword | Main keyword |
| I | Secondary Keywords | Supporting keywords |
| J | Meta Description | SEO description |
| K | Read Time | Estimated reading time |
| L | API Used | OpenAI/Claude |
| M | Generation Time | How long it took |
| N | Content Preview | First 200 characters |
| O | Schema Markup | Yes/No |
| P | Internal Links | Number of internal links |
| Q | Status | generated/published |
| R | Published Date | When published |
| S | Performance Score | Overall performance |
| T | Notes | Your notes |

### **Prompts & Settings Sheet**
| Setting | Purpose |
|---------|---------|
| **CURRENT BLOG PROMPT** | Main AI prompt for articles |
| **TITLE GENERATION PROMPT** | Prompt for SEO titles |
| **META DESCRIPTION PROMPT** | Prompt for meta descriptions |
| **EXPERIMENTAL PROMPT** | Test new prompts here |
| **POSTING FREQUENCY** | How often to post |
| **MIN/MAX WORDS** | Article length settings |
| **TARGET SEO SCORE** | Quality target |

## 🎮 **How to Use**

### **Adding New Topics**
1. **Open Topics Management sheet**
2. **Add new row** with:
   - **ID**: Next available number
   - **Title**: Your topic idea
   - **Category**: wild/planten/regelgeving/etc.
   - **Keywords**: Comma-separated
   - **Priority**: high/medium/low
3. **System will sync** on next run

### **Experimenting with Prompts**
1. **Open Prompts & Settings sheet**
2. **Edit the EXPERIMENTAL PROMPT** cell
3. **System will use it** for next generation
4. **Monitor results** in Generated Articles sheet

### **Monitoring Performance**
1. **Check Generated Articles sheet** for new entries
2. **Review SEO scores** and performance
3. **Add notes** for improvement ideas
4. **Track topic usage** patterns

## 🔄 **Sync Behavior**

### **Bidirectional Sync**
- ✅ **Local → Sheets**: System pushes topics and articles
- ✅ **Sheets → Local**: System pulls new topics you add
- ✅ **Real-time**: Updates happen every generation cycle

### **What Gets Synced**
- **Topics**: All topic data, usage stats, performance
- **Articles**: Every generated article with full metadata
- **Prompts**: Custom prompts from sheets are used
- **Settings**: Configuration changes affect behavior

## 📱 **Mobile Access**

Access your dashboard from anywhere:
- **Google Sheets mobile app**
- **Web browser on phone/tablet**
- **Real-time updates** as articles are generated

## 🎊 **Example Usage Workflow**

1. **💡 Get Content Ideas**
   - Add new topics to Google Sheets
   - Set priority levels
   - Add relevant keywords

2. **🧪 Experiment with Prompts**
   - Try different writing styles
   - Test new keyword strategies
   - Monitor SEO score improvements

3. **📊 Monitor Performance**
   - Track which topics perform best
   - See SEO score trends
   - Identify successful patterns

4. **🔄 Optimize Content Strategy**
   - Focus on high-performing categories
   - Refine prompts based on results
   - Plan content calendar

## 🚨 **Troubleshooting**

### **Common Issues**

**Service Account Access Denied**
- Verify sheet is shared with service account email
- Check credentials JSON is valid
- Ensure APIs are enabled

**Environment Variables Not Working**
- Check JSON is properly formatted (one line)
- Verify Railway variables are set
- Restart Railway service after changes

**Sync Not Working**
- Check Railway logs for Google Sheets errors
- Verify internet connection in Railway
- Check API quotas not exceeded

**Sheet Structure Wrong**
- System auto-creates correct headers
- Don't modify header row
- Let system initialize sheets first

## 💡 **Pro Tips**

1. **Use Conditional Formatting** in sheets to highlight high-performing topics
2. **Add Charts** to visualize SEO score trends
3. **Use Filters** to focus on specific categories
4. **Set up Notifications** for new articles via Google Sheets
5. **Export Data** regularly for analysis

---

**🎯 Your Google Sheets dashboard gives you complete visibility and control over your automated blog system!** 