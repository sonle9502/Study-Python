from selenium import webdriver
import undetected_chromedriver as uc

try:
    driver = uc.Chrome()
    driver.get("https://example.com")
    # Web 操作を行う
finally:
    # ドライバを確実にシャットダウン
    if driver:
        driver.quit()
