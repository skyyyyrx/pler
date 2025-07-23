from daytona import Daytona, DaytonaConfig
import time

config = DaytonaConfig(api_key="dtn_65c10bd3da5ba392171806def2b21f0ad1013852708ff74c3566f34f9764bd41")
daytona = Daytona(config)

sandbox = daytona.create()
time.sleep(5)

# Semua command shell kamu dikombinasi dalam satu string Python dan dijalankan via subprocess
commands = '''
import subprocess

subprocess.run("apt update && apt upgrade -y", shell=True)
subprocess.run("wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb", shell=True)
subprocess.run("dpkg -i google-chrome-stable_current_amd64.deb || apt --fix-broken install -y", shell=True)
subprocess.run("dpkg -i google-chrome-stable_current_amd64.deb", shell=True)
subprocess.run("wget https://storage.googleapis.com/chrome-for-testing-public/137.0.7151.103/linux64/chromedriver-linux64.zip", shell=True)
subprocess.run("unzip chromedriver-linux64.zip", shell=True)
subprocess.run("chmod +x chromedriver-linux64/chromedriver", shell=True)
subprocess.run("mv chromedriver-linux64/chromedriver /usr/local/bin/", shell=True)
subprocess.run("apt install python3-pip -y", shell=True)
subprocess.run("python3 -m pip install selenium", shell=True)
subprocess.run("wget -O vv.py https://raw.githubusercontent.com/skyyyyrx/pler/refs/heads/main/128.py", shell=True)
subprocess.run("python3 vv.py", shell=True)
'''

# Jalankan command di sandbox
response = sandbox.code_run(commands)

if response.exit_code != 0:
    print(f"[!] Error: {response.exit_code}")
    print(response.result)
else:
    print("[+] Output:")
    print(response.result)
