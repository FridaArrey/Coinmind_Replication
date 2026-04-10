import pandas as pd

def calculate_adjusted_prevalence(q, f_stat=0.01):
    """
    Adjusts Hardy-Weinberg for non-random mating (Endogamy/Consanguinity).
    Formula: q^2 + Fpq
    """
    p = 1 - q
    prev_adjusted = (q**2) + (f_stat * p * q)
    return prev_adjusted

def run_blood_audit():
    try:
        df = pd.read_csv('execution_plan_results.csv')
        
        # 1. G6PD (X-Linked Logic)
        g6pd_q = df[df['Mutation_Name'] == 'G202A_G6PD']['AF_afr'].values[0]
        
        # 2. Sickle Cell / Hemoglobinopathy (Autosomal Logic)
        scd_vars = ['HbS_Sickle_Cell', 'HbC_Variant']
        scd_q = df[df['Mutation_Name'].isin(scd_vars)]['AF_afr'].sum()

        print("--- Advanced Blood Disorder Audit: AFR Cohort ---")
        print("Note: Incorporating F-statistics to address HWE critiques.")
        
        # G6PD Output (X-linked frequency is q in males regardless of F)
        print(f"\n[G6PD Deficiency - X-Linked]")
        print(f"Male Prevalence (q):   1 in {int(1/g6pd_q)}")
        print(f"Female Affected (q^2): 1 in {int(1/(g6pd_q**2))}")

        # Sickle Cell Output with Sensitivity Analysis
        print(f"\n[Sickle Cell / HbC - Sensitivity Analysis]")
        print(f"Total Pathogenic Burden (q): {scd_q:.4f}")
        
        for f in [0, 0.01, 0.05]:
            label = "Random Mating (HWE)" if f == 0 else f"Endogamy Level F={f}"
            adj_prev = calculate_adjusted_prevalence(scd_q, f)
            print(f"  > {label.ljust(20)}: 1 in {int(1/adj_prev)}")

    except Exception as e:
        print(f"Audit Error: {e}")

if __name__ == "__main__":
    run_blood_audit()
