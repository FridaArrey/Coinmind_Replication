import pandas as pd

# Data from our previous analysis
q_afr_specific = 0.0042  # rs28942205 (3120+1G>A)
q_rare_sum = 0.00082     # Aggregate of other 2-star pathogenic variants

# Calculation
# Probability of being a compound heterozygote (carrying one of each)
# P(CH) = 2 * q1 * q2
prob_compound_het = 2 * q_afr_specific * q_rare_sum

# Probability of being a simple homozygote (carrying two of the same frequent variant)
# P(Hom) = q1^2
prob_homozygote = q_afr_specific**2

# Total Affected (Total disease prevalence)
total_prevalence = (q_afr_specific + q_rare_sum)**2

# Results
print("-" * 40)
print(f"COMPOUND HETEROZYGOSITY ANALYSIS (AFR)")
print("-" * 40)
print(f"Prob. Compound Het: {prob_compound_het:.8f} (1 in {int(1/prob_compound_het):,})")
print(f"Prob. Homozygote:   {prob_homozygote:.8f} (1 in {int(1/prob_homozygote):,})")
print(f"Total Predicted:    {total_prevalence:.8f} (1 in {int(1/total_prevalence):,})")
print("-" * 40)
print(f"Insight: Compound heterozygotes make up { (prob_compound_het/total_prevalence)*100:.1f}% of affected cases.")
