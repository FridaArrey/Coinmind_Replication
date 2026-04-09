import matplotlib.pyplot as plt
import numpy as np

# Data (Based on your terminal runs)
disorders = ['G6PD (Male affected)', 'SCD (HbS+HbSC Total)', 'CF (Affected total)']
prevalence_raw = [1/8, 1/104, 1/39681] # Prevalence
populations_affected = [p * 100 for p in prevalence_raw]

# Colorblind-safe palette (Wong Palette)
# Orange, Blue, Green
safe_colors = ['#E69F00', '#56B4E9', '#009E73']

# Plot Setup
plt.figure(figsize=(12, 7))
plt.suptitle('Health Equity Dashboard: Genomic Burden Comparison', fontsize=16, fontweight='bold')

# Main comparative plot (Log Scale)
bars = plt.bar(disorders, populations_affected, color=safe_colors)
plt.ylabel('Affected individuals (%)', fontsize=12)
plt.title('Common Condition vs. Rare Disease Frequencies (Log Scale)', fontsize=13)

# Add texture/hatch for double encoding (grayscale accessible)
bars[0].set_hatch('//')
bars[1].set_hatch('..')
bars[2].set_hatch('x')

# Add Labels
for bar, raw_p in zip(bars, prevalence_raw):
    height = bar.get_height()
    # For very low heights, place the label above
    label_y = height + 1 if height > 0.05 else height + 0.1
    plt.text(bar.get_x() + bar.get_width()/2, label_y,
             f'1 in {int(1/raw_p):,}', ha='center', va='bottom', fontweight='bold', fontsize=10)

# Set Y-axis to Log Scale to visualize the massive difference
plt.yscale('log')
plt.yticks([0.001, 0.01, 0.1, 1, 10, 100], ['0.001%', '0.01%', '0.1%', '1%', '10%', '100%'])
plt.grid(axis='y', which='both', linestyle='--', alpha=0.5)

plt.tight_layout(rect=[0, 0.03, 1, 0.95])
plt.savefig('disorder_comparison.png')
print("Comparison generated: disorder_comparison.png")
