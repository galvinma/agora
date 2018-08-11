from operator import itemgetter
from index import hierdenc_index
from cluster import assign, merge, connectivity
#
# HIERDENC function
#
def hierdenc(objects):
    # Initial conditions
    print("Entering HIERDENC function...")
    clusters = {}               # radius : {object ID : cluster ID}
    r = 0                       # radius of hypercubes
    m = len(objects[0]) - 1     # number of attributes
    n = len(objects)            # number of objects
    c = len(clusters)           # number of items clustered
    connectivity = 0            # current connectivity score
    unassigned = []             # list of objects unassigned to a cluster
    proceed = bool(1)

    for k,v in in objects.items():
        unassigned.append(k)

    while r < m and proceed = bool(1):
        r += 1      # increase radius
        # Merge and calculate connectivity
        if len(clusters):
            clusters[r] = merge(clusters[r-1], r)
            current = connectivity(clusters, r)
            if current <= connectivity:
                proceed = bool(0)
                break

        # Update the index
        index = hierdenc_index(unassigned, objects, r)
        sort = sorted(index.items(), key=itemgetter(1), reverse=True)

        # Assign new objects to clusters
        clusters[r], unassigned = assign(index, clusters[r], r, unassigned)



    return clusters
