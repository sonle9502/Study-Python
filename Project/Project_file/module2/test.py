import undetected_chromedriver as uc

# 最新のChromeDriverをダウンロードして使用するオプション
options = uc.ChromeOptions()
options.add_argument("--headless")  # ヘッドレスモードで実行（必要に応じて）

driver = uc.Chrome(options=options)
driver.get('http://example.com')

# 他のコード...
driver.quit()
