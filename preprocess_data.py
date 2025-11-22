import pandas as pd

# Load the data
# Load only the necessary columns for RFM. Postal code is used as CustomerID.
df = pd.read_csv('data/amazon_sale_report.csv', usecols=['Order ID', 'Date', 'Qty', 'Amount', 'ship-postal-code'])

# Drop all rows that have ANY null values
df = df.dropna()

# Remove rows without any monetary value
# Drop rows where 'Amount' is zero, as they are not real sales.
df = df[(df['Amount'] != 0)]

# Remove rows with zero quantity
# A zero quantity would prevent computing unit price, and likely indicates no actual sale.
df = df[df['Qty'] != 0]

# Parse the date column into datetime objects
# Converting the 'Date' string into pandas datetime makes it easy to calculate recency later.
df['Date'] = pd.to_datetime(df['Date'], format='%m-%d-%y')

# Drop any duplicate records
# If the exact same transaction appears more than once, we remove duplicates to avoid double-counting.
df = df.drop_duplicates()

# Rename columns to RFM-friendly names
# We rename 'Order ID' to 'InvoiceNo' and 'Date' to 'InvoiceDate' to match RFM terminology.
df = df.rename(columns={
    'Order ID': 'InvoiceNo',
    'Date': 'InvoiceDate',
    'Qty': 'Quantity',
    'Amount': 'TotalPrice'
})

# Use POSTAL CODE as CustomerID
df['CustomerID'] = df['ship-postal-code'].astype(str)

# Remove the postal code column (no longer needed)
df = df.drop(columns=['ship-postal-code'])

# Calculate UnitPrice from TotalPrice and Quantity
# This gives the price per item in each transaction row (useful for analysis).
df['UnitPrice'] = df['TotalPrice'] / df['Quantity']

# 9. Reorder columns for clarity
df = df[['InvoiceNo', 'InvoiceDate', 'CustomerID', 'Quantity', 'UnitPrice', 'TotalPrice']]

# 10: Save the cleaned file
df.to_csv('output/processed_sales.csv', index=False)
print(f"Successfully cleaned and saved {len(df)} records to output/processed_sales.csv")
