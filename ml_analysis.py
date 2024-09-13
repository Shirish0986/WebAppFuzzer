from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

# Function to generate a simple report
def generate_report(vulnerabilities):
    c = canvas.Canvas("vulnerability_report.pdf", pagesize=letter)
    c.drawString(100, 750, "Vulnerability Report")
    c.drawString(100, 730, "Identified vulnerabilities:")
    for i, vuln in enumerate(vulnerabilities):
        c.drawString(100, 710 - i * 20, vuln)
    c.save()

# Example usage
if __name__ == "__main__":
    vulnerabilities = [
        "SQLi vulnerability in login form",
        "XSS vulnerability in comment form"
    ]
    generate_report(vulnerabilities)
