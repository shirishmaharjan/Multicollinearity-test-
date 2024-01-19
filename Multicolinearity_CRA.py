# %%
#Multi colinearity test for CRA

import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from scipy import stats

# %%
# Load dataset 

Multicolinearity_CRA = pd.read_excel("C:/GIIS/IMWI (Palika Area)/Multicolinearity Test/Data/Multicolinearity_CRA.xlsx")
Multicolinearity_CRA

# %%
# Drop front 2 columns 

Multicolinearity_CRA = Multicolinearity_CRA.drop(Multicolinearity_CRA.columns[:2],axis=1)
Multicolinearity_CRA

# %%
# Create a correlation matrix
#correlation_matrix = Multicolinearity_CRA.corr()
#correlation_matrix

# Assuming Multicolinearity_CRA is your DataFrame
#correlation_matrix, p_values = stats.pearsonr(Multicolinearity_CRA, Multicolinearity_CRA)

# Assuming Multicolinearity_CRA is your DataFrame
num_variables = len(Multicolinearity_CRA.columns)
correlation_matrix = np.zeros((num_variables, num_variables))
p_values = np.ones((num_variables, num_variables))

columns = Multicolinearity_CRA.columns  # Get the column names

for i in range(num_variables):
    for j in range(i+1, num_variables):
        corr_coeff, p_value = stats.pearsonr(Multicolinearity_CRA[columns[i]], Multicolinearity_CRA[columns[j]])
        correlation_matrix[i, j] = corr_coeff
        correlation_matrix[j, i] = corr_coeff
        p_values[i, j] = p_value
        p_values[j, i] = p_value

# %%
correlation_matrix
#p_values

# %%
# Create a mask to display only the upper triangular part
mask = np.triu(np.ones_like(correlation_matrix, dtype=bool))

# Replace values greater than 0.8 and less than -0.8 with NaN
correlation_matrix[(correlation_matrix > 0.8) | (correlation_matrix < -0.8)] = np.nan

# Replace values with NaN where p-value is greater than 0.05
correlation_matrix[p_values > 0.05] = np.nan

# Create a heatmap using seaborn
plt.figure(figsize=(20,10))
sns.heatmap(correlation_matrix, annot=True, fmt=".1f", cmap='coolwarm', vmin=-1, vmax=1, mask=mask, xticklabels=columns, yticklabels=columns)

# Rotate the x-axis labels to be displayed at the top
plt.tick_params(axis='x', labelrotation=90)

plt.title('Multicolinearity plot CRA')

# Save the figure with a white background
plt.savefig('Multicolinearity_CRA.png', format='png', dpi=300, bbox_inches='tight', facecolor='white')

# Display the plot
plt.show()


