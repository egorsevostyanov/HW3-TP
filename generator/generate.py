import csv
import random
import os
import sys

NUM_ROWS = 50

COLUMNS = ["drink_name", "degree", "volume_ml", "type"]

def generate_row():
    drinks = [
        "Absolut Vodka", "Jack Daniel's", "Jameson", "Hendrick's Gin",
        "Bacardi Rum", "Jose Cuervo", "Johnnie Walker Red", "Baileys",
        "Aperol", "Campari", "Jagermeister", "Kahlua",
        "Glenfiddich 12", "Monkey Shoulder", "Tanqueray", "Captain Morgan",
    ]
    types = ["Vodka", "Whiskey", "Gin", "Rum", "Tequila", "Liqueur"]

    return {
        "drink_name": random.choice(drinks),
        "degree": round(random.uniform(5.0, 60.0), 1),
        "volume_ml": random.choice([200, 350, 500, 700, 750, 1000]),
        "type": random.choice(types),
    }

OUTPUT_DIR = sys.argv[1] if len(sys.argv) > 1 else "/data"
OUTPUT_FILE = os.path.join(OUTPUT_DIR, "data.csv")

os.makedirs(OUTPUT_DIR, exist_ok=True)

rows = [generate_row() for _ in range(NUM_ROWS)]

with open(OUTPUT_FILE, "w", newline="", encoding="utf-8") as f:
    writer = csv.DictWriter(f, fieldnames=COLUMNS)
    writer.writeheader()
    writer.writerows(rows)