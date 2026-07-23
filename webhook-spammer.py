#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
WEBHOOK SPAMMER v1.0 — Discord Webhook Spammer By Forever™
"""

import os, sys, re, time, requests
from datetime import datetime

os.system(""); os.system("chcp 65001 >nul 2>&1")

def resize_con(w, h):
    if os.name != "nt": return
    try:
        from ctypes import windll, byref, wintypes
        hOut = windll.kernel32.GetStdHandle(-11)
        windll.kernel32.SetConsoleScreenBufferSize(hOut, wintypes._COORD(w+30, 999))
        windll.kernel32.SetConsoleWindowInfo(hOut, True, byref(wintypes._SMALL_RECT(0,0,w-1,h-1)))
    except:
        try: os.system(f"mode con: cols={w} lines={h}")
        except: pass

# ─── COULEURS ────────────────────────────────────────────────
sv1 = "\033[38;5;255m"
sv2 = "\033[38;5;252m"
sv3 = "\033[38;5;250m"
sv4 = "\033[38;5;247m"
sv5 = "\033[38;5;244m"
red = "\033[91m"
gre = "\033[92m"
yel = "\033[93m"
rst = "\033[0m"
bld = "\033[1m"

# ─── REGEX ANSI ─────────────────────────────────────────────
re_a = re.compile(r'\033\[[0-9;]*[mHl]')

def strip_ansi(s):
    return re_a.sub('', s)

# ─── BANNIERE ────────────────────────────────────────────────
B = [
    "█     █░▓█████  ▄▄▄▄    ██░ ██  ▒█████   ▒█████   ██ ▄█▀     ██████  ██▓███   ▄▄▄       ███▄ ▄███▓",
    "▓█░ █ ░█░▓█   ▀ ▓█████▄ ▓██░ ██▒▒██▒  ██▒▒██▒  ██▒ ██▄█▒    ▒██    ▒ ▓██░  ██▒▒████▄    ▓██▒▀█▀ ██▒",
    "▒█░ █ ░█ ▒███   ▒██▒ ▄██▒██▀▀██░▒██░  ██▒▒██░  ██▒▓███▄░    ░ ▓██▄   ▓██░ ██▓▒▒██  ▀█▄  ▓██    ▓██░",
    "░█░ █ ░█ ▒▓█  ▄ ▒██░█▀  ░▓█ ░██ ▒██   ██░▒██   ██░▓██ █▄     ▒   ██▒▒██▄█▓▒ ▒░██▄▄▄▄██ ▒██    ▒██ ",
    "░░██▒██▓ ░▒████▒░▓█  ▀█▓░▓█▒░██▓░ ████▓▒░░ ████▓▒░▒██▒ █▄   ▒██████▒▒▒██▒ ░  ░ ▓█   ▓██▒▒██▒   ░██▒",
    "░ ▓░▒ ▒  ░░ ▒░ ░░▒▓███▀▒ ▒ ░░▒░▒░ ▒░▒░▒░ ░ ▒░▒░▒░ ▒ ▒▒ ▓▒   ▒ ▒▓▒ ▒ ░▒▓▒░ ░  ░ ▒▒   ▓▒█░░ ▒░   ░  ░",
    "  ▒ ░ ░   ░ ░  ░▒░▒   ░  ▒ ░▒░ ░  ░ ▒ ▒░   ░ ▒ ▒░ ░ ░▒ ▒░   ░ ░▒  ░ ░░▒ ░       ▒   ▒▒ ░░  ░      ░",
    "  ░   ░     ░    ░    ░  ░  ░░ ░░ ░ ░ ▒  ░ ░ ░ ▒  ░ ░░ ░    ░  ░  ░  ░░         ░   ▒   ░      ░   ",
    "    ░       ░  ░ ░       ░  ░  ░    ░ ░      ░ ░  ░  ░            ░                 ░  ░       ░   ",
    "                      ░",
]

resize_con(120, 42)

def show_banner(c=sv1):
    for l in B:
        print(f"{c}{l}{rst}")

# ─── PLUS D'ANIMATION SHIMMER — juste le banner statique ──

# ─── STATS ───────────────────────────────────────────────────
S = {"sent":0,"ok":0,"fail":0,"total":0}

# ─── BOITES ──────────────────────────────────────────────────
W = 100
HW = W - 4

def top():
    sys.stdout.write(f"  ┏{'━' * HW}┓\n")

def bot():
    sys.stdout.write(f"  ┗{'━' * HW}┛\n")

def mid():
    sys.stdout.write(f"  ┣{'━' * HW}┫\n")

def lin(txt):
    plain = strip_ansi(txt)
    pad = HW - len(plain)
    if pad < 0: pad = 0
    sys.stdout.write(f"  ┃{txt}{' ' * pad}┃\n")

def box_header():
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    top()
    lin(f"{bld}{sv2}  WEBHOOK SPAMMER v1.0  {sv4}│{rst}  {sv4}Author:{sv1} Forever™{rst}  {sv4}│{rst}  {sv5}{now}{rst}")
    bot()

def box_stats():
    top()
    lin(f"{sv2}  Sent {sv1}{S['sent']:>5}  {sv2}Success {gre}{S['ok']:>5}  {sv2}Failed {red}{S['fail']:>5}  {sv2}Total {sv1}{S['total']:>5}{rst}")
    bot()

def box_menu():
    items = [("01","Spam"), ("02","Send Single"), ("03","Send Multiple"),
             ("04","Webhook Info"), ("05","Delete Webhook"), ("06","Clear Stats"), ("07","Exit")]
    top()
    lin(f"{bld}{sv1}  MENU{rst}")
    mid()
    for n,l in items:
        lin(f"  {sv4}[{sv1}{bld}{n}{rst}{sv4}]{rst}  {sv2}{l}{rst}")
    bot()

def prompt():
    return input(f"\n  {sv4}[{sv1}{bld}Webhook-Spammer{rst}{sv4}]{rst} {sv3}->{rst} ").strip()

# ─── WEBHOOK API ─────────────────────────────────────────────
def parse_webhook(url):
    m = re.search(r"discord(?:app)?\.com/api/webhooks/(\d+)/([A-Za-z0-9_-]+)", url.strip())
    return (m.group(1), m.group(2)) if m else (None, None)

def webhook_send(u, c, un=None):
    p = {"content": c}
    if un: p["username"] = un
    try:
        r = requests.post(u, json=p, headers={"Content-Type":"application/json"}, timeout=10)
        return r.status_code, r
    except Exception as e: return None, str(e)

def webhook_info(u):
    try:
        r = requests.get(u, timeout=10)
        return (r.status_code, r.json()) if r.status_code == 200 else (r.status_code, r.text[:100])
    except Exception as e: return None, str(e)

def webhook_delete(u):
    try:
        r = requests.delete(u, timeout=10)
        return r.status_code, "OK" if r.status_code == 204 else r.text[:60]
    except Exception as e: return None, str(e)

def pause():
    input(f"\n  {sv5}Press Enter...{rst}")

# ─── ACTIONS ─────────────────────────────────────────────────
def act_spam():
    print(f"\n  {'━' * 60}")
    print(f"  {bld}{sv1}SPAM LOOP  {yel}[Ctrl+C]{rst}")
    print(f"  {'━' * 60}")
    url = input(f"  {sv4}[{sv1}?{sv4}]{rst} URL: {sv3}->{rst} ").strip()
    if not url or not parse_webhook(url)[0]:
        return  # SILENT — pas de message d'erreur
    msg = input(f"  {sv4}[{sv1}?{sv4}]{rst} Message: {sv3}->{rst} ").strip()
    if not msg: return
    d = 0.01
    dd = input(f"  {sv4}[{sv1}?{sv4}]{rst} Delay (0.01): {sv3}->{rst} ").strip()
    if dd:
        try: d = float(dd)
        except: pass
    ctr = 0
    try:
        while True:
            ctr+=1; S["sent"]+=1; S["total"]+=1
            c,_ = webhook_send(url,msg)
            if c in (200,204):
                S["ok"]+=1
                print(f"  {sv4}[{sv1}{ctr}{sv4}]{rst} {gre}OK{rst}  {sv5}{datetime.now().strftime('%H:%M:%S')}{rst}")
            else:
                S["fail"]+=1
                # FAIL masqué — aucune sortie
            time.sleep(d)
    except KeyboardInterrupt:
        print(f"\n  {yel}[!] Stopped ({ctr} msgs){rst}")

def act_single():
    print(f"\n  {'━' * 60}")
    print(f"  {bld}{sv1}SEND SINGLE MESSAGE{rst}")
    print(f"  {'━' * 60}")
    url = input(f"  {sv4}[{sv1}?{sv4}]{rst} URL: {sv3}->{rst} ").strip()
    if not url or not parse_webhook(url)[0]:
        return
    msg = input(f"  {sv4}[{sv1}?{sv4}]{rst} Message: {sv3}->{rst} ").strip()
    if not msg: return
    un = input(f"  {sv4}[{sv1}?{sv4}]{rst} Username: {sv3}->{rst} ").strip() or None
    S["sent"]+=1; S["total"]+=1
    c,r = webhook_send(url,msg,un)
    if c in (200,204):
        S["ok"]+=1
        print(f"  {gre}[+] Sent ({c}){rst}")
    else:
        S["fail"]+=1  # rien n'est affiché

def act_multi():
    print(f"\n  {'━' * 60}")
    print(f"  {bld}{sv1}SEND MULTIPLE{rst}")
    print(f"  {'━' * 60}")
    url = input(f"  {sv4}[{sv1}?{sv4}]{rst} URL: {sv3}->{rst} ").strip()
    if not url or not parse_webhook(url)[0]:
        return
    try: n = int(input(f"  {sv4}[{sv1}?{sv4}]{rst} Count: {sv3}->{rst} ").strip())
    except: return
    msg = input(f"  {sv4}[{sv1}?{sv4}]{rst} Message: {sv3}->{rst} ").strip()
    if not msg: return
    d = 0.5
    dd = input(f"  {sv4}[{sv1}?{sv4}]{rst} Delay (0.5): {sv3}->{rst} ").strip()
    if dd:
        try: d = float(dd)
        except: pass
    for i in range(1,n+1):
        S["sent"]+=1; S["total"]+=1
        c,_ = webhook_send(url,msg)
        if c in (200,204):
            S["ok"]+=1
            print(f"  {gre}[{i}/{n}] OK{rst}  {sv5}({d}s){rst}")
        else:
            S["fail"]+=1  # FAIL masqué
        time.sleep(d)
    print(f"  {sv2}Done.{rst}")

def act_info():
    print(f"\n  {'━' * 60}")
    print(f"  {bld}{sv1}WEBHOOK INFO{rst}")
    print(f"  {'━' * 60}")
    url = input(f"  {sv4}[{sv1}?{sv4}]{rst} URL: {sv3}->{rst} ").strip()
    if not url: return
    wid, wt = parse_webhook(url)
    if not wid: return
    c,d = webhook_info(url)
    if c == 200:
        print(f"\n  {'━'*60}")
        for k in ['id','name','channel_id','guild_id']:
            print(f"  {sv4}{k:<12}{sv1}{d.get(k,'N/A')}{rst}")
        print(f"  {sv4}Token{':'*9}{sv1}{wt}{rst}")
        if d.get('avatar'): print(f"  {sv4}avatar{':'*8}{sv1}{d['avatar']}{rst}")
        print(f"  {'━'*60}")
    # FAIL silencieux

def act_del():
    print(f"\n  {'━' * 60}")
    print(f"  {bld}{sv1}DELETE WEBHOOK  {yel}[IRREVERSIBLE]{rst}")
    print(f"  {'━' * 60}")
    url = input(f"  {sv4}[{sv1}?{sv4}]{rst} URL: {sv3}->{rst} ").strip()
    if not url or not parse_webhook(url)[0]:
        return
    cf = input(f"  {yel}[!] Confirm? (y/N): {rst}").strip().lower()
    if cf != "y": return
    c,_ = webhook_delete(url)
    if c == 204:
        print(f"  {gre}[+] Deleted!{rst}")
    # FAIL masqué

def act_clr():
    for k in S: S[k]=0
    print(f"  {gre}[+] Cleared{rst}")

# ─── MAIN ────────────────────────────────────────────────────
def main():
    # Vérification internet silencieuse — pas de message d'erreur affiché
    try: requests.get("https://discord.com", timeout=5)
    except: pass

    sys.stdout.write("\033[?25l")
    # ─── AFFICHE UNIQUEMENT LE ASCII ART AU LANCEMENT ───
    show_banner()
    sys.stdout.write("\033[?25h")

    while True:
        os.system("cls" if os.name == "nt" else "clear")
        print()
        show_banner()
        print()
        box_header()
        print()
        box_stats()
        print()
        box_menu()

        ch = prompt()
        if ch in ("01","1"):       act_spam()
        elif ch in ("02","2"):     act_single()
        elif ch in ("03","3"):     act_multi()
        elif ch in ("04","4"):     act_info()
        elif ch in ("05","5"):     act_del()
        elif ch in ("06","6"):     act_clr()
        elif ch in ("07","7","exit","quit","q"):
            print(f"\n  {sv2}Bye.{rst}"); break
        # Option invalide → rien n'est affiché non plus (silencieux)
        pause()

if __name__ == "__main__":
    try: main()
    except KeyboardInterrupt: print(f"\n  {yel}[!] Interrupted{rst}")
    except Exception as e: print(f"\n  {red}[!] Error: {e}{rst}")
