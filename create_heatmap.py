import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Read the correlation matrix we created
corr_df = pd.read_csv('correlation.csv', index_col=0)

# Create a figure for the plot
plt.figure(figsize=(6, 5))

# Generate the heatmap
sns.heatmap(corr_df, annot=True, cmap='coolwarm', fmt=".2f", vmin=-1, vmax=1)

plt.title('Supply Chain Metrics Correlation Matrix')
plt.tight_layout()

# Save the heatmap as a PNG image
plt.savefig('heatmap.png', dpi=96)

print("Successfully created heatmap.png")
