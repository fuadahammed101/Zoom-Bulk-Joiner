# Simple Zoom Bulk Joiner Script

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from time import sleep
import os

# Function to read names from names.txt file
def load_names():
    with open("names.txt", "r") as file:
        names = file.read().splitlines()
    return names

# Function to setup Chrome driver with basic options
def setup_driver():
    options = Options()
    options.add_experimental_option("detach", True)  # Keep browser open after script finishes
    options.add_argument("--use-fake-ui-for-media-stream")  # Allow mic/cam without prompt
    # Disable images to save bandwidth
    prefs = {"profile.managed_default_content_settings.images": 2}
    options.add_experimental_option("prefs", prefs)
    driver = webdriver.Chrome(options=options)
    return driver

# Function to join Zoom meeting using meeting ID and password
def join_by_id_password(meeting_id, meeting_password, names):
    for name in names:
        driver = setup_driver()
        url = f"https://zoom.us/wc/{meeting_id}/join"
        driver.get(url)
        sleep(1)

        # Switch to iframe where password and name inputs are
        iframe = driver.find_element(By.TAG_NAME, "iframe")
        driver.switch_to.frame(iframe)

        # Enter password
        password_input = driver.find_element(By.ID, "input-for-pwd")
        password_input.clear()
        password_input.send_keys(meeting_password)

        # Enter display name
        name_input = driver.find_element(By.ID, "input-for-name")
        name_input.clear()
        name_input.send_keys(name)

        # Mute audio by clicking audio button twice
        audio_button = driver.find_element(By.ID, "preview-audio-control-button")
        audio_button.click()
        sleep(0.1)
        audio_button.click()

        # Press Enter to join
        name_input.send_keys(Keys.RETURN)

        print(f"Joined meeting as: {name}")
        sleep(2)  # Wait a bit before next join

# Function to join Zoom meeting using meeting link
def join_by_link(meeting_link, names):
    for name in names:
        driver = setup_driver()
        driver.get(meeting_link)
        sleep(5)  # Wait for page to load

        # Try to dismiss any popups by clicking cancel buttons if present
        try:
            cancel_button = driver.find_element(By.CLASS_NAME, "mbTuDeF1")
            cancel_button.click()
        except:
            pass

        # Try to click "Join from Your Browser" link if present
        try:
            join_browser_link = driver.find_element(By.LINK_TEXT, "Join from Your Browser")
            join_browser_link.click()
        except:
            pass

        sleep(5)  # Wait for iframe to load

        # Switch to iframe for entering name
        iframe = driver.find_element(By.TAG_NAME, "iframe")
        driver.switch_to.frame(iframe)

        # Wait for name input to be present
        name_input = driver.find_element(By.CLASS_NAME, "preview-meeting-info-field-input")
        name_input.clear()
        name_input.send_keys(name)

        # Mute audio by clicking audio button twice
        audio_button = driver.find_element(By.ID, "preview-audio-control-button")
        audio_button.click()
        sleep(0.1)
        audio_button.click()

        # Press Enter to join
        name_input.send_keys(Keys.RETURN)

        print(f"Joined meeting as: {name}")
        sleep(2)  # Wait a bit before next join

# Clear screen function for Windows and Unix
def clear_screen():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")

# Main program
def main():
    clear_screen()
    print("Welcome to the Zoom Bulk Joiner!")
    names = load_names()
    print(f"Loaded {len(names)} names from names.txt")

    print("Choose how to join the meeting:")
    print("1. By Meeting ID and Password")
    print("2. By Meeting Link")
    choice = input("Enter 1 or 2: ").strip()

    if choice == "1":
        meeting_id = input("Enter Zoom Meeting ID: ").strip()
        meeting_password = input("Enter Zoom Meeting Password: ").strip()
        join_by_id_password(meeting_id, meeting_password, names)
    elif choice == "2":
        meeting_link = input("Enter Zoom Meeting Link: ").strip()
        join_by_link(meeting_link, names)
    else:
        print("Invalid choice. Exiting.")

if __name__ == "__main__":
    main()
