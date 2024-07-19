import undetected_chromedriver as uc
from bs4 import BeautifulSoup
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


# ユーザーエージェントを設定
options = uc.ChromeOptions()
options.add_argument("--user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36")

def get_url(position,localtion):
    template = 'https://jp.indeed.com/jobs?q={}&l={}'
    url = template.format(position,localtion)
    return url

# ブラウザを起動
driver = uc.Chrome(options=options)

try:
    # URLにアクセス
    url = get_url("データアナリスト", "東京都")
    driver.get(url)

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
            next_button = driver.find_element(By.LINK_TEXT, '次へ')  # 次のページへのリンクテキストを指定
            next_button.click()
            page_number += 1
            time.sleep(2)  # 次のページが読み込まれるのを待つ
        except:
            print("すべてのページを取得しました。")
            break

finally:
    # ブラウザを閉じる
    driver.quit()