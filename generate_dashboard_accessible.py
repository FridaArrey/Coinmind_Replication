import matplotlib.pyplot as plt

# Data
populations = ['African (AFR)', 'European (EUR)']
prevalence_rates = [1/39681, 1/3000] 
carrier_rates = [1/100, 1/28]

# Colorblind-safe palette (Wong Palette)
# Blue: #0072B2, Orange: #E69F00
safe_colors = ['#0072B2', '#E69F00']

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 6))
fig.suptitle('Accessible Health Equity Dashboard: CFTR Variant Burden', fontsize=16, fontweight='bold')

# Panel 1: Disease Prevalence
bars1 = ax1.bar(populations, [p * 100000 for p in prevalence_rates], color=safe_colors)
# Add texture for double-encoding
bars1[0].set_hatch('//')
bars1[1].set_hatch('..')

ax1.set_title('Predicted Disease Prevalence\n(Affected per 100,000)', fontsize=12)
ax1.set_ylabel('Individuals')

# Panel 2: Carrier Frequency
bars2 = ax2.bar(populations, [c * 100 for c in carrier_rates], color=safe_colors)
# Add texture for double-encoding
bars2[0].set_hatch('//')
bars2[1].set_hatch('..')

ax2.set_title('Carrier Frequency\n(Percentage of Population)', fontsize=12)
ax2.set_ylabel('Percentage (%)')

# Add Labels
for ax, rates in zip([ax1, ax2], [prevalence_rates, carrier_rates]):
    for i, bar in enumerate(ax.patches):
        label = f'1 in {int(1/rates[i]):,}' if ax == ax1 else f'{rates[i]*100:.1f}%'
        ax.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 0.1, 
                 label, ha='center', va='bottom', fontweight='bold')

plt.tight_layout(rect=[0, 0.03, 1, 0.95])
plt.savefig('health_equity_dashboard_accessible.png')
print("Accessible Dashboard generated: health_equity_dashboard_accessible.png")
