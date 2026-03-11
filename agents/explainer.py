from groq import Groq
import os
from dotenv import load_dotenv

load_dotenv()

client = Groq(api_key=os.getenv("GROQ_API_KEY"))


def run_explainer(regulator_results):

    explanations = []

    for item in regulator_results:

        txn = item["transaction"]
        investigation = item["investigation"]
        regulation = item["regulation"]

        prompt = f"""
You are a financial compliance AI assistant.

Transaction details:
ID: {txn["txn_id"]}
Amount: ₹{txn["amount_inr"]}

Investigation:
{investigation}

Relevant regulation:
{regulation}

Write a short compliance explanation describing why this transaction may violate financial regulations.
"""

        response = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[{"role": "user", "content": prompt}]
        )

        explanations.append({
            "transaction": txn,
            "investigation": investigation,
            "regulation": regulation,
            "explanation": response.choices[0].message.content
        })

    return explanations