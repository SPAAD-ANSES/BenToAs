# Import necessary modules
import os, re

# Get input and output file paths from Snakemake variables 
fasta_files = snakemake.input.fasta
output_files = snakemake.output.genome_lists

# List of prefixes used to classify the .fa files (based on species names)
prefixes = ['Bacillus', 'Brucella', 'Vibrio_cholerae', 'Vibrio_parahaemolyticus', 'Xylella', 'Yersinia', 'Salmonella', 'Staphylococcus', 'Listeria', 'Burkholderia', 'Campylobacter', 'Clostridium', 'E_coli', 'Klebsiella', 'Leptospira', 'Mycobacterium', 'Neisseria', 'Pseudomonas', 'Taylorella_asini', 'Taylorella_equi','Ralstonia']

# Initialize a dictionary to store files for each prefix
files_dict = {prefix: [] for prefix in prefixes}

# Loop through each FASTA file to classify them based on the prefix
for fasta_file in fasta_files:
    # Extract the filename from the full path
    basename = os.path.basename(fasta_file)

    # Try to infer the prefix based on the filename structure (separated by underscores "_")    
    prefix = "_".join(basename.split('_')[:-3]).capitalize()


    # If the final prefix is valid
    if prefix in files_dict:
        files_dict[prefix].append(fasta_file)
    else:
        # If the prefix doesn't match any known prefixes, print a warning
        print(f"Prefix for cgMLST schema not recognize {basename}: {prefix}")

# Create and write genome list files for each prefix
for prefix, files in files_dict.items():
    output_file = os.path.join(os.path.dirname(snakemake.output.genome_lists[0]), f'genome_list_{prefix}.txt')

    # Write the list of files for the prefix to the output file
    with open(output_file, 'w') as out:
        for file in files:
            out.write(file + '\n')

    # Print a message indicating how many files were written to the genome list
    print(f"Write  {len(files)} files in  {output_file}")