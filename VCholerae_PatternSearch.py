from PatternMatching import PatternMatching
import os, sys

# The script reads in the genome of Vibrio cholerae and returns
# a space-separated list of nucleotide sequence 'CTTGATCAT'

# Read in the V. cholerae genome
with open('Vibrio_cholerae.txt', 'r') as file:
	Genome = file.read().replace('\n','')

# Get the pattern for which we need to search
Pattern = 'CTTGATCAT'

# Return list of starting positions
match = PatternMatching(Pattern, Genome)

# How many times does the pattern occur in the genome?
print("""Nucleotide sequence {} appears {} times in V. cholerae genome.""".format(Pattern, len(match)))
# Make the list comma separated
match_str = ' '.join(map(str, match))