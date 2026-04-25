from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph, Spacer
from tracker import get_all_transactions, get_summary, get_all_goals
from datetime import date

def generate_report():
    filename = f"finance_report_{date.today()}.pdf"
    doc = SimpleDocTemplate(filename, pagesize=A4)
    styles = getSampleStyleSheet()
    elements = []

    # Title
    elements.append(Paragraph(" Personal Finance Report", styles['Title']))
    elements.append(Paragraph(f"Generated on: {date.today()}", styles['Normal']))
    elements.append(Spacer(1, 20))

    # Summary Section
    total_income, total_expenses, balance = get_summary()
    elements.append(Paragraph("Summary", styles['Heading2']))

    summary_data = [
        ["Total Income", f"${total_income:.2f}"],
        ["Total Expenses", f"${total_expenses:.2f}"],
        ["Balance", f"${balance:.2f}"],
    ]

    summary_table = Table(summary_data, colWidths=[250, 150])
    summary_table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor('#2ecc71')),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.white),
        ('FONTNAME', (0, 0), (-1, -1), 'Helvetica'),
        ('FONTSIZE', (0, 0), (-1, -1), 11),
        ('ROWBACKGROUNDS', (0, 1), (-1, -1), [colors.whitesmoke, colors.white]),
        ('GRID', (0, 0), (-1, -1), 0.5, colors.grey),
        ('PADDING', (0, 0), (-1, -1), 8),
    ]))

    elements.append(summary_table)
    elements.append(Spacer(1, 20))

    # Transactions Section
    elements.append(Paragraph("All Transactions", styles['Heading2']))

    transactions = get_all_transactions()
    if transactions:
        tx_data = [["Date", "Type", "Category", "Amount", "Description"]]
        for t in transactions:
            tx_data.append([
                t.date,
                t.type.capitalize(),
                t.category,
                f"${t.amount:.2f}",
                t.description or "-"
            ])

        tx_table = Table(tx_data, colWidths=[80, 70, 90, 80, 170])
        tx_table.setStyle(TableStyle([
            ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor('#3498db')),
            ('TEXTCOLOR', (0, 0), (-1, 0), colors.white),
            ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
            ('FONTNAME', (0, 1), (-1, -1), 'Helvetica'),
            ('FONTSIZE', (0, 0), (-1, -1), 9),
            ('ROWBACKGROUNDS', (0, 1), (-1, -1), [colors.whitesmoke, colors.white]),
            ('GRID', (0, 0), (-1, -1), 0.5, colors.grey),
            ('PADDING', (0, 0), (-1, -1), 6),
        ]))
        elements.append(tx_table)
    else:
        elements.append(Paragraph("No transactions recorded yet.", styles['Normal']))

    elements.append(Spacer(1, 20))

    # Savings Goals Section
    elements.append(Paragraph("Savings Goals", styles['Heading2']))

    goals = get_all_goals()
    if goals:
        goal_data = [["Goal", "Target", "Saved", "Remaining", "Progress"]]
        for g in goals:
            goal_data.append([
                g.name,
                f"${g.target_amount:.2f}",
                f"${g.saved_amount:.2f}",
                f"${g.remaining():.2f}",
                f"{g.progress_percentage():.1f}%"
            ])

        goal_table = Table(goal_data, colWidths=[120, 80, 80, 80, 80])
        goal_table.setStyle(TableStyle([
            ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor('#9b59b6')),
            ('TEXTCOLOR', (0, 0), (-1, 0), colors.white),
            ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
            ('FONTNAME', (0, 1), (-1, -1), 'Helvetica'),
            ('FONTSIZE', (0, 0), (-1, -1), 9),
            ('ROWBACKGROUNDS', (0, 1), (-1, -1), [colors.whitesmoke, colors.white]),
            ('GRID', (0, 0), (-1, -1), 0.5, colors.grey),
            ('PADDING', (0, 0), (-1, -1), 6),
        ]))
        elements.append(goal_table)
    else:
        elements.append(Paragraph("No savings goals recorded yet.", styles['Normal']))

    doc.build(elements)
    print(f"Report saved as '{filename}'")