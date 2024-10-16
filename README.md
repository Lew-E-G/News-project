## ROAD

This is a Python-based web application that aggregates and displays news data about various topics, such as knife, theft, and drug related crime. The app pulls data from multiple APIs, cleans and processes the data, and stores it in a SQL database. The app uses **Flask** for the backend and displays the data via HTML, CSS, and JavaScript on the front end.

## Table of Contents
1. [Features](#features)
2. [Technologies Used](#technologies-used)
3. [Project Structure](#project-structure)
4. [How to Run](#how-to-run)
    - [Prerequisites](#prerequisites)
    - [Step-by-Step Guide](#step-by-step-guide)
5. [Project Details](#project-details)
    - [API Integration](#api-integration)
    - [Data Cleaning](#data-cleaning)
    - [Database](#database)
    - [Front-End](#front-end)
6. [Contributing](#contributing)
    - [How to Contribute](#how-to-contribute)

## Features
- Aggregates news data from various public APIs
- Cleans and processes the data before storing it in a SQL database
- Web interface built with Flask to display news articles
- Separate categories for knife crime, theft, and drug-related articles
- Refresh button to manually update the news data from the APIs
- Pagination and navigation to filter news by category

## Technologies Used
- **Python**: Core language for backend processing
- **Flask**: Backend framework for routing and handling HTTP requests
- **SQL**: For storing the aggregated news data
- **Pandas**: For data cleaning and processing
- **HTML, CSS, JavaScript**: For the front-end web interface
- **API Integration**: Pulling data from multiple public APIs

## Project Structure

  ```bash
    project-root/
    ├── app.py                     # Main Flask app for routing and serving content
    ├── main.py                    # Main logic for fetching, cleaning, and storing news data
    ├── templates/                 # HTML templates folder
    │   ├── index.html             # Main landing page for the app
    │   └── category.html          # Template for displaying categorized news articles
    ├── static/                    # Static files like CSS and images
    │   ├── styles.css             # Custom styles for the app
    │   └── images/                # Folder for any images used in the app
    ├── instance/
    │   └── cleaned_articles.db    # SQLite database where the news articles are stored
    ├── requirements.txt           # Python dependencies required for the project
    └── README.md                  # Project documentation (this file)
  ```

## How to Run

### Prerequisites
- **Python 3.x** installed on your system
- **Flask** and other dependencies listed in `requirements.txt`

### Step-by-Step Guide

1. **Clone the repository**:
   ```bash
    git clone https://github.com/YourUsername/news-aggregation-app.git
    cd news-aggregation-app
   ```

2. **Set up a virtual environment** (recommended):
    ```bash
    python3 -m venv env
    source env/bin/activate  # On Windows use `env\Scripts\activate`
    ```

3. **Install dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

4. **Run the Flask app**:
    ```bash
    flask run
    ```
    Navigate to [http://127.0.0.1:5000/](http://127.0.0.1:5000/) in your browser to view the app.

5. **Manually refresh the news data**:
    - Navigate to the "Refresh" button in the app to pull the latest news from the APIs and store them in the database.

## Project Details

### API Integration
The app pulls data from public news APIs related to knife crime, theft, and drugs. These APIs provide article URLs, publication dates, and article summaries, which are stored in a SQL database.

### Data Cleaning
Once fetched, the data is cleaned using Pandas to remove duplicates, fill missing data, and ensure proper formatting before it's stored in the database.

### Database
The cleaned data is stored in a SQLite database (`cleaned_articles.db`). Each article is categorized by type (knife crime, theft, or drugs) and includes the following fields:
- **Source**: Where the article was published (e.g., BBC, The Guardian)
- **Published Date**: When the article was published
- **URL**: A link to the original article

### Front-End
The app’s front-end is built with HTML, CSS, and JavaScript. Users can view news articles categorized by topic, and a refresh button allows manual updates of the news data.

## Contributing
If you'd like to contribute to this project, feel free to submit a pull request or open an issue. Contributions in the form of new features, bug fixes, or performance improvements are welcome!

### How to Contribute
1. **Fork the repository**
2. **Create a new branch** for your feature or fix:
    ```bash
    git checkout -b feature/new-feature
    ```
3. **Commit your changes**:
    ```bash
    git commit -m "Add a new feature"
    ```
4. **Push to your branch**:
    ```bash
    git push origin feature/new-feature
    ```
5. **Submit a pull request**
