def CheckClumpLength(clump, L, t, k):
    """
    Check if the set of t k-mers fits within the length L.
    -------
    Inputs:
    -------
    - clump(string): A sequence within which t k-mers should fit.
    - L(int): Length of the sequence within which t k-mers should fit
    - t(int): Number of k-mers falling into the sequence clump within length L
    - k(int): Length of the k-mer
    -------
    Outputs:
    - (Bool): Logical value
    """
    for i in range(len(clump)-t+1):
        if clump[t+i-1] - clump[i] <= L-k:
            return True
        
    return False

def FastClumpFinding(genome, k, L, t):
    """
    Finds patterns forming clumps in a string.
    The "clump" is defined as the k-mer that occurs in the genome segment
    of length L at least t times.
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

    # Define an empty dictionary for storing k-mers
    kmer_dict = {}
    
    # Define an empty list of output clumps
    kmers_out = []
    
    # Iterate over the genome length
    for i in range(len(genome)-k+1):
        # Test if the given k-mer exists in dict, if yes, increase the count
        # for the given k-mer and also store the starting index of the k-mer
        # If k-mer is not yet in the dictionary, create a new key for the k-mer and add to count
        if genome[i:i+k] in kmer_dict:
            
            kmer_dict[genome[i:i+k]][0] += 1
            kmer_dict[genome[i:i+k]][1].append(i)
            
        else:
            kmer_dict[genome[i:i+k]] = [1, [i]]
    # Check the if the candidate k-mers appear at least t-times, 
    # and check their indicies (where they appear)
    kmer_list = [ [kmer[0], kmer[1][1]] for kmer in kmer_dict.items() if kmer[1][0] >= t]
    
    # Only pick those k-mers of which at least t fall within a sequence of length L    
    for kmer_c in kmer_list:
        if CheckClumpLength(kmer_c[1], L, t, k):
            kmers_out.append(kmer_c[0])
    
    return sorted(kmers_out)