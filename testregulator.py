from agents.detector import run_detector
from agents.investigator import run_investigator
from agents.regulator import run_regulator

print("\nRunning detector...")
flagged = run_detector()

print("\nRunning investigator...")
investigations = run_investigator(flagged)

print("\nRunning regulator agent...")
results = run_regulator(investigations)


for r in results:

    txn = r["transaction"]

    print("\nTransaction:", txn["txn_id"])
    print("Sender:", txn["sender_name"])
    print("Amount:", txn["amount_inr"])

    print("\nInvestigation:")
    print(r["investigation"])

    print("\nRelevant Regulation:")
    print(r["regulation"])

    print("\n------------------------")