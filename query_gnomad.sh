#!/bin/bash

# Define the variants
VARIANTS='["rs28942205", "rs75527207"]'

echo "Attempting a lighter query for gnomAD r4 AFR data..."

# Using a more robust GraphQL structure for v4
curl -X POST https://gnomad.broadinstitute.org/api \
-H "Content-Type: application/json" \
-d "{
  \"query\": \"{ variants(rsids: $VARIANTS, dataset: gnomad_r4) { rsid genome { freq { population(name: \\\"afr\\\") { al_freq: allele_frequency } } } } }\"
}" | jq '.'
