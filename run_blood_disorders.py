import pandas as pd

# 1. Sickle Cell (HBB) - Autosomal Recessive
q_s = 0.08  # HbS frequency
q_c = 0.02  # HbC frequency

# Calculate Genotypes (Hardy-Weinberg)
ss_anemia = q_s**2
sc_disease = 2 * q_s * q_c
total_scd = ss_anemia + sc_disease

# 2. G6PD Deficiency - X-Linked (Approx)
q_g6pd = 0.116
male_affected = q_g6pd # Hemizygous males

print("-" * 45)
print("SICKLE CELL DISEASE (HBB) PROJECTIONS")
print("-" * 45)
print(f"HbSS (Homozygous): {ss_anemia:.4f} (1 in {int(1/ss_anemia)})")
print(f"HbSC (Compound Het): {sc_disease:.4f} (1 in {int(1/sc_disease)})")
print(f"Total SCD Burden:   {total_scd:.4f} (1 in {int(1/total_scd)})")
print("\n" + "-" * 45)
print("G6PD DEFICIENCY PROJECTIONS (MALE)")
print("-" * 45)
print(f"Affected Males:    {male_affected:.4f} (1 in {int(1/male_affected)})")
