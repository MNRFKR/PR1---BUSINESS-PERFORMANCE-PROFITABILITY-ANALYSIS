import seaborn as sns
import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages
import pandas as pd
import os

# Load your Excel file
df = pd.read_excel(r"C:\Marvel\Desktop\project 1\RAW SALES DATA.xlsx", engine="openpyxl")

# Convert numeric columns
df['Price'] = pd.to_numeric(df['Price'], errors='coerce')
df['Discount'] = pd.to_numeric(df['Discount'], errors='coerce')
df['Units Sold'] = pd.to_numeric(df['Units Sold'], errors='coerce')
df['Inventory Level'] = pd.to_numeric(df['Inventory Level'], errors='coerce')

# Calculations
df['Sales'] = (df['Price'] - df['Discount']) * df['Units Sold']
df['Cost'] = df['Sales'] * 0.7
df['Profit'] = df['Sales'] - df['Cost']
df['ProfitMargin'] = df['Profit'] / df['Sales']
df['InventoryDays'] = df['Inventory Level'] / df['Units Sold']

# Path to save PDF
pdf_path = r"C:\Marvel\Desktop\project 1\Analysis_Report.pdf"
os.makedirs(os.path.dirname(pdf_path), exist_ok=True)

with PdfPages(pdf_path) as pdf:
    # Page 1: scatterplot
    sns.scatterplot(x='InventoryDays', y='ProfitMargin', data=df)
    sns.regplot(x='InventoryDays', y='ProfitMargin', data=df, scatter=False, color='red')
    plt.title("Inventory Days vs Profit Margin")
    plt.xlabel("Inventory Days")
    plt.ylabel("Profit Margin")
    plt.grid(True)
    pdf.savefig()
    plt.close()

    # Page 2: embed the entire script file contents
    fig, ax = plt.subplots(figsize=(8.5, 11))
    ax.axis("off")
    with open(r"C:\Marvel\Desktop\project 1\p7.py", "r") as f:  # adjust filename to your script
        code_text = f.read()
    ax.text(0, 1, code_text, va="top", ha="left", fontsize=8, family="monospace")
    pdf.savefig(fig)
    plt.close(fig)

print("PDF saved at:", pdf_path)
