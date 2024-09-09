from API_Guardian import fetch_guardian
from API_News import fetch_bbc
from cleanup import order_articles_csv, order_articles_db
import pandas as pd
import sqlite3
import os

#variables for the stored data
bbc_data = fetch_bbc()
guardian_data = fetch_guardian()

#create DataFrames for the fetched data
df_bbc = pd.DataFrame(bbc_data)
df_guardian = pd.DataFrame(guardian_data)

#combine the dataframes and drop duplicates
df_allArticles = pd.concat([df_bbc,df_guardian], ignore_index=True).drop_duplicates(subset='url')

#DB file
db_file = 'cleaned_articles.db'
conn = sqlite3.connect('cleaned_articles.db')
cursor = conn.cursor()

#combine the dataframes and drop duplicates
df_allArticles = pd.concat([df_bbc,df_guardian], ignore_index=True).drop_duplicates(subset='url')

#fills in missing data
df_allArticles['title'].fillna('No headline available', inplace=True)
df_allArticles['published_at'].fillna('No date available', inplace=True)
df_allArticles['url'].fillna('No URL available', inplace=True)

cursor.execute('''
    CREATE TABLE IF NOT EXISTS articles_table (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        api TEXT,
        published_at NUMERIC,
        title TEXT,
        url TEXT 
    )
''')

df_allArticles.to_sql('articles_table', conn, if_exists='append', index=False)

conn.close()
# Specify the CSV file name
# csv_file = 'cleaned_articles.csv'

# Check if the file already exists
# if os.path.exists(csv_file):
#     # Load the existing file to check if it's empty
    
#     # Append new data to the existing CSV file
#     df_allArticles.to_sql(csv_file, mode='a', index=False, header=existing_data.empty)
# else:
#     # If the file does not exist, write the data with headers
#     df_allArticles.to_sql(csv_file, mode='w', index=False)

#function to clean up CSV
# order_articles_csv(csv_file)

#function that clears duplicates and in db
order_articles_db(db_file)

# Print confirmation
print(f"Data has been appended to or created in '{db_file}'")

#for testing purposes printing the DataFrames
# print(df_allArticles)
