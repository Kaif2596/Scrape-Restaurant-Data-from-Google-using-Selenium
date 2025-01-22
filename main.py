from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from bs4 import BeautifulSoup
import pandas as pd

web = 'http://surl.li/gkedpy'
path = 'D:\\chromedriver-win64\\chromedriver.exe'
service = Service(executable_path=path)
driver = webdriver.Chrome(service=service)

# Open the webpage
driver.get(web)

soup = BeautifulSoup(driver.page_source, 'html.parser')

# Find product elements
products = soup.find_all('div', class_='VkpGBb')

Restaurant_Name = []
Restaurant_Rating = []
Cuisine_Type = []
Restaurant_Address = []
Restaurant_Phone = []

for product in products:
    # Extract Restaurant Name
    name = product.find('div', class_='dbg0pd')
    Restaurant_Name.append(name.text.strip() if name else "N/A")

    # Extract Restaurant Rating
    rating = product.find('span', class_='Y0A0hc')
    Restaurant_Rating.append(rating.text.strip() if rating else "N/A")

    # Extract Cuisine Type
    cuisine = product.find('div', class_='pJ3Ci')
    Cuisine_Type.append(cuisine.text.strip() if cuisine else "N/A")

    # Extract Restaurant Address
    address = product.find('div', class_='rllt__details')
    Restaurant_Address.append(address.text.strip() if address else "N/A")


# Close the browser
driver.quit()

# Function to clean unwanted characters from text
def clean_text(text):
    if isinstance(text, str):
        return text.encode('ascii', 'ignore').decode('ascii')
    return text

# Create a DataFrame and clean the data
df_Restaurant = pd.DataFrame({
    'Restaurant_Name': Restaurant_Name,
    'Restaurant_Rating': Restaurant_Rating,
    'Cuisine_Type': [clean_text(address) for address in Cuisine_Type],
    'Restaurant_Address': [clean_text(address) for address in Restaurant_Address],
})

df_Restaurant.to_csv('Restaurants.csv', index=False)

print("Data scraped successfully and saved to Restaurants.csv!")
