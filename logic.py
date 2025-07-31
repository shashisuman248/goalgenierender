import pandas as pd

def get_recommendation(data):
    df = pd.read_csv("recommendation_matrix.csv")

    sip = int(data.get("sip", 0))
    tenure = int(data.get("tenure", 0))
    risk = data.get("risk", "").lower()

    def match(row):
        return (
            row["min_sip"] <= sip <= row["max_sip"] and
            row["min_tenure"] <= tenure <= row["max_tenure"] and
            row["risk_profile"].lower() == risk
        )

    filtered = df[df.apply(match, axis=1)]

    if len(filtered) < 3:
        filtered = df[df["risk_profile"].str.lower() == risk].head(3)

    recommendations = []
    for _, row in filtered.head(3).iterrows():
        fund = row["fund_name"]
        logic_en = row.get("logic_en", "No explanation provided.")
        logic_hi = row.get("logic_hi", "")
        recommendations.append(
            f"👉 **{fund}**\n{logic_en}\n**{logic_hi}**\n"
        )

    return {
        "message": "\n\n".join(recommendations)
    }
