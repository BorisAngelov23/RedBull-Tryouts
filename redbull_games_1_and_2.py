# INSTRUCTIONS:
# 1. Run the script
# 2. Wait for the first game to start
# 3. Click the red points on the track once as they appear
# 4. When the first game ends, press 'g' on your keyboard
# 5. Wait for the second game to start and end
# 6. Do the third game manually
# 7. Vamooo, you got yourself a sweatshirt!

from time import sleep

import keyboard
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pyautogui
from pynput import mouse

chrome_options = webdriver.ChromeOptions()
chrome_options.binary_location = 'C:/WINDOWS/system32/chromedriver/win64-121.0.6146.0/chromedriver-win64/chromedriver.exe'

driver = webdriver.Chrome(options=chrome_options)

driver.get('https://www.redbull.com/bg-bg/projects/tryoutsbg/game')

# memory
points_dict = {}

sleep(5)

prev_element_text = '...'


def on_click(x, y, button, pressed, pet=prev_element_text):
    element_text = driver.find_element(By.CLASS_NAME, 'subheader__title').get_attribute('innerText')
    if pressed and element_text != pet:
        points_dict[element_text] = (x, y)
        print(points_dict[element_text])
        pet = element_text
        sleep(0.69)


listener_thread = mouse.Listener(on_click=on_click)
listener_thread.start()
second_part_started = False

try:
    print("started")
    while True:
        if driver.find_element(By.CLASS_NAME, 'subheader__title').get_attribute('innerText') == 'ИГРАТА ЗАПОЧВА СЕГА!':
            second_part_started = True
            listener_thread.stop()
        elif second_part_started:
            element_txt = driver.find_element(By.CLASS_NAME, 'subheader__title').get_attribute('innerText')
            if element_txt in points_dict.keys():
                pyautogui.click(x=points_dict[element_txt][0], y=points_dict[element_txt][1])
            if keyboard.is_pressed('g'):
                print("memory game ends here")
                break
    pass
except KeyboardInterrupt:
    print("Script interrupted by user.")

# reflex
try:
    while True:
        yellow_element = WebDriverWait(driver, 60, 0.0001).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, '.progress-bar--yellow'))
        )
        pyautogui.click()
except KeyboardInterrupt:
    print("Script interrupted by user.")
finally:
    pass
