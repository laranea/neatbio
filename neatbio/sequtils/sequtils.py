#!/usr/bin/env python
from collections import Counter
from itertools import groupby

# Translate Table
CodonTable = {
    # 'M' - START, '*' - STOP
    "GCT": "A", "GCC": "A", "GCA": "A", "GCG": "A",
    "TGT": "C", "TGC": "C",
    "GAT": "D", "GAC": "D",
    "GAA": "E", "GAG": "E",
    "TTT": "F", "TTC": "F",
    "GGT": "G", "GGC": "G", "GGA": "G", "GGG": "G",
    "CAT": "H", "CAC": "H",
    "ATA": "I", "ATT": "I", "ATC": "I",
    "AAA": "K", "AAG": "K",
    "TTA": "L", "TTG": "L", "CTT": "L", "CTC": "L", "CTA": "L", "CTG": "L",
    "ATG": "M",
    "AAT": "N", "AAC": "N",
    "CCT": "P", "CCC": "P", "CCA": "P", "CCG": "P",
    "CAA": "Q", "CAG": "Q",
    "CGT": "R", "CGC": "R", "CGA": "R", "CGG": "R", "AGA": "R", "AGG": "R",
    "TCT": "S", "TCC": "S", "TCA": "S", "TCG": "S", "AGT": "S", "AGC": "S",
    "ACT": "T", "ACC": "T", "ACA": "T", "ACG": "T",
    "GTT": "V", "GTC": "V", "GTA": "V", "GTG": "V",
    "TGG": "W",
    "TAT": "Y", "TAC": "Y",
    "TAA": "*", "TAG": "*", "TGA": "*"
}


full_amino_acid_name ={'Alanine': 'Ala',
 'Cysteine': 'Cys',
 'Aspartic acid': 'Asp',
 'Glutamic acid': 'Glu',
 'Phenylalanine': 'Phe',
 'Glycine': 'Gly',
 'Histidine': 'His',
 'Isoleucine': 'Ile',
 'Lysine': 'Lys',
 'Leucine': 'Leu',
 'Methionine': 'Met',
 'Asparagine': 'Asn',
 'Proline': 'Pro',
 'Glutamine': 'Gln',
 'Arginine': 'Arg',
 'Serine': 'Ser',
 'Threonine': 'Thr',
 'Valine': 'Val',
 'Tryptophan': 'Trp',
 'Tyrosine': 'Tyr'}

aa3_to1_dict  = {'Ala': 'A',
 'Cys': 'C',
 'Asp': 'D',
 'Glu': 'E',
 'Phe': 'F',
 'Gly': 'G',
 'His': 'H',
 'Ile': 'I',
 'Lys': 'K',
 'Leu': 'L',
 'Met': 'M',
 'Asn': 'N',
 'Pro': 'P',
 'Gln': 'Q',
 'Arg': 'R',
 'Ser': 'S',
 'Thr': 'T',
 'Val': 'V',
 'Trp': 'W',
 'Tyr': 'Y'}


 

def gc_content(seq):
    """Return GC Content of Sequence"""
    result = float(str(seq).count('G') + str(seq).count('C'))/len(seq) *100
    return result


def at_content(seq):
    """Return AT Content of Sequence"""
    result = float(str(seq).count('A') + str(seq).count('T'))/len(seq) *100
    return result

def gc_frequency(self):
    """Return the number of GC Count/Frequence in the Sequence """
    result = str(self.seq).count("G") + str(self.seq).count("C")
    return result

    
def at_frequency(self):
    """Return the number of AT Count/Frequence in the Sequence """
    result = str(self.seq).count("A") + str(self.seq).count("T")
    return result


# Get Keys
def __get_key(val,my_dict):
    for key,value in my_dict.items():
        if val == value:
            return key

# Get Values
def __get_value(val,my_dict):
    for key,value in my_dict.items():
        if val == key:
            return value


def convert_1to3(seq):
    """Convert 1 letter Amino Acid to 3 letter Amino Acid

    >>> convert_1to3('L')
    >>> Lys

    """
    term_list = []
    for i in seq:
        res = __get_key(i,aa3_to1_dict)
        term_list.append(res)
    return "".join(term_list)

def __kmers(seq,k=2):
    pair_list = []
    for i in range(0,len(seq),k):
        pair_list.append(seq[i:i+k])
    return pair_list

def convert_3to1(seq):
    """Convert 3 letter Amino Acid to 1 letter Amino Acid

    >>> convert_3to1('Lys')
    >>> L

    """
    term_list = []
    for i in __kmers(seq,k=3):
        res = __get_value(i,aa3_to1_dict)
        term_list.append(res)
    return ''.join(term_list)

def get_kmers(seq,k=2):
    """Get the K-mers of A Sequence where k is the number

    >>> get_kmers(seq1,3)

    """
    pair_list = []
    for i in range(0,len(seq),k):
        pair_list.append(str(seq)[i:i+k])
    return pair_list


def hamming_distance(lhs,rhs):
    """Returns the Hamming Distance of Two Equal Sequence/Strings

    """
    return len([(x,y) for x,y in zip(lhs,rhs) if x !=y])

def occurence(main_seq,sub_seq):
    """Check for the occurence of a sub sequence in a sequence

    >>>occurence(seq1,sub_seq1)

    """
    start= 0
    indices =[]
    while True:
        start = main_seq.find(sub_seq,start)
        if start > 0:
            indices.append(start)
        else:
            break
        start +=1
    return indices


def get_acid_name(seq):
    """Returns the Fullname of a 3letter Amino Acid
    
    example: 
    >>> get_acid_name("Ala")
    "Alanine"

    """
    term_list = []
    for i in __kmers(seq,k=3):
        res = __get_key(i,full_amino_acid_name)
        term_list.append(res)
    return ''.join(term_list)


def codon_frequency(seq, aminoacid):
    """Provides the frequency of each codon encoding a given aminoacid in a DNA sequence"""
    tmpList = []
    for i in range(0, len(seq) - 2, 3):
        if CodonTable[seq[i:i + 3]] == aminoacid:
            tmpList.append(seq[i:i + 3])

    freqDict = dict(Counter(tmpList))
    totalScore = sum(freqDict.values())
    for seq in freqDict:
        freqDict[seq] = round(freqDict[seq] / totalScore, 2)
    return freqDict



# For Dot plot
def __delta(x,y):
    return 0 if x == y else 1


def __M(seq1,seq2,i,j,k):
    return sum(__delta(x,y) for x,y in zip(seq1[i:i+k],seq2[j:j+k]))


def __makeMatrix(seq1,seq2,k):
    n = len(seq1)
    m = len(seq2)
    return [[__M(seq1,seq2,i,j,k) for j in range(m-k+1)] for i in range(n-k+1)]


def __plotMatrix(M,t, seq1, seq2, nonblank = chr(0x25A0), blank = ' '):
    print(' |' + seq2)
    print('-'*(2 + len(seq2)))
    for label,row in zip(seq1,M):
        line = ''.join(nonblank if s < t else blank for s in row)
        print(label + '|' + line)

def dotplot(seq1,seq2,k = 1,t = 1):
    """Create a Simple Dotplot(Black and white) of 2 sequences 

    example: 
    >>> dotplot(seq1,seq2)

    """
    M = __makeMatrix(str(seq1),str(seq2),k)
    __plotMatrix(M, t, str(seq1),str(seq2)) #experiment with character choice



def count_kmers(seq, k=3):
    """Returns the Count or Frequency of Kmers generated in a sequence"""
    # Start with an empty dictionary
    counts = {}
    # Calculate how many kmers of length k there are
    num_kmers = len(str(seq)) - k + 1
    # Loop over the kmer start positions
    for i in range(num_kmers):
        # Slice the string to get the kmer
        kmer = str(seq)[i:i+k]
        # Add the kmer to the dictionary if it's not there
        if kmer not in counts:
            counts[kmer] = 0
        # Increment the count for this kmer
        counts[kmer] += 1
    # Return the final counts
    return counts

def kmer_distance(seq1,seq2,k=3):
    """Returns the Kmer-Distance which is Non-Unique Kmers among two sequences 

    example: 
    >>> kmer_distance('ACTGTCTAGTC','ATCGCATGATC',k=3)
    {'CTG', 'AGT', 'CAT', 'GCA', 'CGC', 'GAT', 'ATG', 'GTC', 'ACT', 'TAG', 'TGA', 'TGT', 'TCT', 'ATC', 'CTA', 'TCG'}
    1.0
    """
    seq1_set = set(count_kmers(seq1,k).keys())
    seq2_set = set(count_kmers(seq2,k).keys())
    union_seq = seq1_set.union(seq2_set)
    dissimilarity = seq1_set ^ seq2_set
    distance = len(dissimilarity)/len(union_seq)
    print(dissimilarity)
    return distance 

def back_translate(seq):
    """Returns a Probable Nucleotide Sequence of A Protein
    
    example:
    >>> import neatbio.sequtils as utils
    >>> utils.back_translate('IKGLYLPR')
    'ATAAAAGGTTTATATTTACCTCGT'

    """

    base_nucleotide_list = []
    for i in seq:
        res = __get_key(i,CodonTable)
        base_nucleotide_list.append(res)
    return ''.join(base_nucleotide_list)




def read_fasta(fasta_name):
    """
    Parse A Fasta File and yields a dictionary of header, sequence
    (Modified from Brent Pedersen)
    """
    
    """first open the file outside """
    file_handler = open(fasta_name)

    # ditch the boolean (x[0]) and just keep the header or sequence since
    # we know they alternate.
    fasta_iter = (x[1] for x in groupby(file_handler, lambda line: line[0] == ">"))

    for header in fasta_iter:
        # drop the ">"
        headerStr = header.__next__()[1:].strip()

        # join all sequence lines to one.
        seq = "".join(s.strip() for s in fasta_iter.__next__())

        # yield (headerStr, seq)
        result_record = {'header':headerStr,'seqRecord':seq}
        return result_record