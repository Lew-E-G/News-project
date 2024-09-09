import feedparser
import ssl

# Disable SSL verification (not secure for production)
ssl._create_default_https_context = ssl._create_unverified_context
# Define the RSS feed URL for Sky News UK
rss_feed_url = 'https://feeds.skynews.com/feeds/rss/uk.xml'

# Parse the RSS feed using feedparser
feed = feedparser.parse(rss_feed_url)

# Print out some details about the feed
print(f"Feed Title: {feed.feed.get('title', 'No title available')}")
print(f"Feed Link: {feed.feed.get('link', 'No link available')}")
print(f"Feed Description: {feed.feed.get('description', 'No description available')}")
print("\nArticles:\n")

# Loop through the entries (articles) in the feed
for entry in feed.entries:
    print(f"Title: {entry.title}")
    print(f"Published: {entry.published}")
    print(f"Link: {entry.link}")
    print(f"Summary: {entry.summary}")
    print("-" * 50)