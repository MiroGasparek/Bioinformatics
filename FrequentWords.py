from PatternCount import PatternCount

def FrequentWords(Text, k):
	"""
	Find the most frequent k-mers in a string
	------
	Inputs: 
	------
	Text(string): A sequence in which the k-mers should be searched for.
	k(int): length of the k-mer
	------
	Outputs:
	-------
	FrequentPatterns(string): Lengths of the most frequent k-mers.
	"""

	# Initialize the empty variables
	FrequentPatterns = list()
	Count = list()

	# Get the text length
	lT = len(Text)

	# Iterate over the 'Text' to find the patterns of k-mer length
	for i in range(lT - k):
		Pattern = Text[i:i+k]
		Count.append(PatternCount(Text, Pattern))

	# Get the longest pattern
	maxCount = max(Count)

	# Iterate over the 'Text' to find the longest patterns
	# and store them to the list 
	for j in range(lT-k):
		if Count[j] == maxCount:
			FrequentPatterns.append(Text[j:j+k])
			print(FrequentPatterns)

	# Remove duplicates
	FrequentPatterns = list(set(FrequentPatterns))
	print(FrequentPatterns)
	return FrequentPatterns

