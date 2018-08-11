from dissimilarity import dissimilarity
#
# clustering algorithm
#

def update_unassigned(unassigned, assigned):
    for i in assigned:
        for j in unassigned:
            if i == j:
                del unassigned[j]
    return unassigned

def assign(sort, clusters, r, cluster_id, associated_objects):
    # Starting with the densest object in index, assign a cluster.
    # Merge objects that are within distance r
    assigned = []
    for i in sort:
        if i not in assigned:
            # Create a new cluster centered at i
            clusters[i] = cluster_id
            assigned.append(i)

            # Add associated_objects to current cluster
            if i in associated_objects:
                associated = associated_objects[i]
                for j in associated:
                    clusters[j] = cluster_id
                    assigned.append(j)

            # Increment cluster_id
            cluster_id += 1

    return clusters, assigned, cluster_id


def merge(clusters, r, m, cluster_id):
    # Merge clusters within distance r.
    within_radius = m - r
    for k,v in clusters.items():
        for m,n in clusters.items():
            if m != k:
                score = dissimilarity(v[1:], n[1:])
                if score >= within_radius and n != v:
                    # merge
                    cluster_id += 1
                    for a,b in clusters.items():
                       if b == v or b == n:
                           clusters[a] = cluster_id
    return clusters, cluster_id


def connectivity(clusters, r):
    return
