from faker import Faker
import pandas as pd
import random
from datetime import datetime, timedelta

fake = Faker("en_IN")

banks = ["SBI","HDFC","ICICI","Axis","Kotak"]
channels = ["UPI","NEFT","RTGS","IMPS"]
cities = ["Mumbai","Delhi","Hyderabad","Bangalore","Chennai","Pune"]

transactions = []

start_time = datetime.now()

# Generate normal transactions
for i in range(80):

    txn = {
        "txn_id": f"TXN-{i:04}",
        "sender_name": fake.name(),
        "sender_account": fake.bban(),
        "sender_upi": fake.user_name()+"@upi",
        "receiver_name": fake.name(),
        "receiver_account": fake.bban(),
        "amount_inr": random.randint(5000,500000),
        "currency": "INR",
        "channel": random.choice(channels),
        "bank": random.choice(banks),
        "city": random.choice(cities),
        "timestamp": start_time + timedelta(minutes=i)
    }

    transactions.append(txn)


# Structuring pattern (below ₹10L)
for i in range(3):

    base_time = start_time + timedelta(hours=2)

    for j in range(3):

        txn = {
            "txn_id": f"STRUCT-{i}-{j}",
            "sender_name": "Rajesh Kumar",
            "sender_account": "HDFC-STRUCT-001",
            "sender_upi": "rajesh@okhdfcbank",
            "receiver_name": fake.name(),
            "receiver_account": fake.bban(),
            "amount_inr": random.randint(900000,990000),
            "currency": "INR",
            "channel": "NEFT",
            "bank": "HDFC",
            "city": "Mumbai",
            "timestamp": base_time + timedelta(minutes=j*20)
        }

        transactions.append(txn)


# UPI layering pattern
for j in range(6):

    txn = {
        "txn_id": f"LAYER-{j}",
        "sender_name": "Amit Sharma",
        "sender_account": "SBI-LAYER-001",
        "sender_upi": "amit@oksbi",
        "receiver_name": fake.name(),
        "receiver_account": fake.bban(),
        "amount_inr": random.randint(100000,200000),
        "currency": "INR",
        "channel": "UPI",
        "bank": "SBI",
        "city": "Delhi",
        "timestamp": start_time + timedelta(minutes=10*j)
    }

    transactions.append(txn)


df = pd.DataFrame(transactions)

df.to_csv("data/transactions.csv", index=False)

print("Dataset created: data/transactions.csv")