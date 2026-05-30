# 🧋 AI BobaGenie

Tell the Oracle how you're feeling. It picks your boba.

A tiny AI-powered web app that recommends boba drinks based on your mood and the weather — complete with sweetness, ice level, toppings, and exactly how to order at the shop.

**🔗 Live: [[your-render-url-here](https://boba-oracle.onrender.com/)]**

---

## ✨ What it does

- Type your mood (`"ugh today was so long..."`) and the weather (`"rainy and cold"`)
- The Oracle returns **two** personalized boba picks
- Each pick includes:
  - Drink name + a vibe label
  - Why it fits your moment (one warm sentence)
  - Recommended sweetness, ice level, and toppings
  - A copy-pastable order line for the boba shop
  - Quick customization tips
- Every boba cup is hand-drawn in pure CSS — no images, just vibes 

## 🛠 Built with

- **FastAPI** — Python backend, one tiny `main.py`
- **Anthropic Claude API** (`claude-haiku-4-5`) — the Oracle's brain
- **Vanilla HTML + CSS + JavaScript** — no frameworks, no build step
- **Render** — free-tier deployment

## 🚀 Run it locally

**1. Clone the repo**
```bash
