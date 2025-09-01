import requests
from bs4 import BeautifulSoup

# Target URL
url = 'https://www.amazing-africa.co.za/3-facts-about-port-elizabeth/'

# Send HTTP request
headers = {'User-Agent': 'Mozilla/5.0'}
response = requests.get(url, headers=headers)

# Parse HTML content
soup = BeautifulSoup(response.text, 'lxml')

# Extract and print all visible text
print("Text from the Amazing Africa:")
print(soup.get_text(separator='\n', strip=True))
