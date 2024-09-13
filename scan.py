# scan.py
import argparse
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup

def scan_web_app(url):
    # Initialize the Chrome WebDriver
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

    # Load the web page
    driver.get(url)

    # Get the page source and analyze with BeautifulSoup
    soup = BeautifulSoup(driver.page_source, 'html.parser')

    # Find forms and input fields
    forms = soup.find_all('form')
    input_fields = soup.find_all('input')

    # Print forms and input fields
    print("Forms:")
    for form in forms:
        print(form)
    print("Input Fields:")
    for field in input_fields:
        print(field)

    # Close the driver
    driver.quit()

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Scan a web application")
    parser.add_argument('url', help="Target URL to scan")
    args = parser.parse_args()

    scan_web_app(args.url)
