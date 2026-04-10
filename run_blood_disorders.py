import pandas as pd

def run_blood_audit():
    try:
        df = pd.read_csv('execution_plan_results.csv')
        
        # 1. G6PD (X-Linked Logic)
        g6pd_q = df[df['Mutation_Name'] == 'G202A_G6PD']['AF_afr'].values[0]
        
        # 2. Sickle Cell (Autosomal Recessive Logic)
        # We sum HbS and HbC for a total "Hemoglobinopathy" risk
        scd_vars = ['HbS_Sickle_Cell', 'HbC_Variant']
        scd_q = df[df['Mutation_Name'].isin(scd_vars)]['AF_afr'].sum()

        print("--- Blood Disorder Equity Audit: AFR Cohort ---")
        
        # G6PD Output
        print(f"\n[G6PD Deficiency - X-Linked]")
        print(f"Male Prevalence:   1 in {int(1/g6pd_q)}")
        print(f"Female Affected:   1 in {int(1/(g6pd_q**2))}")
        print(f"Female Carriers:   1 in {int(1/(2 * (1-g6pd_q) * g6pd_q))}")

        # Sickle Cell Output
        scd_prev = scd_q**2
        print(f"\n[Sickle Cell / Hemoglobinopathies - Autosomal]")
        print(f"Carrier Frequency: 1 in {int(1/(2 * (1-scd_q) * scd_q))}")
        print(f"Predicted Prevalence: 1 in {int(1/scd_prev)}")

    except Exception as e:
        print(f"Audit Error: {e}")

if __name__ == "__main__":
    run_blood_audit()
