[Genomic Health Equity Pipeline.md](https://github.com/user-attachments/files/26601230/Genomic.Health.Equity.Pipeline.md)
# **Genomic Health Equity Pipeline**

### ***A Coinmind Replication & Extension for Underrepresented Populations***

This project replicates the award-winning **Coinmind** methodology to estimate the prevalence of genetic diseases in African populations using high-resolution population sequencing data (**gnomAD v4.0**). By pivoting from European-centric benchmarks to population-specific allele frequencies, this pipeline identifies diagnostic "blind spots" in global health.

## **🧬 Core Methodology: The "Equity" Logic**

Most clinical genetic panels are optimized for European cohorts. This pipeline recalibrates risk by:

1. **Targeting Population-Specific Variants:** Focusing on variants like rs28942205 ($3120+1G\>A$) which are prevalent in African ancestry but rare elsewhere.  
2. **Accounting for Compound Heterozygosity:** Calculating the probability of an individual carrying one common regional variant and one rare "private" mutation—a major source of misdiagnosis.  
3. **Multi-Model Support:** Applying Hardy-Weinberg for autosomal recessive traits (CF, Sickle Cell) and hemizygous modeling for X-linked traits (G6PD).

## **🛠 Project Structure**

Bash  
.  
├── calc\_prevalence.py          \# Core logic for CFTR risk modeling  
├── run\_blood\_disorders.py      \# Extension script for HBB and G6PD  
├── generate\_dashboard.py       \# Accessible, colorblind-friendly visualizations  
├── execution\_plan\_results.csv  \# Validated scientific ledger (AFR frequencies)  
└── README.md                   \# Project documentation

## **📊 Benchmarked Results**

The pipeline was tested across three distinct genetic architectures within the African (AFR) cohort:

| Disorder | Frequency Model | Key Variant | Predicted Prevalence |
| :---- | :---- | :---- | :---- |
| **Cystic Fibrosis** | Rare/Drift | rs28942205 | **1 in 39,681** |
| **Sickle Cell (SCD)** | Balancing Selection | rs334 (HbS) | **1 in 104** |
| **G6PD Deficiency** | X-Linked | rs1050828 | **1 in 8 (Males)** |

## **🚀 Key Technical Features**

* **Infrastructure Resilience:** Developed a "Local-First" data injection strategy to bypass cloud API 503 errors during high-traffic periods.  
* **Accessibility-First Design:** All visualizations utilize the **Wong Palette** and double-encoding (hatch patterns) for colorblind accessibility.  
* **ClinVar Validation:** Every variant in the ledger is cross-referenced for pathogenicity (2-star minimum evidence).

## **💡 How to Run**

1. **Update the Ledger:** Add new rsIDs and frequencies to execution\_plan\_results.csv.  
2. **Execute Analysis:**  
   Bash  
   python3 calc\_prevalence.py  
3. **Generate Dashboard:**  
   Bash  
   python3 generate\_dashboard\_accessible.py  
   

## **🎓 Author**

**Frida Arrey, PhD, MSc** *Data Analytics & Life Science AI Consultant* Specializing in Immunological Research and Public Health Data Integrity.

---

*This project is a replication of the Coinmind study (Lemanic Hackathon 2025\) and serves as a framework for inclusive genomic diagnostics.*

