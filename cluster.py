import statistics
from dissimilarity import dissimilarity
#
# clustering algorithm
#

def assign(sort, clusters, r, cluster_id, associated_objects, mode, objects, m, mode_lookup):
    # Starting with the densest object in index, assign a cluster.
    # Merge objects that are within distance r
    assigned = []
    clustcount = cluster_id
    for i in sort:
        if i[0] not in assigned and i[0] not in clusters and i[1] > 0:
            # Create a new cluster
            # print("Assigning object " + str(i[0]) + " with density count "
            # + str(i[1]) + " to cluster " + str(clustcount))
            # Attempt to add point to an existing cluster
            # If addition fails, create a new cluster centered at i
            clusters[i[0]] = clustcount
            mode = create_cluster_counter(m, clustcount, mode)
            mode = update_mode(i[0], objects, clustcount, mode)
            mode_lookup = calculate_mode(mode_lookup, mode, clustcount)
            assigned.append(i[0])

            # Add associated_objects to current cluster
            if i[0] in associated_objects:
                associated = associated_objects[i[0]]
                for j in associated:
                    if j not in assigned:
                        # print("Assigning object " + str(j) + " to cluster " + str(clustcount))
                        clusters[j] = clustcount
                        mode = update_mode(j, objects, clustcount, mode)
                        mode_lookup = calculate_mode(mode_lookup, mode, clustcount)
                        assigned.append(j)
            # Increment cluster_id
            clustcount += 1

    return clusters, assigned, clustcount, mode, mode_lookup


def merge(objects, clusters, r, m, cluster_id, mode_lookup, mode):
    clustcount = cluster_id
    # Merge clusters within distance r.
    within_radius = m - r
    for k,v in clusters.items():
        for x,n in clusters.items():
            if x != k and v != n:
                # Compare cluster modes to determine merge
                score = dissimilarity(mode_lookup[v], mode_lookup[n])
                if score >= within_radius:
                    # merge
                    # print("Merging clusters " + str(v) + " and " + str(n) + " because mode calculation"
                    # + " score of " + str(score) + " is within the minimum radius of " + str(within_radius) +
                    # ". All objects within those clusters are now placed in cluster " + str(clustcount))
                    mode = create_cluster_counter(m, clustcount, mode)
                    for a,b in clusters.items():
                       if b == v or b == n:
                           clusters[a] = clustcount
                           mode = update_mode(a, objects, clustcount, mode)
                    mode_lookup = calculate_mode(mode_lookup, mode, clustcount)
                    clustcount += 1
    return clusters, clustcount, mode, mode_lookup

def update_unassigned(unassigned, assigned):
    for i in assigned:
        if i in unassigned:
            unassigned.remove(i)
    return unassigned

# function creates list of empty lists for mode calculation
def create_cluster_counter(m, cluster, mode):
    attributes = []
    for i in range(m):
        attributes.append([])
    mode[cluster] = attributes
    return mode

def update_mode(id, objects, cluster, mode):
    for i, j in zip(objects[id][1:], mode[cluster]):
        j.append(int(i))
    return mode

def calculate_mode(mode_lookup, mode, cluster):
    # reset for calculation
    mode_lookup[cluster] = []
    for i in mode[cluster]:
        # If tie, return first mode
        c = max(i, key = i.count)
        mode_lookup[cluster].append(c)
    return mode_lookup

def connectivity(clusters, r):
    return
