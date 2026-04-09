import matplotlib.pyplot as plt

# Data
populations = ['African (Calculated)', 'European (Benchmark)']
prevalence_rates = [1/39681, 1/3000] # Standard EUR prevalence is approx 1 in 3,000
labels = ['1 in 39,681', '1 in 3,000']

# Plotting
plt.figure(figsize=(10, 6))
bars = plt.bar(populations, [p * 100000 for p in prevalence_rates], color=['#2ca02c', '#d62728'])
plt.ylabel('Affected individuals per 100,000')
plt.title('Cystic Fibrosis Predicted Prevalence: AFR vs EUR')

# Adding labels
for bar, label in zip(bars, labels):
    height = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/2., height + 0.5, label, ha='center', va='bottom', fontweight='bold')

plt.savefig('prevalence_comparison.png')
print("Report generated: prevalence_comparison.png")
