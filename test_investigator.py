from agents.detector import run_detector
from agents.investigator import run_investigator

# Step 1: detect suspicious transactions
flagged = run_detector()

print("\nRunning investigator agent...\n")

# Step 2: investigate them using Gemini
results = run_investigator(flagged)

# Step 3: print results
for r in results[:5]:

    txn = r["transaction"]

    print("Transaction ID:", txn["txn_id"])
    print("Sender:", txn["sender_name"])
    print("Amount:", txn["amount_inr"])
    print("Investigation:\n", r["investigation"])
    print("\n-----------------------------\n")