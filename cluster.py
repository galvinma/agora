import collections
from dissimilarity import dissimilarity
#
# clustering algorithm
#

def update_unassigned(unassigned, assigned):
    for i in assigned:
        if i in unassigned:
            unassigned.remove(i)
    return unassigned

def assign(sort, clusters, r, cluster_id, associated_objects, mode, objects, m):
    # Starting with the densest object in index, assign a cluster.
    # Merge objects that are within distance r
    assigned = []
    clustcount = cluster_id
    for i in sort:
        if i[0] not in assigned and i[0] not in clusters and i[1] > 0:
            # Create a new cluster
            print("Assigning object " + str(i[0]) + " with density count "
            + str(i[1]) + " to cluster " + str(clustcount))
            # Attempt to add point to an existing cluster
            # If addition fails, create a new cluster centered at i
            clusters[i[0]] = clustcount
            mode = create_cluster_counter(m, clustcount, mode)
            mode = update_mode(i[0], objects, clustcount, mode)
            assigned.append(i[0])

            # Add associated_objects to current cluster
            if i[0] in associated_objects:
                associated = associated_objects[i[0]]
                for j in associated:
                    if j not in assigned:
                        print("Assigning object " + str(j) + " to cluster " + str(clustcount))
                        clusters[j] = clustcount
                        mode = update_mode(j, objects, clustcount, mode)
                        assigned.append(j)
            # Increment cluster_id
            clustcount += 1

    return clusters, assigned, clustcount, mode


def merge(objects, clusters, r, m, cluster_id):
    clustcount = cluster_id
    # Merge clusters within distance r.
    within_radius = m - r
    for k,v in clusters.items():
        for m,n in clusters.items():
            if m != k and v != n:
                # Compare cluster modes to determine merge
                score = dissimilarity(objects[k][1:], objects[m][1:])
                if score >= within_radius:
                    # merge
                    clustcount += 1
                    print("Merging clusters " + str(v) + " and " + str(n) + " because objects "
                    + str(k) + " and " + str(m) + " scored " + str(score) +
                    " which is within the minimum radius of " + str(within_radius) +
                    ". All objects within those clusters are now placed in cluster " + str(clustcount))
                    for a,b in clusters.items():
                       if b == v or b == n:
                           clusters[a] = clustcount
    return clusters, clustcount

# function creates list of empty lists for mode calculation
def create_cluster_counter(m, cluster, mode):
    attributes = []
    for i in range(m):
        attributes.append([])
    mode[cluster] = attributes
    return mode

def update_mode(id, objects, cluster, mode):
    for i, j in zip(objects[id][1:], mode[cluster]):
        j.append(i)
    return mode

def connectivity(clusters, r):
    return
