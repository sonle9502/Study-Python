import undetected_chromedriver as uc
from bs4 import BeautifulSoup
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import time
import os
from utils import dataPath

def get_url(position, location):
    template = 'https://jp.indeed.com/jobs?q={}&l={}'
    url = template.format(position, location)
    return url

def save_html(soup,position, page_number):
    file_path = dataPath.create_filepath(position, page_number)

    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(soup.prettify())

def click_element(driver, element):
    try:
        driver.execute_script("arguments[0].click();", element)
    except Exception as e:
        print(f"クリックに失敗しました: {e}")

def get_htmlFileFromWeb(position, location):
    # ユーザーエージェントを設定
    options = uc.ChromeOptions()
    options.add_argument("--user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36")
    # ブラウザを起動
    driver = uc.Chrome(options=options)
    try:
        # URLにアクセス
        url = get_url(position, location)
        driver.get(url)
        page_number = 1
        size = dataPath.count_files_in_folder(position)

        while page_number <= 100:
            print(f"{page_number}ページ目を処理しています")

            # Cloudflareのチェックを待つ
            WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.TAG_NAME, "body")))
            
            # ページのHTMLを取得
            html = driver.page_source

            # BeautifulSoupでHTMLをパース
            soup = BeautifulSoup(html, 'html.parser')
            save_html(soup, position, page_number)
            
            if page_number >= 1:
                get_next_page(driver)

            page_number += 1
    except Exception as e:
        print(f"スクレイピング中にエラーが発生しました: {e}")
    finally:
        # 全てのページがスクレイピングされた後にブラウザを閉じる
        print("ブラウザを閉じます")
        driver.quit()

def get_next_page(driver):
    print("次のページへのリンクを探します")
    try:
        # # 1. Cookieバナーを閉じる
        # try:
        #     cookie_banner = WebDriverWait(driver, 10).until(
        #         EC.element_to_be_clickable((By.CLASS_NAME, "gnav-CookiePrivacyNoticeBanner"))
        #     )
        #     driver.execute_script("arguments[0].click();", cookie_banner)
        #     print("Cookieバナーを閉じました")
        # except Exception as e:
        #     print(f"Cookieバナーが見つかりませんでした: {e}")

        # # 2. ブラウザのポップアップが表示されたらポップアップを閉じる
        # try:
        #     popup = WebDriverWait(driver, 20).until(
        #         EC.element_to_be_clickable((By.CSS_SELECTOR, "button[class='css-yi9ndv e8ju0x51']"))
        #     )
        #     if popup:
        #         driver.execute_script("arguments[0].click();", popup)
        #         print("ポップアップを閉じました")
        # except Exception as e:
        #     print(f"ポップアップが見つかりませんでした: {e}")

        # 3. 次のページボタンまでスクロールしてから次のページに移動
        next_button = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "a[data-testid='pagination-page-next']"))
        )

        if next_button:
            print("次のページボタンまでスクロールします")
            driver.execute_script("arguments[0].scrollIntoView(true);", next_button)
            time.sleep(1)  # スクロール後に少し待機

            print("次のページボタンをクリックします")
            driver.execute_script("arguments[0].click();", next_button)
            # ページがロードされるのを待機
            WebDriverWait(driver, 30).until(
                EC.presence_of_element_located((By.TAG_NAME, "body"))
            )
            time.sleep(2)  # 少し待機してページが完全にロードされるのを待つ
        else:
            print("次のページボタンが見つかりませんでした")
    except Exception as e:
        print(f"次のページへの移動中にエラーが発生しました: {e}")

