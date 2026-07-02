git add tools/repayment_pdf.py
git commit -m "Add repayment schedule PDF generator script"
git push origin main
mkdir tools
nano tools/repayment_pdf.py
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas

def generate_repayment_pdf(filename):
    c = canvas.Canvas(filename, pagesize=A4)
    c.setFont("Helvetica-Bold", 14)
    c.drawString(200, 800, "Repayment Schedule - 4 Paydays")

    headers = ["Loan Amount (K)", "Interest Rate", "Total Repayment (K)", "Per Payday Deduction (K)"]
    y = 770
    c.setFont("Helvetica", 12)
    for i, h in enumerate(headers):
        c.drawString(80 + i*120, y, h)

    y -= 30
    for loan in range(50, 3001, 50):  # loans from 50K to 3000K
        interest_rate = 0.50
        total_repayment = loan + (loan * interest_rate)
        per_payday = total_repayment / 4

        row = [loan, "50%", round(total_repayment, 2), round(per_payday, 2)]
        for i, item in enumerate(row):
            c.drawString(80 + i*120, y, str(item))
        y -= 20

        if y < 50:
            c.showPage()
            y = 770

    c.save()

generate_repayment_pdf("repayment_schedule.pdf")
