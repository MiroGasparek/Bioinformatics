import itertools

def ReverseComplement(Pattern):
	"""
	Computes the reverse complement of a DNA Patternuence
	------
	Inputs: 
	------
	Pattern(string): A nucleotide Patternuence for which the reverse complement
	strand is to be determined, direction is 5' to 3'
	------
	Outputs:
	-------
	rev_compl(string): A nucleotide Patternuence representing the reverese
	complement of the original strand.
	"""
	# Convert Patternuence into the upper case letters
	Pattern = Pattern.upper()
	rev_compl = []

	for ind in range(len(Pattern)):

		if Pattern[ind] == 'A':
			rev_compl.append('T')

		elif Pattern[ind] == 'T':
			rev_compl.append('A')

		elif Pattern[ind] == 'C':
			rev_compl.append('G')

		elif Pattern[ind] == 'G':
			rev_compl.append('C')

	rev_compl.reverse()
	rev_compl_str = ''.join(map(str, rev_compl))

	return rev_compl_str

