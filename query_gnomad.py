import requests
import json

def query_gnomad(gene_symbol):
    url = "https://gnomad.broadinstitute.org/api"
    # gnomAD v4 uses reference_genome: GRCh38
    query = """
    query GetGene($gene_symbol: String!) {
      gene(gene_symbol: $gene_symbol, reference_genome: GRCh38) {
        variants(dataset: gnomad_r4) {
          variant_id
          rsids
          exome {
            populations { id af ac an }
          }
          genome {
            populations { id af ac an }
          }
        }
      }
    }
    """
    variables = {"gene_symbol": gene_symbol}
    response = requests.post(url, json={"query": query, "variables": variables})
    if response.status_code == 200:
        return response.json()
    else:
        raise Exception(f"Query failed with status code {response.status_code}: {response.text}")

try:
    data = query_gnomad("CFTR")
    variants = data['data']['gene']['variants']

    # Target mutations we identified:
    # 3120+1G>A (rs75096551)
    # G551D (rs75527207)
    # The user also asked for rs28942205 (which search suggests might be linked to rs75527207 in older nomenclature or a different variant)
    target_rsids = ["rs28942205", "rs75527207", "rs75096551"]
    results = []

    for v in variants:
        found_rsid = None
        if v['rsids']:
            for r in v['rsids']:
                if r in target_rsids:
                    found_rsid = r
                    break
        
        if found_rsid:
            # Extract AFR frequency
            afr_info = None
            # Combine genome and exome for gnomad_r4 if necessary, or just extract both
            for source in ['genome', 'exome']:
                if v[source] and v[source]['populations']:
                    for pop in v[source]['populations']:
                        if pop['id'] == 'afr':
                            afr_info = pop
                            break
                if afr_info: break
            
            results.append({
                'variant_id': v['variant_id'],
                'rsids': v['rsids'],
                'af_afr': afr_info['af'] if afr_info else 0,
                'ac_afr': afr_info['ac'] if afr_info else 0
            })

    print(json.dumps(results, indent=2))
except Exception as e:
    print(f"Error: {e}")
