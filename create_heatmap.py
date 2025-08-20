import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Read the correlation matrix we created
corr_df = pd.read_csv('correlation.csv', index_col=0)

# UPDATED: Create a smaller figure for the plot
plt.figure(figsize=(5, 4.2)) # This creates a 480x403 pixel image with dpi=96

# Generate the heatmap (no changes here)
sns.heatmap(corr_df, annot=True, cmap='coolwarm', fmt=".2f", vmin=-1, vmax=1)

plt.title('Supply Chain Metrics Correlation Matrix')
plt.tight_layout() # Adjusts plot to ensure everything fits without overlapping

# Save the heatmap as a PNG image
plt.savefig('heatmap.png', dpi=96) # dpi remains 96

print("Successfully created heatmap.png with dimensions under 512x512.")
