import requests
import json
from keys import news_key
from datetime import datetime, timedelta


# Your API key (replace with your actual API key)
api_key = news_key

# Base URL for the News API
url = 'https://newsapi.org/v2/everything'
seven_days_ago_str = (datetime.now() - timedelta(days=30)).strftime('%Y-%m-%d')

# Parameters for the API request
knife_params = {
    'q': '"knife" OR "blade" OR "stab" OR "stabbing" OR "stabbed"',
    'apiKey': api_key,
    'language': 'en',
    'dateStart': seven_days_ago_str,
    'sortBy': 'relevancy',
    'pageSize': 100,  # Number of articles to fetch
    'sources': 'bbc-news'  # You can specify specific sources
}
def fetch_knife_bbc():
    # Make the API request
    response = requests.get(url, params=knife_params)

    # Shows remaining requests do this key
    # rate_limit_remaining = response.headers.get('X-Cache-Remaining')
    # print(f"Requests Remaining: {rate_limit_remaining}")

    # Shows name of all headers in response
    # for header, value in response.headers.items():
    #     print(f"{header}: {value}")

    # Check if the request was successful
    if response.status_code == 200:
        # Parse the JSON response
        results = response.json()['articles']
        # Prints all info (pretty)
        # print(json.dumps(articles, indent=4))
        
        # Create a list to store the fetched articles
        articles = []

        # Display the fetched news articles
        for article in results:
            article_data = {
                'API':'BBC',
                'published_at': article['publishedAt'],
                'title': article['title'],
                # 'body': article['fields'].get('body', 'No body content available'),
                'url': article['url']
            }
            #for testing to see what article data was fetched
            #print(article_data)
            articles.append(article_data)
        return articles
    else:
        print(f"Failed to retrieve news. Status code: {response.status_code}")

theft_params = {
    'q': '"theft" OR "stole" OR "stolen" OR "robbery"',
    'apiKey': api_key,
    'language': 'en',
    'dateStart': seven_days_ago_str,
    'sortBy': 'relevancy',
    'pageSize': 100,  # Number of articles to fetch
    'sources': 'bbc-news'  # You can specify specific sources
}

def fetch_theft_bbc():
    # Make the API request
    response = requests.get(url, params=theft_params)

    # Check if the request was successful
    if response.status_code == 200:
        # Parse the JSON response
        results = response.json()['articles']
        # Prints all info (pretty)
        # print(json.dumps(articles, indent=4))
        
        # Create a list to store the fetched articles
        articles = []

        # Display the fetched news articles
        for article in results:
            article_data = {
                'API':'BBC',
                'published_at': article['publishedAt'],
                'title': article['title'],
                # 'body': article['fields'].get('body', 'No body content available'),
                'url': article['url']
            }
            #for testing to see what article data was fetched
            #print(article_data)
            articles.append(article_data)
        return articles
    else:
        print(f"Failed to retrieve news. Status code: {response.status_code}")

drug_params = {
    'q': '"drug" OR "drugs" OR "narcotics"',
    'apiKey': api_key,
    'language': 'en',
    'dateStart': seven_days_ago_str,
    'sortBy': 'relevancy',
    'pageSize': 100,  # Number of articles to fetch
    'sources': 'bbc-news'  # You can specify specific sources
}

def fetch_drug_bbc():
    # Make the API request
    response = requests.get(url, params=drug_params)

    # Check if the request was successful
    if response.status_code == 200:
        # Parse the JSON response
        results = response.json()['articles']
        # Prints all info (pretty)
        # print(json.dumps(articles, indent=4))
        
        # Create a list to store the fetched articles
        articles = []

        # Display the fetched news articles
        for article in results:
            article_data = {
                'API':'BBC',
                'published_at': article['publishedAt'],
                'title': article['title'],
                # 'body': article['fields'].get('body', 'No body content available'),
                'url': article['url']
            }
            #for testing to see what article data was fetched
            #print(article_data)
            articles.append(article_data)
        return articles
    else:
        print(f"Failed to retrieve news. Status code: {response.status_code}")

if __name__ == '__main__':
    fetch_knife_bbc()
    fetch_theft_bbc()
    fetch_drug_bbc()