def ClumpFinding(genome, k, L, t):
	"""
	Finds patterns forming clumps in a string.	
	------
	Inputs: 
	------
	- genome(string): A nucleotide sequence in which
	clumps are to be found
	- k(int): length of k-mer forming (L,t) clumps in genome

	- Genome(string): A nucleotide sequence within which
	the occurences of the patern should be searched for
	------
	Outputs:
	-------
	match_ind(list): All starting positions where Pattern 
	appears as a substring of Genome
	"""

	# Convert Pattern into the upper case letters,
	# just in case
	Pattern = Pattern.upper()
	

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
