from agents.detector import run_detector

flagged = run_detector()

print("Flagged Transactions:")

for txn in flagged[:10]:
    print(txn["txn_id"], txn["amount_inr"], txn["sender_name"])