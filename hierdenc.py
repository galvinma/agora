from operator import itemgetter
from index import hierdenc_index
from cluster import assign, merge, connectivity, update_unassigned
#
# HIERDENC function
#
def hierdenc(objects):
    # Initial conditions
    print("Entering HIERDENC function...")
    clusters = {}               # radius : {object ID : cluster ID}
    r = 0                       # radius of hypercubes
    cluster_id = 0              # cluster ID
    m = len(objects[0]) - 1     # number of attributes
    n = len(objects)            # number of objects
    c = len(clusters)           # number of items clustered
    connectivity = 0            # current connectivity score
    unassigned = []             # list of objects unassigned to a cluster
    proceed = bool(1)

    for k,v in objects.items():
        unassigned.append(k)

    while r < m and proceed == bool(1):
        r += 1      # increase radius
        # Merge and calculate connectivity
        if len(clusters):
            # merge
            clusters[r], cluster_id = merge(clusters[r-1], r, m, cluster_id)
            # check connectivity score
            # current = connectivity(clusters, r)
            # if current <= connectivity:
            #     proceed = bool(0)
            #     break

        # Update the index
        index, associated_objects = hierdenc_index(unassigned, objects, r)
        sort = sorted(index.items(), key=itemgetter(1), reverse=True)

        # Assign new objects to clusters
        clusters[r] = {}
        clusters[r], assigned, cluster_id = assign(sort, clusters[r], r, cluster_id, associated_objects)

        # Update unassigned list
        unassigned = update_unassigned(unassigned, assigned)

    return clusters
