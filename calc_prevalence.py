import pandas as pd

def run_reconciliation():
    try:
        df = pd.read_csv('execution_plan_results.csv')
        
        # CRITICAL FILTER: Only include CFTR variants
        # We look for the 3120+1G>A or G551D strings specifically
        cf_variants = ['3120+1G>A', 'G551D', 'Other_Pathogenic']
        df_cf = df[df['Mutation_Name'].isin(cf_variants)]
        
        q_total = df_cf['AF_afr'].fillna(0).sum()
        p = 1 - q_total
        
        prevalence = q_total**2
        carrier_rate = 2 * p * q_total
        
        print("--- Genomic Equity Audit: CFTR (AFR Cohort) ---")
        print(f"Variants Analyzed:    {len(df_cf)}")
        print(f"Total CF Risk (q):    {q_total:.6f}")
        print(f"Carrier Frequency:     1 in {int(1/carrier_rate) if carrier_rate > 0 else 0}")
        print(f"Predicted Prevalence:  1 in {int(1/prevalence) if prevalence > 0 else 0}")
        print(f"Affected per 100k:    {prevalence * 100000:.2f}")

    except Exception as e:
        print(f"Pipeline Error: {e}")

if __name__ == "__main__":
    run_reconciliation()
