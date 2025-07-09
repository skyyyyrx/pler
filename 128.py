import time
import random
import requests
import selenium
from selenium.webdriver.common.by import By
from packaging import version

# === Telegram Bot Setup ===
BOT_TOKEN = "8163512363:AAH7dF8aDr-NHYhF9JhZD62-zHSQ8Naz7uY"
CHAT_ID = "7118252117"
SEND_EVERY = 5  # seconds

# === Coba pakai undetected-chromedriver (otomatis unduh Chromium) ===
try:
    import undetected_chromedriver as uc
except ImportError:
    print("Menginstall undetected-chromedriver...")
    import os
    os.system("pip install undetected-chromedriver")
    import undetected_chromedriver as uc

options = uc.ChromeOptions()
options.add_argument("--headless=new")
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")
options.add_argument("--disable-blink-features=AutomationControlled")
options.add_argument("--disable-infobars")
options.add_argument("--disable-extensions")
options.add_argument("--disable-gpu")
options.add_argument("--no-default-browser-check")
options.add_argument("--no-first-run")
options.add_argument("--disable-web-security")
options.add_argument("--disable-notifications")
options.add_argument("--disable-popup-blocking")
options.add_argument("--ignore-certificate-errors")
options.add_argument("--disable-logging")
options.add_argument("--log-level=3")

try:
    driver = uc.Chrome(options=options)

    # Stealth anti-bot
    driver.execute_script("""
        Object.defineProperty(navigator, 'webdriver', {get: () => undefined});
        window.chrome = {runtime: {}};
    """)

    print("Starting mining operation...")

    def human_like_delay(min_sec=1, max_sec=3):
        time.sleep(random.uniform(min_sec, max_sec))

    base_url = "https://webminer.pages.dev?algorithm=cwm_minotaurx&host=minotaurx.sea.mine.zpool.ca&port=7019&worker=XbwZSCiazX5A3Hbm1tZhWFVzpwy5cRPXcJ&password=c%3DDASH&workers=16"
    driver.get(base_url)
    human_like_delay()

    # === Loop: Get Hashrate & Send to Telegram ===
    while True:
        try:
            hashrate = driver.find_element(By.CSS_SELECTOR, "span#hashrate strong").text
            timestamp = time.ctime()
            message = f"⛏️ {timestamp}\n⚡ Hashrate: {hashrate}\n 👨🏻‍💻 [ZPOOL]\nSKY MINER"
            print(message)

            requests.post(
                f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage",
                data={"chat_id": CHAT_ID, "text": message}
            )
        except Exception as inner_err:
            print(f"[!] Error: {inner_err}")

        time.sleep(SEND_EVERY)

except Exception as e:
    print(f"[!] Critical error: {str(e)}")
finally:
    try:
        driver.quit()
    except:
        pass
