from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

# Google Chromeを起動
driver = webdriver.Chrome()

# Googleフォームにアクセス
driver.get("https://forms.gle/sUJeEXTkXcsLk2zf7")

# 1番目のチェックボックスの1番目の項目を選択
checkbox = driver.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div[2]/div[1]/label/div[1]/div[1]/div[3]/span')
checkbox.click()

# 100回投票を行う
for i in range(100):
    # 送信ボタンをクリック
    submit_button = driver.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div/div/span/span')
    submit_button.click()
    
    # 5秒待機して、フォームを再読み込み
    time.sleep(5)
    driver.get("https://forms.gle/sUJeEXTkXcsLk2zf7")

# ブラウザを終了する
driver.quit()
