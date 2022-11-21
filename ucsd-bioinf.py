# Author: Marie Fortuno
# Course: UCSD's "Biology Meets Programming: Bioinformatics for Beginners"


# Week 1: Where in the Genome Does Replication Begin? (Part 1)

# PatternCount outputs the number of times a certain pattern appears in a string
def PatternCount(text, pattern):
	count = 0
	textLen = len(text)
	patternLen = len(pattern)
	for i in range(textLen - patternLen + 1):
		if text[i:i+patternLen] == pattern:
			count += 1
	return count

# FreqWords returns a list containing all k-mers that have the maximum frequencies
## k-mer: string of length k
def FreqWords(text, k):
	freq = {}
	n = len(text) - k
	for i in range(n+1):
		pattern = text[i:i+k]
		freq[pattern] = PatternCount(text, pattern)
	words = []
	m = max(freq.values())
	for key in freq:
		if freq[key] == m:
			words.append(key) 
	return words

# ReverseComplement outputs the reverse complement a string of nucleotides
def ReverseComplement(pattern):
	complement = []
	for base in pattern[::-1]:
		if base == "A":
			complement.append("T")
		elif base == "C":
			complement.append("G")
		elif base == "T":
			complement.append("A")
		elif base == "G":
			complement.append("C")
	return ''.join(complement)
	
# PatternMatching outputs all starting positions in a genome where a certain pattern appears as a subtring
def PatternMatching(pattern, genome):
    match = []
    n = len(genome)-len(pattern)
    for i in range(n+1):
        gen = genome[i:i+len(pattern)]
        if gen == pattern:
            match.append(i)
    return match


# Week 2: Where in the Genome Does Replication Begin? (Part 2)

def SymbolArray(Genome, symbol):
	array = {}
	n = len(Genome)
	ExtendedGenome = Genome + Genome[0:n//2]
	for i in range(n):
		array[i] = PatternCount(ExtendedGenome[i:i+(n//2)], symbol)
	return array
