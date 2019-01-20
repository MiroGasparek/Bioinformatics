def PatternCount(Text, Pattern):
	"""
	Counts the number of occurences of string Pattern
	in the template Text.
	------
	Inputs: 
	------
	Text(string): A sequence in which the pattern should be searched for.
	Pattern(string): A sequence that is being searched for in 'Text'.
	------
	Outputs:
	-------
	count(string): Number of occurences of the Pattern in String.
	"""

	count = 0

	lT = len(Text)
	lP = len(Pattern)

	for i in range(lT - lP + 1):
		if Text[i:i+lP] == Pattern:
			count = count+1

	return count