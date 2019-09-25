from PatternCount import PatternCount
from collections import Counter

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
	- t(int): Number of times that clump occurs within the window
	------
	Outputs:
	-------
	kmer_list (list): All distinct k-mers forming (L,t)-clumps in Genome
	"""

	# Get the length of the genome
	gL = len(genome)

	# Define empty list of kmers to be outputted
	kmer_list = list()

	# Get the most frequent kmers 
	freq_kmers = list()

	# Iterate over the frequency array
	for i in range(gL+1 - L):

		count = list()
		freq_kmers = list()
		# freq_kmers = list()
		Text = genome[i:i+L]
		# Iterate over the 'Text' to find the patterns of k-mer length
		for j in range(L+1 - k):
			# Get the pattern of length k
			Pattern = Text[j:j+k]
			# Count the number of occurences in the string 'Text'
			count.append(PatternCount(Text, Pattern))
			max_count = max(count)

		# Loop over the string to get the patterns of the 
		# prescribed length with most occurences
		for m in range(L+1 - k):
			if count[m] == max_count:
				freq_kmers.append(Text[m:m+k])

		# Flatten the list of lists 'count_list'
		flat_list = [item for sublist in freq_kmers for item in sublist]

		# Use counter to get the dictionary where each kmer
		# is a key and number of occurences in the string
		# 'genome' is a value
		kmer_dict = Counter(freq_kmers)

		# Loop over the dictionary of and only select the kmers
		# that appear 't' times or more
		for kmer, count in kmer_dict.items():
			if count >= t:
				kmer_list.append(kmer)

		# Remove duplicates from the list
		kmer_list= list(set(kmer_list))
		kmer_list.sort()


	return kmer_list