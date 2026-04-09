import pandas as pd

# We will populate this with the data from the agent
data = {
    'variant': ['3120+1G>A', 'G551D', 'Others'],
    'q_af_afr': [0.0042, 0.00002, 0.0008] # Placeholders for agent output
}

df = pd.DataFrame(data)
q_total = df['q_af_afr'].sum()
p = 1 - q_total

prevalence = q_total**2
affected_per_100k = prevalence * 100000

print(f"Total Pathogenic Frequency (q): {q_total:.6f}")
print(f"Estimated Prevalence: 1 in {int(1/prevalence) if prevalence > 0 else 0}")
print(f"Affected per 100,000: {affected_per_100k:.2f}")
