import pandas as pd
import sqlite3
import os

db_file = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'instance', 'cleaned_articles.db')
conn = sqlite3.connect(db_file)
cursor = conn.cursor()

def order_articles_csv(csv_file):
    # Read the CSV file into a DataFrame
    df = pd.read_csv(csv_file)
    
    # Convert the 'published_at' column to datetime format, handling errors
    df['published_at'] = pd.to_datetime(df['published_at'], errors='coerce')
    print(df)
    # Check for any NaT values (errors in conversion)
    if df['published_at'].isna().any():
        print("Some dates could not be converted and are set to NaT.")
    
    # Sort the DataFrame by the 'published_at' column
    df_sorted = df.sort_values(by='published_at', ascending=False)
    
    # Remove duplicates based on the 'url' column to keep only unique articles
    df_sorted_unique = df_sorted.drop_duplicates(subset='url')
    
    # Save the modified DataFrame back to the CSV file
    df_sorted_unique.to_csv(csv_file, index=False)

#main function to clean the tables
def order_articles_db(tables):
    db_file = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'instance', 'cleaned_articles.db')
    conn = sqlite3.connect(db_file)
    cursor = conn.cursor()
    for table in tables:
        # Step 1: Read the data from each table into a Pandas DataFrame
        df = pd.read_sql(f'SELECT * FROM {table}', conn)
        
        # Step 2: Remove duplicates based on the 'url' column
        df_cleaned = df.drop_duplicates(subset=['url'])

        # Order by date the article was published
        df_ordered = df_cleaned.sort_values(by='published_at')
        
        # Step 3: Write the cleaned DataFrame back to the SQLite table (replace the old data)
        df_ordered.to_sql(table, conn, if_exists='replace', index=False)
    conn.close()

if __name__ == '__main__':
    order_articles_db()
    order_articles_csv()