import pandas as pd
import sqlite3

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

def order_articles_db(db_file):
    # Connect to SQLite database
    conn = sqlite3.connect(db_file)

    # Step 1: Read the existing data from the table into a Pandas DataFrame
    df = pd.read_sql('SELECT * FROM articles_table ORDER BY published_at', conn)

    # Step 2: Remove duplicates
    df_cleaned = df.drop_duplicates(subset=['url'])

    # Step 3: Write the cleaned data back to the SQL table, replacing the old data
    df_cleaned.to_sql('articles_table', conn, if_exists='replace', index=False)

    # Close the connection when done
    conn.close()

if __name__ == '__main__':
    order_articles_db()
    order_articles_csv()