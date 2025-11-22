# kmeans_elbow.py
# This script creates the elbow chart to help choose K for K-Means.

import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans

# Load RFM scores
df = pd.read_csv("output/rfm_scores.csv")

# Select the RFM score columns for clustering
X = df[['R_Score', 'F_Score', 'M_Score']]

# Calculate inertia for K = 1 to 10
inertias = []
K_values = range(1, 11)

for k in K_values:
    model = KMeans(n_clusters=k, random_state=42)
    model.fit(X)
    inertias.append(model.inertia_)

# Plot the elbow chart
plt.plot(K_values, inertias, marker='o')
plt.xlabel("Number of Clusters (K)")
plt.ylabel("Inertia")
plt.title("Elbow Method to Determine K")
plt.grid(True)

# Save the elbow plot
plt.savefig("output/elbow_plot.png")
plt.close()

print("Elbow plot saved to output/elbow_plot.png")
