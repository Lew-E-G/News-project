import sqlite3
from flask import Flask, render_template,request
import os
from main import data_refresh

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/refresh')
def refresh_data_route():
    data_refresh()
    return redirect(url_for('knife_crime'))

@app.route('/knife-crime', methods=['GET', 'POST'])
def knife_crime():
    title = 'Knife Crime'
    #refresh button
    if request.method == 'POST':
        data_refresh()  # Call the refresh function to update the data
    #database connection
    db_file = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'instance', 'cleaned_articles.db')
    conn = sqlite3.connect(db_file)
    cursor = conn.cursor()

    #query to db
    cursor.execute("SELECT api, published_at, title, url FROM knife_table")
    articles = cursor.fetchall()

    conn.close()
    return render_template('category.html', title=title, articles=articles)

@app.route('/theft', methods=['GET', 'POST'])
def theft():
    title = 'Theft and Robbery'
    #refresh button
    if request.method == 'POST':
        data_refresh()  # Call the refresh function to update the data
    #database connection
    db_file = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'instance', 'cleaned_articles.db')
    conn = sqlite3.connect(db_file)
    cursor = conn.cursor()

    #query to db
    cursor.execute("SELECT api, published_at, title, url FROM theft_table")
    articles = cursor.fetchall()

    conn.close()
    return render_template('category.html', title=title, articles=articles)

# additional category to add on the backend
# @app.route('/drugs', methods=['GET', 'POST'])
# def drugs():
#     title = 'Drugs'
#     #database connection
#     db_file = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'instance', 'cleaned_articles.db')
#     conn = sqlite3.connect(db_file)
#     cursor = conn.cursor()
#     return render_template('category.html')

if __name__ == '__main__':
    app.run(debug=True)