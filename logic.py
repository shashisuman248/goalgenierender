import pandas as pd
import random

def get_recommendation(data):
    # Load the matrix
    df = pd.read_csv("recommendation_matrix.csv")

    # Extract input
    sip = int(data.get("sip", 0))
    tenure = int(data.get("tenure", 0))
    risk = data.get("risk", "").lower()

    # Define matching logic
    def match(row):
        return (
            row["min_sip"] <= sip <= row["max_sip"] and
            row["min_tenure"] <= tenure <= row["max_tenure"] and
            row["risk_profile"].lower() == risk
        )

    # Filter based on conditions
    filtered = df[df.apply(match, axis=1)]

    # If not enough rows, give top 3 best-effort matches
    if len(filtered) < 3:
        filtered = df[df["risk_profile"].str.lower() == risk].head(3)

    # Prepare list of fund recommendations
    recommendations = []
    for _, row in filtered.head(3).iterrows():
        fund = row["fund_name"]
        logic_en = row.get("logic_en", "No explanation provided.")
        logic_hi = row.get("logic_hi", "")
        recommendations.append(
            f"👉 **{fund}**\n{logic_en}\n**{logic_hi}**\n"
        )

    # Join all responses
    return {
        "message": "\n\n".join(recommendations)
    }
