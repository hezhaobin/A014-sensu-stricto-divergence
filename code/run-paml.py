"""
title: Use PAML to estimate synonymous and nonsynonymous divergence between aligned sequences
author: Bin He
date: 1 dec 2017
"""

# loading requirements
from glob import glob
from Bio import AlignIO
from Bio.Phylo.PAML import codeml

# define functions
def myPAML( f, format="fasta" ):
    """ Use PAML to estimate syn and nonsyn divergence
    Args:
        f (str): the path and filename
        format (str): format of the input alignment, e.g. "fasta"
    Returns:
        parsed output from PAML
    """
    try: 
        aln = AlignIO.read(f, format)
    except ValueError:
        LOG.write( f.split("_")[1] + " doesn't have equal sequence length.\n" )
        return;

    L = aln.get_alignment_length()
    """ 
    to remove the last three nucleotides (stop codon)
    changed to remove the last 18 because some sequences
    have misaligned stop codons that appear in the second
    to last codon position
    """

    aln = aln[:, 0:L-18] 
    
    # edit the sequence name to retain only the species name part
    for record in aln:
        record.id = record.id.split("_")[0]
    
    AlignIO.write(aln, "./scratch/tmp.phy", "phylip-sequential")

    # initialize the PAML codeml object
    cml = codeml.Codeml()
    cml.working_dir = "./scratch"
    cml.alignment = "./scratch/tmp.phy"
    cml.tree = "./scratch/tree"
    cml.read_ctl_file("./scratch/codonml.ctl")
    cml.out_file = "./scratch/" + f.split("_")[1] + ".mlc" # name the output file

    # run PAML
    # note that the working_dir take effect for ctl_file, but not the others
    result = cml.run()

    return result;

    
# open file for output
OUT = open("../output/2017-12-01-Scer-Spar-5.txt", "w")
LOG = open("./run-paml-log-5.txt", "w")

# list all files
all_files = glob("../data/alignment/coding/*.codon.mfa")
print( "There are %i files" % len(all_files) )

i = 0 # counter

for IN in all_files[3155:]:
    # get gene name
    gene = IN.split("_")[1]
    # run PAML
    result = myPAML(IN, "fasta")
    # deal with errors due to unequal sequence length
    if result == None:
        continue
    # deal with cases where PAML run is successful but output is null
    try: 
        dist = result['pairwise']['Scer']['Spar']
        value = [dist[x] for x in ['dN','dS','omega']]
        OUT.write( "\t".join([gene]+map(str, value)) + "\n" )
    except KeyError:
        LOG.write( gene + " didn't yield useful results.\n" )

    # progress report
    i = i + 1
    if i % 5 == 0:
        print( str(i) + ", " )
