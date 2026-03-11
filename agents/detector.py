import pandas as pd
from datetime import timedelta

def load_transactions(path="data/transactions.csv"):
    df = pd.read_csv(path)
    df["timestamp"] = pd.to_datetime(df["timestamp"])
    return df


def detect_structuring(df):

    flagged = []

    grouped = df.groupby("sender_account")

    for account, group in grouped:

        suspicious = group[
            (group["amount_inr"] >= 800000) &
            (group["amount_inr"] <= 999999)
        ]

        if len(suspicious) >= 3:
            flagged.extend(suspicious.to_dict("records"))

    return flagged


def detect_upi_layering(df):

    flagged = []

    upi_txns = df[df["channel"] == "UPI"]

    grouped = upi_txns.groupby("sender_account")

    for account, group in grouped:

        group = group.sort_values("timestamp")

        if len(group) >= 5:
            flagged.extend(group.to_dict("records"))

    return flagged


def run_detector():

    df = load_transactions()

    structuring_cases = detect_structuring(df)
    layering_cases = detect_upi_layering(df)

    flagged = structuring_cases + layering_cases

    print(f"Structuring cases detected: {len(structuring_cases)}")
    print(f"UPI layering cases detected: {len(layering_cases)}")

    return flagged