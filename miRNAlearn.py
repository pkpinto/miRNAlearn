# coding: utf-8

import os
import numpy as np
import viennaRNA


def RNAfold(sequences):
    """
    Folds the sequences in the input list (the sequence suitability is not
    checked) using the ViennaRNA library.
    """
    fold_info = [viennaRNA.seq_fold(s) + viennaRNA.seq_pf_fold(s)
                 for s in sequences]
    mfe_fold, mfe, gfe_fold, gfe = zip(*fold_info)
    return np.array(mfe_fold), np.array(mfe), np.array(gfe_fold), np.array(gfe)


def ground_state_prob(mfe, gfe, kT=None):
    """"""
    if kT is None:
        kT = (37 + 273.15) * 1.98717 / 1000.0  # kT in kcal/mol
    return np.exp(-(mfe - gfe) / kT)


def complexity(folds):
    pass
