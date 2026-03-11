from agents.detector import run_detector
from agents.investigator import run_investigator
from agents.regulator import run_regulator
from agents.explainer import run_explainer
from agents.report import generate_report


def run_aface():

    print("\nRunning Agentic Fraud-Audit & Compliance Engine pipeline...\n")

    print("Step 1: Detecting suspicious transactions")
    flagged = run_detector()

    print("\nStep 2: Investigating suspicious activity")
    investigations = run_investigator(flagged)

    print("\nStep 3: Retrieving relevant regulations")
    reg_results = run_regulator(investigations)

    print("\nStep 4: Generating compliance explanation")
    final_results = run_explainer(reg_results)

    print("\nStep 5: Generating audit report")
    generate_report(final_results)


if __name__ == "__main__":
    run_aface()