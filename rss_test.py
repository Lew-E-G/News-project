import requests
import feedparser
import certifi

def fetch_sky_news():
    url = 'https://feeds.skynews.com/feeds/rss/uk.xml'
    
    # Use requests to fetch the RSS feed, specifying certifi for SSL verification
    response = requests.get(url, verify=certifi.where())
    if response.status_code == 200:
        feed = feedparser.parse(response.content)
        
        articles = []
        for entry in feed.entries:
            articles.append({
                'title': entry.title,
                'headline': entry.title,  # Using the title as the headline
                'publication_date': entry.published,
                'url': entry.link
            })
        
        return articles
    else:
        print(f"Failed to fetch data: {response.status_code}")
        return []

# Example usage
sky_news_articles = fetch_sky_news()
for article in sky_news_articles:
    print(article)
