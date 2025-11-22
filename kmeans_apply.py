# kmeans_apply.py
# This script applies K-Means using your selected K value.

import pandas as pd
from sklearn.cluster import KMeans

#  Set your chosen K
chosen_k = 3   # change this after checking elbow_plot.png

# Load RFM scores
df = pd.read_csv("output/rfm_scores.csv")

# Select features
X = df[['R_Score', 'F_Score', 'M_Score']]

# Fit K-Means with chosen K
model = KMeans(n_clusters=chosen_k, random_state=42)
df['Cluster'] = model.fit_predict(X)

# Add simple cluster names
cluster_names = {
    2: "High Value",
    0: "Low Value",
    1: "Lost"
}

df['ClusterName'] = df['Cluster'].map(cluster_names)

# Save cluster output
df.to_csv("output/rfm_clusters.csv", index=False)
print(f"K-Means clustering completed with K={chosen_k}")
print("Clustered results saved to output/rfm_clusters.csv")

