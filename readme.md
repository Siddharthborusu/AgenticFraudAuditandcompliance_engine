# AFACE — Agentic Fraud-Audit & Compliance Engine

AFACE is an AI-powered compliance investigation system that detects suspicious financial transactions, analyzes them using LLM reasoning, retrieves relevant financial regulations, and generates automated audit reports.

This project simulates how financial institutions investigate suspicious transactions using a modular AI pipeline.

---

## Live Demo

Streamlit App:
(Add your Streamlit link here)

Example workflow:

Upload transaction dataset → Run AFACE analysis → View flagged transactions → Download compliance audit report.

---

## Architecture

AFACE uses a multi-stage agent pipeline:

Transactions Dataset
↓
Fraud Detection Agent
↓
Investigation Agent (LLM reasoning)
↓
Regulatory Retrieval Agent (RAG)
↓
Compliance Explanation Agent
↓
Audit Report Generator

---

## Key Features

Fraud Pattern Detection

* Detects suspicious patterns such as structuring and layering

LLM Investigation

* Uses an LLM to analyze suspicious transactions and generate investigation summaries

Regulatory Retrieval (RAG)

* Retrieves relevant compliance rules and financial regulations

Explainable Compliance AI

* Connects suspicious behavior to regulatory requirements

Automated Audit Reports

* Generates compliance reports in PDF format

Interactive Web Interface

* Streamlit dashboard for uploading datasets and running analysis

---

## Tech Stack

Python
Streamlit
Groq LLM API
Sentence Transformers
FAISS Vector Search
ReportLab
Pandas

---

## Project Structure

aface-project/

agents/

* detector.py
* investigator.py
* regulator.py
* explainer.py
* report.py

rag/

* regulations.txt

data/

* transactions.csv

app.py
main.py
requirements.txt

---

## Running Locally

Install dependencies:

pip install -r requirements.txt

Run the application:

streamlit run app.py

---

## Example Output

AFACE generates a compliance audit report including:

* Suspicious transaction details
* Investigation summary
* Relevant regulations
* Compliance explanation

---

## Why This Project

Financial institutions require explainable AI systems to investigate suspicious financial activity.

AFACE demonstrates how AI agents, LLM reasoning, and regulatory retrieval can be combined to automate parts of the compliance investigation process.

---

## Author

Siddharth Borusu


# AgenticFraudAuditandcompliance_engine
# AgenticFraudAuditandcompliance_engine
