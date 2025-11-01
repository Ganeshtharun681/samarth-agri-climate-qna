import pandas as pd
import re

# ===============================
# LOAD DATASETS
# ===============================
rain = pd.read_csv("data/rainfall.csv")
crop = pd.read_csv("data/crop_production.csv")

# Rename for uniformity (in case this script is run standalone)
rain = rain.rename(columns={'year': 'Year', 'actual': 'Rainfall'})
crop = crop.rename(columns={'name_of_the_state_ut': 'State', 'capacity_in_mt': 'Production'})

# ===============================
# CORE Q&A FUNCTION
# ===============================
def answer_query(question: str):
    q = question.lower()

    # --- Case 1: Compare rainfall between two years ---
    if "rainfall" in q and "compare" in q:
        years = re.findall(r"\b(20\d{2})\b", q)
        if len(years) >= 2:
            y1, y2 = map(int, years[:2])
            r1 = rain[rain["Year"] == y1]["Rainfall"].values
            r2 = rain[rain["Year"] == y2]["Rainfall"].values
            if len(r1) and len(r2):
                diff = r2[0] - r1[0]
                direction = "increase" if diff > 0 else "decrease"
                return (
                    f"Between {y1} and {y2}, rainfall changed from {r1[0]} to {r2[0]}, "
                    f"which is a {abs(diff)} unit {direction}.",
                    "Source: IMD Rainfall Dataset (data.gov.in)"
                )
            else:
                return ("Rainfall data for one or both years not found.", "Rainfall Dataset")

        return ("Please specify two years to compare rainfall (e.g., 2020 and 2024).", "Rainfall Dataset")

    # --- Case 2: Find top producing states ---
    elif "top" in q and "production" in q:
        # Extract how many top results (e.g. 'top 5')
        num = re.findall(r"top (\d+)", q)
        n = int(num[0]) if num else 5
        df = crop.sort_values(by="Production", ascending=False).head(n)
        summary = df[["State", "Production"]].to_string(index=False)
        return (
            f"Top {n} states by production capacity:\n{summary}",
            "Source: Ministry of Agriculture Dataset (data.gov.in)"
        )

    # --- Case 3: General rainfall trend ---
    elif "rainfall" in q and ("trend" in q or "average" in q):
        avg_rain = rain["Rainfall"].mean()
        max_rain = rain.loc[rain["Rainfall"].idxmax()]
        min_rain = rain.loc[rain["Rainfall"].idxmin()]
        return (
            f"Average rainfall across available years is {avg_rain:.2f}.\n"
            f"Highest was {max_rain.Rainfall} in {int(max_rain.Year)}, "
            f"and lowest was {min_rain.Rainfall} in {int(min_rain.Year)}.",
            "Source: IMD Rainfall Dataset (data.gov.in)"
        )

    # --- Default fallback ---
    else:
        return (
            "Sorry, I currently handle only rainfall comparisons and top crop production questions.",
            "No specific dataset used."
        )
