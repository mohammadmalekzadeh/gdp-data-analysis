# Import Library
import pandas as pd
import numpy as np
from scipy.stats import shapiro, pearsonr, spearmanr, skew

# Load Processed Dataset
df = pd.read_csv('../dataset/gdp_processed_data.csv')

cols = {
    'GDP Value (log)': 'GDP_log',
    'Population (log)': 'Population_log',
    'GDP Growth (%)': 'GDP_growth',
    'GDP Per Capita': 'GDP_per_capita',
    'Share of World GDP (%)': 'Share_world_GDP'
}
df.rename(columns=cols, inplace=True)

# Descriptive Statistics
desc_cols = ['GDP_log', 'Population_log', 'GDP_growth', 'GDP_per_capita', 'Share_world_GDP']
desc_stats = df[desc_cols].describe().T
desc_stats['skewness'] = df[desc_cols].skew()
desc_stats = desc_stats[['mean', 'std', 'min', '25%', '50%', '75%', 'max', 'skewness']]

# Normality Check
normality_results = {}
for col in desc_cols:
    stat, p = shapiro(df[col].dropna())
    normality_results[col] = {'Statistic': stat, 'p-value': p}

normality_df = pd.DataFrame(normality_results).T
normality_df['Normal?'] = normality_df['p-value'].apply(lambda x: 'Yes' if x > 0.05 else 'No')

# Correlation Analysis
pairs = [
    ('GDP_log', 'Population_log'),
    ('GDP_log', 'Share_world_GDP'),
    ('GDP_per_capita', 'GDP_growth'),
    ('Population_log', 'GDP_growth')
]
corr_results = []

for a, b in pairs:
    pearson_r, pearson_p = pearsonr(df[a], df[b])
    spearman_r, spearman_p = spearmanr(df[a], df[b])
    corr_results.append({
        'Pair': f'{a} ~ {b}',
        'Pearson_r': pearson_r,
        'Pearson_p': pearson_p,
        'Spearman_r': spearman_r,
        'Spearman_p': spearman_p
    })

corr_df = pd.DataFrame(corr_results)

def interpret_corr(r):
    if abs(r) > 0.8: return 'Strong'
    elif abs(r) > 0.4: return 'Moderate'
    else: return 'Weak'

corr_df['Interpretation'] = corr_df['Pearson_r'].apply(interpret_corr)

# Save results
desc_stats.reset_index().round(4).to_csv('../dataset/eda_descriptive_stats.csv', index= False)
normality_df.reset_index().round(4).to_csv('../dataset/eda_normality_test.csv', index= False)
corr_df.round(4).to_csv('../dataset/eda_correlation_results.csv', index= False)