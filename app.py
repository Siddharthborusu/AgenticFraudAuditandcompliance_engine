import streamlit as st
import groq as Groq
import pandas as pd

from agents.detector import run_detector
from agents.investigator import run_investigator
from agents.regulator import run_regulator
from agents.explainer import run_explainer
from agents.report import generate_report

st.title("Agentic Fraud-Audit & Compliance Engine (AFACE) built and hosted by siddharth borusu")

st.markdown("""
AI-powered system for detecting suspicious financial transactions, 
investigating them using LLM reasoning, retrieving regulatory context,
and generating automated compliance audit reports.

🔗 **GitHub Repo:**  
https://github.com/Siddharthborusu/AgenticFraudAuditandcompliance_engine
""")

uploaded_file = st.file_uploader("Upload Transactions CSV", type=["csv"])

if uploaded_file is not None:

    df = pd.read_csv(uploaded_file)

    st.write("### Uploaded Transactions")
    st.dataframe(df)

    if st.button("Run AFACE Analysis"):

        st.write("Running fraud detection...")

        flagged = run_detector()

        st.write("Running investigation...")

        investigations = run_investigator(flagged)

        st.write("Retrieving regulations...")

        reg_results = run_regulator(investigations)

        st.write("Generating compliance explanations...")

        final_results = run_explainer(reg_results)

        st.success("Analysis complete!")

        st.write("### Flagged Transactions")

        for r in final_results:

            txn = r["transaction"]

            st.write("Transaction ID:", txn["txn_id"])
            st.write("Amount:", txn["amount_inr"])
            st.write("Investigation:", r["investigation"])
            st.write("Regulation:", r["regulation"])
            st.write("Explanation:", r["explanation"])

            st.divider()

        generate_report(final_results)

        with open("aface_audit_report.pdf", "rb") as f:

            st.download_button(
                label="Download Compliance Report",
                data=f,
                file_name="aface_audit_report.pdf",
                mime="application/pdf"
            )
