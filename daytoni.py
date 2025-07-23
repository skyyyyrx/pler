from daytona import Daytona, DaytonaConfig
import time

# Inisialisasi konfigurasi dengan API key kamu
config = DaytonaConfig(api_key="dtn_65c10bd3da5ba392171806def2b21f0ad1013852708ff74c3566f34f9764bd41")
daytona = Daytona(config)

# Buat sandbox (default resource)
sandbox = daytona.create()

# Tunggu beberapa detik agar sandbox siap (opsional)
time.sleep(5)

# Perintah shell kamu
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

# Jalankan semua perintah
response = sandbox.process.shell_run(commands)

# Tampilkan output
if response.exit_code != 0:
    print(f"[!] Error code: {response.exit_code}")
    print("[!] Output:")
    print(response.result)
else:
    print("[+] Output:")
    print(response.result)
