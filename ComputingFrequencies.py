import itertools
import numpy as np

from PatternToNumber import PatternToNumber

def ComputingFrequencies(Text, k):
    """
    Generates the frequency array by first initializing every
    element in the frequency array to zero (4^k operations) and
    then making a single pass down Text (~ len(Text)*k operations),
    increasing the value of the frequency array counter
    corresponding to Patter for each k-mer Pattern encountered.

    k-mer beginning at position i of Text:= Text(i,k)
    ------
    Inputs: 
    ------
    Text(string): A DNA string for which the frequency array
    is computed.
    k(int): k-mer length
    ------
    Outputs:
    -------
    FrequencyArray(list): The frequency array of the given k-mer.
    """

    # Define the frequency array of zeros with predetermined length
    FrequencyArray = []
    for x in range(4**k):
        FrequencyArray.append(0)
        
    # Iterate over the length of the genome to fill the frequency array
    for i in range(len(Text) - (k-1)):

        text_pat = Text[i:i+k]
        num = PatternToNumber(text_pat)
        FrequencyArray[num] = FrequencyArray[num] + 1

    return FrequencyArray
