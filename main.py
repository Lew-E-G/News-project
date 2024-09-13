from API_Guardian import fetch_knife_guardian, fetch_theft_guardian
from API_News import fetch_knife_bbc, fetch_theft_bbc
from cleanup import order_articles_db
import pandas as pd
import sqlite3
import os

#variables for the stored data
bbc_knife_data = fetch_knife_bbc()
guardian_knife_data = fetch_knife_guardian()
bbc_theft_data = fetch_theft_bbc()
guardian_theft_data = fetch_theft_guardian()

def merge_df(bbc, guardian):
    #create DataFrames for the fetched data
    df_bbc = pd.DataFrame(bbc)
    df_guardian = pd.DataFrame(guardian)

    #combine the dataframes and drop duplicates
    df_allArticles = pd.concat([df_bbc,df_guardian], ignore_index=True).drop_duplicates(subset='url')

    #fills in missing data
    df_allArticles['title'].fillna('No headline available', inplace=True)
    df_allArticles['published_at'].fillna('No date available', inplace=True)
    df_allArticles['url'].fillna('No URL available', inplace=True)
    return df_allArticles

df_allKnifeArticles = merge_df(bbc_knife_data, guardian_knife_data)
df_allTheftArticles = merge_df(bbc_theft_data, guardian_theft_data)

#DB file
db_file = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'instance', 'cleaned_articles.db')
conn = sqlite3.connect(db_file)
cursor = conn.cursor()
tables = ['knife_table', 'theft_table']

# Common table structure
table_structure = '''
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    api TEXT,
    published_at NUMERIC,
    title TEXT,
    url TEXT
'''

# Knife crime table
cursor.execute(f'''
    CREATE TABLE IF NOT EXISTS knife_table (
        {table_structure}
    )
''')

# Theft news table
cursor.execute(f'''
    CREATE TABLE IF NOT EXISTS theft_table (
        {table_structure}
    )
''')

#append data to relevant table 
df_allKnifeArticles.to_sql('knife_table', conn, if_exists='append', index=False)
df_allTheftArticles.to_sql('theft_table', conn, if_exists='append', index=False)

#function that clears duplicates and in db
order_articles_db(tables)

conn.close()

# Print confirmation
print(f"Data has been appended to or created in '{db_file}'")

#for testing purposes printing the DataFrames
# print(df_allArticles)
