# ============================================================
# Zillow Clone - Property Scraper + Google Form Automation
# ============================================================
#
# Tested package versions from the original project:
# beautifulsoup4==4.12.2
# requests==2.31.0
# selenium==4.15.1
#
# Install the packages with:
#
# py -m pip install beautifulsoup4 requests selenium
#
# ============================================================

from bs4 import BeautifulSoup
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


# ============================================================
# PART 1 - SCRAPE THE PROPERTY INFORMATION
# ============================================================

# Website we are scraping.
# This is the App Brewery Zillow Clone used for the project.
ZILLOW_CLONE_URL = "https://appbrewery.github.io/Zillow-Clone/"


# User-Agent information.
# This makes the request look like it is coming from a normal browser.
headers = {
    "User-Agent": (
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/142.0.0.0 Safari/537.36"
    ),
    "Accept-Language": "en-GB,en-US;q=0.9,en;q=0.8"
}


print("=" * 60)
print("ZILLOW CLONE PROPERTY SCRAPER")
print("=" * 60)

print("\nConnecting to the Zillow Clone website...")


# ------------------------------------------------------------
# Connect to the website
# ------------------------------------------------------------

try:
    response = requests.get(
        ZILLOW_CLONE_URL,
        headers=headers,
        timeout=20
    )

    # Raise an error if the server returns an HTTP error.
    response.raise_for_status()

    print("Successfully connected to the website.")
    print(f"Status code: {response.status_code}")

except requests.exceptions.ConnectionError:
    print("\nERROR: Could not connect to the website.")
    print("Please check your internet connection or DNS settings.")
    print("Make sure this website opens in your browser:")
    print(ZILLOW_CLONE_URL)
    exit()

except requests.exceptions.Timeout:
    print("\nERROR: The website took too long to respond.")
    print("Please check your internet connection and try again.")
    exit()

except requests.exceptions.RequestException as error:
    print("\nERROR: Something went wrong while connecting.")
    print(error)
    exit()


# ============================================================
# PART 2 - BEAUTIFULSOUP
# ============================================================

# Get the HTML source code.
data = response.text

# Convert the HTML into a BeautifulSoup object.
soup = BeautifulSoup(data, "html.parser")


# ------------------------------------------------------------
# Get all property links
# ------------------------------------------------------------

all_link_elements = soup.select(
    ".StyledPropertyCardDataWrapper a"
)

all_links = [
    link.get("href")
    for link in all_link_elements
    if link.get("href")
]


print(
    f"\nThere are {len(all_links)} property links in total:"
)

for number, link in enumerate(all_links, start=1):
    print(f"{number}. {link}")


# ------------------------------------------------------------
# Get all property addresses
# ------------------------------------------------------------

all_address_elements = soup.select(
    ".StyledPropertyCardDataWrapper address"
)

all_addresses = [
    address.get_text()
    .replace(" | ", " ")
    .replace("\n", " ")
    .strip()
    for address in all_address_elements
]


print(
    f"\nThere are {len(all_addresses)} property addresses:"
)

for number, address in enumerate(all_addresses, start=1):
    print(f"{number}. {address}")


# ------------------------------------------------------------
# Get all property prices
# ------------------------------------------------------------

all_price_elements = soup.select(
    ".PropertyCardWrapper span"
)

all_prices = [
    price.get_text()
    .replace("/mo", "")
    .split("+")[0]
    .strip()
    for price in all_price_elements
    if "$" in price.get_text()
]


print(
    f"\nThere are {len(all_prices)} property prices:"
)

for number, price in enumerate(all_prices, start=1):
    print(f"{number}. {price}")


# ============================================================
# CHECK THAT THE DATA MATCHES
# ============================================================

print("\n" + "=" * 60)
print("CHECKING SCRAPED DATA")
print("=" * 60)

print(f"Links:     {len(all_links)}")
print(f"Addresses: {len(all_addresses)}")
print(f"Prices:    {len(all_prices)}")


# The three lists should contain the same number of properties.
if not (
    len(all_links)
    == len(all_addresses)
    == len(all_prices)
):
    print("\nWARNING!")
    print(
        "The number of links, addresses and prices "
        "does not match."
    )
    print(
        "Please check the website selectors before "
        "continuing."
    )
    exit()


print("\nAll three lists contain the same number of properties.")


# ============================================================
# PART 3 - GOOGLE FORM
# ============================================================

# IMPORTANT:
#
# Replace this URL with YOUR Google Form URL.
#
# Example:
# GOOGLE_FORM_URL = "https://docs.google.com/forms/d/e/XXXXXXXXXXXX/viewform"
#

GOOGLE_FORM_URL = "https://docs.google.com/forms/d/e/1FAIpQLSeZBxvzVNMsOm2QX2X5Wo6YOlUSWDuw3ah64BgeISS2V-Q0dA/viewform?usp=header"


if GOOGLE_FORM_URL == "https://docs.google.com/forms/d/e/1FAIpQLSeZBxvzVNMsOm2QX2X5Wo6YOlUSWDuw3ah64BgeISS2V-Q0dA/viewform?usp=header":

    print("\n" + "=" * 60)
    print("GOOGLE FORM SETUP REQUIRED")
    print("=" * 60)

    print(
        "\nYou need to replace:"
    )

    print(
        'https://docs.google.com/forms/d/e/1FAIpQLSeZBxvzVNMsOm2QX2X5Wo6YOlUSWDuw3ah64BgeISS2V-Q0dA/viewform?usp=header'
    )

    print(
        "\nhttps://docs.google.com/forms/d/e/1FAIpQLSeZBxvzVNMsOm2QX2X5Wo6YOlUSWDuw3ah64BgeISS2V-Q0dA/viewform?usp=header."
    )

    print(
        "\nExample:"
    )

    print(
        'GOOGLE_FORM_URL = "https://docs.google.com/forms/d/e/1FAIpQLSeZBxvzVNMsOm2QX2X5Wo6YOlUSWDuw3ah64BgeISS2V-Q0dA/viewform?usp=header"'
    )

    exit()


# ============================================================
# PART 4 - START SELENIUM
# ============================================================

print("\nStarting Google Chrome...")

# Chrome options.
chrome_options = webdriver.ChromeOptions()

# Keep Chrome open after the program finishes.
# This is useful for debugging.
chrome_options.add_experimental_option(
    "detach",
    True
)


# Start Chrome.
driver = webdriver.Chrome(
    options=chrome_options
)


# Create a WebDriverWait object.
# Selenium will wait up to 15 seconds for elements.
wait = WebDriverWait(driver, 15)


# ============================================================
# PART 5 - FILL THE GOOGLE FORM
# ============================================================

for n in range(len(all_links)):

    print("\n" + "=" * 60)
    print(
        f"Submitting property {n + 1} of {len(all_links)}"
    )
    print("=" * 60)

    # --------------------------------------------------------
    # Open Google Form
    # --------------------------------------------------------

    driver.get(GOOGLE_FORM_URL)

    # Wait for the page to load.
    time.sleep(2)


    # --------------------------------------------------------
    # Find the Address field
    # --------------------------------------------------------

    address = wait.until(
        EC.presence_of_element_located(
            (
                By.XPATH,
                '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input'
            )
        )
    )


    # --------------------------------------------------------
    # Find the Price field
    # --------------------------------------------------------

    price = wait.until(
        EC.presence_of_element_located(
            (
                By.XPATH,
                '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input'
            )
        )
    )


    # --------------------------------------------------------
    # Find the Link field
    # --------------------------------------------------------

    link = wait.until(
        EC.presence_of_element_located(
            (
                By.XPATH,
                '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input'
            )
        )
    )


    # --------------------------------------------------------
    # Find the Submit button
    # --------------------------------------------------------

    submit_button = wait.until(
        EC.element_to_be_clickable(
            (
                By.XPATH,
                '//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div'
            )
        )
    )


    # --------------------------------------------------------
    # Enter the property information
    # --------------------------------------------------------

    address.send_keys(all_addresses[n])

    price.send_keys(all_prices[n])

    link.send_keys(all_links[n])


    # --------------------------------------------------------
    # Submit the form
    # --------------------------------------------------------

    submit_button.click()


    print("\nProperty submitted successfully!")

    print(f"Address: {all_addresses[n]}")
    print(f"Price:   {all_prices[n]}")
    print(f"Link:    {all_links[n]}")


    # Give Google Forms a moment to process the submission.
    time.sleep(2)


# ============================================================
# FINISHED
# ============================================================

print("\n" + "=" * 60)
print("ALL PROPERTIES HAVE BEEN SUBMITTED!")
print("=" * 60)

print(
    f"\nTotal properties submitted: {len(all_links)}"
)

print("\nThe Chrome browser will remain open.")

