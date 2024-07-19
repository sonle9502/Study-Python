from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
from selenium.common.exceptions import TimeoutException
import time

def get_url(position,localtion):
    template = 'https://jp.indeed.com/jobs?q={}&l={}'
    url = template.format(position,localtion)
    return url

driver = webdriver.Chrome()

try:
    # URLにアクセス
    url = get_url("データアナリスト", "東京都")
    driver.get(url)

    # クッキーバナーを閉じる（CSSセレクタは実際のものに合わせて調整）
    try:
        cookie_banner_close_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, 'div.gnav-CookiePrivacyNoticeBanner button'))
        )
        cookie_banner_close_button.click()
    except Exception as e:
        print(f"クッキーバナーを閉じることができませんでした: {e}")

    page_number = 1
    while True:
        # Cloudflareのチェックを待つ
        WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.TAG_NAME, "body")))

        # ページのHTMLを取得
        html = driver.page_source

        # BeautifulSoupでHTMLをパース
        soup = BeautifulSoup(html, 'html.parser')

        # HTMLをファイルに保存
        with open(f'C:\\Users\\s-le\\Desktop\\study-private\\Python\\Study-Python\\Project\\Project_file\\data\\output_page_{page_number}.html', 'w', encoding='utf-8') as file:
            file.write(soup.prettify())

        # 次のページへのリンクを探す
        try:
            next_button = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, 'a[data-testid="pagination-page-next"]'))
            )
            driver.execute_script("arguments[0].scrollIntoView(true);", next_button)
            driver.execute_script("arguments[0].click();", next_button)

            # ポップアップが表示された場合の処理
            try:
                WebDriverWait(driver, 5).until(EC.alert_is_present())
                alert = driver.switch_to.alert
                alert.accept()  # OKボタンをクリック
                print("ポップアップを処理しました")
            except Exception:
                pass  # ポップアップが表示されなかった場合は何もしない

            # ポップアップを閉じる
            try:
                popup_close_button = WebDriverWait(driver, 10).until(
                    EC.element_to_be_clickable((By.CSS_SELECTOR, 'button[aria-label="閉じる"]'))
                )
                popup_close_button.click()
                print("ポップアップを閉じました")
            except TimeoutException:
                pass

            page_number += 1
            print(f"Navigating to page {page_number}")
            time.sleep(2)  # 次のページが読み込まれるのを待つ

        except Exception as e:
            print(f"すべてのページを取得しました: {e}")
            break
finally:
    # ブラウザを閉じる
    driver.quit()