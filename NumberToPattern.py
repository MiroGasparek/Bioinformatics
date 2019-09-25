import itertools

def NumberToPattern(index, k):
	"""
	Returns the nucleotide sequence at position index,
	given the length of the k-mer 'k'.
	------
	Inputs: 
	------
	index(int): position of the nucl. seq. in the frequency array
	k(int): length of the desired k-mer
	------
	Outputs:
	-------
	seq(string): the nucleotide sequence of the lexicographically
	ordered k-mers at the position index.
	"""
	# Initialize the empty variables
	kmer_list = list(range(4**(k)))

	# Make all the permutations of length of Pattern using the nucleotides
	kmer_list = [''.join(map(str, i)) for i in itertools.product(['A','C','T','G'], repeat=k)]

	# Sort the list lexicographically
	kmer_list.sort()


	# Get the nucleotide at the given position
	# indexing from 0
	seq = kmer_list[index]

	return seq


