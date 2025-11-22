# RFM Scoring Script
# This script reads rfm_metrics.csv and assigns percentile-based scores (1 to 4)
# for Recency, Frequency, and Monetary values.

import pandas as pd

# Load the RFM metrics file
df = pd.read_csv("output/rfm_metrics.csv")

# Prepare data for scoring
# Lower Recency value = better, so invert Recency for scoring
df['Recency_inv'] = -df['Recency']

# Convert RFM columns to numeric (safety)
df['Recency_inv'] = pd.to_numeric(df['Recency_inv'], errors='coerce')
df['Frequency'] = pd.to_numeric(df['Frequency'], errors='coerce')
df['Monetary'] = pd.to_numeric(df['Monetary'], errors='coerce')

# Percentile ranking (0 to 1)
df['recency_pct'] = df['Recency_inv'].rank(pct=True)
df['frequency_pct'] = df['Frequency'].rank(pct=True)
df['monetary_pct'] = df['Monetary'].rank(pct=True)

# Convert percentiles into scores (1 to 4)
def to_score(pct):
    if pct <= 0.25:
        return 1
    elif pct <= 0.50:
        return 2
    elif pct <= 0.75:
        return 3
    else:
        return 4

df['R_Score'] = df['recency_pct'].apply(to_score)
df['F_Score'] = df['frequency_pct'].apply(to_score)
df['M_Score'] = df['monetary_pct'].apply(to_score)

# Remove temporary columns
df = df.drop(columns=['Recency_inv', 'recency_pct', 'frequency_pct', 'monetary_pct'])

# Save the scored RFM data
df.to_csv("output/rfm_scores.csv", index=False)
print("RFM scores calculated and saved to output/rfm_scores.csv")
