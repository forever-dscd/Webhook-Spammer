# 🔥 Webhook Spammer

![Python](https://img.shields.io/badge/Python-3.8%2B-blue)
![License](https://img.shields.io/badge/License-MIT-green)
![Discord](https://img.shields.io/badge/Discord-Webhook-5865F2)

Un outil en ligne de commande pour envoyer, tester et gérer des webhooks Discord — conçu pour les tests d'intrusion et la recherche en sécurité.

> ⚠️ **À des fins éducatives uniquement.** À utiliser uniquement sur des webhooks dont vous êtes propriétaire ou sur lesquels vous disposez d'une autorisation explicite de test.

---

## ✨ Fonctionnalités

| # | Fonctionnalité | Description |
|---|----------------|-------------|
| 01 | **Spam** | Envoi rapide de messages avec un délai par défaut de 0.01s (~100 msg/s) |
| 02 | **Envoi Unique** | Envoyer un message personnalisé (avec nom d'utilisateur optionnel) |
| 03 | **Envoi Multiple** | Envoyer N messages avec un délai configurable |
| 04 | **Infos Webhook** | Récupérer et afficher les métadonnées (ID, nom, salon, serveur, token) |
| 05 | **Supprimer Webhook** | Supprimer définitivement un webhook (irréversible — confirmation requise) |
| 06 | **Effacer Stats** | Réinitialiser les compteurs de session |
| 07 | **Quitter** | Quitter l'application |

---

## 🖥️ Aperçu

```
┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
┃ WEBHOOK SPAMMER v1.0 │ Auteur: User │ 2026-07-23 14:30:00                                ┃
┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛
┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
┃ Envoyés 0 ┃ Succès 0 ┃ Échecs 0 ┃ Total 0                                                ┃
┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛
┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
┃                                           MENU                                           ┃
┣━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┫
┃ [01] Spam                                                                                ┃
┃ [02] Envoi Unique                                                                        ┃
┃ [03] Envoi Multiple                                                                      ┃
┃ [04] Infos Webhook                                                                       ┃
┃ [05] Supprimer Webhook                                                                   ┃
┃ [06] Effacer Stats                                                                       ┃
┃ [07] Quitter                                                                             ┃
┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛
```

---

## 🚀 Démarrage Rapide

### Prérequis
- Python 3.8+
- Windows (cible principale) / Linux / macOS

### Installation

```bash
# Cloner le dépôt
git clone https://github.com/forever-dscd/Webhook-Spammer.git
cd webhook-spammer

# Installer les dépendances
pip install -r requirements.txt

# Lancer
python webhook-spammer.py
```

### Windows (en un clic)
Double-cliquez sur `start.bat` — il installera automatiquement les dépendances et lancera l'application.

---

## 📁 Structure du Projet

```text
webhook-spammer/
├── webhook-spammer.py   # Application principale
├── requirements.txt     # Dépendances Python
├── start.bat            # Lanceur Windows
├── README.md            # Ce fichier
├── LICENSE              # Licence MIT
└── results/             # Journaux de session (créés automatiquement)
    └── session_2026-07-23.txt
```

---

## 📊 Journalisation (Logging)

Chaque opération est automatiquement enregistrée dans `results/session_AAAA-MM-JJ.txt` :

```text
========== SESSION STARTED ==========
[SPAM] Sent=247 OK=245 FAIL=2 Time=3.2s Rate=77.2msg/s Target=[https://discord.com/api/webhooks/](https://discord.com/api/webhooks/)...
[MULTI] 50 msgs: OK=50 FAIL=0 Target=[https://discord.com/api/webhooks/](https://discord.com/api/webhooks/)...
[INFO] OK ID=123456789 Name=TestWebhook ...
[DELETE] OK Target=[https://discord.com/api/webhooks/](https://discord.com/api/webhooks/)...
========== SESSION ENDED ==========
```

---

## ⚡ Performances

- **Délai par défaut de la boucle de spam :** 0.01s (~100 messages/seconde théoriques)
- Délai ajustable pour les tests de limite de débit (rate limit)
- Compteur en temps réel avec horodatage
- `Ctrl+C` pour arrêter toute opération en douceur

---

## 🔒 Limite de Débit (Rate Limiting)

Discord applique des limites de débit par webhook (généralement 5 requêtes par tranche de 2 secondes). L'outil prend en compte les réponses de limitation de débit de Discord. Utilisez-le de manière responsable.

---

## 📜 Licence

Licence MIT — Libre d'utilisation, de modification et de distribution.

---

## ⚖️ Avertissement (Disclaimer)

Cet outil est destiné uniquement à des fins éducatives et de tests de sécurité autorisés. Les auteurs ne sont pas responsables de toute mauvaise utilisation ou de tout dommage causé par ce programme. Assurez-vous toujours d'avoir l'autorisation explicite avant de tester des webhooks qui ne vous appartiennent pas.
