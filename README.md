# BenToAs

## Author
**D. Merda**  
Affiliation: **SPAAD**

## Project Description

This project benchmarks **de novo assembly** using **Shovill**, **SPAdes** or **Unicycler** and **core genome multilocus sequence typing (cgMLST)** analysis with **chewBBACA**. The workflow is developed to process bacterial genome sequencing data, perform genome assembly, and compute cgMLST profiles for various species. 

**Date:** September 2024  
**Conda Environment:** `BenToAs`

---

## Workflow Overview

The pipeline is built using **Snakemake** and includes the following steps:

1. **De novo assembly** of paired-end sequencing reads using **Shovill**, **SPAdes** or **Unicycler**.

2. **Preparation** of input files for cgMLST analysis.

3. **Allele calling** using **chewBBACA** for cgMLST profiling.

4. **Distance matrix** and **phylogenetic tree** generation using chewBBACA.

The workflow is configured to handle multiple bacterial species, using predefined **prefixes** and database schemes specified in the configuration file.

---

## Installation and Setup

1. **Clone the repository**:
   ```bash
   git clone https://github.com/SPAAD-ANSES/BenToAs.git
   cd BenToAs

2. **Set up the conda environment**:
   ```
   conda env create -f envs/BenToAs.yaml
   ```

3. **Activate the environment**:
   ```
   conda activate BenToAs
	 ```  

4. **Run the workflow: Execute the workflowwith Snakemake using following command**:
   ```
   snakemake -s snakemake_shovill_chewbbaca.py --stats time.json --cores 4 --latency-wait 60 --use-conda --conda-prefix . --conda-frontend conda
   snakemake -s snakemake_unicycler_chewbbaca.py --stats time.json --cores 4 --latency-wait 60 --use-conda --conda-prefix . --conda-frontend conda
   snakemake -s snakemake_spades_chewbbaca.py --stats time.json --cores 4 --latency-wait 60 --use-conda --conda-prefix . --conda-frontend conda
   ```
---

## Input Data

The workflow processes paired-end FASTQ files (compressed as .fq.gz), which should be placed in the base directory defined in the configuration (config.yaml).

Exemple FASTQ file structure:
   ```
   <PATH_TO_READS>
   ├── sample1_75X_GQ_1.fq.gz
   ├── sample1_75X_GQ_2.fq.gz
   ├── sample2_75X_GQ_1.fq.gz
   └── sample2_75X_GQ_2.fq.gz
The workflow will automatically detect samples based on this file structure. 
	 ```
---

## Output Data

1. **De novo assembled contigs** (FASTA files for each sample):
Located in: assemblage_assembleur/{sample}_75X_assembleur/{sample}_75X_assembleur.fa

2. **cgMLST analysis results** for each bacterial species (prefix):
- alleles.tsv : allele calls
- contigsInfo.tsv : information about contigs
- statistics.tsv : summary statistics of the analysis

3. **Distance matrix** (alleles.dist) and **phylogentic tree** (alleles.tre) generated from the allele calls.

---

## Configuration

The workflow uses a YAML configuration file (config.yaml) to define key parameters, including paths to input data, output directories, and database locations for each bacterial species' cgMLST schem

** Sample configuration (config.yaml)**:
   ```yaml
   # Base directories
   paths:
     BASE_DIR: "<PATH_TO_READS>"
     WDIR: "<PATH_TO_WRITE_RESULTS>"
     dataset_dir: "{BASE_DIR}/dataset1"

   # List of species prefixes to process
   prefixes:
     - Bacillus
     - Brucella
     - Vibrio_cholerae
     ...

   # Database paths for cgMLST
   db:
     cgMLST:
       Bacillus: "<PATH_TO_cgMLST_SCHEMA>"
       ...

---

## Rules

The workflow is composed of the following main rules:

1. **Shovill assembly** (shovill) **or SPAdes assembly** (spades) **or Unicycler assembly** (unicycler):
- Assembles reads into contigs
- Input: Paired-end FASTQ files
- Output: Assembled contigs in FASTA format

2. **chewBBACA preparation** (chewbbaca_prepare):
Prepares the input for cgMLST analysis based on species-specific genome lists.

3. **Allele calling** (chewbbaca_allele):
Runs chewBBACA allele calling for each species.

4. **Distance matrix calcultation** (chewbbaca_dist):
Computes distance matrices from allele profiles.

5. **Phylogenetic tree generation (chewbbaca_tree):
Constructs phylogenetic trees in Newick format.

---

## Dependencies

- **Shovill**, **SPAdes** or **Unicycler** for genome assembly.

- **chewBBACA** for cgMLST profiling.

- **Grapetree** for distance and phylogenetic tree generation.

- Python libraries (for data handling) sush as **pandas**.

- Conda for environment and dependency management.

All dependencies are managed through Conda environments, which are defined in .yaml files included in the repository.

---

## References


---

## License


---
