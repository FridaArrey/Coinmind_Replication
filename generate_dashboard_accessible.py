import pandas as pd
import matplotlib.pyplot as plt

# Set backend to Agg for headless environments (prevents GUI errors)
import matplotlib
matplotlib.use('Agg')

# 1. Dynamic Data Loading
try:
    df = pd.read_csv('execution_plan_results.csv')
    # Filter for CFTR variants only to avoid 'Super-Disease' inflation
    cf_vars = ['3120+1G>A', 'G551D', 'Other_Pathogenic']
    q_afr = df[df['Mutation_Name'].isin(cf_vars)]['AF_afr'].sum()
except Exception as e:
    print(f"Data Error: {e}. Falling back to baseline.")
    q_afr = 0.00502

# 2. Genomic Math
afr_prevalence = q_afr**2
afr_carrier = 2 * (1 - q_afr) * q_afr

# Comparison Benchmarks (AFR vs EUR)
populations = ['African (AFR)', 'European (EUR)']
prevalence_rates = [afr_prevalence, 1/3000] 
carrier_rates = [afr_carrier, 1/28]

# 3. Visualization Setup (Wong Palette & Double-Encoding)
# Blue: #0072B2, Orange: #E69F00
safe_colors = ['#0072B2', '#E69F00']
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 6))
fig.suptitle('Accessible Health Equity Dashboard: CFTR Variant Burden', fontsize=16, fontweight='bold')

# Panel 1: Disease Prevalence
bars1 = ax1.bar(populations, [p * 100000 for p in prevalence_rates], color=safe_colors)
bars1[0].set_hatch('//') # Double-encoding for accessibility
bars1[1].set_hatch('..')
ax1.set_title('Predicted Disease Prevalence\n(Affected per 100,000)', fontsize=12)
ax1.set_ylabel('Individuals')

# Panel 2: Carrier Frequency
bars2 = ax2.bar(populations, [c * 100 for c in carrier_rates], color=safe_colors)
bars2[0].set_hatch('//')
bars2[1].set_hatch('..')
ax2.set_title('Carrier Frequency\n(Percentage of Population)', fontsize=12)
ax2.set_ylabel('Percentage (%)')

# 4. Annotation Logic
for ax, rates in zip([ax1, ax2], [prevalence_rates, carrier_rates]):
    for i, bar in enumerate(ax.patches):
        if ax == ax1:
            label = f'1 in {int(1/rates[i]):,}'
        else:
            label = f'{rates[i]*100:.1f}%'
        ax.text(bar.get_x() + bar.get_width()/2, bar.get_height() + (bar.get_height() * 0.05), 
                label, ha='center', va='bottom', fontweight='bold')

plt.tight_layout(rect=[0, 0.03, 1, 0.95])
plt.savefig('health_equity_dashboard_accessible.png', dpi=300)
print("Success: Dynamic Dashboard generated as health_equity_dashboard_accessible.png")
