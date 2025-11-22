import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load the clustered data
df = pd.read_csv("output/rfm_clusters.csv")

sns.set(style="whitegrid")

# Create 1 row, 3 columns
fig, axes = plt.subplots(1, 3, figsize=(18, 5))

# -----------------------
# Plot 1: Monetary vs Recency
# -----------------------
sns.scatterplot(
    data=df,
    x="Recency",
    y="Monetary",
    hue="ClusterName",
    palette="deep",
    s=80,
    alpha=0.7,
    ax=axes[0]
)
axes[0].set_title("Monetary vs Recency")

# -----------------------
# Plot 2: Frequency vs Recency
# -----------------------
sns.scatterplot(
    data=df,
    x="Recency",
    y="Frequency",
    hue="ClusterName",
    palette="deep",
    s=80,
    alpha=0.7,
    ax=axes[1]
)
axes[1].set_title("Frequency vs Recency")

# -----------------------
# Plot 3: Monetary vs Frequency
# -----------------------
sns.scatterplot(
    data=df,
    x="Frequency",
    y="Monetary",
    hue="ClusterName",
    palette="deep",
    s=80,
    alpha=0.7,
    ax=axes[2]
)
axes[2].set_title("Monetary vs Frequency")

plt.savefig("output/all_three_plots.png")
plt.close()

print("Saved 3-in-1 plot: output/all_three_plots.png")
