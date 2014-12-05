miRNAlearn
==========

miRNAlearn uses several sklearn classifiers to discriminate between putative miRNA sequences. We initially use only two variables, MFE and P_MFE, to characterise the miRNAs. This gives us a very simple start point for the implementation of the various learning algorithms.

The iPython notebook (miRNAlearn.ipynb) is where the work is being done, but the computations are dependent on the miRNAlearn.py and miRNAlearnIO.py files.

The example dataset is from a Termite genome. These miRNA sequence are the hits of the genome versus the mirbase database (they were not manually curated). The negative dataset is obtaining by shuffling the original sequences while maintaining the original dinucleotide distribution [1].

The viennaRNA Python wrapper (https://github.com/pmsppinto/viennaRNA) is currently required, this might change in the future. However the ViennaRNA library will always be a requirement.

[1] http://clavius.bc.edu/~clotelab/RNAdinucleotideShuffle/dinucleotideShuffle.html
