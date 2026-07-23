# 🔥 Webhook Spammer

![Python](https://img.shields.io/badge/Python-3.8%2B-blue)
![License](https://img.shields.io/badge/License-MIT-green)
![Discord](https://img.shields.io/badge/Discord-Webhook-5865F2)

A sleek terminal-based tool for sending, testing, and managing Discord webhooks — built for penetration testers and security researchers.

> ⚠️ **Educational purposes only.** Only use on webhooks you own or have explicit permission to test.

---

## ✨ Features

| # | Feature | Description |
|---|---------|-------------|
| 01 | **Spam Loop** | Rapid-fire messages at 0.01s default delay (~100 msg/s) |
| 02 | **Send Single** | Send one custom message (with optional username) |
| 03 | **Send Multiple** | Send N messages with configurable delay |
| 04 | **Webhook Info** | Fetch and display webhook metadata (ID, name, channel, guild, token) |
| 05 | **Delete Webhook** | Permanently remove a webhook (irreversible — confirmation required) |
| 06 | **Clear Stats** | Reset session counters |
| 07 | **Exit** | Quit the application |

---

## 🖥️ Preview

```
┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
┃                              WEBHOOK SPAMMER v1.0 │ Author: User │ 2026-07-23 14:30:00 ┃
┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛
┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
┃                               Sent 0   Success 0   Failed 0   Total 0                    ┃
┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛
┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
┃                                           MENU                                           ┃
┣━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┫
┃ [01] Spam Loop                                                                           ┃
┃ [02] Send Single                                                                         ┃
┃ [03] Send Multiple                                                                       ┃
┃ [04] Webhook Info                                                                        ┃
┃ [05] Delete Webhook                                                                      ┃
┃ [06] Clear Stats                                                                         ┃
┃ [07] Exit                                                                                ┃
┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛
```

---

## 🚀 Quick Start

### Prerequisites
- Python 3.8+
- Windows (primary target) / Linux / macOS

### Installation

```bash
# Clone the repository
git clone [https://github.com/your-username/webhook-spammer.git](https://github.com/your-username/webhook-spammer.git)
cd webhook-spammer

# Install dependencies
pip install -r requirements.txt

# Run
python webhook-spammer.py
```

### Windows (one-click)
Double-click `start.bat` — it will auto-install dependencies and launch.

---

## 📁 Project Structure

```text
webhook-spammer/
├── webhook-spammer.py   # Main application
├── requirements.txt     # Python dependencies
├── start.bat            # Windows launcher
├── README.md            # This file
├── LICENSE              # MIT License
└── results/             # Session logs (auto-created)
    └── session_2026-07-23.txt
```

---

## 📊 Logging

Every operation is automatically logged to `results/session_YYYY-MM-DD.txt`:

```text
========== SESSION STARTED ==========
[SPAM] Sent=247 OK=245 FAIL=2 Time=3.2s Rate=77.2msg/s Target=[https://discord.com/api/webhooks/](https://discord.com/api/webhooks/)...
[MULTI] 50 msgs: OK=50 FAIL=0 Target=[https://discord.com/api/webhooks/](https://discord.com/api/webhooks/)...
[INFO] OK ID=123456789 Name=TestWebhook ...
[DELETE] OK Target=[https://discord.com/api/webhooks/](https://discord.com/api/webhooks/)...
========== SESSION ENDED ==========
```

---

## ⚡ Performance

- **Spam Loop default delay:** 0.01s (~100 messages/second theoretical)
- Adjustable delay for rate-limit testing
- Real-time counter with timestamps
- `Ctrl+C` to stop any operation gracefully

---

## 🔒 Rate Limiting

Discord applies rate limits per webhook (typically 5 requests per 2 seconds). The tool respects Discord's rate-limiting responses. Use responsibly.

---

## 📜 License

MIT License — Free to use, modify, and distribute.

---

## 🤝 Contributing

Pull requests are welcome! For major changes, open an issue first.

---

## ⚖️ Disclaimer

This tool is for authorized security testing and educational purposes only. The authors are not responsible for any misuse or damage caused by this program. Always ensure you have explicit permission before testing webhooks you do not own.
