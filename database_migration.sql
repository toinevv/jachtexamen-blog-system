-- Migration script to add missing columns to existing blog_articles table
-- Run this in your Supabase SQL editor

-- Add missing columns
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

-- Rename existing keyword column to primary_keyword if needed
-- (Skip this if you want to keep both)
-- UPDATE public.blog_articles SET primary_keyword = keyword WHERE primary_keyword IS NULL;

-- Add indexes for performance
CREATE INDEX IF NOT EXISTS idx_blog_published ON public.blog_articles(published_at DESC);
CREATE INDEX IF NOT EXISTS idx_blog_category ON public.blog_articles(category);
CREATE INDEX IF NOT EXISTS idx_blog_status ON public.blog_articles(status);
CREATE INDEX IF NOT EXISTS idx_blog_tags ON public.blog_articles USING GIN(tags);

-- Add updated_at trigger
CREATE OR REPLACE FUNCTION update_updated_at_column()
RETURNS TRIGGER AS $$
BEGIN
    NEW.updated_at = NOW();
    RETURN NEW;
END;
$$ language 'plpgsql';

CREATE TRIGGER update_blog_articles_updated_at 
    BEFORE UPDATE ON public.blog_articles 
    FOR EACH ROW EXECUTE FUNCTION update_updated_at_column();

-- Verify the changes
SELECT column_name, data_type, is_nullable, column_default
FROM information_schema.columns 
WHERE table_name = 'blog_articles' 
ORDER BY ordinal_position; 