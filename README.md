
# Scrape Restaurant Data from Google using Selenium

## 📋 Description

This project is a Python-based web scraper designed to extract restaurant data from Google Search results. It leverages Selenium for browser automation and BeautifulSoup for HTML parsing. The scraper gathers details such as restaurant names, ratings, cuisine types, and addresses, and stores the information in a CSV file for easy access and analysis.




## 🚀 Features

**Automated Web Scraping:** Uses Selenium to navigate and scrape Google search results dynamically.

**Data Extraction:** Extracts restaurant details such as:

• Restaurant Name

• Rating

• Cuisine Type

• Address

**Data Cleaning:** Ensures that extracted data is clean and free of unwanted characters.

**CSV Export:** Saves the scraped data into a structured CSV file.


## 🔧 Tech Stack

**Programming Language:** Python

**Libraries/Frameworks:** Selenium and BeautifulSoup

**Data Preprocessing:** Pandas, Numpy

**Visualization:** Matplotlib, wordcloud libraries

**Model Used:** Naive Bayes or Logistic Regression

**Deployment:** Flask/Streamlit for creating a user interface
## 🧠 How It Works

1.) The script launches a Chrome browser using Selenium and navigates to the specified URL.

2.) It parses the page source using BeautifulSoup to locate restaurant details.

3.) Data is extracted from HTML elements using class-based selectors.

4.) Cleaned data is stored in lists and compiled into a Pandas DataFrame.

5.) The resulting DataFrame is exported to a CSV file named Restaurants.csv.


## 🛠️ Installation and Setup

**1.) Prerequisites**

• Python installed on your system.

• Google Chrome browser installed.

• ChromeDriver executable.

**2.) Install dependencies:**

pip install selenium beautifulsoup4 pandas

**3.) Run the application:**

streamlit run app.py



## 📊 Demo

1.) Selenium navigates to the Google search results page for restaurants.

2.) BeautifulSoup extracts relevant details from the page's HTML structure.

3.) Cleaned data is displayed and saved into Restaurants.csv.



 
## 📈 Results

•  A CSV file named Restaurants.csv is generated containing the following fields:

•  Restaurant_Name

• Restaurant_Rating

• Cuisine_Type

• Restaurant_Address

