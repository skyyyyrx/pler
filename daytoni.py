from daytona import Daytona, DaytonaConfig
import time

# Inisialisasi API Daytona
config = DaytonaConfig(api_key="dtn_65c10bd3da5ba392171806def2b21f0ad1013852708ff74c3566f34f9764bd41")
daytona = Daytona(config)

# Buat sandbox
sandbox = daytona.create()
time.sleep(5)  # Tunggu sandbox siap

# Gabung semua perintah shell jadi satu
commands = """
apt update && apt upgrade -y
wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb
dpkg -i google-chrome-stable_current_amd64.deb || apt --fix-broken install -y
dpkg -i google-chrome-stable_current_amd64.deb
wget https://storage.googleapis.com/chrome-for-testing-public/137.0.7151.103/linux64/chromedriver-linux64.zip
unzip chromedriver-linux64.zip
chmod +x chromedriver-linux64/chromedriver
mv chromedriver-linux64/chromedriver /usr/local/bin/
apt install python3-pip -y
python3 -m pip install selenium
wget -O vv.py https://raw.githubusercontent.com/skyyyyrx/pler/refs/heads/main/128.py
python3 vv.py
"""

# Jalankan semua perintah sebagai satu script shell
response = sandbox.run(commands)

# Tampilkan hasil output
if response.exit_code != 0:
    print(f"[!] Error: {response.exit_code}")
    print(response.result)
else:
    print("[+] Output:")
    print(response.result)
