from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import time

# Импортирование csv
import csv

# Инициализация веб-драйвера (здесь используется ChromeDriver)
driver = webdriver.Chrome()

# Открытие сайта
url = 'https://www.cian.ru/snyat-kvartiru-1-komn-ili-2-komn/'
driver.get(url)

# Ожидание загрузки элементов
time.sleep(5)

# Сбор данных о ценах
prices = driver.find_elements(By.XPATH, "//span[@data-mark='MainPrice']/span")

# Создание и открытие CSV-файла для записи
with open("prices.csv", mode="w", encoding="utf-8", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["Цена"])  # Указываем заголовок столбца

    # Запись данных в файл
    for price in prices:
        writer.writerow([price.text])

print("Данные успешно сохранены в файл prices.csv")

# Закрытие браузера
driver.quit()
