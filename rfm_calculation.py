# RFM Calculation Script
# This script reads processed_sales.csv and calculates RFM metrics per customer

import pandas as pd

# Load the cleaned sales data
df = pd.read_csv("output/processed_sales.csv", parse_dates=['InvoiceDate'])

# Set the snapshot date to the day after the last transaction
snapshot_date = df['InvoiceDate'].max() + pd.Timedelta(days=1)

# Group by CustomerID and calculate RFM
rfm = df.groupby('CustomerID').agg({
    'InvoiceDate': lambda x: (snapshot_date - x.max()).days,  # Recency
    'InvoiceNo': 'nunique',                                   # Frequency
    'TotalPrice': 'sum'                                       # Monetary
}).reset_index()

# Rename the columns
rfm.columns = ['CustomerID', 'Recency', 'Frequency', 'Monetary']

# Save RFM table
rfm.to_csv("output/rfm_metrics.csv", index=False)
print("RFM metrics calculated and saved to output/rfm_metrics.csv")
