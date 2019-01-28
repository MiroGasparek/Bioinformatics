import itertools

def PatternToNumber(Pattern):
	"""
	Computes the frequency array
	------
	Inputs: 
	------
	Pattern(string): A nucleotide sequence for which the frequency array
	is to be determined
	------
	Outputs:
	-------
	kmer_ind(int): Integer with the lexicographic position of the given
	k-mer.
	"""
	# Initialize the empty variables
	kmer_list = list(range(4**(len(Pattern))))

	# Make all the permutations of length of Pattern using the nucleotides
	kmer_list = [''.join(map(str, i)) for i in itertools.product(['A','C','T','G'], repeat=len(Pattern))]

	# Sort the list lexicographically
	kmer_list.sort()
	# Get the index of the Pattern
	kmer_ind = kmer_list.index(Pattern)

	return kmer_ind


