import undetected_chromedriver as uc
from bs4 import BeautifulSoup
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import time

# ユーザーエージェントを設定
options = uc.ChromeOptions()
options.add_argument("--user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36")

def get_url(position, location):
    template = 'https://jp.indeed.com/jobs?q={}&l={}'
    url = template.format(position, location)
    return url

# ブラウザを起動
driver = uc.Chrome(options=options)

def save_html(soup, page_number):
    with open(f'C:\\Users\\s-le\\Desktop\\study-private\\Python\\Study-Python\\Project\\Project_file\\datatest\\output_page_{page_number}.html', 'w', encoding='utf-8') as file:
        file.write(soup.prettify())

def click_element(driver, element):
    try:
        driver.execute_script("arguments[0].click();", element)
    except Exception as e:
        print(f"クリックに失敗しました: {e}")

try:
    # URLにアクセス
    url = get_url("データアナリスト", "東京都")
    driver.get(url)
    page_number = 1

    while page_number <= 100:  # 50ページまでの制限を追加
        # Cloudflareのチェックを待つ
        WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.TAG_NAME, "body")))
        
        # ページのHTMLを取得
        html = driver.page_source

        # BeautifulSoupでHTMLをパース
        soup = BeautifulSoup(html, 'html.parser')

        # HTMLをファイルに保存
        save_html(soup, page_number)

        # 次のページへのリンクを探す
        try:
            # Cookieバナーを閉じる
            try:
                cookie_banner = WebDriverWait(driver, 10).until(
                    EC.element_to_be_clickable((By.CLASS_NAME, "gnav-CookiePrivacyNoticeBanner"))
                )
                click_element(driver, cookie_banner)
            except Exception as e:
                print(f"Cookieバナーが見つかりませんでした: {e}")

            # close_button = WebDriverWait(driver, 20).until(
            close_button = WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, "button[class='css-yi9ndv e8ju0x51']"))
            )
            if close_button:
                click_element(driver,close_button)

            # 次のページボタンがクリック可能になるまで待機
            next_button = WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, "a[data-testid='pagination-page-next']"))
            )
            
            # スクロールしてから次のページボタンをクリック
            actions = ActionChains(driver)
            actions.move_to_element(next_button).perform()
            click_element(driver, next_button)

            page_number += 1

            # ページがロードされるのを待機
            WebDriverWait(driver, 30).until(
                EC.presence_of_element_located((By.TAG_NAME, "body"))
            )
            time.sleep(2)  # 少し待機してページが完全にロードされるのを待つ

        except Exception as e:
            print(f"次のページへの移動中にエラーが発生しました: {e}")
            break

finally:
    # ブラウザを閉じる
    driver.quit()
