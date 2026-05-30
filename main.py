from fastapi import FastAPI
from fastapi.responses import JSONResponse, FileResponse
from fastapi.staticfiles import StaticFiles
from anthropic import Anthropic
from dotenv import load_dotenv
import os

load_dotenv()

app = FastAPI()
client = Anthropic(api_key=os.getenv("ANTHROPIC_API_KEY"))

app.mount("/static", StaticFiles(directory="static"), name="static")


@app.get("/")
def home():
    return FileResponse("static/index.html")


def get_defaults(drink_type):
    defaults = {
        "milk_tea": {
            "sweetness": "50%",
            "ice": "less ice",
            "toppings": ["pearls", "pudding"],
            "tips": ["add cheese foam", "try 30% sugar"]
        },
        "fruit_tea": {
            "sweetness": "50%",
            "ice": "regular ice",
            "toppings": ["lychee jelly", "crystal boba"],
            "tips": ["add aloe vera", "try less sugar"]
        },
        "matcha": {
            "sweetness": "30%",
            "ice": "less ice",
            "toppings": ["pearls", "red bean"],
            "tips": ["add oat milk", "add cheese foam"]
        },
        "taro": {
            "sweetness": "50%",
            "ice": "less ice",
            "toppings": ["pearls", "pudding"],
            "tips": ["make it creamy", "add crystal boba"]
        },
        "brown_sugar": {
            "sweetness": "50%",
            "ice": "less ice",
            "toppings": ["brown sugar pearls", "cream foam"],
            "tips": ["add pudding", "ask for extra drizzle"]
        },
        "cheese_foam": {
            "sweetness": "50%",
            "ice": "regular ice",
            "toppings": ["cheese foam", "crystal boba"],
            "tips": ["sip without straw first", "add fruit jelly"]
        }
    }

    return defaults.get(drink_type, defaults["milk_tea"])


def fallback_recommendations(mood, weather):
    weather_lower = weather.lower()

    if "rain" in weather_lower or "cold" in weather_lower:
        drinks = [
            ("Brown Sugar Milk Tea", "brown_sugar", "Cozy Pick", "Creamy and comforting for gloomy weather."),
            ("Taro Milk Tea", "taro", "Soft Comfort Pick", "Sweet and gentle when you need a calm treat.")
        ]
    elif "sun" in weather_lower or "hot" in weather_lower:
        drinks = [
            ("Mango Green Tea", "fruit_tea", "Sunny Refresh Pick", "Fruity and cooling for hot weather."),
            ("Iced Matcha Latte", "matcha", "Calm Energy Pick", "Refreshing but still smooth and focused.")
        ]
    else:
        drinks = [
            ("Classic Milk Tea", "milk_tea", "Safe Favorite Pick", "Balanced and comforting for any mood."),
            ("Brown Sugar Milk Tea", "brown_sugar", "Sweet Reset Pick", "Rich and cozy when you want a treat.")
        ]

    return build_response(drinks, mood, weather)


def build_response(drinks, mood, weather):
    recommendations = []

    for drink, drink_type, vibe, why in drinks:
        defaults = get_defaults(drink_type)

        recommendations.append({
            "drink": drink,
            "drinkType": drink_type,
            "vibe": vibe,
            "why": why,
            "sweetness": defaults["sweetness"],
            "ice": defaults["ice"],
            "toppings": defaults["toppings"],
            "orderInstructions": f"Order {drink} with {defaults['sweetness']} sweetness, {defaults['ice']}, and {', '.join(defaults['toppings'])}.",
            "customizeTips": defaults["tips"]
        })

    return {
        "mood": mood,
        "weather": weather,
        "recommendations": recommendations,
        "affirmation": "You deserve a sweet little treat today."
    }


@app.get("/oracle")
def oracle(mood: str = "happy", weather: str = "sunny"):
    prompt = f"""
Give 2 boba recommendations for this mood and weather.

Mood: {mood}
Weather: {weather}

Return only 2 lines.
Format:
drink|drinkType|vibe|why

Allowed drinkType:
milk_tea, fruit_tea, matcha, taro, brown_sugar, cheese_foam

Keep each field short.
No markdown.
"""

    try:
        message = client.messages.create(
            model="claude-haiku-4-5",
            max_tokens=300,
            messages=[
                {
                    "role": "user",
                    "content": prompt
                }
            ],
        )

        response_text = message.content[0].text.strip()

        print("RAW CLAUDE RESPONSE:")
        print(response_text)

        lines = response_text.splitlines()
        drinks = []

        allowed_types = {
            "milk_tea",
            "fruit_tea",
            "matcha",
            "taro",
            "brown_sugar",
            "cheese_foam"
        }

        for line in lines:
            parts = [p.strip() for p in line.split("|")]

            if len(parts) != 4:
                continue

            drink, drink_type, vibe, why = parts

            if drink_type not in allowed_types:
                drink_type = "milk_tea"

            drinks.append((drink, drink_type, vibe, why))

        if len(drinks) < 2:
            return JSONResponse(fallback_recommendations(mood, weather))

        return JSONResponse(build_response(drinks[:2], mood, weather))

    except Exception as e:
        print("ERROR:", str(e))
        return JSONResponse(fallback_recommendations(mood, weather))