import numpy as np
from dissimilarity import dissimilarity
#
# HIERDENC Index
#
def hierdenc_index(objects):
    index = np.zeros((len(objects), len(objects)))
    for k,v in objects.items():
        for m,n in objects.items():
            if m == k:
                index[k][m] = -1
            else:
                index[k][m] = dissimilarity(v[1:], n[1:])
    return index
