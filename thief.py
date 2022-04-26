"""
Грязный вор, ворует комменты в стримах инсты
"""

import pyautogui
import pytesseract
from pytesseract import image_to_string
from PIL import Image
import time

pytesseract.pytesseract.tesseract_cmd = 'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'
# pytesseract.pytesseract.tesseract_cmd = r'C:\Users\USER\AppData\Local\Tesseract-OCR\tesseract.exe'

chat_screenshot = pyautogui.screenshot(region=(170, 870, 620, 240))
chat_screenshot.save(r'file name.png')
image = Image.open('file name.png')
print(image_to_string(image, lang="rus"))

def event_loop():
    while True:
        start_time = time.time()
        chat_screenshot = pyautogui.screenshot(region=(170, 870, 620, 240))
        chat_screenshot.save(r'file name.png')
        image = Image.open('file name.png')
        recognited_text = image_to_string(image, lang="rus")
        print(recognited_text)
        print(f"Время выполнения: {time.time() - start_time}")


def main():
    event_loop()


if __name__ == '__main__':
    main()
    # TODO: Неудачная попытка парсить с помощью распознавания текста тессерактом