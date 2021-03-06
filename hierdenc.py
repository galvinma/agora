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

    print("Clustering " + str(n) + " objects with " + str(m) + " attributes.")

    for k,v in objects.items():
        unassigned.append(k)

    # Create an empty dictionary for r = 0
    clusters[r] = {}

    while r < 5 and proceed == bool(1):
        r += 1      # increase radius

        # Update the index
        index, associated_objects = hierdenc_index(unassigned, objects, r)
        sort = sorted(index.items(), key=itemgetter(1), reverse=True)

        # Assign new objects to clusters
        clusters[r], assigned, cluster_id = assign(sort, clusters[r-1], r, cluster_id, associated_objects)

        # Update unassigned list
        unassigned = update_unassigned(unassigned, assigned)

        # Merge and calculate connectivity
        clusters[r], cluster_id = merge(objects, clusters[r], r, m, cluster_id)
        # check connectivity score
        # current = connectivity(clusters, r)
        # if current <= connectivity:
        #     proceed = bool(0)
        #     break

    # Assign remaining clusters
    for i in unassigned:
        clusters[r][i] = cluster_id
        cluster_id +=1
    return clusters
