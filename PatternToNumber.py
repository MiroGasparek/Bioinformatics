def SymbolToNumber(base):
    """
    Transforms the base into respective integer:
    A -> 0
    C -> 1
    G -> 2
    T -> 3
    -------
    Inputs:
    -------
    base(string): A nucleotide that is last in the string of nucleotides to be transformed
    -------
    Outputs:
    -------
    A number corresponding to the given base.
    """
    
    # Define a simple dictionary of bases and select one usint get() method
    # for Python dictionary
    base_dict = {'A':0, 'C':1, 'G':2, 'T':3}
    return base_dict.get(base)

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
    Integer with the lexicographic position of the given k-mer.
    """
    # If pattern contains no symbols return zero
    if Pattern == "":
        return 0
    
    # Get the terminal nucleotide
    symbol = Pattern[-1]
    # Get the previous pattern
    prefix = Pattern[:-1]

    return 4*PatternToNumber(prefix) + SymbolToNumber(symbol)