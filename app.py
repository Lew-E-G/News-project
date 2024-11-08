import sqlite3
from flask import Flask, render_template, request, flash, url_for, redirect, session
import os
from main import data_refresh
from datetime import datetime

app = Flask(__name__)
app.secret_key = 'a_random_and_secure_string'


@app.route('/')
def index():
    return redirect(url_for('login'))  # Redirect root to login

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        # Process login form (e.g., check username and password)
        username = request.form.get('username')
        password = request.form.get('password')
        # Placeholder for actual authentication logic
        if username == "user" and password == "pass":  # Example check
            session['authenticated'] = True  # Set authentication status
            return redirect(url_for('home'))  # Redirect to home if login successful
        else:
            flash('Invalid credentials, please try again.')
            return redirect(url_for('login'))

    return render_template('login.html')  # Render login page on GET

@app.route('/home')
def home():
    if not session.get('authenticated'):  # Check if user is authenticated
        flash('Please log in to access this page.')
        return redirect(url_for('login'))
    return render_template('index.html')  # Render the main page after login

@app.route('/knife-crime', methods=['GET', 'POST'])
def knife_crime():
        # Check if the user is authenticated
    if not session.get('authenticated'):
        flash('Please log in to access this page.')
        return redirect(url_for('login'))
    
    try:
        data_refresh()  # Call the refresh function
        flash("Data refreshed successfully!", "success")  # Success message
    except Exception as e:
        flash(f"An error occurred during refresh: {str(e)}", "danger")  # Error message
    
    page_title = 'Knife Crime'
    #refresh button
    if request.method == 'POST':
        try:
            data_refresh()  # Call the refresh function
            flash("Data refreshed successfully!", "success")  # Success message
        except Exception as e:
            flash(f"An error occurred during refresh: {str(e)}", "danger")  # Error message

    #database connection
    db_file = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'instance', 'cleaned_articles.db')
    conn = sqlite3.connect(db_file)
    cursor = conn.cursor()

    #query to db
    cursor.execute("SELECT api, published_at, title, url FROM knife_table")
    articles = cursor.fetchall()
    formatted_articles = []

    #reformats the date column removing the time
    for article in articles:
        api, published_at, title, url = article
        # Parse and format the date
        date_obj = datetime.strptime(published_at, "%Y-%m-%dT%H:%M:%SZ")
        formatted_date = date_obj.strftime("%d/%m/%Y")  # Format as DD/MM/YYYY
        # Append the formatted article
        formatted_articles.append((api, formatted_date, title, url))

    conn.close()

    current_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    return render_template('category.html', page_title=page_title, articles=formatted_articles, current_time=current_time)

@app.route('/theft', methods=['GET', 'POST'])
def theft():
        # Check if the user is authenticated
    if not session.get('authenticated'):
        flash('Please log in to access this page.')
        return redirect(url_for('login'))
    
    try:
        data_refresh()  # Call the refresh function
        flash("Data refreshed successfully!", "success")  # Success message
    except Exception as e:
        flash(f"An error occurred during refresh: {str(e)}", "danger")  # Error message
    
    page_title = 'Theft and Robbery'
    #refresh button
    if request.method == 'POST':
        try:
            data_refresh()  # Call the refresh function
            flash("Data refreshed successfully!", "success")  # Success message
        except Exception as e:
            flash(f"An error occurred during refresh: {str(e)}", "danger")  # Error message

    #database connection
    db_file = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'instance', 'cleaned_articles.db')
    conn = sqlite3.connect(db_file)
    cursor = conn.cursor()

    #query to db
    cursor.execute("SELECT api, published_at, title, url FROM theft_table")
    articles = cursor.fetchall()
    formatted_articles = []
    
    #reformats the date column removing the time
    for article in articles:
        api, published_at, title, url = article
        # Parse and format the date
        date_obj = datetime.strptime(published_at, "%Y-%m-%dT%H:%M:%SZ")
        formatted_date = date_obj.strftime("%d/%m/%Y")  # Format as DD/MM/YYYY
        # Append the formatted article
        formatted_articles.append((api, formatted_date, title, url))

    conn.close()

    current_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    return render_template('category.html', page_title=page_title, articles=formatted_articles, current_time=current_time)

# additional category to add on the backend
@app.route('/drugs', methods=['GET', 'POST'])
def drugs():

        # Check if the user is authenticated
    if not session.get('authenticated'):
        flash('Please log in to access this page.')
        return redirect(url_for('login'))

    try:
        data_refresh()  # Call the refresh function
        flash("Data refreshed successfully!", "success")  # Success message
    except Exception as e:
        flash(f"An error occurred during refresh: {str(e)}", "danger")  # Error message

    page_title = 'Drugs'
    #refresh button
    if request.method == 'POST':
        try:
            data_refresh()  # Call the refresh function
            flash("Data refreshed successfully!", "success")  # Success message
        except Exception as e:
            flash(f"An error occurred during refresh: {str(e)}", "danger")  # Error message

    #database connection
    db_file = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'instance', 'cleaned_articles.db')
    conn = sqlite3.connect(db_file)
    cursor = conn.cursor()

    #query to db
    cursor.execute("SELECT api, published_at, title, url FROM drug_table")
    articles = cursor.fetchall()
    formatted_articles = []
    
    #reformats the date column removing the time
    for article in articles:
        api, published_at, title, url = article
        # Parse and format the date
        date_obj = datetime.strptime(published_at, "%Y-%m-%dT%H:%M:%SZ")
        formatted_date = date_obj.strftime("%d/%m/%Y")  # Format as DD/MM/YYYY
        # Append the formatted article
        formatted_articles.append((api, formatted_date, title, url))

    conn.close()

    current_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    return render_template('category.html', page_title=page_title, articles=formatted_articles, current_time=current_time)

if __name__ == '__main__':
    app.run(debug=True)