# Genomic Health Equity Pipeline
### A Coinmind Replication & Extension for Underrepresented Populations

This project replicates and extends the award-winning **Coinmind** methodology to estimate the prevalence of genetic diseases in African populations using high-resolution population sequencing data (**gnomAD v4.1/2026**). By pivoting from European-centric benchmarks to population-specific allele frequencies, this pipeline identifies diagnostic "blind spots" and quantifies the health equity gap.

## 🧬 Core Methodology: The "Equity" Logic

Most clinical genetic panels are optimized for European cohorts. This pipeline recalibrates risk by:
* **Targeting Population-Specific Variants:** Focusing on variants like `rs28942205` (3120+1G>A) which are prevalent in African ancestry but virtually absent in European standard panels.
* **Accounting for Genetic Architecture:** Moving beyond simple counting to model diverse inheritance patterns:
    * **Autosomal Recessive (Rare):** CFTR risk modeling.
    * **Autosomal Recessive (High-Frequency):** Sickle Cell modeling with **F-statistic adjustments** for population structure.
    * **X-Linked (Hemizygous):** Distinct modeling for G6PD prevalence in males vs. females.

## 🛠 Project Structure

```bash
.
├── calc_prevalence.py          # Core logic for CFTR risk modeling
├── run_blood_disorders.py      # X-linked (G6PD) and HBB Sensitivity Analysis
├── generate_dashboard.py       # Accessible, colorblind-friendly visualizations
├── execution_plan_results.csv  # Validated scientific ledger (AFR frequencies)
└── README.md                   # Project documentation


## 📊 Benchmarked Results (AFR Cohort)

| Disorder | Inheritance | Model Type | Predicted Prevalence |
| :--- | :--- | :--- | :--- |
| **Cystic Fibrosis** | Autosomal Rec. | Rare/Drift | 1 in 39,681 |
| **G6PD Deficiency** | X-Linked | Hemizygous | 1 in 8 (Males) |
| **Sickle Cell (SCD)** | Autosomal Rec. | HWE (F=0) | 1 in 99 |
| **Sickle Cell (SCD)** | Autosomal Rec. | **Endogamy (F=0.05)** | **1 in 68** |

---

## 🚀 Key Technical Features

* **X-Linked Logic:** Correctly models male prevalence as $q$, identifying significant gender-based diagnostic gaps.
* **Accessibility:** Visuals utilize the **Wong Palette** and double-encoding (hatch patterns) for colorblind safety.
* **Sensitivity Modeling:** Incorporates $F$-statistics to address the "Hardy-Weinberg Critique" in populations with high endogamy.
* **Scientific Integrity:** All variants cross-referenced via ClinVar for pathogenic evidence (2-star minimum).

---

## 💡 How to Run

1. **Update the Ledger:** Add new rsIDs to `execution_plan_results.csv`.
2. **Execute Audit:**
   ```bash
3. **Generate Dashboard:**  
   Bash  
   python3 generate\_dashboard\_accessible.py  
   

## **🎓 Author**

**Frida Arrey, PhD, MSc** *Data Analytics & Life Science AI Consultant* Specializing in Immunological Research and Public Health Data Integrity.

---

*This project is a replication of the Coinmind study (Lemanic Hackathon 2025\) and serves as a framework for inclusive genomic diagnostics.*

