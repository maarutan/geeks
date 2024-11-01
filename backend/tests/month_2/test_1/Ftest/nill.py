import os
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from fake_useragent import UserAgent
from faker import Faker

fake = Faker()


# Функция для генерации уникального мнения
def generate_unique_opinion(prompt):
    return fake.text()


# Функция для генерации уникального User-Agent
def generate_user_agent():
    ua = UserAgent()
    return ua.random


# Функция для сохранения результатов в файл
def save_results(wallet, unique_code):
    with open('results/results.txt', 'a') as file:
        file.write(f'{wallet}:{unique_code}\n')


# Функция для сохранения скриншота
def save_screenshot(driver, wallet):
    screenshots_dir = 'screenshots'
    if not os.path.exists(screenshots_dir):
        os.makedirs(screenshots_dir)
    screenshot_path = os.path.join(screenshots_dir, f'{wallet}.png')
    driver.save_screenshot(screenshot_path)
    print(f"Saved screenshot for wallet: {wallet}")


# Функция для обработки вопросов на странице
def handle_questions(driver, wait, questions):
    for question in questions:
        if question["type"] == "click":
            wait.until(EC.element_to_be_clickable((By.XPATH, question["xpath"]))).click()
        elif question["type"] == "text":
            opinion = generate_unique_opinion(question["prompt"])
            wait.until(EC.presence_of_element_located((By.XPATH, question["xpath"]))).send_keys(opinion)
        elif question["type"] == "submit":
            wait.until(EC.element_to_be_clickable((By.XPATH, question["xpath"]))).click()


# Основная функция
def main():
    # Проход по файлам в папке wallets
    wallets_dir = 'wallets'
    processed_wallets_file = os.path.join('results', 'processed_wallets.txt')
    processed_wallets = set()

    if os.path.exists(processed_wallets_file):
        with open(processed_wallets_file, 'r') as f:
            processed_wallets = set(line.strip() for line in f.readlines())

    for wallet_file in os.listdir(wallets_dir):
        wallet = os.path.splitext(wallet_file)[0]

        if wallet in processed_wallets:
            print(f"Wallet {wallet} has already been processed, skipping...")
            continue

        # Генерация уникального User-Agent
        user_agent = generate_user_agent()
        print(f"Generated User Agent: {user_agent}")

        # Проверка наличия папок для результатов и скриншотов
        results_dir = 'results'
        screenshots_dir = 'screenshots'
        if not os.path.exists(results_dir):
            os.makedirs(results_dir)
        if not os.path.exists(screenshots_dir):
            os.makedirs(screenshots_dir)

            print(f"Processing wallet: {wallet}")

        try:
            chrome_options = Options()
            chrome_options.add_argument(f'--user-agent={user_agent}')

            service = Service('C:\soft\chromedriver2\chromedriver-win64\chromedriver.exe')
            driver = webdriver.Chrome(service=service, options=chrome_options)
            driver.maximize_window()
            wait = WebDriverWait(driver, 10)

            driver.get("https://nillpill.nillion.com/")
            time.sleep(5)
            take_the_pill_button = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="button-jiVb6SBRvG_btn"]')))
            take_the_pill_button.click()

            wallet_input = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="6II1eGtsydas7JbxZOuF"]')))
            time.sleep(1)
            wallet_input.click()  # Очистка поля перед вводом
            time.sleep(1)
            wallet_input.send_keys(wallet)

            wait.until(
                EC.element_to_be_clickable((By.XPATH, '//*[@id="_builder-form"]/div/div[2]/div/div/div/button'))).click()
            time.sleep(2)

            # Первая страница вопросов
            driver.get("https://nillpill.nillion.com/109978")
            questions_page_1 = [
                {"type": "click", "xpath": '//*[@id="q1"]/div[2]'},
                {"type": "text", "xpath": '//*[@id="freeFormAnswer"]',
                 "prompt": "In your own words, what sets “level 3 data” apart from levels 1 and 2?"},
                {"type": "click", "xpath": '//*[@id="q3"]/div[3]'},
                {"type": "click", "xpath": '//*[@id="q4"]/div[1]'},
                {"type": "submit", "xpath": '//*[@id="custom-code-C_t70I_iFj"]/div/button'}
            ]
            handle_questions(driver, wait, questions_page_1)
            time.sleep(2)

            # Вторая страница вопросов
            driver.get("https://nillpill.nillion.com/25337")
            questions_page_2 = [
                {"type": "click", "xpath": '//*[@id="q1"]/div[2]'},
                {"type": "text", "xpath": '//*[@id="freeFormAnswer"]',
                 "prompt": "Current widely used methods of encryption have a big flaw. Describe that flaw in your own words."},
                {"type": "click", "xpath": '//*[@id="q3"]/div[2]'},
                {"type": "click", "xpath": '//*[@id="q4"]/div[3]'},
                {"type": "submit", "xpath": '//*[@id="custom-code-djBm4eDWUe"]/div/button'}
            ]
            handle_questions(driver, wait, questions_page_2)
            time.sleep(2)

            # Третья страница вопросов
            driver.get("https://nillpill.nillion.com/31550")
            questions_page_3 = [
                {"type": "click", "xpath": '//*[@id="q1"]/div[3]'},
                {"type": "click", "xpath": '//*[@id="q2"]/div[3]'},
                {"type": "text", "xpath": '//*[@id="freeFormAnswer"]',
                 "prompt": "Innovation in the world of PETs is currently stuck in “silos” - how does the orchestration layer solve this and leverage every breakthrough in the PET world?"},
                {"type": "click", "xpath": '//*[@id="q4"]/div[2]'},
                {"type": "submit", "xpath": '//*[@id="custom-code-Rv8hY5HGXq"]/div/button'}
            ]
            handle_questions(driver, wait, questions_page_3)
            time.sleep(2)

            # Финальная страница
            final_prompt = "We seek the most passionate minds to help Nillion win the Data War. Why do you think this mission is right for you, and what will you personally do to help fight?"
            final_opinion = generate_unique_opinion(final_prompt)
            wait.until(EC.presence_of_element_located(
                (By.XPATH, '//*[@id="_builder-form"]/div/div[1]/div/div/textarea'))).send_keys(final_opinion)
            time.sleep(2)

            # Отметка согласия
            element_to_click = driver.find_element(By.XPATH,
                                                   '/html/body/div[1]/div/div[2]/div[2]/div[2]/div/div/div/div[3]/div/div/div/div[2]/div/div/section/div/div/div/div[4]/div/div/label')
            element_to_click.click()

            time.sleep(20)  # Даем время для загрузки страницы с уникальным кодом

            wait.until(EC.element_to_be_clickable(
                (By.XPATH, '//*[@id="_builder-form"]/div/div[5]/div/div/div/button'))).click()

            time.sleep(6)

            wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="copy"]')))
            unique_code_url = driver.current_url
            unique_code = unique_code_url.split('=')[1]

            time.sleep(5)

            # Сохранение результата в файл
            save_results(wallet, unique_code)

            # Сохранение скриншота страницы с уникальным кодом
            save_screenshot(driver, wallet)

            time.sleep(5)

        except Exception as e:
            print(f"Error processing wallet {wallet}: {e}")

        finally:
            # Сохраняем информацию о кошельке в файл processed_wallets.txt
            with open(processed_wallets_file, 'a') as f:
                f.write(f"{wallet}\n")

            # Закрытие браузера и освобождение ресурсов
            if 'driver' in locals():
                driver.quit()
                print(f"Closed browser for wallet: {wallet}")

            # Пауза перед следующим запуском
            time.sleep(5)

    # Подготовка к завершению работы
    print("All wallets processed. Program finished successfully.")


if __name__ == "__main__":
    main()
