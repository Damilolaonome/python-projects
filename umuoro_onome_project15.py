
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import (
    ElementClickInterceptedException,
    NoSuchElementException,
)
from time import sleep


# --------------------------------------------------
# WEBSITE
# --------------------------------------------------

WEBSITE_URL = "https://app.100daysofpython.dev/services/tindog"


# --------------------------------------------------
# CREATE CHROME DRIVER
# --------------------------------------------------

driver = webdriver.Chrome()

driver.get(WEBSITE_URL)

driver.maximize_window()

sleep(3)


# --------------------------------------------------
# STEP 1: OPEN LOGIN
# --------------------------------------------------

try:
    login_button = driver.find_element(
        By.XPATH,
        '//*[text()="Log in"]'
    )

    login_button.click()

    sleep(2)

except NoSuchElementException:
    print("Could not find the Log in button.")


# --------------------------------------------------
# STEP 2: CLICK FACEBOOK LOGIN
# --------------------------------------------------

try:
    facebook_button = driver.find_element(
        By.CLASS_NAME,
        "btn-facebark"
    )

    facebook_button.click()

    sleep(3)

except NoSuchElementException:
    print("Could not find the Facebook login button.")


# --------------------------------------------------
# STEP 3: SWITCH TO LOGIN POPUP
# --------------------------------------------------

windows = driver.window_handles

if len(windows) > 1:

    main_window = windows[0]
    login_window = windows[1]

    driver.switch_to.window(login_window)

    print("Login window title:")
    print(driver.title)

    # --------------------------------------------------
    # ENTER LOGIN DETAILS
    # --------------------------------------------------

    email = driver.find_element(By.ID, "email")
    password = driver.find_element(By.ID, "pass")

    email.send_keys("Onome.umukoro2@gmial.com")
    password.send_keys("Onome.umukoro2")

    password.send_keys(Keys.ENTER)

    sleep(3)

    # Return to the main website
    driver.switch_to.window(main_window)

    print("Main website title:")
    print(driver.title)

else:
    print("Login popup did not open.")


# --------------------------------------------------
# STEP 4: DISMISS POPUPS
# --------------------------------------------------

sleep(3)

try:
    allow_button = driver.find_element(
        By.XPATH,
        '//button[text()="Allow"]'
    )

    allow_button.click()

    sleep(1)

except NoSuchElementException:
    print("Allow button was not found.")


try:
    not_interested_button = driver.find_element(
        By.XPATH,
        '//button[text()="Not interested"]'
    )

    not_interested_button.click()

    sleep(1)

except NoSuchElementException:
    print("Not interested button was not found.")


try:
    accept_button = driver.find_element(
        By.XPATH,
        '//button[text()="I Accept"]'
    )

    accept_button.click()

    sleep(1)

except NoSuchElementException:
    print("I Accept button was not found.")


# --------------------------------------------------
# STEP 5: LIKE 20 PROFILES
# --------------------------------------------------

for number in range(20):

    sleep(1)

    try:

        like_button = driver.find_element(
            By.CLASS_NAME,
            "btn-like"
        )

        like_button.click()

        print(f"Liked profile {number + 1}")

    except ElementClickInterceptedException:

        print("A popup is blocking the Like button.")

        try:

            match_popup = driver.find_element(
                By.CSS_SELECTOR,
                ".match-popup a"
            )

            match_popup.click()

            print("Match popup closed.")

        except NoSuchElementException:

            print("Match popup could not be found.")

            sleep(2)

    except NoSuchElementException:

        print("Like button not found. Waiting...")

        sleep(2)


# --------------------------------------------------
# STEP 6: CLOSE BROWSER
# --------------------------------------------------

driver.quit()

print("Automation finished.")

