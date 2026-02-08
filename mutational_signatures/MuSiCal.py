"""
Mutational signatures with MusiCal
"""

import numpy as np
import scipy.stats as stats
import matplotlib.pyplot as plt
import seaborn as sns
import matplotlib as mpl
import pandas as pd
import time
import scipy as sp
import pickle
import os
import musical


X = pd.read_csv('./data/PCAWG-146_profiles.csv', index_col=0)
model = musical.DenovoSig(X, 
                          min_n_components=1, # Minimum number of signatures to test
                          max_n_components=20, # Maximum number of signatures to test
                          init='random', # Initialization method
                          method='mvnmf', # mvnmf or nmf
                          n_replicates=20, # Number of mvnmf/nmf replicates to run per n_components
                          ncpu=16, # Number of CPUs to use
                          max_iter=100000, # Maximum number of iterations for each mvnmf/nmf run
                          bootstrap=True, # Whether or not to bootstrap X for each run
                          tol=1e-8, # Tolerance for claiming convergence of mvnmf/nmf
                          verbose=1, # Verbosity of output
                          normalize_X=False # Whether or not to L1 normalize each sample in X before mvnmf/nmf
                        )
model.fit()

model.W.to_csv('./data/PCAWG-146_W.csv', index_col=0)
model.H.to_csv('./data/PCAWG-146_H.csv', index_col=0)

with open('./data/PCAWG-146_model_0.pkl', 'wb') as f:
    pickle.dump(model, f)

with open('./data/PCAWG-146_model_0.pkl', 'rb') as f:
    model = pickle.load(f)


thresh_grid = np.array([
    0.0001, 0.0002, 0.0005,
    0.001, 0.002, 0.005,
    0.01, 0.02, 0.05,
    0.1, 0.2, 0.5,
    1., 2., 5.
])

catalog = musical.load_catalog('COSMIC-MuSiCal_v3p2_SBS_WGS')
W_catalog = catalog.W
print(W_catalog.shape[1])


model.assign_grid(W_catalog, 
                  method_assign='likelihood_bidirectional', # Method for performing matching and refitting
                  thresh_match_grid=thresh_grid, # Grid of threshold for matchinng
                  thresh_refit_grid=thresh_grid, # Grid of threshold for refitting
                  thresh_new_sig=0.0, # De novo signatures with reconstructed cosine similarity below this threshold will be considered novel
                  connected_sigs=False, # Whether or not to force connected signatures to co-occur
                  clean_W_s=False # An optional intermediate step to avoid overfitting to small backgrounds in de novo signatures for 96-channel SBS signatures
                 )

model.validate_grid(validate_n_replicates=1, # Number of simulation replicates to perform for each grid point
                    grid_selection_method='pvalue', # Method for selecting the best grid point
                    grid_selection_pvalue_thresh=0.05 # Threshold used for selecting the best grid point
                   )

with open('./results/PCAWG-146_model.pkl', 'wb') as f:
    pickle.dump(model, f)