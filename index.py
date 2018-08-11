import numpy as np
from dissimilarity import dissimilarity
#
# HIERDENC Index
#
def hierdenc_index(unassigned, objects, r):
    # objects[0] includes name of object as well as attributes
    within_radius = len(objects[0]) - 1 - r
    index = {}
    associated_objects = {}
    # dissimilarity_matrix = np.zeros((len(objects), len(objects)))
    for i in unassigned:
        k = i
        v = objects[k]
        index[k] = 0
        for m,n in objects.items():
            if m != k:
                score = dissimilarity(v[1:], n[1:])
                if score >= within_radius:
                    index[k] += 1
                    if k in associated_objects:
                        associated_objects[k].append(m)
                    else:
                        associated_objects[k] = [m]

    return index, associated_objects
