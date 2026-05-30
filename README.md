# 🧋 AI BobaGenie

Tell the AI BobaGenie how you're feeling. It picks your boba.

A tiny AI-powered web app that recommends boba drinks based on your mood and the weather — complete with sweetness, ice level, toppings, and exactly how to order at the shop.

**🔗 Live: [[AI BobaGenieURL](https://boba-oracle.onrender.com/)]**

---

## ✨ What it does

- Type your mood (`"ugh today was so long..."`) and the weather (`"rainy and cold"`)
- The AI BobaGenie returns **two** personalized boba picks
- Each pick includes:
  - Drink name + a vibe label
  - Why it fits your moment (one warm sentence)
  - Recommended sweetness, ice level, and toppings
  - A copy-pastable order line for the boba shop
  - Quick customization tips
- Every boba cup is hand-drawn in pure CSS — no images, just vibes 

## 🛠 Built with

- **FastAPI** — Python backend, one tiny `main.py`
- **Anthropic Claude API** (`claude-haiku-4-5`) — the AI BobaGenie's brain
- **Vanilla HTML + CSS + JavaScript** — no frameworks, no build step
- **Render** — free-tier deployment

## 🚀 Run it locally

**1. Clone the repo**
```bash
git clone https://github.com/nischita44/boba-oracle.git
cd boba-oracle
```

**2. Set up a virtual environment**
```bash
python3 -m venv venv
source venv/bin/activate
```

**3. Install dependencies**
```bash
pip install -r requirements.txt
```

**4. Add your Anthropic API key**

Create a `.env` file in the project root:


Get a key at [console.anthropic.com](https://console.anthropic.com). New accounts get free credits — this app uses pennies.

**5. Run it**
```bash
python -m uvicorn main:app --reload
```

Open [http://127.0.0.1:8000](http://127.0.0.1:8000) and consult the AI BobaGenie. 🧋

## 📁 Project structure

boba-oracle/
├── main.py              # FastAPI app + Claude integration
├── static/
│   └── index.html       # UI (HTML + CSS + JS in one file)
├── requirements.txt
├── .env                 # API key (not in git)
└── .gitignore

## 💡 Why I built this

I wanted a tiny, joyful weekend project that uses AI for warmth rather than productivity. The AI BobaGenie has a persona, baked-in boba knowledge, and a shareable result card — small things that make it feel different from just asking ChatGPT.

Built in a weekend during a career transition. Open source so anyone can fork it, customize the AI BobaGenie's voice, or swap in their own boba menu.

## 📜 License

Do whatever you want with it. Make a CoffeeGenie. A Pizza Genie. The world is yours.

---

Made with 🧋 by ([LinkedIn](https://www.linkedin.com/in/nischitha-sadananda/))
