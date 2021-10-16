import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

'''
https://github.com/elegant-scipy/elegant-scipy/blob/master/data/genes.csv
https://github.com/elegant-scipy/elegant-scipy/blob/master/data/counts.txt.bz2
'''
pd.set_option('display.max_columns', 500)
#plt.style.use('style/elegant.mplstyle')
plt.style.use('ggplot')

def reduce_xaxis_labels(ax, factor):
    """Show only every ith label to prevent crowding on x-axis
        e.g. factor = 2 would plot every second x-axis label,
        starting at the first.

    Parameters
    ----------
    ax : matplotlib plot axis to be adjusted
    factor : int, factor to reduce the number of x-axis labels by
    """
    plt.setp(ax.xaxis.get_ticklabels(), visible=False)
    for label in ax.xaxis.get_ticklabels()[factor-1::factor]:
        label.set_visible(True)

data_table = pd.read_csv('counts.txt', index_col=0)
print(data_table.columns)
print(data_table.iloc[:5, :5])

gene_info = pd.read_csv('genes.csv', index_col=0)
print(gene_info.iloc[:5, :])

print("Genes in data_table: ", data_table.shape[0])
print("Genes in gene_info: ", gene_info.shape[0])
matched_index = pd.Index.intersection(data_table.index, gene_info.index)

counts = np.asarray(data_table.loc[matched_index], dtype=int)

gene_names = np.array(matched_index)

# Check how many genes and individuals were measured
print(f'{counts.shape[0]} genes measured in {counts.shape[1]} individuals.')
gene_lengths = np.asarray(gene_info.loc[matched_index]['GeneLength'],
                          dtype=int)
print(counts.shape)
print(gene_lengths.shape)

total_counts = np.sum(counts, axis=0)
density = stats.kde.gaussian_kde(total_counts)
x = np.arange(min(total_counts), max(total_counts), 10000)
# Make the density plot
fig, ax = plt.subplots()
ax.plot(x, density(x))
ax.set_xlabel("Total counts per individual")
ax.set_ylabel("Density")
plt.show()

print(f'Count statistics:\n  min:  {np.min(total_counts)}'
      f'\n  mean: {np.mean(total_counts)}'
      f'\n  max:  {np.max(total_counts)}')
# Subset data for plotting
np.random.seed(seed=7) # Set seed so we will get consistent results
# Randomly select 70 samples
samples_index = np.random.choice(range(counts.shape[1]), size=70, replace=False)
counts_subset = counts[:, samples_index]
# Bar plot of expression counts by individual
fig, ax = plt.subplots(figsize=(4.8, 2.4))

with plt.style.context('ggplot'):
    ax.boxplot(np.log(counts_subset + 1))
    ax.set_xlabel("Individuals")
    ax.set_ylabel("log gene expression counts")
    reduce_xaxis_labels(ax, 5)
    plt.show()