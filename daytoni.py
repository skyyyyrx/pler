from daytona import Daytona, DaytonaConfig, Resources
import time

# Inisialisasi konfigurasi dengan API key kamu
config = DaytonaConfig(api_key="dtn_65c10bd3da5ba392171806def2b21f0ad1013852708ff74c3566f34f9764bd41")
daytona = Daytona(config)

# Atur resource untuk sandbox
resources = Resources(cpu_count=2, memory_mb=2048)  # 2 core CPU dan 2GB RAM

# Buat sandbox dengan resource khusus
sandbox = daytona.create(resources=resources)

# Tunggu sampai sandbox siap (opsional, tergantung API)
time.sleep(5)

# Perintah shell yang ingin kamu jalankan
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

# Jalankan perintah shell di sandbox
response = sandbox.process.shell_run(commands)

# Tampilkan hasilnya
if response.exit_code != 0:
    print(f"[!] Error Code: {response.exit_code}")
    print("[!] Output:")
    print(response.result)
else:
    print("[+] Output:")
    print(response.result)
