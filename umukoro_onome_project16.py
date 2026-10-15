print("Speedtest Twitter Bot")
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


PROMISED_DOWN = 150
PROMISED_UP = 10

TWITTER_EMAIL = "Onome.umukoro2@gmail.com"
TWITTER_PASSWORD = "Onome.umukoro2"


class InternetSpeedTwitterBot:

    def __init__(self):
        self.driver = webdriver.Chrome()
        self.up = 0
        self.down = 0

    def get_internet_speed(self):

        self.driver.get("https://www.speedtest.net/")

        print("Opening Speedtest...")

        wait = WebDriverWait(self.driver, 20)

        # Accept cookies if the button appears
        try:
            accept_button = wait.until(
                EC.element_to_be_clickable(
                    (By.ID, "onetrust-accept-btn-handler")
                )
            )
            accept_button.click()
            print("Cookies accepted.")

        except Exception:
            print("No cookie popup found.")

        # Find the Speedtest GO button
        try:
            go_button = wait.until(
                EC.element_to_be_clickable(
                    (
                        By.CSS_SELECTOR,
                        "a.js-start-test"
                    )
                )
            )

            go_button.click()

            print("Speed test started...")

        except Exception as error:
            print("Could not find the Speedtest GO button.")
            print("Error:", error)
            return

        # Give Speedtest enough time to complete
        print("Waiting for the speed test to finish...")

        time.sleep(60)

        # Get download speed
        try:
            self.down = self.driver.find_element(
                By.CSS_SELECTOR,
                ".download-speed"
            ).text

            self.up = self.driver.find_element(
                By.CSS_SELECTOR,
                ".upload-speed"
            ).text

            print(f"Download speed: {self.down} Mbps")
            print(f"Upload speed: {self.up} Mbps")

        except Exception as error:
            print("Could not retrieve the speed results.")
            print("Error:", error)

    def tweet_at_provider(self):
        pass


bot = InternetSpeedTwitterBot()

bot.get_internet_speed()

bot.tweet_at_provider()

print("Speedtest Twitter Bot")
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


PROMISED_DOWN = 150
PROMISED_UP = 10

TWITTER_EMAIL = "Onome.umukoro2@gmail.com"
TWITTER_PASSWORD = "Onome.umukoro2"


class InternetSpeedTwitterBot:

    def __init__(self):
        self.driver = webdriver.Chrome()
        self.up = 0
        self.down = 0

    def get_internet_speed(self):

        self.driver.get("https://www.speedtest.net/")

        print("Opening Speedtest...")

        wait = WebDriverWait(self.driver, 20)

        # Accept cookies if the button appears
        try:
            accept_button = wait.until(
                EC.element_to_be_clickable(
                    (By.ID, "onetrust-accept-btn-handler")
                )
            )
            accept_button.click()
            print("Cookies accepted.")

        except Exception:
            print("No cookie popup found.")

        # Find the Speedtest GO button
        try:
            go_button = wait.until(
                EC.element_to_be_clickable(
                    (
                        By.CSS_SELECTOR,
                        "a.js-start-test"
                    )
                )
            )

            go_button.click()

            print("Speed test started...")

        except Exception as error:
            print("Could not find the Speedtest GO button.")
            print("Error:", error)
            return

        # Give Speedtest enough time to complete
        print("Waiting for the speed test to finish...")

        time.sleep(60)

        # Get download speed
        try:
            self.down = self.driver.find_element(
                By.CSS_SELECTOR,
                ".download-speed"
            ).text

            self.up = self.driver.find_element(
                By.CSS_SELECTOR,
                ".upload-speed"
            ).text

            print(f"Download speed: {self.down} Mbps")
            print(f"Upload speed: {self.up} Mbps")

        except Exception as error:
            print("Could not retrieve the speed results.")
            print("Error:", error)

    def tweet_at_provider(self):
        pass


bot = InternetSpeedTwitterBot()

bot.get_internet_speed()

bot.tweet_at_provider()

