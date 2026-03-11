import os
from dotenv import load_dotenv
from groq import Groq

load_dotenv()

client = Groq(api_key=os.getenv("GROQ_API_KEY"))


def run_investigator(flagged_transactions):

    investigations = []

    transactions_to_investigate = flagged_transactions

    for i, txn in enumerate(transactions_to_investigate):

        print(f"Investigating transaction {i+1} / {len(transactions_to_investigate)}")

        prompt = f"""
You are a financial compliance investigator.

Analyze this transaction and return ONLY 3 lines.

Transaction ID: {txn["txn_id"]}
Amount: ₹{txn["amount_inr"]}
Channel: {txn["channel"]}

Output format:

Pattern: <fraud pattern>
Reason: <short reason>
Suspicion Score: <1-10>
"""

        try:

            response = client.chat.completions.create(
                model="llama-3.3-70b-versatile",
                messages=[
                    {"role": "user", "content": prompt}
                ]
            )

            investigations.append({
                "transaction": txn,
                "investigation": response.choices[0].message.content
            })

        except Exception as e:

            print("Groq API error:", e)

            investigations.append({
                "transaction": txn,
                "investigation": "Investigation failed due to API error."
            })

    return investigations