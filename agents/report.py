from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas


def generate_report(results):

    file_name = "aface_audit_report.pdf"

    c = canvas.Canvas(file_name, pagesize=letter)

    width, height = letter
    y = 750

    # Report Title
    c.setFont("Helvetica-Bold", 16)
    c.drawString(180, y, "Agentic Fraud-Audit & Compliance Engine Report")

    y -= 40

    c.setFont("Helvetica", 10)

    for r in results:

        txn = r["transaction"]

        # Transaction Details
        c.drawString(50, y, f"Transaction ID: {txn['txn_id']}")
        y -= 15

        c.drawString(50, y, f"Sender: {txn['sender_name']}")
        y -= 15

        c.drawString(50, y, f"Amount: INR{txn['amount_inr']}")
        y -= 15

        c.drawString(50, y, f"Bank: {txn['bank']}")
        y -= 15

        c.drawString(50, y, f"City: {txn['city']}")
        y -= 20

        # Investigation Section
        c.setFont("Helvetica-Bold", 10)
        c.drawString(50, y, "Investigation:")
        y -= 15

        c.setFont("Helvetica", 10)

        for line in r["investigation"].split("\n"):
            c.drawString(60, y, line.strip())
            y -= 15

        y -= 10

        # Regulation Section
        c.setFont("Helvetica-Bold", 10)
        c.drawString(50, y, "Relevant Regulation:")
        y -= 15

        c.setFont("Helvetica", 10)

        for line in r["regulation"].split("\n"):
            c.drawString(60, y, line.strip())
            y -= 15

        y -= 10

        # Compliance Explanation
        c.setFont("Helvetica-Bold", 10)
        c.drawString(50, y, "Compliance Explanation:")
        y -= 15

        c.setFont("Helvetica", 10)

        for line in r["explanation"].split("\n"):
            c.drawString(60, y, line.strip())
            y -= 15

        y -= 30

        # Page break
        if y < 120:
            c.showPage()
            y = 750
            c.setFont("Helvetica", 10)

    c.save()

    print("\nReport generated: aface_audit_report.pdf")