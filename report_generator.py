# report_generator.py
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

def generate_report(vulnerabilities):
    c = canvas.Canvas("vulnerability_report.pdf", pagesize=letter)
    c.drawString(100, 750, "Vulnerability Report")
    for i, vuln in enumerate(vulnerabilities):
        c.drawString(100, 730 - i * 20, vuln)
    c.save()

if __name__ == "__main__":
    vulnerabilities = ["SQLi vulnerability in login form", "XSS vulnerability in login form"]
    generate_report(vulnerabilities)
