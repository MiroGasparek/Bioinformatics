from PatternCount import PatternCount

def FrequentWords(Text, k):
	"""
	Find all the most frequent k-mers in a string
	------
	Inputs: 
	------
	Text(string): A sequence in which the k-mers should be searched for.
	k(int): length of the k-mer
	------
	Outputs:
	-------
	freq_kmers(string): Lengths of the most frequent k-mers.
	"""

	# Initialize the empty variables
	freq_kmers = list()
	counts = list()

	# Get the text length
	lT = len(Text)

	# Iterate over the 'Text' to find the patterns of k-mer length
	for i in range(lT - k):
		kmer = Text[i:i+k]
		counts.append(PatternCount(Text, kmer))

		# Get the longest pattern
		maxCount = max(counts)
	
	for j in range(lT - k):
		if counts[j] == maxCount:
			freq_kmers.append(Text[j:j+k])

	# Remove duplicates
	freq_kmers = list(set(freq_kmers))
	
	return freq_kmers

