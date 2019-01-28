def PatternMatching(Pattern, Genome):
	"""
	Computes the reverse complement of a DNA Patternuence
	------
	Inputs: 
	------
	- Pattern(string): A nucleotide sequence for which
	the match within the genome should be determined

	- Genome(string): A nucleotide sequence within which
	the occurences of the patern should be searched for
	------
	Outputs:
	-------
	match_ind(list): All starting positions where Pattern 
	appears as a substring of Genome
	"""

	# Convert Pattern and Genome into the upper case letters,
	# just in case
	Pattern = Pattern.upper()
	Genome = Genome.upper()
	

	# Define the starting index
	start = 0
	# Get length of genome and pattern for iteration
	gen_len = len(Genome)
	pat_len = len(Pattern)

	# Define the empty list of matched indices
	match_ind = []

	# Iterate over the Genome string
	for ind in range(gen_len-pat_len+1):

		if Genome[ind:ind+pat_len] == Pattern:
			match_ind.append(ind)


	return match_ind