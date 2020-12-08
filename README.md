# SARS-CoV-2-Secondary-Structure-Project


ViennaRNA Commands used on each fasta file:


# Produces Minimum Free Energy
RNAfold < example.fasta

# Produces ensemble diversity
RNAfold -p --MEA < example.fasta

# Produces RNA Secondary Structure
perl relplot.pl example_ss.ps example_dp.ps > example_rss.ps









For more information on ss.ps and dp.ps files please view ViennaRNA documentation (https://www.tbi.univie.ac.at/RNA/tutorial/).
